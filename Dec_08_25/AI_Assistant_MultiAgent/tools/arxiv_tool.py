from langchain_community.utilities import ArxivAPIWrapper

class ArxivTool:
    def __init__(self):
        self.tool = ArxivAPIWrapper()

    def run(self, query: str) -> str:
        try:
            return self.tool.run(query)
        except Exception as e:
            return f"An error occurred while fetching data from arXiv: {str(e)}"
