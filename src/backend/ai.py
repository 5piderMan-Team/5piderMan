from openai import OpenAI
from .config import OPENAI_API_KEY, OPENAI_API_HOST

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_API_HOST,  # 可以不用
)


def gpt(input: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": input,
            },
        ],
    )
    return completion.choices[0].message.content
