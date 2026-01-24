"use client"


import { useSearchParams, useRouter } from "next/navigation";


export default function Aboutus() {
  
  const router = useRouter();
  
  
  const handleGit = () => {
    router.push("https://github.com/dylanshulman12/HackCWRU");
  };

  const handleAboutUs = () => {
    router.push("/aboutus");
  };

  const handleBack = () => {
    router.push("/");
  };

  return (
    <>
      <div className="top">
        <button className="icon" onClick={handleBack}>
          <img src="/back_arrow.svg" alt="Back" />
        </button>
        <div style={{justifyContent: 'flex-end'}}>
        <button className="icon" onClick={handleAboutUs}>
          <img src="/about_us.svg" alt="About Us" />
        </button>
        <button className="icon" onClick={handleGit}>
          <img src="/github_logo.svg" alt="Github" />
        </button>
        </div>
      </div>
      <div>About us yo</div>
    </>
  );
}
