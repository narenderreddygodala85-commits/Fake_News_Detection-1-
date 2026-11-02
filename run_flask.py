#!/usr/bin/env python
import subprocess
import sys

# Start Flask app as subprocess
proc = subprocess.Popen(
    [sys.executable, "app.py"],
    cwd="D:\\opencode\\fake_news_detection-main",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)

print("Flask app started with PID: " + str(proc.pid))
print("Access at: http://127.0.0.1:5000")

# Wait a bit then test
import time
time.sleep(3)

# Test if it's running
import requests
try:
    resp = requests.get("http://127.0.0.1:5000/api/health", timeout=5)
    print("Health check:", resp.status_code, resp.json())
except Exception as e:
    print("Could not connect yet, app still starting...")
    
# Keep the script running
proc.wait()