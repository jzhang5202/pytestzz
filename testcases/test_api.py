import json
import re
from string import Template

import pytest
import requests
import yaml

from common.all_request import AllRequest
from common.yaml_util import write_yaml, read_yaml,read_testcase_yaml


class TestApi:
    containerName =""

    #获取用户列表
    @pytest.mark.parametrize("caseinfo",read_testcase_yaml("getUserList.yml"))
    # @pytest.mark.smoke
    def test_get_userList(self,caseinfo):
        url = caseinfo['request']['url']
        method = caseinfo['request']['method']

        res = AllRequest().all_send_request(method,url=url)

        NameStr = res.json()["result"]
        pattern = re.compile(r'(?<=(dmsUK\|\|))(.*)')
        containerName = pattern.search(NameStr)[0]

        #把数据组合成dict字典
        extract_data={"containerName":containerName}
        write_yaml(extract_data)

        print(res.text)



    #获取Ukey状态
    def test_getDevState(self):
        url = "http://127.0.0.1:4433/SOF_GetDevState"
        res = requests.get(url=url)
        print(res.text)


    #登录
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("login.yml"))
    def test_login(self,caseinfo):
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        params = caseinfo['request']['params']
        res = requests.post(url=url,params=params)
        print(res.text)


    # #登出
    # @pytest.mark.run(order=-1)
    # def test_loginOut(self):
    #     url="http://127.0.0.1:4433/SOF_LoginOut"
    #     res = requests.post(url=url)
    #     print(res.text)


    #导出签名证书
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("exportSignCert.yml"))
    # @pytest.mark.users
    def test_post_ExportSignCert(self,caseinfo):
        url = caseinfo['request']['url']
        params = {
            "containerName": read_yaml("containerName")
        }
        # json.loads()#把json字符串转成dict
        # json.dumps() #把dict转成json字符串

        # params = caseinfo['request']['params']
        print("params", params)
        res = requests.post(url=url,params=params)
        print(res.text)

        SignCertBase64 = res.json()["result"]
        print("SignCertBase64:",SignCertBase64)
        # #把数据组合成dict字典
        extract_data={"SignCertBase64":SignCertBase64}
        write_yaml(extract_data)

    #3.1.9	导出加密类型的用户标识 SOF_ExportEncCert
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("exportEncCert.yml"))
    def test_ExportEncCert(self,caseinfo):
        url = caseinfo['request']['url']
        params = caseinfo['request']['params']
        print("params", params)
        res = requests.post(url=url, params=params)
        print(res.text)

        encCertBase64 = res.json()["result"]
        print("encCertBase64:",encCertBase64)
        # #把数据组合成dict字典
        extract_data={"encCertBase64":encCertBase64}
        write_yaml(extract_data)

    # #3.1.10	修改PIN SOF_ChangePassWd
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("changePassWd.yml"))
    # def test_ChangePassWd(self,caseinfo):
    #     url = caseinfo['request']['url']
    #     params = caseinfo['request']['params']
    #     print("params", params)
    #     res = requests.post(url=url, params=params)
    #     print(res.text)

    # #3.1.11	获取PIN重试次数 SOF_GetPinRetryCount
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("getPinRetryCount.yml"))
    # def test_GetPinRetryCount(self,caseinfo):
    #     url = caseinfo['request']['url']
    #     res = requests.post(url=url)
    #     print(res.text)


    # #3.1.12	重置用户PIN码SOF_ResetPassWd
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("resetPassWd.yml"))
    # def test_ResetPassWd(self,caseinfo):
    #     url = caseinfo['request']['url']
    #     params = caseinfo['request']['params']
    #     print("params", params)
    #     res = requests.post(url=url, params=params)
    #     print(res.text)

    #3.1.13	数字签名 SOF_SignData
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("signData.yml"))
    def test_SignData(self,caseinfo):
        url = caseinfo['request']['url']
        params = caseinfo['request']['params']
        print("params", params)
        res = requests.post(url=url, params=params)
        print(res.text)

        signValue = res.json()["result"]
        # #把数据组合成dict字典
        extract_data={"signValue-"+caseinfo['request']['params']['type']:signValue}
        write_yaml(extract_data)


    #3.1.14	数字验签 SOF_VerifySignedData
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("verifySignedData.yml"))
    def test_VerifySignedData(self,caseinfo):

        url = caseinfo['request']['url']

        # params = {
        #     "Base64EncodeCert": read_yaml("SignCertBase64"),
        #     "inData": caseinfo['request']['inData'],
        #     "signValue":read_yaml("signValue-base64"),
        #     "type":caseinfo['request']['type']
        # }
        if caseinfo['name']=="verifySignedDatabase64":
            data = {'signValue': read_yaml("signValue-base64")}
        elif caseinfo['name']=="verifySignedDatanobase64":
            data = {'signValue': read_yaml("signValue-nobase64")}
        data['Base64EncodeCert'] = read_yaml('SignCertBase64')

        re = Template(str(caseinfo)).safe_substitute(data)
        paramsInfo = yaml.safe_load(stream=re)
        print('paramsInfo:',paramsInfo)

        res = requests.post(url=url, params=paramsInfo['request']['params'])
        print(res.text)



    # 3.15 消息签名 SOF_SignMessage
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("signMessage.yml"))
    def test_SignMessage(self,caseinfo):
        url = caseinfo['request']['url']
        params = {
            "containerName":read_yaml("containerName"),
            "inData": caseinfo['request']['inData'],
            "type": caseinfo['request']['type']
        }
        print("params:",params)
        res = requests.post(url=url,params=params)

        print(res.text)

        signMessageValue = res.json()["result"]
        # #把数据组合成dict字典
        extract_data={"signMessageValue-"+caseinfo['request']['type']:signMessageValue}
        write_yaml(extract_data)

    # 3.16 消息验签 SOF_VerifySignedMessage
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("verifySignedMessage.yml"))
    def test_VerifySignedMessage(self,caseinfo):
        url = caseinfo['request']['url']

        if caseinfo['name']=="verifySignedMessageBase64":
            data = {'messageData': read_yaml("signMessageValue-base64")}
        elif caseinfo['name']=="verifySignedMessagenoBase64":
            data = {'messageData': read_yaml("signMessageValue-nobase64")}


        # with open("E:\\python\\pytestzj\\testcases\\verifySignedMessage.yml",encoding="utf-8") as f:
        #     re = Template(f.read()).safe_substitute(data)


        #替换文本中的$占位符 Template.substitute、 Template.safe_substitute,即从caseinfo（str类型）中查找$对应的变量，用data（dict）中的数据进行替换
        re = Template(str(caseinfo)).safe_substitute(data)
        # 返回字典格式的数据---反序列化
        paramsInfo = yaml.safe_load(stream=re)
        print("paramsInfo:",paramsInfo)

        #发送请求
        res = requests.request(method='post',url=url,params=paramsInfo["request"]["params"])
        print(res.text)

    # 3.1.31	数据信封加密SOF_EncryptData
    @pytest.mark.parametrize('caseinfo',read_testcase_yaml('encryptData.yml'))
    def test_encryptData(self,caseinfo):
        url = caseinfo['request']['url']
        data = {}
        data['containerName'] = read_yaml('containerName')
        data['base64EncodeCert'] = read_yaml('encCertBase64')
        re = Template(str(caseinfo)).safe_substitute(data)
        paramsInfo = yaml.safe_load(stream=re)

        #发送请求
        res = requests.request(method='post',url=url,params=paramsInfo['request']['params'])
        print(res.text)
        encryptDataRel = res.json()['result']
        extract_data = {'encryptData':encryptDataRel}
        write_yaml(extract_data)

    # 3.1.32	数字信封解密SOF_DecryptData
    @pytest.mark.parametrize('caseinfo',read_testcase_yaml('decryptData.yml'))
    def test_decryptData(self,caseinfo):
        url = caseinfo['request']['url']
        method = caseinfo['request']['method']
        data = {}
        data['containerName'] = read_yaml('containerName')
        data['encryptData'] = read_yaml('encryptData')
        re = Template(str(caseinfo)).safe_substitute(data)
        paramsInfo = yaml.safe_load(stream=re)

        #发送请求
        res = requests.request(method=method,url=url,params=paramsInfo['request']['params'])
        print(res.text)







        













    # @pytest.mark.run(order=1)
    # # @pytest.mark.smoke
    # def test_post_login(self):
    #     url = "http://127.0.0.1:4433/SOF_Login"
    #     params = {
    #         "containerName": TestApi.containerName,
    #         "passWd": "12345678"
    #     }
    #
    #     res = requests.post(url=url, params=params)
    #     # print(res.json())  # 把返回值转化成dict对象
    #     print(res.text)  # 把返回值转化成文本
    #     # print(res.content)  # 把返回值转化成字节类型数据
    #     # print(res.status_code)  # 返回码
    #     # print(res.reason)  # 返回信息
    #     # print(res.cookies)  # 返回的cookies 信息
    #     # print(res.encoding)  # 编码格式
    #     # print(res.headers)  # 响应头
    #     # print(res.request.method) #请求方式
#
# @pytest.mark.usefixtures('execute_database_sql')
# class Testaaa:
#     def test_aaa(self):
#         print("test_aaa")
#
# class Testbbb:
#     def test_bbb(self):
#         print("test_bbbb")
#




