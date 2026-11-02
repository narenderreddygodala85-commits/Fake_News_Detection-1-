$process = Start-Process -FilePath "C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe" -ArgumentList "D:\opencode\fake_news_detection-main\run_app.py" -WorkingDirectory "D:\opencode\fake_news_detection-main" -PassThru
Start-Sleep -Seconds 5
try {
    $result = Invoke-RestMethod "http://127.0.0.1:5000/api/health"
    Write-Output "Health: $result"
    $pred = Invoke-RestMethod -Method Post -ContentType "application/json" -Body "{\"text\":\"India launches Gaganyaan mission successfully\",\"ensemble\":true,\"fact_check_mode\":\"wikipedia\"}" "http://127.0.0.1:5000/predict"
    Write-Output "Predict: $pred"
}
catch {
    Write-Output "Error: $_"
}