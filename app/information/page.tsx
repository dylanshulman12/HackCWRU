"use client";

import { Suspense } from "react";
import Display from "./Display";

export default function Page() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Display />
    </Suspense>
  );
}
