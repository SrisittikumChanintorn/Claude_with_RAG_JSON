# Claude with RAG JSON

This project implements a specialized chatbot system that combines Large Language Models (Claude) with Retrieval Augmented Generation (RAG) using JSON data sources to create domain-specific conversational agents.

## Project Overview

The system works by:
1. Taking JSON files as input data sources
2. Converting JSON data into document format
3. Splitting documents into manageable chunks
4. Creating embeddings for these chunks through vectorization
5. Storing vectors in a Vector Database
6. Using this external knowledge to augment LLM responses

This approach allows the chatbot to provide accurate and detailed information beyond the LLM's original training data, making it ideal for specialized applications with specific knowledge requirements.

## Example Use Case: Fruit Shop Chatbot

This repository demonstrates the system with a fruit shop chatbot that can:
- Answer detailed questions about specific fruits
- Provide information on inventory, pricing, and product characteristics
- Make recommendations based on customer preferences
- Handle customer inquiries with domain-specific knowledge

## Repository Structure

- `main.py`: Main application entry point
- `chatbot.py`: Core chatbot implementation
- `fruit.json`: Sample JSON data containing fruit shop information
- `requirements.txt`: Dependencies required for the project

## How It Works

1. **Data Ingestion**: JSON files (like `fruit.json`) are loaded into the system
2. **Document Conversion**: JSON data is transformed into document format suitable for RAG processing
3. **Chunking**: Documents are split into appropriate segments for embedding
4. **Vectorization**: Text chunks are converted to vector embeddings
5. **Vector Storage**: Embeddings are stored in a vector database for efficient retrieval
6. **Query Processing**: When a user asks a question, relevant information is retrieved from the vector database
7. **Augmented Response**: The LLM (Claude) generates responses using both its base knowledge and the retrieved information

## Setup 🛠️

1. Clone this project to your repository:

2. Create Virtual Environment (optional but recommended)

3. Activate Virtual Environment (venv) or Select Python Interpreture 📦 
   
```bash
source venv/bin/activate  # On MacOS use this with CMD
venv\Scripts\activate     # On Windows use this with CMD
```

4. Install dependencies ⬇️
```bash
pip install -r requirements.txt
```

5. Configure API key 🔑
```bash   
# Generate API KEY from Claude and OpenAI website and define as a variable.
os.environ["ANTHROPIC_API_KEY"] =  "YOUR_API_KEY"  # Replace with your actual API key
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"      # Replace with your actual  API key
```

6. Run the analysis ▶️

```bash
python main.py
```
    


## Configuration

The system can be configured by modifying parameters in the configuration files:
- LLM API keys and endpoints
- Vector database settings
- Chunking and embedding parameters
- Response formatting options

## Custom Implementation

To adapt this system for your own specialized chatbot:
1. Replace `fruit.json` with your domain-specific JSON data
2. Adjust chunking parameters to suit your data characteristics
3. Modify prompt templates if necessary
4. Configure the system for your specific use case

## Benefits

- **Enhanced Accuracy**: Provides specific, accurate information beyond the LLM's training data
- **Domain Specialization**: Creates chatbots with deep knowledge in particular domains
- **Reduced Hallucinations**: RAG significantly reduces incorrect or fabricated information
- **Up-to-date Information**: Can incorporate the latest data without retraining the LLM
- **Customizable**: Easily adaptable to different domains by changing the input data
