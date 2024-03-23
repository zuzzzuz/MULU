from openai import OpenAI
client = OpenAI()



def get_completions(system_prompt,user_prompt,model="gpt-3.5-turbo"):
    system_message = {"role":"system","content":system_prompt}
    user_message = {"role":"user","content":user_prompt}
    messages = [system_message, {"role": "user", "content": "我不想上班"}, {"role": "assistant", "content": "居民楼"},user_message]
    
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature= 0
        
    )
    
    return response.choices[0].message.content


with open("thing_list.txt", "rb") as f:
    thing_list = f.read()


system_prompt = f""" 我想让你扮演一个愿望到物体的转译者，我会给你一个物体列表，你需要通过我给你的愿望经过思考想出富有想象力并符合逻辑的在物体列表中相对应的物体 
```{thing_list}```   """




response = get_completions(system_prompt,user_prompt)
response_byte = response.encode()
thing_list = thing_list.replace(response_byte, b'')
print(response)

with open("thing_list.txt", "wb") as f:
    f.write(thing_list)
