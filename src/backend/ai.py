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
                            "description": "搜索关键词, 应尽量简洁。例如用户输入“我想找一个java开发的工作”，那么这里的关键词应该是“java”，而不是“java开发”或者“java工作”",
                        },
                    },
                    "required": ["keyword"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "job_filter_by_city",
                "description": "给用户展示某城市的工作",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "城市中文名字。例如用户输入“我想找一个北京的工作”，那么city应该是“北京”，而不是“beijing”",
                        },
                    },
                    "required": ["city"],
                },
            },
        },
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
