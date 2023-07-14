from init import *
from llama_index import SimpleDirectoryReader, LLMPredictor, ServiceContext
from llama_index.node_parser import SimpleNodeParser
from llama_index import VectorStoreIndex
from llama_index.llms import OpenAI
from llama_index import download_loader


class Index:
    def __init__(self, dir="data"):
        """Initialize the index."""
        self.loader = download_loader("UnstructuredReader")()
        self.docs = self.load(dir)
        self.nodes = SimpleNodeParser.from_defaults().get_nodes_from_documents(self.docs)

        llm_predictor = LLMPredictor(llm=OpenAI(model="gpt-3.5-turbo", temperature=0))
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, chunk_size=1000)
        self.index = VectorStoreIndex(self.nodes, service_context=service_context)

        self.query_engine = self.index.as_query_engine(streaming=True)
        self.retriever = self.index.as_retriever()

    def load(self, dir="data"):
        """Load all documents from a directory."""
        print(f"Loading directory: {dir}")
        doc_files = []
        for path, subdirs, files in os.walk(dir):
            for name in files:
                doc_files.append(os.path.join(path, name))
        docs = []
        for f in doc_files:
            print(f"Loading file: {f}")
            try:
                docs += self.loader.load_data(f, split_documents=False)
            except Exception as e:
                print(e, "Skipping.")
        return docs

    def query(self, query):
        """Query the index."""
        print("Query:", query)
        response = self.query_engine.query(query)
        print("Response:", response)
        return response


if __name__ == "__main__":
    index = Index(dir="data")
    response = index.query("What is the meaning of life?")
