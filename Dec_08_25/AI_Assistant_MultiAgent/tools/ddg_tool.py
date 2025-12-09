from langchain_community.tools import DuckDuckGoSearchRun

class DDGTool:
    def __init__(self):
        self.tool = DuckDuckGoSearchRun()

    def run(self, query: str)-> str:
        return self.tool.run(query)