import json

import requests


class AllRequest:
    session = requests.session()  #会话

    def all_send_request(self,method,url,data=None,**kwargs):
        # params,data,json,files
        method = str(method).lower()
        res = None
        if method=="get":
            res = AllRequest.session.request(method=method,url=url,params=data,**kwargs)
        elif method=="post":
            strdata = json.dumps(data)
            res = AllRequest.session.request(method=method, url=url, params=strdata, **kwargs)
        else:
            print("不支持的请求方式")
        return res