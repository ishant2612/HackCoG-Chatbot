import openai
from django.conf import settings

def get_chat_response(prompt):
    openai.api_key = settings.CHATGPT_KEY

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2046,  
        temperature=0.5,
        n = 1 
    )
    return response.choices[0].text.strip()
