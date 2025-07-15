 ChatPDF AI

A Streamlit-based web application that allows users to upload PDF documents and interact with their content through an AI-powered chat interface.

## Features

- 📄 **PDF Upload**: Support for various PDF formats with text extraction
- 🤖 **AI Chat**: Powered by OpenAI's GPT-4o model for intelligent conversations
- 💬 **Chat History**: Maintains conversation context throughout the session
- 🔍 **Smart Responses**: AI answers questions based solely on PDF content
- ⚡ **Real-time Processing**: Instant text extraction and response generation
- 🛡️ **Error Handling**: Comprehensive error management for various edge cases

## Installation

### Prerequisites
<img width="1109" height="812" alt="Screenshot 2025-07-15 172807" src="https://github.com/user-attachments/assets/b93c6565-91fc-4a8d-a994-014e84a661cb" />


- Python 3.8 or higher
- OpenAI API key (get one at [OpenAI Platform](https://platform.openai.com/))

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd chatpdf-ai
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit openai PyPDF2
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

## Usage

1. **Start the application**: Run `streamlit run main.py` in your terminal
2. **Upload a PDF**: Use the sidebar to upload your PDF document
3. **Wait for processing**: The app will extract text from your PDF automatically
4. **Start chatting**: Ask questions about the document content in the chat interface
5. **Get AI responses**: The AI will answer based on the PDF content

## Project Structure

```
chatpdf-ai/
├── main.py              # Main Streamlit application
├── pdf_processor.py     # PDF text extraction logic
├── chat_handler.py      # OpenAI API integration
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── .env.example         # Environment variables template
└── README.md           # This file
```

## Configuration

### Streamlit Configuration
The app is configured to run on port 5000 with the following settings in `.streamlit/config.toml`:

```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000
```


### Environment Variables
Required environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for AI chat functionality

Some Features:

- <img width="1122" height="813" alt="Screenshot 2025-07-15 172833" src="https://github.com/user-attachments/assets/038db78d-43e6-4d56-873e-7ecabf8e42dd" />
<img width="255" height="303" alt="Screenshot 2025-07-15 172851" src="https://github.com/user-attachments/assets/e2a987d0-8d95-4a82-8706-7bce74c428b5" />





