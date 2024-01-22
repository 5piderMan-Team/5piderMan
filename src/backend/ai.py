from json import tool
from openai import OpenAI
from .config import OPENAI_API_KEY, OPENAI_API_HOST
from openai.types.chat import ChatCompletionToolParam

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_API_HOST,  # 可以不用
)

PROMPT = """
你是一个招聘网站的客服，你的工作是回复用户的咨询，帮助他们跳转到的页面等等。

即使用户的提问很奇怪，你也要尽可能的回答他们。
"""


def gpt(input: str):
    # gpt 可以使用的函数
    tools: list[ChatCompletionToolParam] = [
        {
            "type": "function",
            "function": {
                "name": "go_to_search",
                "description": "让用户的页面跳转到对应的搜索页面",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "搜索关键词",
                        },
                    },
                    "required": ["keyword"],
                },
            },
        }
    ]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": PROMPT,
            },
            {
                "role": "user",
                "content": input,
            },
        ],
        tools=tools,
        tool_choice="auto",
    )
    return completion.choices[0].message
