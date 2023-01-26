import Image from "next/image";
import Features from "@/app/features";
import Header from "@/app/header";
import Footer from "@/app/footer";
import HeroSection from "@/app/heroSection";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col bg-yellow-50/50">
      {/* Header */}
      <Header />

      {/* Main */}
      <main className="flex flex-col space-y-10">
        {/* Hero Section  */}
        <HeroSection />

        {/* Features */}
        <Features />
      </main>
      <Footer />
    </div>
  );
}
