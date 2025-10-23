module.exports = {
  apps: [{
    name: 'penjualan-app',
    script: 'app.py',
    interpreter: 'python3',
    cwd: '/workspace',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      FLASK_ENV: 'production',
      HOST: '0.0.0.0',
      PORT: 8080
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_file: './logs/combined.log',
    time: true
  }]
};