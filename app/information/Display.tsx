"use client";

import { useSearchParams, useRouter } from "next/navigation";
import { useState, useEffect } from "react";
import BackArrow from "/back_arrow.svg";
import about_us from "./about_us.svg";
import github_logo from "./github_logo.svg";
import loadingGif from "./public/loading.gif";
import data from "../src/finalDataReturn.json";


export default function display() {
  const searchParams = useSearchParams();
  const image = searchParams.get("image") ?? "";
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  //object still undefined... Have to specify type
  //   const [information, setInformation] = useState<{ object } | null>(null);
  
    
  const handleBack = () => {
    router.push("/");
  };

  const handleGit = () =>{
    router.push("https://github.com/dylanshulman12/HackCWRU")
  };

  const handleAboutUs = () => {
    router.push('/aboutus')

  };

  console.log(data?.isRecyclable)

  if (loading) {
    return (
      <div>
        {/* top nav bar div with just a top left back button and an info button for team members, with link to git source code*/}
        <div className="top">
          <button className="icon" onClick={handleBack}>
            <img src="/back_arrow.svg" alt="Back" />
          </button>
          <div>
            <button className="icon" onClick={handleAboutUs}>
              <img src="/about_us.svg" alt="About Us" />
            </button>
            <button className="icon" onClick={handleGit}>
              <img src="/github_logo.svg" alt="Github" />
            </button>
          </div>
        </div>
        <div className="page">
          {/* needs to be a side by side view */}
          <div
            style={{
              height: "75vh",
              width: "85vw",
              background: "#414833",
              border: "solid #414833 40px",
              borderRadius: "10px",
            }}
          >
            <div className="info-container">
              <div className="image-container">
                <img
                  src={`/api/files?image=${encodeURIComponent(image)}`}
                />
              </div>
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  height: "100%",
                  width: "65%",
                  justifyContent: "space-between",
                }}
              >
                <div className="status-container">Data: {data?.isRecyclable}</div>
                

                <div className="text-container">Information: {data?.notes}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
  return (
    <>
      <div className="top">
        <button className="icon" onClick={handleBack}>
            <img src="/back_arrow.svg" alt="Back" />
        </button>
        <div>
        <button className="icon" onClick={handleAboutUs}>
            <img src="/about_us.svg" alt="About Us" />
        </button>
        <button className="icon" onClick={handleGit}>
            <img src="/github_logo.svg" alt="Github" />
        </button>
        </div>
      </div>
      <div className="page">
        <img src="/loading.gif" alt="Loading..." />
      </div>
    </>
  );
}
