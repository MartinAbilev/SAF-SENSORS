const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:
  {
    port: process.env.VUE_APP_PORT || 3333, // Use the port from the environment variable or fall back to 3333
  }

})
