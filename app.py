#from flask import Flask, request, render_template
pip install replicate
import json
import time
import requests

q = input("Enter your picture request : ")
body = json.dumps(
	{
		"version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
 		"input": { "prompt": q } 
	}
)
headers = {
	'Authorization': 'Token r8_NOcgCkrCL7hvJJ0UsGwEzmByzRO3qrg31iCmO',
	'Content-Type': 'application/json'
}
output = requests.post('https://api.replicate.com/v1/predictions',data=body,headers=headers)
time.sleep(10)
get_url = output.json()['urls']['get']
print(get_url)
get_result = requests.post(get_url,headers=headers).json()['output']
print(get_result)

#print image
from PIL import Image
image = Image.open(requests.get(get_result[0], stream=True).raw)
image
