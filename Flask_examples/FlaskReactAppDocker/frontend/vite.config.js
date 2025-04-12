import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000, // Ensure this line exists and is set to 3000
    host: '0.0.0.0', // If you need it accessible from outside the container
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        // ... other proxy settings
      },
    },
  },
  // ... other config
});