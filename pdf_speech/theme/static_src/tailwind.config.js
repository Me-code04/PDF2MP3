/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html",
    "../../pdf_app/templates/**/*.html",
    "./src/**/*.{html,js}"
  ],
  theme: { extend: {} },
  plugins: [require("daisyui")]
};
