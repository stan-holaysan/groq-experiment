# 🚀 Quick Start Guide

Get the Chat Application running in under 5 minutes!

## ⚡ Prerequisites Check

Make sure you have these installed:
- [ ] **Python 3.8+** - Check with `python --version`
- [ ] **Node.js 16+** - Check with `node --version`
- [ ] **Git** - Check with `git --version`

## 🔑 Get Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (you'll need it in step 4)

## 📥 Clone and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/chat-app.git
cd chat-app
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd ../frontend
npm install
```

### 4. Configure Environment
```bash
cd ../backend
cp .env.example .env
```

Edit the `.env` file and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 🎯 Start the Application

### Option 1: Use Start Script (Windows)
```bash
# From the root directory
start.bat
```

### Option 2: Manual Start
**Terminal 1 - Backend:**
```bash
cd backend
# Activate virtual environment first
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

## 🌐 Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## ✅ Test It Works

1. Open http://localhost:5173 in your browser
2. Type a message like "Hello, how are you?"
3. Press Send
4. You should see an AI response!

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check Python version: `python --version`
- Make sure virtual environment is activated
- Verify all dependencies installed: `pip list`

**Frontend won't start:**
- Check Node.js version: `node --version`
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`

**API connection failed:**
- Ensure backend is running on port 8000
- Check if Groq API key is correctly set in `.env`
- Verify no firewall blocking the connection

**Groq API errors:**
- Verify API key is valid and has credits
- Check [Groq status page](https://status.groq.com/) for service issues

### Getting Help

1. Check the [full README](README.md) for detailed instructions
2. Look at [common issues](https://github.com/yourusername/chat-app/issues)
3. Create a new issue with:
   - Your operating system
   - Python and Node.js versions
   - Error messages
   - Steps you tried

## 🎉 You're Ready!

Congratulations! You now have a fully functional AI chat application running locally.

### Next Steps
- Read the [Contributing Guide](CONTRIBUTING.md) to make improvements
- Check out the [Deployment Guide](DEPLOYMENT.md) to deploy online
- Explore the codebase and add new features!

---

**Need help?** Create an issue or start a discussion on GitHub!
