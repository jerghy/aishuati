import requests
from requests.auth import HTTPBasicAuth
from tqdm import tqdm
import fitz  # PyMuPDF
import os
import json
from PIL import Image
import io
import base64
import runai
import mod
from openai import OpenAI
import time

name="高中必刷题数学人教A版选择性必修2.pdf"
pagestart=8
pageend=89


# url = "https://chogo.teracloud.jp/dav/documents/output.mp3"
url = "https://chogo.teracloud.jp/dav/shuati/"+name
auth = HTTPBasicAuth("ThomasXie", "43rKo29cev5Uzbyp")

response = requests.get(url, auth=auth, stream=True)

if response.status_code == 200:
    total_size = int(response.headers.get('content-length', 0))
    with open(name, "wb") as f:
        for data in tqdm(response.iter_content(1024), total=total_size // 1024, unit='KB'):
            f.write(data)
    print("下载成功")
else:
    print(f"下载失败，状态码：{response.status_code}")

def pdf_to_images(pdf_path, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    
    # 遍历每一页并保存为图片
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        pix.save(f'{output_folder}/page_{page_num+1}.png')
# 使用示例
pdf_name = name
current_file_path = os.path.abspath(__file__)
pdf_path = os.path.join(os.path.dirname(current_file_path), pdf_name)
print(pdf_path)
output_folder = f'output_{pdf_name.split(".")[0]}'

pdf_to_images(pdf_path, output_folder)


print("PDF转图片完成")

def convert_image_to_webp_base64(input_image_path):
    try:
        with Image.open(input_image_path) as img:
            byte_arr = io.BytesIO()
            img.save(byte_arr, format='webp')
            byte_arr = byte_arr.getvalue()
            base64_str = base64.b64encode(byte_arr).decode('utf-8')
            return base64_str
    except IOError:
        print(f"Error: Unable to open or convert the image {input_image_path}")
        return None

# base64_image=convert_image_to_webp_base64("input.png")




outputrelease={}
pdf_document = fitz.open(pdf_path)
# 遍历每一页range(len(pdf_document))

messages=[
        {
            "role": "user",
            "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "",
                            "detail":"low"
                        }
                    },
                    {
                        "type": "text",
                        "text": "你把图片中的文字有排版的发给我"
                    }
                ]
        },
        {
            "role": "system",
            "content": "不管在什么情况都用中文回答"
        }
    ]
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=mod.aliyunkey,
    base_url=mod.aliyunurl,
)

def aishuati(inputimg):
    global base64_image
    base64_image=convert_image_to_webp_base64(inputimg)
    completion = client.chat.completions.create(
    model=mod.aliModels.qwen2_5_vl_7b_instruct,  # 此处以qwen-vl-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[
            {"role": "user","content": [
                {
                    "type": "text",
                    "text": "你把图片中的文字有排版的发给我"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/webp;base64,{base64_image}"}
                    }
            ]
            }
        ]
    )
    return completion.model_dump_json()

for page_num in range(pagestart,pageend+1):
    pg=f'{output_folder}/page_{page_num+1}.png'
    

    try:
        result=aishuati(pg)
        outputrelease[pg]=result
        print(f"成功 page {pg}")
    except Exception as e:
        print(f"Error processing page {page_num}: {e}")
        print(f"失败 page {pg}")
        time.sleep(30)
        try:
            result=aishuati(pg)
            outputrelease[pg]=result
            print(f"成功 page {pg}")
        except Exception as e:
            print(f"Error processing page {page_num}: {e}")
            print(f"失败 page {pg}")
            time.sleep(60)
            try:
                result=aishuati(pg)
                outputrelease[pg]=result
                print(f"成功 page {pg}")
            except Exception as e:
                print(f"Error processing page {page_num}: {e}")
                print(f"失败 page {pg}")

            
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(outputrelease, f, ensure_ascii=False, indent=4)
    


    
