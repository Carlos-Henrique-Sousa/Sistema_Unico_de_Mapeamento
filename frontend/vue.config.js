// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
      '@components': resolve(__dirname, 'src/components'),
      '@views': resolve(__dirname, 'src/views'),
      '@composables': resolve(__dirname, 'src/composables'),
      '@stores': resolve(__dirname, 'src/store'),
      '@types': resolve(__dirname, 'src/types'),
      '@services': resolve(__dirname, 'src/services'),
      '@assets': resolve(__dirname, 'src/assets')
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    },
    port: 8080,
    hot: true
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@assets/css/variables.scss";`
      }
    }
  },
  build: {
    sourcemap: false,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['vue', 'vue-router', 'pinia'],
          charts: ['chart.js', 'vue-chartjs']
        }
      }
    }
  }
})