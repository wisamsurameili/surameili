@echo off

REM Find and terminate the Python process
taskkill /F /IM python.exe /T

REM Optional: Display a message once the process is terminated
echo Python process terminated.

REM Optional: Pause the script before exiting
pause
