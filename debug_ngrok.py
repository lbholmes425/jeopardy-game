from pyngrok import ngrok, conf
import sys
import os

print(f"Python Executable: {sys.executable}")
print(f"Path: {os.environ.get('PATH')}")

try:
    # Try locating the binary
    print("Checking ngrok installation...")
    path = ngrok.conf.get_default().ngrok_path
    print(f"Default ngrok path: {path}")
    
    # Try connecting
    print("Attempting to connect...")
    url = ngrok.connect(5001).public_url
    print(f"SUCCESS! Url: {url}")
    ngrok.kill()
except Exception as e:
    print(f"ERROR: {e}")
