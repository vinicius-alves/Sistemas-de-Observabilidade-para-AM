import pandas as pd
import numpy as np
import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RequestHelper:

    last_request = None
    
    def random_sleep(self, min_v = 2, max_v = 6):
        #time.sleep(np.random.randint(min_v,max_v))
        time.sleep(0.3)

    def do_request(self, url, data, verify, headers = None,type_req = 'get', callback = None, json = True, max_tentativas = 10):
        
        if headers is None:
            headers = {"user-agent": "okhttp/3.4.0"}
        infomacao_adquirida = False
        erro_no_request = False
        count = 0
        resp = None
        while(not(infomacao_adquirida) and not(erro_no_request)):
            try:
                if(type_req == 'get'):
                    r = requests.get(url, data = data, headers = headers,verify = verify, timeout = 180)
                elif(type_req == 'post'):
                    r = requests.post(url, data = data, headers = headers,verify = verify, timeout = 180)
                
                self.last_request = r

                if(json):
                    resp = r.json()
                else:
                    resp = r.text
                    
                if(callback is not None):
                    callback(resp)
                infomacao_adquirida = True
            except:
                count+=1
                if count>max_tentativas:
                    erro_no_request = True
                else:
                    self.random_sleep()
                    
        return resp, erro_no_request
        




