import os
from fastapi import FastAPI, APIRouter
import importlib
from pathlib import Path

class EnvironmentManager:
    def __init__(self, app: FastAPI):
        print("EnvironmentManager is running...")
        self.app = app
        self.env = os.getenv("ENVIRONMENT", "development")  # Default to 'development'

    def setup_routes(self):
        # Always load common routes (if available)
        self.load_routes("routes.common_routes")

        # Dynamically load all route files
        route_files = Path("routes").glob("*.py")
        for route_file in route_files:
            route_module = route_file.stem  # Get the module name without .py extension

            # Skip common routes and filter by environment
            if route_module == "common_routes" or not route_module.startswith(self.env):
                continue

            self.load_routes(f"routes.{route_module}")

    def load_routes(self, module_path: str):
        """Dynamically load routes from the given module"""
        try:
            # Dynamically import the module
            module = importlib.import_module(module_path)
            print(f"Module Path: {module}")
            # Check if the module has a 'router' attribute
            if hasattr(module, "router"):  # Use 'router' instead of 'routes'
                # Include the router in the FastAPI app
                self.app.include_router(module.router)
                print(f"Included routes from {module_path}")
            else:
                print(f"No 'router' found in {module_path}")
        except ModuleNotFoundError:
            print(f"Module {module_path} not found")
