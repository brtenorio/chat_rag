if __name__=="__main__":
	import os
	import streamlit as st
	import validators
	from pypdf import PdfReader
	import torch
	import requests
	import pandas as pd
	import matplotlib.pyplot as plt
	from chat_rag.qa import QA
	from chat_rag.retriever import retriever
	from chat_rag.load_document import DocLoader

	torch.classes.__path__ = [] # add this line to get rid of error messages.
	os.environ.get("ANTHROPIC_API_KEY") 
    
	# Streamlit app title
	st.title("PDF or URL Loader")

	# Sidebar for input options
	with st.form("document"):
		with st.sidebar:
			st.header("Input Options")
			pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
			url_input = st.text_input("Enter a URL")
			submit_document = st.form_submit_button('Submit Document')

	with st.form("my_model"):
		with st.sidebar:
			option = st.selectbox(
    				"What model would you like to use?",
    				("Haiku", "Sonet", "Any"),
					)
			max_num_tokens = st.selectbox(
    				"What max num of tokens should your model use?",
    				("256", "512", "1024"),
					)
			st.write(f"You selected model option: {option}, max_num_tokens: {max_num_tokens}")
			submit_model = st.form_submit_button('Select Model')
	print('Option: ', option, max_num_tokens, submit_model)

	# Validation: Ensure only one input is provided
	if pdf_file and url_input:
		st.error("Please provide either a PDF file or a URL, not both.")
	elif not pdf_file and not url_input:
		st.warning("Please provide either a PDF file or a URL.")
	else:
		if pdf_file and submit_document:
			# Validate the uploaded PDF file
			try:
				pdf_reader = PdfReader(pdf_file)
				st.success("PDF file uploaded successfully!")
				temp_file = "./temp/temp.pdf"
				with open(temp_file, "wb") as file:
					file.write(pdf_file.getvalue())
				docloader = DocLoader(path=temp_file)
				documents = docloader.load()
				retriever.add_documents(documents)
				os.remove(temp_file)
			except Exception as e:
				st.error(f"Invalid PDF file: {e}")
		elif url_input and submit_document:
			# Validate the URL
			if validators.url(url_input):
				st.success("Valid URL provided!")
				st.write(f"URL: {url_input}")
				docloader = DocLoader(url=url_input)
				documents = docloader.load()
				retriever.add_documents(documents)
			else:
				st.error("Invalid URL. Please enter a valid URL.")

	# Initialize session state for conversation history
	with st.form("query"):
		if "history" not in st.session_state:
			st.session_state.history = []
		# Chatbot interaction
		user_query = st.text_input("Ask a question about the document:")
		submit_query = st.form_submit_button('Submit Query')

		# Get the response from the chatbot
		if submit_query:
			qa = QA(option, max_num_tokens).load()
			response = qa.invoke({"question": user_query},{"chat_history":st.session_state.history})
			st.session_state.history.append((user_query, response["answer"]))
		# Display the conversation
		for i, (query, answer) in enumerate(st.session_state.history):
			st.write(f"**You:** {query}")
			st.write(f"**Bot:** {answer}")