# 📄 RAG Chat App - Similarity Search Tool

A powerful Retrieval-Augmented Generation (RAG) application that combines document processing, semantic search, and conversational AI using Streamlit, Pinecone, and SentenceTransformers.

## Features

✨ **Document Processing**
- Support for multiple file formats: PDF, DOCX, and TXT
- Automatic text extraction and chunking
- Efficient batch processing

🔍 **Semantic Search**
- Vector embeddings using SentenceTransformers
- Cosine similarity matching
- Fast retrieval from Pinecone vector database

💬 **RAG Chat Interface**
- Interactive chat interface built with Streamlit
- Context-aware responses based on uploaded documents
- Real-time document indexing

🚀 **Performance**
- Cached embedding model for faster inference
- Serverless Pinecone infrastructure
- Optimized vector search with cosine metric

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8+**
- **Pinecone API Key** - Get it from [Pinecone Console](https://app.pinecone.io)
- **Internet connection** (for downloading models and API access)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sourabh-Narvariya/Similarity_Search_Tool.git
cd Similarity_Search_Tool
```

### 2. Create a Virtual Environment

```bash
# Using Python venv
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` and add your Pinecone API key:

```
PINECONE_API_KEY=your_pinecone_api_key_here
```

> **⚠️ Important**: Never commit `.env` to version control. Use `.env.example` as a template for documentation.

## Usage

### Run the Application

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`

### How to Use

1. **Upload Documents**: Use the sidebar to upload PDF, DOCX, or TXT files
2. **Process**: The app automatically chunks and embeds your documents
3. **Search**: Ask questions about your documents in the chat interface
4. **Get Answers**: The app retrieves relevant document sections and provides context-aware responses

## Project Structure

```
Similarity_Search_Tool/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project configuration
├── .env.example        # Template for environment variables
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── .venv/              # Virtual environment (not in git)
```

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web UI framework for the chat application |
| **Pinecone** | Vector database for semantic search |
| **SentenceTransformers** | Generate embeddings (all-MiniLM-L6-v2 model) |
| **PyPDF** | Extract text from PDF files |
| **python-docx** | Extract text from DOCX files |
| **python-dotenv** | Load environment variables from .env |

## Configuration

### Embedding Model
- **Model**: `all-MiniLM-L6-v2` (384-dimensional embeddings)
- **Framework**: SentenceTransformers
- **Performance**: Fast, efficient, suitable for RAG tasks

### Pinecone Setup
- **Index Name**: `rag-chat-index`
- **Dimension**: 384
- **Metric**: Cosine similarity
- **Infrastructure**: Serverless on AWS (us-east-1)

## API Keys & Secrets

### Getting Pinecone API Key

1. Go to [Pinecone Console](https://app.pinecone.io)
2. Sign up or log in
3. Create a new project
4. Copy your API key
5. Add it to `.env` file

### For Streamlit Cloud Deployment

If deploying on Streamlit Cloud, add secrets in the app settings:

```
PINECONE_API_KEY = your_api_key_here
```

## Troubleshooting

### Issue: `ImportError: cannot import name 'ServerlessSpec'`

**Solution**: Update the Pinecone package to the latest version:
```bash
pip install --upgrade pinecone
```

### Issue: "Pinecone API key not found"

**Solution**: Ensure `.env` file exists and contains:
```
PINECONE_API_KEY=your_actual_key
```

### Issue: Slow embedding generation

**Solution**: The first run downloads the model (~50MB). Subsequent runs use cache. Consider pre-loading the model on server startup.

### Issue: Rate limiting from Pinecone

**Solution**: Check your Pinecone plan limits and upgrade if needed.

## Performance Tips

- 📊 **Batch Processing**: Upload multiple documents together for efficiency
- 💾 **Caching**: Models are cached using Streamlit's `@st.cache_resource`
- 🔄 **Chunking**: Documents are automatically chunked for better retrieval
- 🎯 **Vector Size**: 384-dimensional embeddings are optimized for speed and accuracy

## Future Enhancements

- [ ] Support for more file formats (Excel, PowerPoint)
- [ ] Advanced chunking strategies (semantic chunking)
- [ ] Multi-language support
- [ ] Chat history persistence
- [ ] Custom embedding models
- [ ] Integration with LLMs for better responses
- [ ] Document metadata filtering
- [ ] Export conversation history

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact & Support

For issues, questions, or suggestions:
- 📧 Email: narvariya@example.com (replace with your email)
- 🐛 GitHub Issues: [Report a bug](https://github.com/Sourabh-Narvariya/Similarity_Search_Tool/issues)

## Acknowledgments

- [Streamlit](https://streamlit.io/) - Interactive web framework
- [Pinecone](https://www.pinecone.io/) - Vector database
- [Hugging Face](https://huggingface.co/) - SentenceTransformers models
- [PyPDF & python-docx](https://github.com) - Document processing libraries

---

**Made with ❤️ by Sourabh Narvariya**

⭐ If you find this project helpful, please consider giving it a star!

