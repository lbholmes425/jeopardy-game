#!/bin/bash
cd "$(dirname "$0")"

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not found."
    exit 1
fi

echo "Starting Tap & Table Jeopardy..."
echo "Detecting Local IP..."

# Get Local IP (simple method for echo)
IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | cut -d\  -f2 | head -1)

echo "Local IP: $IP"
echo "Starting Server..."

# Start Server in background
python3 app.py &
PID=$!

# Wait for server to start
sleep 3

# Open Host View
open "http://localhost:5001/host"

echo "Game is running!"
echo "Host View: http://localhost:5001/host"
echo "Player Join: http://$IP:5001/join"
echo "Close this window to stop the server."

# Wait for user to close
wait $PID
