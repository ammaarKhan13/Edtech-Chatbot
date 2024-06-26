

---

# Edtech Chatbot

This repository contains an Edtech Chatbot that provides answers to questions based on a dataset of approximately 100 prompt-response pairs. The chatbot is built using the LangChain framework, Google's Palm language model, HuggingFace embeddings, and FAISS for vector storage and retrieval. The application is deployed on a Streamlit server.

## Features

- **Data Loading**: Load data from a CSV file with prompt-response pairs.
- **Vector Storage**: Use FAISS to store and retrieve document vectors.
- **Question Answering**: Use a QA chain to generate answers based on the context provided in the CSV file.
- **Streamlit Integration**: Interactive web application for querying the chatbot.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/edtech-chatbot.git
   cd edtech-chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables. Create a `.env` file in the root directory of the repository and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run Main.py
   ```

2. Open your web browser and go to `http://localhost:8501`. You will see the title "Edtech Platform Q&A 🌱".

3. Click the "Create Knowledgebase" button to load the data and create the vector database.

4. Enter a question in the text input box and press Enter. The chatbot will provide an answer based on the context from the CSV file.

## File Descriptions

- **helper.py**: Contains functions to create the vector database from a CSV file and to set up the QA chain using LangChain and other libraries.
- **Main.py**: The main script for the Streamlit application, which includes the UI components and interaction logic.
- **requirements.txt**: Lists all the dependencies required for the project.

## How It Works

1. **Data Loading**: The `CSVLoader` from LangChain is used to load data from `data.csv`, which contains the prompts and responses.
2. **Vector Storage**: FAISS is used to store the document embeddings, which are generated using HuggingFace embeddings.
3. **Question Answering**: A retrieval-based QA chain is created using the Google Palm language model. The QA chain retrieves relevant documents from the vector database and generates answers based on the provided context.
4. **Streamlit Integration**: The Streamlit interface allows users to interact with the chatbot, create the knowledgebase, and ask questions.

## Deployment

The Edtech Chatbot is deployed on a Streamlit server, which makes it accessible via a web browser. This deployment ensures that users can easily interact with the chatbot and get responses based on the dataset.
Here is the link: https://edtech-chatbot-ammaarkhan.streamlit.app/

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
