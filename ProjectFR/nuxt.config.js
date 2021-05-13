let envFileName;

// Retrieve the right config file

envFileName = ".env";


export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    titleTemplate: '%s',
    title: 'Corrections' || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/logoBIT.ico' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
    "leaflet/dist/leaflet.css"
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    {
      src: '~/plugins/infiniteloading',
      ssr: false
    },
    {
      src: '~/plugins/vue-html2pdf',
      ssr: false
    },
    {
      src: '~/plugins/formatDate',
      ssr: false
    },
    {
      src: '~/plugins/editor',
      ssr: false
    },
    // {
    //   src: '~/plugins/axios',
    //   ssr: false
    // }
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/tailwindcss'
  ],
  tailwindcss: {
    configPath: '~/config/tailwind.config.js',
    cssPath: '~/assets/css/tailwind.css',
    purgeCSSInDev: false
  },

  auth: {
    strategies: {
      // local: {
      //   endpoints: {
      //     login: {
      //       url: '/api/v2/crud/qtusers/login',
      //       method: 'post',
      //       propertyName: 'token'
      //     },
      //     user: {
      //       url: 'api/v2/crud/qtusers/currentuser',
      //       method: 'post',
      //       propertyName: false
      //     }
      //   }
      //   // tokenRequired: true,
      //   // tokenType: 'bearer'
      // }
    }
  },


  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    ['@nuxtjs/dotenv'
      // ,
      //   {
      //     path: ".env",
      //     filename: envFileName
      //   }
    ],
    // Simple usage
    'nuxt-buefy',

    // Or you can customize
    ['nuxt-buefy', { css: false, materialDesignIcons: false }],

    ['nuxt-fontawesome', {
      imports: [
        {
          set: '@fortawesome/free-solid-svg-icons',
          icons: ['fas']
        },
        {
          set: '@fortawesome/free-brands-svg-icons',
          icons: ['fab']
        }
      ]
    }
    ],

  ],
  axios: {
    proxy: 'true'
  },
  proxy: {
    '/api/': {
      target: process.env.API_ENDPOINT,
      pathRewrite: { '^/api/': '' }
    }
  },
  // router: {
  //   middleware: 'checkLogin'
  // },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      if (ctx.isDev) {
        config.devtool = ctx.isClient ? 'source-map' : 'inline-source-map'
      }
    }
  }
}
