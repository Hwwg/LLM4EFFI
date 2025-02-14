from openai import OpenAI
class GPTReply:
    def __init__(self,model,client="openai"):
        self.model = model
        self.client = client

    def getreply(self,systemprompt,user1prompt,user2prompt):
        while True:
            try:
                if self.client=="openai":
                    client = OpenAI(api_key="",base_url="")
                # client = OpenAI()
                if self.model=="deepseek-coder":
                    self.model = "deepseek/deepseek-chat"
                completion = client.chat.completions.create(
                    model= self.model,
                    messages = [
                        {"role": "system","content":systemprompt+"_"},
                        {"role" : "user", "content": user1prompt+"_"},
                        {"role": "user", "content": user2prompt+"_"}
                    ],
                    temperature = 0
                )
                return completion.choices[0].message.content
            except Exception as e:
                print(str(e))
                if "maximum context length is" in str(e):
                    return False
                if "Range of input length should" in str(e) or "Exceeded limit on max byt" in str(e):
                    return False
                pass
