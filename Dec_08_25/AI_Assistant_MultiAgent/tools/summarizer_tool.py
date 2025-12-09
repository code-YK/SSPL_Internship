from services.llm import get_groq_llm

class SummarizerTool:
    def __init__(self):
        self.llm = get_groq_llm()

    def run(self, text: str) -> str:
        prompt = (
            "Summarize the following text in concise bullet points:\n\n"
            f"{text}"
        )
        
        # Correct method: invoke()
        response = self.llm.invoke(prompt)

        # Correct extraction
        return response.content
