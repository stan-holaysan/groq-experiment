# 💬 Chat Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Node.js](https://img.shields.io/badge/Node.js-16+-green.svg)](https://nodejs.org/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.0+-4FC08D.svg)](https://vuejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/Groq-API-orange.svg)](https://groq.com/)

A modern, responsive chat application built with Vue.js frontend and FastAPI backend, integrated with Groq LLM for intelligent conversations.

![Chat Application Screenshot] <img width="922" height="580" alt="image" src="https://github.com/user-attachments/assets/0c2225b0-b3af-42af-8299-4898950022eb" />

## 🚀 Features

### Core Features
- **Clean, Modern UI**: Beautiful chat interface with gradient backgrounds and smooth animations
- **Chat Bubbles**: Distinct styling for user and AI messages with timestamps
- **Real-time Messaging**: Instant communication with the AI assistant
- **Loading Indicators**: Visual feedback while waiting for AI responses
- **Error Handling**: Comprehensive error messages and connection status
- **Clear Chat**: Reset conversation with a single click
- **Responsive Design**: Works perfectly on desktop and mobile devices

### Technical Features
- **Auto-scroll**: Automatically scrolls to newest messages
- **Message Animations**: Smooth enter animations for new messages
- **Custom Scrollbar**: Styled scrollbar for better UX
- **Health Checks**: Backend connectivity monitoring
- **CORS Support**: Proper cross-origin resource sharing setup

## 🛠️ Tech Stack
- **Frontend**: Vue.js 3 with Composition API
- **Styling**: Tailwind CSS with custom animations
- **Backend**: FastAPI with async support
- **LLM**: Groq API (Llama 3 8B model)
- **HTTP Client**: Axios for API communication
- **Build Tool**: Vite for fast development

## 📋 Prerequisites
- Python 3.8+ 
- Node.js 16+
- Groq API key (get one at [console.groq.com](https://console.groq.com/))

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
1. Run the setup script: `setup.bat`
2. Get your Groq API key from [console.groq.com](https://console.groq.com/)
3. Copy `backend\.env.example` to `backend\.env`
4. Add your API key to `backend\.env`: `GROQ_API_KEY=your_key_here`
5. Run the start script: `start.bat`

### Option 2: Manual Setup

#### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your Groq API key
uvicorn main:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🌐 Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the backend directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### API Endpoints
- `GET /`: Root endpoint
- `GET /health`: Health check and configuration status
- `POST /chat`: Send message and receive AI response

## 🎨 UI Components

### Chat Interface
- **Header**: App title with clear chat button
- **Message Area**: Scrollable container with chat bubbles
- **Input Area**: Text input with send button
- **Loading State**: Animated dots while AI is thinking
- **Error Display**: User-friendly error messages

### Styling Features
- **Gradient Backgrounds**: Beautiful blue gradient theme
- **Smooth Animations**: Message enter animations and loading states
- **Responsive Layout**: Adapts to different screen sizes
- **Custom Scrollbar**: Styled scrollbar for better aesthetics

## 🔍 Troubleshooting

### Common Issues
1. **Backend won't start**: Check if Python and pip are installed
2. **Frontend won't start**: Check if Node.js and npm are installed
3. **API connection failed**: Ensure backend is running on port 8000
4. **Groq API errors**: Verify your API key is correct and has credits

### Error Messages
- **"Cannot connect to backend"**: Backend server is not running
- **"Groq API key not configured"**: Missing or invalid API key
- **"Server error"**: Check backend logs for detailed error information

## 📁 Project Structure
```
chat-app/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example        # Environment variables template
│   └── .env                # Your environment variables (create this)
├── frontend/
│   ├── src/
│   │   ├── App.vue         # Main Vue component
│   │   ├── main.js         # Vue app entry point
│   │   └── style.css       # Tailwind CSS and custom styles
│   ├── package.json        # Node.js dependencies
│   ├── vite.config.js      # Vite configuration
│   ├── tailwind.config.js  # Tailwind CSS configuration
│   └── index.html          # HTML template
├── setup.bat               # Automated setup script
├── start.bat               # Start both servers
└── README.md               # This file
```

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

### Quick Contribution Guide
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 🐛 Issues and Support

- **Bug Reports**: Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- **Feature Requests**: Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- **Security Issues**: See our [Security Policy](SECURITY.md)

## 🏆 Contributors

Thanks to all the contributors who have helped make this project better!

<!-- Contributors will be automatically added here -->

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/chat-app?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/chat-app?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/chat-app)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/chat-app)

## 🗺️ Roadmap

### Upcoming Features
- [ ] User authentication and profiles
- [ ] Message persistence and history
- [ ] File upload and sharing
- [ ] Multiple AI model support
- [ ] Dark mode theme
- [ ] Mobile app (React Native)

See the [open issues](https://github.com/yourusername/chat-app/issues) for a full list of proposed features and known issues.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing the LLM API
- [Vue.js](https://vuejs.org/) for the reactive frontend framework
- [FastAPI](https://fastapi.tiangolo.com/) for the high-performance backend framework
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework

## 📞 Contact

- Create an [issue](https://github.com/yourusername/chat-app/issues) for bug reports or feature requests
- Start a [discussion](https://github.com/yourusername/chat-app/discussions) for questions or ideas

---

⭐ **Star this repository if you found it helpful!**
