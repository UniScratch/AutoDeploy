from flask import Flask, request
import hashlib
import hmac
import subprocess
from config import *

def verify_hmac_hash(data, signature):
    mac = hmac.new(bytes(SECRET, 'UTF-8'), msg=data, digestmod=hashlib.sha256)
    return hmac.compare_digest('sha256=' + mac.hexdigest(), signature)


app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if(verify_hmac_hash(request.data,request.headers.get('X-Hub-Signature-256'))):
        subprocess.Popen(DEPLOY_COMMAND, shell=True)
        return "success"
    else:
        return("auth failed",500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='11460', debug=True)
