import streamlit as st
import os
from pdf_processor import PDFProcessor
from chat_handler import ChatHandler

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""
if "pdf_filename" not in st.session_state:
    st.session_state.pdf_filename = ""


def main():
    st.set_page_config(page_title="ChatPDF AI", page_icon="📄", layout="wide")

    st.title("📄 ChatPDF AI")
    st.subheader("Upload a PDF and Chat With It")

    # Sidebar for PDF upload
    with st.sidebar:
        st.header("📁 Upload PDF")
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type="pdf",
            help="Upload a PDF file to start chatting with its content")

        if uploaded_file is not None:
            # Process PDF if it's a new file
            if uploaded_file.name != st.session_state.pdf_filename:
                with st.spinner("Processing PDF..."):
                    try:
                        processor = PDFProcessor()
                        text = processor.extract_text(uploaded_file)

                        if text.strip():
                            st.session_state.pdf_text = text
                            st.session_state.pdf_filename = uploaded_file.name
                            st.session_state.messages = [
                            ]  # Clear previous chat
                            st.success(
                                f"✅ PDF '{uploaded_file.name}' processed successfully!"
                            )
                            st.info(
                                f"Document contains {len(text.split())} words")
                        else:
                            st.error(
                                "❌ No text could be extracted from this PDF. Please try a different file."
                            )
                            st.session_state.pdf_text = ""
                            st.session_state.pdf_filename = ""
                    except Exception as e:
                        st.error(f"❌ Error processing PDF: {str(e)}")
                        st.session_state.pdf_text = ""
                        st.session_state.pdf_filename = ""

        # Display current document info
        if st.session_state.pdf_filename:
            st.markdown("---")
            st.markdown("**Current Document:**")
            st.markdown(f"📄 {st.session_state.pdf_filename}")
            if st.button("🗑️ Clear Document"):
                st.session_state.pdf_text = ""
                st.session_state.pdf_filename = ""
                st.session_state.messages = []
                st.rerun()

    # Main chat interface
    if not st.session_state.pdf_text:
        st.info(
            "👆 Please upload a PDF file using the sidebar to start chatting!")
        st.markdown("""
        ### How to use ChatPDF AI:
        1. **Upload a PDF** using the file uploader in the sidebar
        2. **Wait for processing** - the text will be extracted automatically
        3. **Start chatting** - ask questions about the document content
        4. **View responses** - get AI-powered answers based on your PDF
        
        ### Supported features:
        - ✅ Text extraction from PDF documents
        - ✅ AI-powered question answering
        - ✅ Conversation history
        - ✅ Real-time responses
        - ✅ Error handling and validation
        """)
    else:
        # Chat interface
        st.markdown("### 💬 Chat with your PDF")

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("Ask a question about your PDF..."):
            # Add user message to chat history
            st.session_state.messages.append({
                "role": "user",
                "content": prompt
            })
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate AI response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        chat_handler = ChatHandler()
                        response = chat_handler.get_response(
                            question=prompt,
                            pdf_text=st.session_state.pdf_text,
                            chat_history=st.session_state.
                            messages[:-1]  # Exclude current message
                        )
                        st.markdown(response)

                        # Add assistant response to chat history
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response
                        })

                    except Exception as e:
                        error_msg = f"❌ Error generating response: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg
                        })


if __name__ == "__main__":
    main()