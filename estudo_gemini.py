from google import genai
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura o cliente moderno
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# --- NOVO PROMPT ESTRUTURADO ---
instrucao_sistema = """
Role: You are a senior Customer Experience (CX) specialist.
Goal: Produce a sentiment classification for a support team that achieves high accuracy in identifying business success.

Context:
- Project: Automated feedback analysis for a tech company.
- Inputs: Raw customer text strings.
- Assumptions: Focus on the resolution of the problem as the primary metric.

Instructions:
- If the input is clear: respond with a single word (POSITIVO, NEGATIVO, NEUTRO).
- If the input is ambiguous or empty: ASK a clarifying question instead of classifying.

Quality checks:
- Verify if the problem was solved. If it was, prioritize POSITIVO even if there were delays.
- If something is ambiguous, ask one clarifying question before producing the final result.
- Is the input just punctuation or empty? If yes, DO NOT classify. Ask for more details.
Now create the classification.
"""

# Testando o modelo com a nova biblioteca
#feedback = "O suporte demorou muito para responder, mas resolveu o problema."
feedback = "..."

response = client.models.generate_content(
    model="gemini-2.0-flash", # Usando a versão mais atual disponível
    config={'system_instruction': instrucao_sistema},
    contents=feedback
)

print(f"Feedback: {feedback}")
print(f"Classificação: {response.text}")