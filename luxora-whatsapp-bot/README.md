# 🤖 Luxora – AI Hotel WhatsApp Concierge Bot

**Luxora** is a 24/7 AI-powered WhatsApp assistant designed for the hotel industry. It uses **Flask**, **Twilio**, and **Lyzr AI** to automate hotel guest interactions like room service requests, check-in help, and local recommendations via WhatsApp.

---

## 🌟 Features

- 📲 WhatsApp Concierge: Handles bookings, requests, and FAQs in real-time
- 🧠 Lyzr AI: Smart, context-aware assistant trained for hospitality
- ☁️ Flask Webhook: Receives and processes messages between WhatsApp and Lyzr
- 🔐 Secure: API keys handled with best practices

---

## 🧰 Tech Stack

- **Flask** – Python web framework
- **Twilio** – WhatsApp messaging API
- **Lyzr Studio** – AI Agent Platform
- **ngrok** – Tunnel Flask server for public access

---

## 🚀 Quickstart Guide

### 🔹 Step 1: Clone the Repo
```bash
git clone https://github.com/yourusername/luxora-whatsapp-bot.git
cd luxora-whatsapp-bot
```

### 🔹 Step 2: Install Requirements
```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Add Your Lyzr Credentials

Open `app.py` and replace the placeholders:
```python
LYZR_AGENT_URL = "https://agent-prod.studio.lyzr.ai/v3/agents/YOUR_AGENT_ID/chat"
LYZR_API_KEY = "Bearer YOUR_LYZR_API_KEY"
```

You can find these by logging into [https://studio.lyzr.ai](https://studio.lyzr.ai) under **Account & API Key**.

### 🔹 Step 4: Run the Flask Server
```bash
python app.py
```

### 🔹 Step 5: Run ngrok (Windows Example)
```bash
ngrok http 5000
```

Copy the HTTPS forwarding URL from the terminal.

### 🔹 Step 6: Configure Twilio Sandbox

1. Go to: [Twilio WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox)
2. Paste your ngrok URL in the **“When a message comes in”** field, like:
```
https://abcd1234.ngrok.io/whatsapp
```
3. Send the provided keyword (e.g., `join wisdom-fire`) from your WhatsApp to the Twilio sandbox number.

---

## 🧪 Test It

Try sending messages like:
- "I'd like to order room service"
- "What are your check-out times?"
- "Can you recommend a local restaurant?"

Luxora will respond using Lyzr AI via Twilio.

---

## 📁 Project Structure

```
luxora-whatsapp-bot/
├── app.py              # Flask app for webhook handling
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🔐 Security Notice

- Do NOT share your Lyzr API Key or Agent ID publicly.
- Use `.env` or secret management in production.

---

## 📌 Future Enhancements

- ✅ Add support for multiple hotel branches
- ✅ Connect to booking and payment APIs
- ✅ Persist guest preferences using a database
- ✅ Admin dashboard to monitor and edit conversations

---

## 🧠 Powered By

- [Lyzr Studio](https://studio.lyzr.ai)
- [Twilio WhatsApp API](https://www.twilio.com/whatsapp)
- [ngrok](https://ngrok.com)

---

## 📜 License

MIT License – feel free to use and modify.

---

### 💬 Questions or Suggestions?
Open an issue or submit a pull request!

