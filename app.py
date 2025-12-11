from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "user", "content": "Hello, say hi!"}
    ]
)

print(response.choices[0].message["content"])
