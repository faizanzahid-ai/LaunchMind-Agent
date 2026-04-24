"""
Test script for Product Agent
"""
from message_bus import MessageBus
from agents.product_agent import ProductAgent

print("=" * 60)
print("  Product Agent Test")
print("=" * 60)

# Initialize message bus and Product agent
bus = MessageBus()
product = ProductAgent(bus, mock=False)

# Simulate CEO sending a task
print("\n[TEST] CEO sending task to Product Agent")
bus.send_message("ceo", "product", "task", {
    "idea": "A solar-powered smart water bottle",
    "focus": "Full spec"
})

# Process the message
print("\n[PROCESSING] Product Agent processing...")
product.process()

# Check messages sent
print("\n[RESULT] Product Agent sent messages:")
for agent in ["engineer", "marketing", "ceo"]:
    messages = bus.get_messages(agent)
    if messages:
        print(f"\n  To {agent.upper()}:")
        for msg in messages:
            print(f"    Type: {msg['message_type']}")
            if msg['message_type'] == 'task':
                print(f"    Spec keys: {list(msg['payload']['spec'].keys())}")
            else:
                print(f"    Payload: {msg['payload']}")

print("\n" + "=" * 60)
print("  Test Complete")
print("=" * 60)
