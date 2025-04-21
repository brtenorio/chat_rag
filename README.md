# URL
[View and Use the app with this link](https://chatrag-production.up.railway.app/)   👈👈👈


# Interactive Chatbot with PDF and URL Loader

## Overview
This project is an interactive chatbot built using LangChain with Streamlit that allows users to upload a PDF document or provide a URL to engage in multi-turn conversations. The chatbot can answer questions based on the content of the uploaded PDF or the content fetched from the provided URL, maintaining context throughout the conversation. You can chose between Anthropic's Sonet and Haiku models, along with the maximum number of tokens.

## Features
- **PDF Upload**: Users can upload a PDF file, and the chatbot will extract and utilize its content.
- **URL Input**: Users can provide a valid URL, and the chatbot will simulate fetching content from it.
- **Multi-Turn Conversations**: The chatbot retains context across multiple interactions, allowing for a natural conversational flow.
- **Interactive Interface**: Built with Streamlit for a user-friendly experience.

## Technologies Used
- Python
- Streamlit
- PyPDF2
- LangChain
- Anthropic API
- Chroma db (for vector storage)

## Installation
To install and set up the project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/brtenorio/Dog_Breed_Classifier
    cd Dog_Breed_Classifier
    ```

2. **Install Poetry (if not already installed):**
    ```sh
    pip install poetry==1.8.3 
    ```

3. **Set up the virtual environment and install dependencies:**
    ```sh
    make all
    ```

## Usage

To run the application, use:

    make run-app

## Development

To retrain the model, if needed, use:

    make retrain-model

Notice the trained model is already available in `saved_models/model.h5`. 

## Running Tests

To test the model, use:

    make test

## Docker

To containerize the application, use:

    make docker-build

followed by
    
    make docker-run-app

## API built with FastAPI

To run the API with docker, use

    make docker-run-api
