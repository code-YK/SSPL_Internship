from langchain_community.utilities import WikipediaAPIWrapper

class WikiTool:
    def __init__(self):
        self.tool = WikipediaAPIWrapper(description="Useful for searching information on Wikipedia")
    
    def run(self, query: str) -> str:
        try:
            return self.tool.run(query)
        except Exception as e:
            return f"An error occurred while fetching data from Wikipedia: {str(e)}"