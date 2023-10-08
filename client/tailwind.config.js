/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
        lora: ['Lora', 'san-serif'],
      },
      boxShadow: {
        full: '0px 0px 5px 1px rgba(0,0,0,0.2)',
      },
    },
  },
  plugins: [],
};
