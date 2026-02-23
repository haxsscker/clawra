@echo off
for /f "delims=" %%i in ('dir /o:-d /b "C:\Users\admin\.openclaw\workspace\skills\ai_girl\*.jpg" 2^>nul') do (
    echo C:\Users\admin\.openclaw\workspace\skills\ai_girl\%%i
    exit /b 0
)
echo No images found
exit /b 1
