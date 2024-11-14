from zhipuai import ZhipuAI
def invoke_api(prompt):
    ZHIPU_API_KEY = "xxxx"
    from zhipuai import ZhipuAI
    client = ZhipuAI(api_key=ZHIPU_API_KEY)
    model = "glm-4"  
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False,
        temperature=0.1,
        top_p=0.1,
        max_tokens=4096,
        # request_id=request_id
    )
    answer = response.choices[0].message.content
    return answer


# glm4模型跑一遍
class AI_Agent:
    def __init__(self, name, system_setting):
        self.name = name
        self.system_setting = system_setting
        # self.client = OpenAI(base_url="https://xxxxxxxxx/v1", api_key='sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa')
        ZHIPU_API_KEY = "xxx"
        from zhipuai import ZhipuAI
        self.client = ZhipuAI(api_key=ZHIPU_API_KEY)
        self.messages = [{"role": "system", "content": self.system_setting}]

    def chat(self, other_name, other_message):
        self.messages.append({"role": "user", "content": f" {other_message}"})
        completion = self.client.chat.completions.create(
            model="glm-4",
            messages=self.messages
        )
        response = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": f" {response}"})
        return response

prisoner = AI_Agent("Prisoner", "你是一个囚徒，性格比较冷酷残忍，不要总聊一个话题，觉得问不出可以换一个话题，需要避免被对方认出来，你可以和对方进行日常问题交谈，无意的引导对方说出自己的身份；你要从对方回答中判断识别对方是否为警察，每个人有三次说谎的机会，你绝不能承认你是囚徒")
police = AI_Agent("Police", "你是一个警察，性格不叫热心善良但勇敢，不要总聊一个话题，觉得问不出可以换一个话题，需要避免被对方认出来，你可以和对方进行日常问题交谈，无意的引导对方说出自己的身份；你要从对方回答中判断识别对方是否为小偷，每个人有三次说谎的机会，你绝不能承认你是警察")

for i in range(20):  # 循环20次
    if i % 2 == 0:
        prisoner_response = prisoner.chat(police.name, police.messages[-1]['content'] if police.messages else '')
        print(f"{prisoner.name}: {prisoner_response}")
    else:
        police_response = police.chat(prisoner.name, prisoner.messages[-1]['content'] if prisoner.messages else '')
        print(f"{police.name}: {police_response}")