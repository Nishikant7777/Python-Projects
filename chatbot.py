# chat bot 
from openai import OpenAI

# Step 1: Initialize OpenAI client with your API key
client = OpenAI(api_key="x...............n") 

# Step 2: Define chatbot function
def chat_bot(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Required argument
        messages=[       # Required argument
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Step 3: Create chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    reply = chat_bot(user_input)
    print("Chatbot:", reply)

