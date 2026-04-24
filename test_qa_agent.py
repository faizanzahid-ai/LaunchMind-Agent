"""
Test script for QA Agent
"""
from message_bus import MessageBus
from agents.qa_agent import QAAgent

print("=" * 60)
print("  QA Agent Test")
print("=" * 60)

# Initialize message bus and QA agent
bus = MessageBus()
qa = QAAgent(bus, mock=False)

# Simulate receiving a task from CEO
print("\n[TEST] QA Agent receiving task with spec and outputs")
bus.send_message("ceo", "qa", "task", {
    "spec": {
        "value_proposition": "Solar-powered smart water bottle",
        "features": [
            {"name": "Temperature display", "priority": 5},
            {"name": "UV sterilization", "priority": 4}
        ]
    },
    "engineer_output": {
        "status": "Completed",
        "html": "<html><body><h1>Solar Bottle</h1></body></html>"
    },
    "marketing_output": {
        "tagline": "Stay hydrated, stay powered",
        "description": "Smart water bottle with solar charging"
    }
})

# Process the message
print("\n[PROCESSING] QA Agent processing...")
qa.process()

# Check message sent to CEO
ceo_messages = bus.get_messages("ceo")
if ceo_messages:
    print(f"\n[RESULT] QA Agent sent to CEO:")
    for msg in ceo_messages:
        print(f"  Type: {msg['message_type']}")
        print(f"  Payload: {msg['payload']}")

print("\n" + "=" * 60)
print("  Test Complete")
print("=" * 60)
