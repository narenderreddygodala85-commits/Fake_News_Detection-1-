import sys
sys.path.insert(0, r'D:\opencode\fake_news_detection-main')
import os
os.chdir(r'D:\opencode\fake_news_detection-main')
from app import app
app.run(host='127.0.0.1', port=5000, debug=False)