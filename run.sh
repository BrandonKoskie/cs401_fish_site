#!/bin/bash
echo "🌊 Starting Hawaii Seafood Watch..."
echo "Seeding database..."
python3 seed.py
echo "Starting server at http://127.0.0.1:5001"
echo "Press Ctrl+C to stop"
python3 -m flask --app api/app.py run --debug --port 5001
