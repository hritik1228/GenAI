# GenAI Learning Project

Welcome to my **Generative AI Learning Journey**! This repository documents my exploration and experimentation with modern GenAI technologies.

## 📚 What I'm Learning

- **LangChain Framework** - Building AI chains and workflows
  - Simple chains for basic operations
  - Sequential chains for multi-step processes
  - Parallel chains for concurrent execution
  - Conditional chains for decision-based logic

- **LLM Models** - Working with cutting-edge language models
  - Google Gemini API integration
  - Model selection and configuration
  - Prompt engineering best practices

- **Generative AI Concepts**
  - Chaining multiple AI operations
  - Embeddings and vector operations
  - RAG (Retrieval-Augmented Generation)
  - Prompt optimization

## 📁 Project Structure

```
GenAI/
├── config.py                 # Configuration and API key management
├── requirements.txt          # Python dependencies
├── LangChain/
│   ├── langchain-chains/     # Various chain implementations
│   │   ├── simple-chain.py
│   │   ├── sequential_chain.py
│   │   ├── parallel_chain.py
│   │   ├── conditional_chain.py
│   │   └── model.py
│   └── langchain-models/     # Model implementations
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key (see `.env.example` for template)
   ```bash
   cp .env.example .env
   ```

4. Add your API key to `.env`

### Running Examples

```bash
# Run a simple chain
cd LangChain/langchain-chains
python simple-chain.py

# Run sequential chain
python sequential_chain.py

# Run parallel chain
python parallel_chain.py
```

## 🔑 API Key Setup

**Important:** Never commit your API keys! Store them securely:

1. Create a `.env` file in the root directory
2. Add your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   GEMINI_MODEL=gemini-2.5-flash
   ```
3. Add `.env` to `.gitignore`

See `config.py` for usage details.

## 📝 Key Learnings

- How to structure LLM applications with chains
- Building complex workflows with multiple LLMs
- Error handling and fallback strategies
- API integration and configuration management

## 🛠️ Technologies Used

- **LangChain** - LLM framework for building chains
- **Google Gemini API** - Advanced language model
- **Python 3** - Programming language
- **python-dotenv** - Environment variable management

## 📖 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [AI/ML Best Practices](https://cloud.google.com/ai-hub)

## 💡 Next Steps

- [ ] Implement RAG with embeddings
- [ ] Add streaming responses
- [ ] Build a multi-turn conversation system
- [ ] Integrate memory/chat history
- [ ] Deploy as a service

## 📄 License

Personal Learning Project

---

*Last Updated: December 2025*
