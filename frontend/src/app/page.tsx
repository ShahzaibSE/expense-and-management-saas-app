import WelcomeComponent from "@/custom_components/welcome";

export default function Home() {
  return (
    <div className="flex flex-col justify-center items-center min-h-screen">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <WelcomeComponent />
      </main>
    </div>
  );
}
