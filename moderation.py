import openai
import json
import os

# 파일로 관리할 경우
'''with open("private") as f:
    api_key = f.read().strip()

openai.api_key = api_key # API Key'''

# 텍스트로 따로 붙여야할경우
openai.api_key = "sk-TNjP_ORsBVIwYouwdCRofJkpBb3zUJNcFdiwXhks_rT3BlbkFJQliMPzxI8AST_0rJ_6bmcxMxzZlEYifnpoQa0jpQ0A"

client = openai.OpenAI(api_key=openai.api_key)

response = client.moderations.create(
    model = "omni-moderation-latest",
    input = "너는 바보야",
)
print(response.results[0])