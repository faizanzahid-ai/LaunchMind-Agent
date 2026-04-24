"""
Test script for CEO Agent
"""
from message_bus import MessageBus
from agents.ceo_agent import CEOAgent

print("=" * 60)
print("  CEO Agent Test")
print("=" * 60)

# Initialize message bus and CEO agent
bus = MessageBus()
ceo = CEOAgent(bus, mock=False)

# Test 1: Start process with startup idea
print("\n[TEST 1] CEO starting process with startup idea")
ceo.start_process("A solar-powered smart water bottle")

# Check messages sent
product_messages = bus.get_messages("product")
if product_messages:
    print(f"\n  CEO sent to Product:")
    for msg in product_messages:
        print(f"    Type: {msg['message_type']}")
        print(f"    Idea: {msg['payload']['idea']}")

# Test 2: Review output from an agent (approve)
print("\n[TEST 2] CEO reviewing output (should approve)")
bus.send_message("engineer", "ceo", "result", {
    "status": "Completed",
    "html": "<html><body>Solar Bottle</body></html>"
})
for m in bus.get_messages("ceo"):
    approved = ceo.review_output(m)
    print(f"  Review result: {'APPROVED' if approved else 'REJECTED'}")

# Test 3: Review output (reject - revision request)
print("\n[TEST 3] CEO reviewing poor output (should reject)")
bus.send_message("marketing", "ceo", "result", {
    "copy": "bad copy here"
})
for m in bus.get_messages("ceo"):
    approved = ceo.review_output(m)
    print(f"  Review result: {'APPROVED' if approved else 'REJECTED'}")

# Check if revision request was sent
marketing_messages = bus.get_messages("marketing")
if marketing_messages:
    print(f"  CEO sent revision request to Marketing:")
    for msg in marketing_messages:
        print(f"    Type: {msg['message_type']}")
        print(f"    Feedback length: {len(msg['payload']['feedback'])} chars")

print("\n" + "=" * 60)
print("  Test Complete")
print("=" * 60)
