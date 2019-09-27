from base64 import b64encode
from sys import argv
import json
import requests

# python label_detection_example.py (APIキー) (画像ファイルのパス)

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

if __name__ == '__main__':
    api_key, *image_filenames = argv[1:]

    img_requests = []
    for imgname in image_filenames:
        with open(imgname, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                    'image': {'content': ctxt},
                    'features': [{
                        'type': 'LABEL_DETECTION',
                        'maxResults': 5
                     }]
            })
            
    response = requests.post(ENDPOINT_URL,
                             data=json.dumps({"requests": img_requests}).encode(),
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})

    for idx, resp in enumerate(response.json()['responses']):
        print(json.dumps(resp, indent=2))