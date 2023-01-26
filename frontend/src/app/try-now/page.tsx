import Header from "@/app/header";
import Footer from "../footer";
import Prediction from "./prediction";

export default function TryNow() {
  return (
    <div className="flex min-h-screen flex-col bg-yellow-50/50">
      {/* Header */}
      <Header />

      {/* Main */}
      <main className="flex flex-col space-y-10 items-center justify-center min-h-[70vh]">
        <div className="flex flex-col space-y-2 items-center">
          <h1 className="font-bold text-center text-2xl text-sky-600 flex flex-col">
            Tuberculosis Detection App
          </h1>
        </div>
        {/* Prediction Section  */}
        <Prediction />
      </main>
      <Footer />
    </div>
  );
}
