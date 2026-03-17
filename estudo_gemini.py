from google import genai
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# System instruction now includes a clearer "Contract"
system_instruction = """
Role: Senior Customer Experience Specialist.
Instructions:
- Analyze feedback into a JSON object.
- Keys: "sentiment" (POSITIVE/NEGATIVE/NEUTRAL), "subject", "urgency" (1, 2, or 3).
- Urgency levels: 1=Low, 2=Medium, 3=High.
- Output ONLY valid JSON.
"""

feedback = "Excellent service! They solved my problem quickly and with great attention."

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config={
            'system_instruction': system_instruction,
            'response_mime_type': 'application/json', 
        },
        contents=feedback
    )

    data = json.loads(response.text)
    
    # Mapping numbers to labels
    urgency_map = {1: "LOW", 2: "MEDIUM", 3: "HIGH"}
    final_urgency = urgency_map.get(data.get('urgency'), "UNKNOWN")

    # Cost Calculation
    usage = response.usage_metadata
    cost = (usage.prompt_token_count * 0.0000001) + (usage.candidates_token_count * 0.0000004)

    print("\n" + "="*40)
    print(f"😊 Sentiment: {data.get('sentiment')}")
    print(f"📁 Subject: {data.get('subject')}")
    print(f"🚨 Urgency: {final_urgency}")
    print("-" * 40)
    print(f"💰 Estimated Cost: ${cost:.6f}")
    print("="*40 + "\n")

except Exception as e:
    print(f"🚨 Error: {e}")