import openai
# Replace 'YOUR_API_KEY' with your actual API key
openai.api_key = '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'

def ask_chat_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Replace with the appropriate engine name for ChatGPT
            prompt=prompt,
            max_tokens=150,  # Adjust the response length as needed
            temperature=0.7,  # Adjust the temperature for more/less randomness
            stop=["\n"]  # You can add custom stop sequences to control the response termination
        )
        return response.choices[0].text.strip()
    except Exception as e:
        # Handle API errors
        return str(e)

# Example usage
prompt = "You: Who are you?"
response = ask_chat_gpt(prompt)
print(response)

