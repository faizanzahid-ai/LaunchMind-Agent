"""
Test script for LLM Handler
"""
from llm_handler import LLMHandler

print("=" * 60)
print("  LLM Handler Test")
print("=" * 60)

# Test 1: Mock mode
print("\n[TEST 1] Mock Mode")
llm_mock = LLMHandler(mock=True)
response = llm_mock.call("System prompt", "User prompt")
print(f"Response: {response}")

# Test 2: Mock mode with JSON
print("\n[TEST 2] Mock Mode (JSON)")
json_response = llm_mock.call("System prompt", "User prompt", json_m=True)
print(f"Response: {json_response}")

# Test 3: Real API call (if keys available)
print("\n[TEST 3] Real API Call")
try:
    llm_real = LLMHandler(provider="groq", mock=False)
    response = llm_real.call(
        "You are a helpful assistant.",
        "What is a solar-powered water bottle in one sentence?"
    )
    print(f"Response: {response}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 60)
print("  Test Complete")
print("=" * 60)
