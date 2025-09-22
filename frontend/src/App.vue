<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
    <div class="w-full max-w-4xl bg-white rounded-2xl shadow-2xl overflow-hidden">
      <!-- Header -->
      <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
              </svg>
            </div>
            <div>
              <h1 class="text-xl font-bold">AI Chat Assistant</h1>
              <p class="text-blue-100 text-sm">Powered by Groq</p>
            </div>
          </div>
          <button
            @click="clearChat"
            class="bg-white/20 hover:bg-white/30 text-white px-4 py-2 rounded-lg transition-colors duration-200 flex items-center space-x-2"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
            </svg>
            <span>Clear</span>
          </button>
        </div>
      </div>

      <!-- Chat Messages Container -->
      <div 
        ref="chatContainer"
        class="chat-container h-96 overflow-y-auto p-6 space-y-4 bg-gray-50"
      >
        <!-- Welcome Message -->
        <div v-if="messages.length === 0" class="text-center py-12">
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
            </svg>
          </div>
          <h3 class="text-lg font-semibold text-gray-700 mb-2">Welcome to AI Chat!</h3>
          <p class="text-gray-500">Start a conversation by typing a message below.</p>
        </div>

        <!-- Chat Messages -->
        <TransitionGroup name="message" tag="div">
          <div
            v-for="message in messages"
            :key="message.id"
            :class="[
              'flex',
              message.type === 'user' ? 'justify-end' : 'justify-start'
            ]"
          >
            <div
              :class="[
                'max-w-xs lg:max-w-md px-4 py-3 rounded-2xl shadow-sm',
                message.type === 'user'
                  ? 'bg-blue-600 text-white rounded-br-md'
                  : 'bg-white text-gray-800 rounded-bl-md border border-gray-200'
              ]"
            >
              <p class="text-sm leading-relaxed whitespace-pre-wrap">{{ message.content }}</p>
              <p 
                :class="[
                  'text-xs mt-2',
                  message.type === 'user' ? 'text-blue-100' : 'text-gray-500'
                ]"
              >
                {{ formatTime(message.timestamp) }}
              </p>
            </div>
          </div>
        </TransitionGroup>

        <!-- Loading Indicator -->
        <div v-if="isLoading" class="flex justify-start">
          <div class="bg-white text-gray-800 rounded-2xl rounded-bl-md border border-gray-200 px-4 py-3 shadow-sm">
            <div class="flex items-center space-x-2">
              <div class="flex space-x-1">
                <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.1s"></div>
                <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
              </div>
              <span class="text-sm text-gray-500">AI is thinking...</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Input Area -->
      <div class="p-6 bg-white border-t border-gray-200">
        <form @submit.prevent="sendMessage" class="flex space-x-4">
          <div class="flex-1 relative">
            <input
              v-model="newMessage"
              type="text"
              placeholder="Type your message here..."
              :disabled="isLoading"
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all duration-200 disabled:bg-gray-100 disabled:cursor-not-allowed"
              @keydown.enter.prevent="sendMessage"
            />
          </div>
          <button
            type="submit"
            :disabled="!newMessage.trim() || isLoading"
            class="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed text-white px-6 py-3 rounded-xl transition-colors duration-200 flex items-center space-x-2 font-medium"
          >
            <svg v-if="!isLoading" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
            </svg>
            <svg v-else class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
            </svg>
            <span>{{ isLoading ? 'Sending...' : 'Send' }}</span>
          </button>
        </form>

        <!-- Error Message -->
        <div v-if="errorMessage" class="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg">
          <div class="flex items-center space-x-2">
            <svg class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <p class="text-red-700 text-sm">{{ errorMessage }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, nextTick, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'App',
  setup() {
    const messages = ref([])
    const newMessage = ref('')
    const isLoading = ref(false)
    const errorMessage = ref('')
    const chatContainer = ref(null)
    const messageIdCounter = ref(0)

    // API base URL
    const API_BASE_URL = 'http://localhost:8000'

    // Format timestamp
    const formatTime = (timestamp) => {
      const date = new Date(timestamp)
      return date.toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: true 
      })
    }

    // Scroll to bottom of chat
    const scrollToBottom = () => {
      nextTick(() => {
        if (chatContainer.value) {
          chatContainer.value.scrollTop = chatContainer.value.scrollHeight
        }
      })
    }

    // Add message to chat
    const addMessage = (content, type, timestamp = new Date().toISOString()) => {
      messages.value.push({
        id: messageIdCounter.value++,
        content,
        type,
        timestamp
      })
      scrollToBottom()
    }

    // Send message to API
    const sendMessage = async () => {
      if (!newMessage.value.trim() || isLoading.value) return

      const userMessage = newMessage.value.trim()
      newMessage.value = ''
      errorMessage.value = ''

      // Add user message
      addMessage(userMessage, 'user')

      // Set loading state
      isLoading.value = true

      try {
        const response = await axios.post(`${API_BASE_URL}/chat`, {
          message: userMessage
        }, {
          timeout: 30000 // 30 second timeout
        })

        if (response.data.success) {
          // Add bot response
          addMessage(response.data.response, 'bot', response.data.timestamp)
        } else {
          throw new Error(response.data.error || 'Unknown error occurred')
        }
      } catch (error) {
        console.error('Chat error:', error)
        
        let errorMsg = 'Failed to get response from AI. Please try again.'
        
        if (error.code === 'ECONNREFUSED') {
          errorMsg = 'Cannot connect to the server. Please make sure the backend is running.'
        } else if (error.response?.status === 500) {
          errorMsg = 'Server error. Please check if the Groq API key is configured.'
        } else if (error.response?.data?.detail) {
          errorMsg = error.response.data.detail
        }
        
        errorMessage.value = errorMsg
        
        // Add error message to chat
        addMessage('Sorry, I encountered an error. Please try again.', 'bot')
      } finally {
        isLoading.value = false
      }
    }

    // Clear chat
    const clearChat = () => {
      messages.value = []
      errorMessage.value = ''
    }

    // Check backend health on mount
    const checkBackendHealth = async () => {
      try {
        await axios.get(`${API_BASE_URL}/health`)
        console.log('Backend is healthy')
      } catch (error) {
        console.warn('Backend health check failed:', error.message)
        errorMessage.value = 'Cannot connect to backend. Please make sure the server is running on port 8000.'
      }
    }

    onMounted(() => {
      checkBackendHealth()
    })

    return {
      messages,
      newMessage,
      isLoading,
      errorMessage,
      chatContainer,
      sendMessage,
      clearChat,
      formatTime
    }
  }
}
</script>
