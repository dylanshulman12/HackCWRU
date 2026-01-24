import { useSearchParams, useRouter } from "next/navigation";
import { useState, useEffect } from "react";

const searchParams = useSearchParams();
const image = searchParams.get("image");
const router = useRouter();
const [file, setFile] = useState<File | null>(null);
//object still undefined... Have to specify type
const [information, setInformation] = useState<{object} | null>(null);

const handleBack = () => {
  router.push("/");
};

useEffect(() => {
    //get other info from backend
    async function fetchInfo() {
      
        const info = await fetch("http://localhost:8000/api/info")
        const response = await info.json();
        console.log(response);
    }
    fetchInfo();
  }, []);

function display() {
  if (file != null && information != null) {
    return (
      <div>
        <button className="backbutton">
          <img src={file} />
        </button>

        <div>
          {/* top nav bar div with just a top left back button and an info button for team members, with link to git source code*/}
          {/* needs to be a side by side view */}
          <div className="maincontent">
            <div>Image</div>
            <div>Information</div>
          </div>
        </div>
      </div>
    );
  }
  return <div>Sorry an error occured</div>;
}
