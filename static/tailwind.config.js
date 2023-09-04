/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html"],
  theme: {
    extend: {
      colors: {
      'green': '#aec7a9',
      'link-hover': 'gray-500'
      },

      width: {
        'logoSize': 'calc((1vw + 1vh + .5vmin) * 8)',
        'footer-logo': '20px',
        'header-logo': '25px'
      },

      fontSize: {
        'relativeSize': 'calc(1vw + 1vh + .5vmin)',
        'headerLink': 'calc((1vw + 1vh + .5vmin) * 0.65)',
        'main-title-xs': '48px',
        'aboutAsHeader': 'calc((1vw + 1vh + .5vmin) * 0.84)',
        'aboutAsSize': 'calc((1vw + 1vh + .5vmin) * 0.82)',
      },
      padding: {
        big: '50px'
      },
      screens: {
        s: '320px',
        sm: '480px',
        xsm: '640px',
        md: '768px',
        xmd: '930px',
        lg: '1028px',
        xlg:'1200px',
        xl: '1440px'
      },
      fontWeight: {
        'linkHeaderWeight': 'font-semibold'
      },

  }
  },
  plugins: [],
}