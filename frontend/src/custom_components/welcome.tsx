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

export default function WelcomeComponent() {
  return (
    <Card className="w-full">
      <CardHeader className="flex flex-col justify-center items-center">
        <CardTitle><span className="text-xl">Expense Management</span></CardTitle>
      </CardHeader>
      <CardContent className="flex flex-col justify-between items-center">
        <Button className="w-full my-2 p-2">
          Create Account
        </Button>
        <Separator className="my-6 border-gray-400" />
        <div className="w-full">
          <Button className="w-full my-1">
            Sign In with Email
          </Button>
          <Button className="w-full">
            Sign In with Google
          </Button>
        </div>
      </CardContent>
      <CardFooter className="flex flex-col justify-between items-center text-sm text-gray-500">
        <div>
          <h1 className="font-bold">Terms & Services</h1>
        </div>
      </CardFooter>
    </Card>
  );
}
