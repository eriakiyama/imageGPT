from flask import Flask, request, render_template
import json, time, request, os

app = Flask(__name__)

headers = {
    'Authorization': 'Token r8_NOcgCkrCL7hvJJ0UsGwEzmByzRO3qrg31iCmO',
    'Content-Type' : 'application/json'
}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        q = request.form.get("q")
        print(q)
        body = json.dumps(
        {
            "version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
            "input": { "prompt": q } 
        }
        )
        
        output = request.post('https://api.replicate.com/v1/predictions',data=body,headers=headers)
        time.sleep(10) #online/in internet we need it, but now dont need
        get_url = output.json()['urls']['get']
        get_result = requests.post(get_url,headers=headers).json()['output']

        return(render_template("index.html", result = get_result[0]))
    else:
        return(render_template("index.html", result="waiting for question......."))
    
if __name__ =="__main__":
    app.run()
