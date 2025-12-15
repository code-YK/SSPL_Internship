from langgraph.graph import StateGraph, END
from graph.state import AgentState
from agents import extractor_agent, validator_agent, memory_keeper_agent, assistant_agent


def build_graph():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("extractor", extractor_agent)
    graph.add_node("validator", validator_agent)
    graph.add_node("memory_keeper", memory_keeper_agent)

    # Entry
    graph.set_entry_point("extractor")

    # Flow
    graph.add_edge("extractor", "validator")

    # HITL decision point
    graph.add_conditional_edges(
        "validator",
        lambda state: "memory_keeper" if not state["awaiting_confirmation"] else END,
        {
            "memory_keeper": "memory_keeper",
            END: END
        }
    )

    # End after memory is stored
    graph.add_edge("memory_keeper", END)

    return graph.compile()