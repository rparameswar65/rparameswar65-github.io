from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

temperatures = [0.0, 0.3, 0.7, 1.2]

for temp in temperatures:
    print(f"\n--- Temperature {temp} ---")

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "user", "content": "Say hello to the world creatively in one sentence."}
        ],
        temperature=temp,
        max_tokens=50
    )

    print(response.choices[0].message.content)
