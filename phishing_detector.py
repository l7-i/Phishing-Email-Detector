
# phishing_detector.py

def is_phishing_email(text):
    phishing_keywords = [
        "urgent", "account suspended", "click here", "verify your identity",
        "update payment", "unauthorized access", "login now", "bank alert",
        "free gift", "you won", "limited time", "security alert"
    ]

    text_lower = text.lower()
    score = sum(keyword in text_lower for keyword in phishing_keywords)
    if score >= 2:
        return "⚠️ Warning: This email may be a phishing attempt."
    elif score == 1:
        return "⚠️ Caution: This email contains suspicious content."
    else:
        return "✅ This email appears to be safe."

if __name__ == "__main__":
    print("=== Phishing Email Detector ===")
    user_input = input("Paste the email content here:\n")
    result = is_phishing_email(user_input)
    print(result)
    input("Press Enter to exit...")
