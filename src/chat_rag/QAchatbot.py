from qa import qa
from retriever import retriever
from load_document import DocLoader

url = "https://en.wikipedia.org/wiki/Hendrik_Lorentz"

history = []
docloader = DocLoader(url=url)
documents = docloader.load()
retriever.add_documents(documents)

ik = 0
while ik < 5:
    query = input("User query: ")

    if query.lower() in ["quit","exit","bye"]:
        print("Good bye!")
        break
    else:
        result = qa.invoke({"question": query},{"chat_history":history})
        history.append((query,result["answer"]))
        print(result["answer"])
        ik+=1
