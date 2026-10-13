# BDConnect Read-Only Showcase

Standalone demonstration of BDConnect using fictional workflow descriptions.

No patient records, database, OTP, payment gateway or report uploads.

## Render
Build: pip install -r requirements.txt
Start: gunicorn --bind 0.0.0.0:$PORT app:app
Health check: /health

The original BDConnect application is not included.
