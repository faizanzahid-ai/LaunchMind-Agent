"""
LaunchMind MAS - Main Entry Point
Multi-Agent Startup Simulation System
"""
import time
from message_bus import MessageBus
from agents.ceo_agent import CEOAgent
from agents.product_agent import ProductAgent
from agents.engineer_agent import EngineerAgent
from agents.marketing_agent import MarketingAgent
from agents.qa_agent import QAAgent
from dotenv import load_dotenv
import os

load_dotenv()

# Configuration
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"


def run_sim(idea, mock=False):
    """
    Run the complete multi-agent simulation.
    
    Args:
        idea: Startup idea as string
        mock: Whether to use mock mode (no API calls)
    """
    # Initialize message bus
    bus = MessageBus()
    
    # Initialize all agents
    ceo = CEOAgent(bus, mock)
    product = ProductAgent(bus, mock)
    engineer = EngineerAgent(bus, mock)
    marketing = MarketingAgent(bus, mock)
    qa = QAAgent(bus, mock)
    
    # Track status
    st = {"eng": None, "mkt": None}
    
    # CEO starts the process
    ceo.start_process(idea)
    
    # Main simulation loop
    for turn in range(15):
        # Process messages for each agent
        product.process()
        engineer.process()
        marketing.process()
        qa.process()
        
        # Process CEO messages
        for m in bus.get_messages("ceo"):
            if m["message_type"] == "result":
                if ceo.review_output(m):
                    if m["from_agent"] == "engineer":
                        st["eng"] = m["payload"]
                        bus.send_message("ceo", "marketing", "pr_info", {"pr_url": "Skipped"})
                    elif m["from_agent"] == "marketing":
                        st["mkt"] = m["payload"]
                    elif m["from_agent"] == "qa" and m["payload"].get("verdict") == "PASS":
                        print("\n🎊 SUCCESS!")
                        return
        
        # Trigger QA when both Engineer and Marketing are done
        if st["eng"] and st["mkt"] and not [h for h in bus.history if h["from_agent"] == "qa"]:
            spec = next(
                (h["payload"]["spec"] for h in bus.history if h["from_agent"] == "product"),
                None
            )
            if spec:
                bus.send_message("ceo", "qa", "task", {
                    "engineer_output": st["eng"],
                    "marketing_output": st["mkt"],
                    "spec": spec
                })
        
        time.sleep(0.5)


if __name__ == "__main__":
    print("=" * 60)
    print("  LaunchMind MAS - Multi-Agent Startup Simulation")
    print("=" * 60)
    print()
    
    # Default startup idea
    idea = "A solar-powered smart water bottle."
    
    # Run simulation
    run_sim(idea, mock=MOCK_MODE)
    
    print()
    print("=" * 60)
    print("  Simulation Complete")
    print("=" * 60)
