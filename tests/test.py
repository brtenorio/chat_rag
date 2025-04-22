import pytest
from unittest.mock import patch, MagicMock
from langchain.prompts import PromptTemplate

@pytest.fixture
def mock_chain_response():
    return {"text": "This is the revised message."}

def test_prompt_template_renders_correctly():
    prompt_template = PromptTemplate(
        template="""Please revise the following message for {use_case}: {message}""",
        input_variables=["use_case", "message"]
    )

    result = prompt_template.format(use_case="email", message="helo world")
    assert "helo world" in result
    assert "email" in result

@pytest.fixture
def embedding_model():
    from chat_rag.embedding import embeddings
    model = embeddings
    return model

def test_embedding_dimension(embedding_model):
    """Test that the output embedding has the correct dimensionality."""
    input_text = "Check the dimensionality of this embedding."
    embedding = embedding_model.embed_query(input_text)

    expected_dimension = 768
    assert len(embedding) == expected_dimension, f"Embedding should have {expected_dimension} dimensions."

@pytest.fixture
def chat_model():
    from chat_rag.chat_model import LLMmodel
    llm = LLMmodel().load()
    return llm

def test_initial_response(chat_model):
    """Test that the chat model provides a welcome message or initial response."""
    response = chat_model.invoke("Hello")
    assert response is not None, "The chat model should provide a response to greetings."