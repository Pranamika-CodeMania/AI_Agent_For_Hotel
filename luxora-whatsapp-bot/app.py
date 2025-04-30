from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Replace these with your actual Lyzr details
LYZR_AGENT_URL = "https://agent-prod.studio.lyzr.ai/v3/agents/681244d2f4097946d9c27092/chat"
LYZR_API_KEY = "sk-default-zOeTkI1bDYhIB34I6IU4gi1MokkLnUSG"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get('Body')
    
    # Send message to Lyzr
    response = requests.post(
        LYZR_AGENT_URL,
        headers={"Authorization": LYZR_API_KEY},
        json={"message": incoming_msg}
    )
    
    try:
        lyzr_reply = response.json().get("reply", "Sorry, I couldn't understand that.")
    except:
        lyzr_reply = "There was an error processing your request."

    # Respond via WhatsApp
    twilio_response = MessagingResponse()
    msg = twilio_response.message()
    msg.body(lyzr_reply)
    return str(twilio_response)

if __name__ == "__main__":
    app.run(port=5000)
