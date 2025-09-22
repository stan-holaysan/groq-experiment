@echo off
echo Starting Chat Application...
echo.

echo Starting Backend Server...
start "Backend Server" cmd /k "cd backend && venv\Scripts\activate && uvicorn main:app --reload"

timeout /t 3 /nobreak > nul

echo Starting Frontend Development Server...
start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo.
echo Both servers are starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Press any key to exit...
pause > nul
