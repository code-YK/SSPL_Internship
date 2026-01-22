from core.utils import load_pdf, split_text, create_vector_store, retrieve_similar_documents, PROMPT_TEMPLATE
from config.llm_config import llm
from config.logger_config import setup_logger

logger = setup_logger(__name__)

class RAGPipeline:
    def __init__(self):
        logger.info("Initializing RAG Pipeline")
        self.llm = llm
        self.vector_store = None

    def ingest_pdf(self, file_path: str) -> None:
        '''Ingest a PDF file Once,
          split its content into chunks, 
          and create a vector store.
        '''
        try:
            logger.info(f"Ingesting PDF file from path: {file_path}")
            documents = load_pdf(file_path)
            chunks = split_text(documents)
            self.vector_store = create_vector_store(chunks)
            logger.info("PDF ingested and vector store created successfully.")
        except Exception as e:
            logger.error(f"Error ingesting PDF: {e}")
            raise

    def chat(self, query: str, chat_history: str = "") -> str:
        """
        Given a user query and optional chat history,
        retrieve relevant documents and generate a response using the LLM.
        """
        logger.info(f"Processing query: {query}")

        try:
            if not self.vector_store:
                raise ValueError("No document uploaded yet")

            # Retrieve relevant document chunks
            docs = retrieve_similar_documents(self.vector_store, query)

            # Build document context
            context = "\n".join(d.page_content for d in docs)

            # Build full prompt with memory + context
            full_prompt = f"""
    You are a document-based assistant.

    Conversation so far:
    {chat_history}

    Document context:
    {context}

    User question:
    {query}

    Answer:
    """
            # Invoke LLM
            response = self.llm.invoke(full_prompt)

            return response.content

        except Exception as e:
            logger.error(f"Error in chat processing: {e}")
            raise


if __name__ == "__main__":
    rag_pipeline = RAGPipeline()
    rag_pipeline.ingest_pdf("E:\\SSPL_Internship_Repo\\Jan_20_26\\DocuChat\\data\\demo.pdf")
    while True:
        user_query = input("Enter your question (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        response = rag_pipeline.chat(user_query)
        print("Response:", response.content if hasattr(response, 'content') else response)