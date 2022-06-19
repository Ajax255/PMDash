/** @type {import('tailwindcss').Config} */
module.exports = {
  plugins: [require('@tailwindcss/forms')],
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
}
