from .nodes import general_node, research_node, writer_node, planner_node
from .router import router
from .state import Agentstate

def run_pipeline(state: Agentstate):
    route = router(state)
    state.route = route

    if route == "writer":
        return writer_node(state)
    elif route == "research":
        return research_node(state)
    elif route == "planner":
        return planner_node(state)
    else:
        return general_node(state)
