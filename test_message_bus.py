"""
Test script for Message Bus
"""
from message_bus import MessageBus

print("=" * 60)
print("  Message Bus Test")
print("=" * 60)

# Initialize message bus
bus = MessageBus()

print("\n[TEST 1] Sending messages")
# Send messages
msg1_id = bus.send_message("ceo", "product", "task", {"idea": "Solar bottle"})
msg2_id = bus.send_message("product", "engineer", "task", {"spec": "details"})
msg3_id = bus.send_message("engineer", "ceo", "result", {"status": "done"})

print(f"  Message 1 ID: {msg1_id}")
print(f"  Message 2 ID: {msg2_id}")
print(f"  Message 3 ID: {msg3_id}")

print("\n[TEST 2] Getting messages for specific agent")
product_messages = bus.get_messages("product")
print(f"  Product agent received {len(product_messages)} message(s):")
for msg in product_messages:
    print(f"    From: {msg['from_agent']}, Type: {msg['message_type']}")

print("\n[TEST 3] Getting messages again (should be empty)")
product_messages = bus.get_messages("product")
print(f"  Product agent received {len(product_messages)} message(s)")

print("\n[TEST 4] Viewing message history")
history = bus.get_history()
print(f"  Total messages in history: {len(history)}")
print("\n  Message details:")
for i, msg in enumerate(history, 1):
    print(f"    {i}. {msg['from_agent']} -> {msg['to_agent']} ({msg['message_type']})")

print("\n[TEST 5] Message with parent ID for traceability")
parent_id = bus.send_message("ceo", "product", "task", {"idea": "test"})
child_id = bus.send_message("product", "ceo", "confirmation", {"status": "ready"}, parent_id=parent_id)
print(f"  Parent ID: {parent_id}")
print(f"  Child ID: {child_id}")

# Find child message
for msg in bus.get_history():
    if msg['message_id'] == child_id:
        print(f"  Child's parent: {msg['parent_message_id']}")

print("\n" + "=" * 60)
print("  Test Complete")
print("=" * 60)
