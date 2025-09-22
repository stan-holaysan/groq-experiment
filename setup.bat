@echo off
echo Setting up Chat Application...
echo.

echo 1. Setting up Backend...
cd backend
echo Creating virtual environment...
py -m venv venv
call venv\Scripts\activate.bat
echo Installing Python dependencies...
pip install -r requirements.txt
echo.
echo Backend setup complete!
echo Don't forget to:
echo - Copy .env.example to .env
echo - Add your Groq API key to .env
echo - Run: uvicorn main:app --reload
echo.

echo 2. Setting up Frontend...
cd ..\frontend
echo Installing Node.js dependencies...
npm install
echo.
echo Frontend setup complete!
echo Run: npm run dev
echo.

echo Setup complete! 
echo.
echo Next steps:
echo 1. Get a Groq API key from https://console.groq.com/
echo 2. Copy backend\.env.example to backend\.env
echo 3. Add your API key to backend\.env
echo 4. Start backend: cd backend && uvicorn main:app --reload
echo 5. Start frontend: cd frontend && npm run dev
echo.
pause
