"""
Message Bus Implementation for LaunchMind MAS
Handles structured message passing between agents
"""
import uuid
from datetime import datetime
from typing import Dict, List


class MessageBus:
    """
    Central communication hub for agent messages.
    Uses shared dictionary approach (Option A from assignment).
    """
    
    def __init__(self):
        self.bus: Dict[str, List[dict]] = {}
        self.history: List[dict] = []
    
    def send_message(self, from_agent, to_agent, m_type, payload, parent_id=None):
        """
        Send a structured message from one agent to another.
        
        Args:
            from_agent: Name of sending agent
            to_agent: Name of receiving agent
            m_type: Message type (task, result, revision_request, confirmation)
            payload: Message content
            parent_id: Optional parent message ID for traceability
        
        Returns:
            message_id: Unique ID for this message
        """
        msg = {
            "message_id": str(uuid.uuid4()),
            "from_agent": from_agent,
            "to_agent": to_agent,
            "message_type": m_type,
            "payload": payload,
            "timestamp": datetime.now().isoformat() + "Z",
            "parent_message_id": parent_id
        }
        
        if to_agent not in self.bus:
            self.bus[to_agent] = []
        
        self.bus[to_agent].append(msg)
        self.history.append(msg)
        
        print(f"[📩] {from_agent.upper()} ➔ {to_agent.upper()} ({m_type.upper()})")
        return msg["message_id"]
    
    def get_messages(self, agent_name):
        """
        Get all messages for a specific agent and clear them from the bus.
        
        Args:
            agent_name: Name of the agent to get messages for
        
        Returns:
            List of messages addressed to this agent
        """
        msgs = self.bus.get(agent_name, [])
        self.bus[agent_name] = []
        return msgs
    
    def get_history(self):
        """
        Get complete message history for debugging/audit.
        
        Returns:
            List of all messages sent through the bus
        """
        return self.history
