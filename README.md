RAG-AGENTIC-AI
This project is a simple but powerful demo of Retrieval-Augmented Generation (RAG) using Mistral AI models, wrapped in a clean Streamlit interface. The idea is straightforward: load a PDF, split it into meaningful chunks, embed those chunks, and then let a large language model answer questions based on the content — while showing you the sources it used.

What it does
- Loads a PDF (currently set to Ebook-Agentic-AI.pdf).
- Splits the text into chunks using a recursive character splitter (so sentences and paragraphs don’t get cut awkwardly).
- Creates embeddings with MistralAI.
- Stores them in a FAISS vector database for fast retrieval.
- Runs a RetrievalQA chain with mistral-large-latest to answer your questions.
- Displays the answer in a Streamlit app, along with the source snippets.

Tech stack
- Python 3.8+
- Streamlit for the UI
- LangChain for the RAG pipeline
- Mistral AI for embeddings + LLM
- FAISS for vector search
- dotenv for environment variables

Setup
- Clone the repo:
git clone https://github.com/your-username/RAG-AGENTIC-AI.git
cd RAG-AGENTIC-AI
- Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
- Install dependencies:
pip install -r requirements.txt
- Add your Mistral API key to a .env file:
MISTRAL_API_KEY=your_api_key_here



Run the app
Start Streamlit:
streamlit run app.py


Then open the link it gives you (usually http://localhost:8501) in your browser.
Type a question into the input box, and the app will:
- Search the PDF for relevant chunks
- Generate an answer using Mistral
- Show you the sources it pulled from

Example
Question:
What is Agentic AI?


Answer:
Agentic AI refers to systems capable of autonomous decision-making and reasoning...


Sources:
- Ebook-Agentic-AI.pdf (snippet from page X)

Contributing
This is just a starter project. If you have ideas for improvements — like supporting multiple PDFs, adding chat history, or plugging in other models — feel free to open an issue or submit a pull request.

License
MIT License. Do whatever you like with it.

Would you like me to also draft a requirements.txt file (with exact package versions pinned) so that anyone cloning your repo can get it running without dependency issues?
