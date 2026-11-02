$params = @{
    FilePath = "C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe"
    WorkingDirectory = "D:\opencode\fake_news_detection-main"
    ArgumentList = "-c `"`import sys; sys.path.insert(0, '.'); import os; os.chdir('.'); from app import app; app.run(host='0.0.0.0', port=5000, debug=False)`""
}
Start-Process @params