from graph import build_graph

def save_graph_image():
    app = build_graph()

    # Save graph as PNG
    app.get_graph().draw_mermaid_png(
        output_file_path="memory/langgraph_workflow.png"
    )

    print("Graph image saved as memory/langgraph_workflow.png")


if __name__ == "__main__":
    save_graph_image()
