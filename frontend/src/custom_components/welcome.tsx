import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { cn } from "@/lib/utils";
import { Separator } from "@/components/ui/separator";
import { FcGoogle } from "react-icons/fc";

export default function WelcomeComponent() {
  return (
    <Card className="w-full">
      <CardHeader className="flex flex-col justify-center items-center">
        <CardTitle>
          <span className="text-xl">
            Expense Management
          </span>
        </CardTitle>
      </CardHeader>
      <CardContent className="flex flex-col justify-between items-center">
        <Button className="w-full my-6 p-2">
          Create Account
        </Button>
        <div className="w-full">
          <Button className="w-full my-1">
            Sign In with Email
          </Button>
          <Button
            className={cn(
              "flex items-center justify-center w-full px-4 py-2 border rounded-lg shadow-sm",
              "border-gray-300 bg-white hover:bg-gray-100",
              "focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500", "text-black"
            )}
          >
            <FcGoogle className="w-5 h-5 mr-2" />
            <span className="text-black">Sign in with Google</span>
          </Button>
        </div>
      </CardContent>
      <CardFooter className="flex flex-col justify-between items-center text-sm text-gray-500">
        <div>
          <h1 className="font-bold xl:text-[16px]">
            Powered By Shahzaib Noor
          </h1>
        </div>
      </CardFooter>
    </Card>
  );
}
