import requests
import base64
import json
from sys import argv

# python text_detection_example.py (APIキー) (画像ファイルのパス)

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate?key='

def request_cloud_vison_api(image_base64):
    api_url = ENDPOINT_URL + api_key
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_base64.decode('utf-8')
            },
            'features': [{
                'type': 'TEXT_DETECTION', # 分析内容変更はここ
                'maxResults': 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

def img_to_base64(filepath):
    for imgname in filepath:
        with open(imgname, 'rb') as img:
            img_byte = img.read()
        return base64.b64encode(img_byte)

if __name__ == '__main__':
    api_key, *image_filenames = argv[1:]

    img_base64 = img_to_base64(image_filenames)
    result = request_cloud_vison_api(img_base64)

    #print("{}".format(json.dumps(result, indent=4))) #文字位置など全情報出力

    text_r = result["responses"][0]["fullTextAnnotation"]["text"] #認識文字のみ出力
    print(text_r)