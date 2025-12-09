from typing import Dict, Any, List
from dataclasses import dataclass, field

@dataclass
class Agentstate:
    user_inputs: str = ""
    route : str = ""
    intermediate_steps: Dict[str, Any] = field(default_factory=dict)
    result: Dict[str, Any] = field(default_factory=dict)
