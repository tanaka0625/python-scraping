import openai
openai.api_key = 'XXXXXXXXXXXXXXXXXXXXX'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"Please tell me about tokyo city"},
    ]
)

print(response)