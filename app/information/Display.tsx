"use client";

import { useSearchParams, useRouter } from "next/navigation";
import { useState, useEffect } from "react";

export default function Display() {
  const searchParams = useSearchParams();
  const image = searchParams.get("image") ?? "";
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [data, setData] = useState<any>(null);

  const handleBack = () => {
    router.push("/");
  };

  const handleGit = () => {
    router.push("https://github.com/dylanshulman12/HackCWRU");
  };

  const handleAboutUs = () => {
    router.push("/aboutus");
  };

  useEffect(() => {
    async function loadData() {
      try {
        const response = await fetch(
          `/api/materialGet?file=${encodeURIComponent(
            image
          )}&city=Cleveland&state=Ohio&zipCode=44106`,
          { cache: "no-store" }
        );

        const result = await response.json();
        setData(result);
      } catch (err) {
        console.error("Failed to fetch data:", err);
      }

      setLoading(false);
    }

    if (image) {
      loadData();
    }
  }, [image]);

  if (loading) {
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

  return (
    <div>
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
        <div className="border">
          <div className="info-container">
            <div className="image-container">
              <img src={`/localhost:8000/api/files?image=${encodeURIComponent(image)}`} />
            </div>

            <div
              style={{
                display: "flex",
                flexDirection: "column",
                height: "100%",
                width: "65%",
                justifyContent: "center",
                gap: "5vh"
              }}
            >
              <div className="status-container">
                {data?.isRecyclable ?? "Unknown"}
              </div>

              <div className="text-container">
                {data?.notes ?? "No information available"}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}