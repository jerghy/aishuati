import requests
import mod
url = mod.free_url


messages=[
        {
            "role": "user",
            "content": "What opportunities and challenges will the Chinese large model industry face in 2025?"
        }
    ]
payload = {
    "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    "messages": messages,
    "stream": False,
    "max_tokens": 506,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "frequency_penalty": 0.5,
    "n": 1,
}
headers = {
    "Authorization": f"Bearer {mod.free_key[0]}",
    # "Authorization" : "Bearer sk-htxjzlywpzxdjkczbmsazayluvhoilxwupboyfdzixgckwsp",
    "Content-Type": "application/json"
}
class Client:
    def __init__(self, model):
        self.messages=[]
        self.headers = headers
        self.model = model
        self.payload = {
            "model": self.model,
            "messages": self.messages,
            "stream": False,
            "max_tokens": 506,
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 50,
            "frequency_penalty": 0.5,
            "n": 1,
        }
    def setmessages(self, messages):
        self.messages = messages
        self.changepayload()
    def changepayload(self, ):
        self.payload = {
            "model": self.model,
            "messages": self.messages,
            "stream": False,
            "max_tokens": 4096,
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 50,
            "frequency_penalty": 0.5,
            "n": 1,
        }
    def send(self):
        response = requests.request("POST", url, json=self.payload, headers=self.headers)
        return response.text,response.status_code


# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)