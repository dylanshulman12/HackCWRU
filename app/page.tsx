"use client";

import Image from "next/image";
import { useState, useEffect, useRef } from "react";
import { useRouter } from "next/navigation";
import { error } from "console";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [jsonupload, setJSON] = useState<File |null>(null);
  const [location, setLocation] = useState<{
    latitude: number;
    longitude: number;
    postal: number;
    city: string;
  } | null>(null);
  // so we can customize button!
  const hiddenFileInput = useRef(null);
  const router = useRouter();

  useEffect(() => {
    async function informationSwap() {
      if (file != null) {
        const image = file?.name;

        //send file
        const formData = new FormData();
        formData.append("file", file);

        //upload photo to /uploads
        const upload = await fetch("/api/upload", {
          method: "POST",
          body: formData,
        });
        const response = await upload.json();
        console.log("image path thing: " + image);

        const jsonfile = await fetch(`/api/materialGet?file=${encodeURIComponent(image)}&city=Cleveland&state=Ohio&zipCode=44106`)

        //change to information page, and get image for display
        router.push(`/information?image=${encodeURIComponent(image)}`);
      }
    }
    informationSwap();
  }, [file]); 

  useEffect(() => {
    //get location!
    async function getLocation() {
      //json of the users location
      const data = await fetch("https://ipapi.co/json/");
      const j = await data.json();
      console.log(j);

      setLocation({
        latitude: j.latitude,
        longitude: j.longitude,
        postal: j.postal,
        city: j.city,
      });
    }

    getLocation();
  }, []);

  // useEffect(() => {
  //   async function getInfo() {
  //     if (jsonupload)
  //     const data = await fetch("http://localhost:8000/api/info", {
  //       method: "POST",

  //     });

  //   }
  //   getInfo()
  // }, []);

  let choice = false;


  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  //Git Click
  const handleGit = () =>{
    router.push("https://github.com/dylanshulman12/HackCWRU")
  }

  //About us Page
  const handleAboutUs = () => {
    router.push('/aboutus')
  }

  function PrintPosition() {
    if (location != null) {
      return (
        <div>
          <div>latitude: {location?.latitude}</div>
          <div>Longitude: {location?.longitude}</div>
          <div>Postal: {location?.postal}</div>
          <div>City: {location?.city} </div>
        </div>
      );
    }
    return <div>Position Loading..</div>;
  }

  return (
    <>
      <div className="top-main">
          <button className="icon" onClick={handleAboutUs}>
            <img src="/about_us.svg" alt="About Us" />
          </button>
          <button className="icon" onClick={handleGit}>
            <img src="/github_logo.svg" alt="Github" />
          </button>
      </div>
      <div className="page"> 
        <img src="/cats_logo.png" alt="Logo" style={{height : "50%", }}/>
        <div
            style={{
              display : "flex",
              height: "30vh",
              width: "85vw",
              background: "#414833",
              border: "solid #414833 40px",
              borderRadius: "10px",
              padding: "10px",
              
              alignContent : "center",
              justifyContent : "center",
            }}
          >
            {/* <PrintPosition /> */}
            <div className="button" onClick={handleClick1}>
              Upload Files
            </div>
            <input
              id="file"
              type="file"
              ref={hiddenFileInput}
              style={{ display: "none" }}
              onChange={handleFileChange}
            />
          </div>
        </div>
    </>
  );
}
