#!/usr/bin/env python
"""
Email Integration Test Script
Tests RESEND email sending functionality
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
TEST_RECEIVER_EMAIL = os.getenv("TEST_RECEIVER_EMAIL")

print("=" * 60)
print("  EMAIL INTEGRATION TEST")
print("=" * 60)
print()

# Validate configuration
print("[1/4] Checking configuration...")
issues = []

if not RESEND_API_KEY:
    issues.append("❌ RESEND_API_KEY is missing in .env")
else:
    print(f"✅ RESEND_API_KEY: {RESEND_API_KEY[:20]}...")

if not SENDER_EMAIL:
    issues.append("❌ SENDER_EMAIL is missing in .env")
else:
    print(f"✅ SENDER_EMAIL: {SENDER_EMAIL}")

if not TEST_RECEIVER_EMAIL:
    issues.append("❌ TEST_RECEIVER_EMAIL is missing in .env")
else:
    print(f"✅ TEST_RECEIVER_EMAIL: {TEST_RECEIVER_EMAIL}")

if issues:
    print()
    for issue in issues:
        print(issue)
    print()
    print("Please update your .env file with missing values")
    sys.exit(1)

print()

# Test imports
print("[2/4] Testing imports...")
try:
    import resend
    print("✅ resend package imported successfully")
except ImportError:
    print("❌ resend package not installed")
    print("   Installing now...")
    os.system("pip install resend")
    import resend
    print("✅ resend package installed and imported")

print()

# Initialize Resend client
print("[3/4] Initializing Resend client...")
try:
    resend.api_key = RESEND_API_KEY
    print(f"✅ Resend client initialized with API key")
except Exception as e:
    print(f"❌ Failed to initialize Resend: {e}")
    sys.exit(1)

print()

# Send test email
print("[4/4] Sending test email...")
print(f"   From: {SENDER_EMAIL}")
print(f"   To: {TEST_RECEIVER_EMAIL}")
print()

try:
    email = resend.Emails.send({
        "from": SENDER_EMAIL,
        "to": TEST_RECEIVER_EMAIL,
        "subject": "LaunchMind MAS - Email Integration Test ✅",
        "html": """
        <h1>Email Integration Test</h1>
        <p>This is a test email from <strong>LaunchMind MAS</strong>.</p>
        <p>If you received this email, the email integration is working correctly! ✅</p>
        <hr>
        <p><em>Sent at: """ + str(__import__('datetime').datetime.now()) + """</em></p>
        """
    })
    
    print(f"✅ Email sent successfully!")
    print(f"   Message ID: {email['id']}")
    print()
    print("=" * 60)
    print("  ✅ ALL TESTS PASSED - EMAIL INTEGRATION WORKING!")
    print("=" * 60)
    
except Exception as e:
    print(f"❌ Failed to send email: {e}")
    print()
    print("Troubleshooting tips:")
    print("  1. Verify your RESEND_API_KEY is correct")
    print("  2. Check that SENDER_EMAIL is verified in Resend")
    print("  3. Ensure RESEND_API_KEY has email sending permissions")
    print()
    sys.exit(1)
