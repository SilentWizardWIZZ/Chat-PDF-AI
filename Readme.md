# ChatPDF AI

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

## Technical Details

### PDF Processing
- Uses PyPDF2 library for text extraction
- Handles encrypted PDFs with appropriate error messages
- Supports multi-page documents
- Cleans and normalizes extracted text

### AI Integration
- Uses OpenAI's GPT-4o model (latest as of May 2024)
- Implements conversation context management
- Limits document content to avoid token limits
- Includes comprehensive error handling for API issues

### Session Management
- Stores chat history in Streamlit session state
- Maintains PDF content until new document upload
- Provides document clearing functionality

## Error Handling

The application handles various error scenarios:

- **Encrypted PDFs**: Clear error messages for password-protected files
- **Corrupted files**: Validation and error reporting for invalid PDFs
- **API issues**: Rate limiting, quota, and authentication error handling
- **Network problems**: Graceful degradation with user-friendly messages

## Limitations

- PDF content is truncated to 8000 characters to fit within API token limits
- Session data is not persistent across browser sessions
- Requires active internet connection for AI functionality
- Only processes text-based PDFs (image-based PDFs may not work properly)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the error messages in the application
2. Verify your OpenAI API key is valid and has sufficient credits
3. Ensure your PDF file is text-based and not corrupted
4. Review the console logs for detailed error information