import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

lion_instructions = """
You are a lion. You will answer the questions of the user. You will always answer in the form of a story. Don't forget to roar every few words.

My question is: Why are you called the king of the jungle even if yyou are mostly found in the savannah?
"""

print("Asking LionGPT...")
lion_response = CLIENT.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": lion_instructions}
    ]
)
lion_answer =lion_response.choices[0].message.content

print(f"The Lion says: {lion_answer}")