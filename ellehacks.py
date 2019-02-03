# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:58:04 2019

@author: Daria Yampolsky
"""

import json
import os
from flask import Flask
from flask import request
from flask import make_response


#flask app should start in global layout
app = Flask(__name__)
#'http://489bc730.ngrok.io'
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print('Request:')
    print(json.dumps(req,indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res,indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

# =============================================================================
# def makewebhookresult(req):
#     if req.get('queryresult').get('action')!= 'interest':
#         return {}
#     result = req.get('queryresult')
#     parameters = result.get('parameters')
#     search_term = parameters.get('medicalterm')
#     links = {"vomit": "vomit-url", "abdominal pain": "stomach-ache url", "heart attack": "heart attack url"}
#     out_message = "here is an article about {}:{}".format(search_term, str(links[search_term]))
#     print("response:")
#     print(out_message)
#     return {
#         #'speech': out_message,
#         'fulfillmenttext': out_message,
#         'source': 'bobbot'
#     }
# =============================================================================


    
#promise = Promise(lambda resolve,reject: resolve('RESOLVED!'))  

def makeWebhookResult(req):
    if req.get('queryResult').get('action') == 'Suicide':   
     #   result = req.get('queryResult')
      #  parameters = result.get('parameters')
       # search_term = parameters.get('medicalName')
        return {
        "fulfillmentText": "displayed&spoken response",
  "fulfillmentMessages": [
    {    
     "payload":{ 
     "facebook": {   
     "attachment":{
      "type":"template",
       "payload": {
   
"template_type":"button",
        "text":" I've noticed you're in distress. If you are having suicidal thoughts at this time I would like you to contact Crisis Service Canada.",
        "buttons":[
          {
            "type":"phone_number",
            "title":"Call Representative",
            "payload":"+18334564566 "
          }
        ]
  }}}}}],}
    
    else:
        return {}
    

    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    print("Starting app on port %d" %(port))
    app.run(debug=True, port=port,host='0.0.0.0')    
    
    
    
    
    
    
    