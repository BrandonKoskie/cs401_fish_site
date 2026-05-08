#!/bin/bash
echo "=== Hawaii Seafood Guide Quick Test ==="
echo ""

# Check Python
echo "1. Checking Python..."
python3 --version

# Check virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies
echo "2. Installing dependencies..."
pip install -r requirements.txt -q

# Seed database
echo "3. Seeding database..."
python seed.py

# Start Flask in background
echo "4. Starting Flask server..."
python -m api.app &
FLASK_PID=$!
sleep 3

# Test endpoints
echo "5. Testing API endpoints..."
echo "  - Home page: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:5000/)"
echo "  - Basics page: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:5000/basics)"
echo "  - Overfished API: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:5000/api/overfished-areas)"
echo "  - Imported API: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:5000/api/imported-species)"
echo "  - Methods API: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:5000/api/fishing-methods)"

# Run pytest
echo "6. Running unit tests..."
python -m pytest test_api.py -v

# Cleanup
kill $FLASK_PID 2>/dev/null
echo ""
echo "=== Test Complete ==="
echo "Open http://localhost:5000/basics to view the site"
