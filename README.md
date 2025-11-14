# Agentic Voice-to-Voice AI Assistant for Product Discovery

A multi-agent voice assistant for e-commerce product discovery using LangGraph, MCP tools, and RAG.

## Project Structure

```project/
├── graph/                      # CORE PIPELINE (Your work)
│   ├── router/                 # Intent extraction
│   ├── planner/                # Retrieval planning
│   ├── retriever/              # RAG Team modifies this
│   ├── answerer/               # Answer generation
│   ├── tools/                  # Web Search Team adds this
│   ├── models/                 # LLM management
│   ├── nodes.py                # Node implementations
│   ├── state.py                # State schema
│   └── graph.py                # Graph definition
│
├── voice/                      # Voice Team creates this
│   ├── asr.py                  # Speech-to-text
│   ├── tts.py                  # Text-to-speech
│   └── pipeline.py             # Voice pipeline
│
├── ui/                         # UI Team creates this
│   └── app.py                  # Streamlit app
│
├── scripts/                    # Data processing
│   └── extract_metadata.py    # RAG Team improves this
│
├── data/                       # Data storage
│   └── amazon_enriched.parquet
│
├── chroma_db/                  # Vector database
│
└── tests/                      # Test files
    ├── test_router.py
    ├── test_planner.py
    ├── test_retriever.py
    └── test_answerer.py
```
