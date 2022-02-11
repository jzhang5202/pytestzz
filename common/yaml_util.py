import os

import yaml



#读取yaml文件
def read_yaml(key):
    with open(os.getcwd()+'/extract.yml',encoding="utf-8") as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

#写入yaml文件
def write_yaml(data):
    with open(os.getcwd()+'/extract.yml',encoding="utf-8",mode="a") as f:
        yaml.dump(data,stream=f,allow_unicode=True)

#清空yaml文件,mode='w'
def clean_yaml():
    with open(os.getcwd()+'/extract.yml',encoding="utf-8",mode="w") as f:
        f.truncate()

#读取测试用例的yaml文件
def read_testcase_yaml(yaml_name):
    with open(os.getcwd()+'/testcases/'+yaml_name,encoding="utf-8") as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value


# # 读取extract.yml 中的containerName 的值
# def get_extract_containerName(node_name):
#     return read_testcase_yaml()
