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

      <div className="page">
        <div style={{
        fontSize: "30px",
        color: "#081c15",
        textAlign: "center",
        }}>
          <strong>------------------------------------<br></br>MAKING RECYCLING<br></br>SIMPLE EVERYWHERE<br></br>------------------------------------ </strong>
        </div>

        <div style={{
          color: "#081c15",
          textAlign: "center",
          maxWidth: "600px",
          padding: "20px",
        }}>
          In 2021, <strong>85 percent</strong> of all discarded plastic in the U.S. ended up in landfills. Every day, people throw away plastic bottles, glass bottles, cans, etc, not because they don’t care about the environment, but because identifying recyclable materials and understanding local recycling rules is confusing and inconsistent. When plastics are misidentified or recycled incorrectly, good intentions often end in contamination and waste.
          <br></br><br></br>
          To meaningfully reduce plastic pollution, people need clear, accurate guidance at the exact moment a decision is made.
          <br></br><br></br>
          IsItRecyclable aims to do exactly that through the use of <strong>computer vision</strong> and our own <strong>AI model</strong> to identify plastic and other recyclable types from a single photo. By combining material detection with location specific recycled laws, we provide clear, actionable guidance on whether an item can be recycled.

        </div>
      </div>
    </>
  );
}
