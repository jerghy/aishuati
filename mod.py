from openai import OpenAI

api_openai="https://api.gptapi.us/v1/chat/completions"
api_anthropic="https://api.gptapi.us/v1/messages"
free_key="sk-ethgdjypryiwfidbmcqxpzatzsfvjgrcjpdkqsvsbubusauk", # 从https://cloud.siliconflow.cn/account/ak获取
free_url="https://api.siliconflow.cn/v1/chat/completions"
doubaourl="https://ark.cn-beijing.volces.com/api/v3/chat/completions"
doubaokey="0f38123d-549a-48c5-a2ab-46dde690c019"
aliyunurl="https://dashscope.aliyuncs.com/compatible-mode/v1"
aliyunkey="sk-f104fdb232104364b72b565df9839a82"
class gptModel:
    def __init__(self):
        self.o3_mini="o3-mini"
        self.deepseek_r1="deepseek-r1"
        self.deepseek_v3="deepseek-v3"
        self.gpt_4o="gpt-4o"
        self.gpt_4o_mini="gpt-4o-mini"
        self.gpt_4o_2024_11_20="gpt-4o-2024-11-20"
class freeModel:
    def __init__(self):
        self.DeepSeek_R1_Distill_Qwen_7B="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
        # deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
        self.DeepSeek_R1_Distill_Qwen_1_5B="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
        # Qwen/Qwen2.5-7B-Instruct  编码和数学等领域具有显著改进的能力
        self.Qwen_Qwen2_5_7B_Instruct="Qwen/Qwen2.5-7B-Instruct"
        # Qwen/Qwen2.5-Coder-7B-Instruct 增强了编码能力，还保持了数学和通用能力的优势
        self.Qwen_Qwen2_5_Coder_7B_Instruct="Qwen/Qwen2.5-Coder-7B-Instruct"
        # Qwen/Qwen2-7B-Instruct
        self.Qwen_Qwen2_7B_Instruct="Qwen/Qwen2-7B-Instruct"
class nofreemod:
    def __init__(self):
        # Qwen2-VL-7B-Instruct (Pro)
        self.Qwen2_VL_7B_Instruct="Pro/Qwen/Qwen2-VL-7B-Instruct"
class doubaomod:
    def __init__(self):
        # Doubao-1.5-vision-pro-32k
        self.Doubao_1_5_vision_pro_32k="doubao-1-5-vision-pro-32k-250115"
        # Doubao-vision-lite-32k
        self.Doubao_vision_lite_32k="doubao-vision-lite-32k-241015"
class aliModel:
    def __init__(self):
        # qwen2.5-vl-7b-instruct
        self.qwen2_5_vl_7b_instruct="qwen2.5-vl-7b-instruct"

gptmods=gptModel()
freemods=freeModel()
nofreemods=nofreemod()
doubaomods=doubaomod()
aliModels=aliModel()

api_key="sk-L2rYdR6vAoFYIrwDF8B863D5274a4fFd85012c54EcC93424"
