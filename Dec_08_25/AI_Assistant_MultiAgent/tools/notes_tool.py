from services.llm import get_groq_llm

class NotesTool:
    def __init__(self, model_name: str = "llama-3.1-8b-instant"):
        self.llm = get_groq_llm(model_name)

    def run(self, topic: str, summary: str) -> str:
        prompt = (
            f"Create clean, well-structured study notes for the topic: {topic}.\n\n"
            f"Use the following summary as your source:\n\n{summary}\n\n"
            "Structure the notes as:\n"
            "- Overview\n"
            "- Key Points\n"
            "- Further Reading\n\n"
            "Keep the explanation concise and clear."
        )

        # Correct call
        response = self.llm.invoke(prompt)

        # Correct extraction
        return response.content
