/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: '#121212',
        secondary: '#1F1F1F',
        text: '#A0A0A0',
        accent: '#00FF88'
      },
      fontFamily: {
        title: ["Montserrat"]
      }
    },
  },
  plugins: []
}

