"""
Test script for Marketing Agent
"""
from message_bus import MessageBus
from agents.marketing_agent import MarketingAgent

print("=" * 60)
print("  Marketing Agent Test")
print("=" * 60)

# Initialize message bus and Marketing agent
bus = MessageBus()
marketing = MarketingAgent(bus, mock=False)

# Simulate Product agent sending a task
print("\n[TEST] Product sending task to Marketing Agent")
bus.send_message("product", "marketing", "task", {
    "spec": {
        "value_proposition": "Solar-powered smart water bottle",
        "features": [
            {"name": "Temperature display", "priority": 5},
            {"name": "UV sterilization", "priority": 4}
        ]
    }
})

# Process the message
print("\n[PROCESSING] Marketing Agent processing...")
marketing.process()

# Check messages sent
print("\n[RESULT] Marketing Agent sent messages:")
ceo_messages = bus.get_messages("ceo")
if ceo_messages:
    print("\n  To CEO:")
    for msg in ceo_messages:
        print(f"    Type: {msg['message_type']}")
        print(f"    Payload: {msg['payload']}")

# Simulate CEO sending PR info
print("\n[TEST 2] CEO sending PR info to Marketing Agent")
bus.send_message("ceo", "marketing", "pr_info", {"pr_url": "Skipped"})

# Process the message
print("\n[PROCESSING] Marketing Agent processing...")
marketing.process()

# Check final result
ceo_messages = bus.get_messages("ceo")
if ceo_messages:
    print("\n  To CEO (final):")
    for msg in ceo_messages:
        print(f"    Type: {msg['message_type']}")
        if 'copy' in msg['payload']:
            print(f"    Copy keys: {list(msg['payload']['copy'].keys())}")

print("\n" + "=" * 60)
print("  Test Complete")
print("=" * 60)
