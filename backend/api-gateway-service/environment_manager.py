import os
from fastapi import FastAPI, APIRouter
import importlib

class EnvironmentManager:
    def __init__(self, app: FastAPI):
        self.app = app
        self.env = os.getenv("ENVIRONMENT", "development")  # Default to 'development'

    def setup_routes(self):
        # Always load common routes
        self.load_routes("routes.common_routes")

        # Dynamically load environment-specific routes
        if self.env == "development":
            self.load_routes("routes.development_routes")
        elif self.env == "staging":
            self.load_routes("routes.staging_routes")
        elif self.env == "production":
            self.load_routes("routes.production_routes")
        else:
            print(f"Unknown environment: {self.env}")

    def load_routes(self, module_path: str):
        """Dynamically load routes from the given module"""
        try:
            # Dynamically import the module
            module = importlib.import_module(module_path)
            # Check if the module has a 'router' attribute
            if hasattr(module, "router"):
                # Include the router in the FastAPI app
                self.app.include_router(module.router)
                print(f"Included routes from {module_path}")
            else:
                print(f"No 'router' found in {module_path}")
        except ModuleNotFoundError:
            print(f"Module {module_path} not found")
