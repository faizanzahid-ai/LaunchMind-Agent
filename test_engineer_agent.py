"""
Test script for Engineer Agent
"""
from message_bus import MessageBus
from agents.engineer_agent import EngineerAgent

print("=" * 60)
print("  Engineer Agent Test")
print("=" * 60)

# Initialize message bus and Engineer agent
bus = MessageBus()
engineer = EngineerAgent(bus, mock=False)

# Simulate Product agent sending a task
print("\n[TEST] Product sending task to Engineer Agent")
bus.send_message("product", "engineer", "task", {
    "spec": {
        "value_proposition": "Solar-powered smart water bottle",
        "features": [
            {"name": "Temperature display", "priority": 5},
            {"name": "UV sterilization", "priority": 4}
        ]
    }
})

# Process the message
print("\n[PROCESSING] Engineer Agent processing...")
engineer.process()

# Check messages sent
print("\n[RESULT] Engineer Agent sent messages:")
ceo_messages = bus.get_messages("ceo")
if ceo_messages:
    print("\n  To CEO:")
    for msg in ceo_messages:
        print(f"    Type: {msg['message_type']}")
        print(f"    Status: {msg['payload'].get('status')}")
        if 'html' in msg['payload']:
            html = msg['payload']['html']
            print(f"    HTML length: {len(html)} characters")
            print(f"    HTML preview: {html[:100]}...")

print("\n[NOTE] GitHub integration is not implemented yet (marked as 'Skipped')")

print("\n" + "=" * 60)
print("  Test Complete")
print("=" * 60)
