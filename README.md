# Gemini API Study 🚀

An automated system to analyze customer feedback using Google's Gemini 2.0 Flash model.

## Features
- **Sentiment Analysis:** Classifies feedback as POSITIVE, NEGATIVE, or NEUTRAL.
- **Categorization:** Identifies the main subject of the customer's message.
- **Urgency Scoring:** Maps priority levels (1-3) for support teams.
- **Cost Tracking:** Real-time calculation of token usage and API costs.

## Tech Stack
- Python 3.x
- Google GenAI SDK
- Dotenv (Environment Variables)

## Setup
1. Clone the repo: `git clone https://github.com/edsonmellosjunior/estudo-gemini-api.git`
2. Install dependencies: `pip install google-genai python-dotenv`
3. Create a `.env` file with your `GEMINI_API_KEY`.
4. Run: `python study_gemini.py`