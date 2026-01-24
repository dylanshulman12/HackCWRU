import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  reactStrictMode: true,
  allowedDevOrigins: [
    'http://192.168.122.1:3000',   // the origin that triggered the warning
    'http://localhost:3000'        // optional: your local browser
  ],
};

export default nextConfig;
