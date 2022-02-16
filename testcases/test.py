import base64
import OpenSSL
import asn1tools

# data1='@'
# #base64编码
# baseData1=base64.b64encode(data1.encode('utf-8'))
# print(baseData1)


# data2=b'dmsTestaaaa'
# # print(type(data2))
# print("hex:",data2.hex())
# #base64编码
# baseData2=base64.b64encode(data2)
# print(baseData2)
#
# with open("F:\\test\\pkm2","rb") as fp:
#     crt_data = fp.read()
# #base64编码
# readFilebase64=base64.b64encode(crt_data)
# print(readFilebase64)


#
# #base64解码
# decodeData1 = base64.b64decode(baseData1)
# # str(yuan,'utf-8')
# print(decodeData1)

# #base64解码
# decodeData2 = base64.b64decode(baseData2)
# # str(yuan,'utf-8')
# print(decodeData2)
#
#
# #对证书进行base64解码
# base64Cert="MIID4TCCA46gAwIBAgIOAP82uoFQQTbGpeLZWd4wCgYIKoEcz1UBg3UwgYcxFzAVBgNVBAMMDkFJRElNQ0VOVElUWUlEMRMwEQYDVQQLDAoxMjM0NTY3ODkwMTEwLwYKCZImiZPyLGQBGRYhSFNNejVrODJ1OE52eVo0dUNvQ0xwQlpxVDhhMlZ4MmpXMRcwFQYKCZImiZPyLGQBGRYHQUlEREFJRDELMAkGA1UEBhMCQ04wHhcNMjIwMTE5MDIyNTM1WhcNMjcwMTE5MTU1OTU5WjBsMREwDwYDVQQDDAhkbXNpZDAwNDExMC8GCgmSJomT8ixkARkWIUhTTXo1azgydThOdnlaNHVDb0NMcEJacVQ4YTJWeDJqVzEXMBUGCgmSJomT8ixkARkWB0FJRERBSUQxCzAJBgNVBAYTAkNOMIGcMBQGByqGSM49AgEGCSqBHM9VAYIsAgOBgwAEc7JWnxYV8GpiwAyQd1KpYOgzrn6MWatpu1QeAN/zQjd9ihO98/SE2VdB7SSxCZPvSpC8QwRzPnl6icBso6eCJgQGt2PgbdEhDNkOm6UWocy8KEaXRoto32kbGCZeg/zjgw9rnj7IFKdqZNW53N59vanARVH8o6/dlKLeljRvleC/o4IBsjCCAa4wKQYDVR0OBCIEIPS4WOI1mz1/eOBYDLOKch9ZOyhE/ilc4JHo0wwtzkh+MIHNBgNVHSMEgcUwgcKAII4lmzkAoScXdXPxftbH+Agehpelp35Y9mfDEb28o4EsoYGNpIGKMIGHMRcwFQYDVQQDDA5BSURJTUNFTlRJVFlJRDETMBEGA1UECwwKMTIzNDU2Nzg5MDExMC8GCgmSJomT8ixkARkWIUhTTXo1azgydThOdnlaNHVDb0NMcEJacVQ4YTJWeDJqVzEXMBUGCgmSJomT8ixkARkWB0FJRERBSUQxCzAJBgNVBAYTAkNOgg4A/te6j5F9BcH4cbkaijAmBgNWHhgEHzAdMBugGaAXhhVsZGFwOi8vMTcyLjE2LjEuNjozODkwDgYDVR0PAQH/BAQDAgO4MBYGA1UdJQEB/wQMMAoGCCsGAQUFBwMCMGEGA1UdHwRaMFgwVqBUoFKGUGxkYXA6Ly8xMjcuMC4wLjE6Mzg5L09VPWlybCxEQz1IU016NWs4MnU4TnZ5WjR1Q29DTHBCWnFUOGEyVngyalcsREM9QUlEREFJRCxDPUNOMAoGCCqBHM9VAYN1A0EAbqvRhGzTalTI88MK0euogWnle6wrC5SrK5M23EG7Z2b4KdFStR2ZeetbIPfTTni5albCpcJSdM881oZsj5lg0w=="
# base64DecodeCert = base64.b64decode(base64Cert)
# #将解码后的证书保存成文件
# certFile = open("C:\\Users\\zhangjuan\\Downloads\\topUkeyCert.cer","wb+")
# certFile.write(base64DecodeCert)
# certFile.close()


# #读取本地证书
# with open("C:\\Downloads\\EnvelopedData1(2).dat","rb") as fp:
#     crt_data = fp.read()
# #进行base64编码
# certBase64=base64.b64encode(crt_data)
# print("certBase64",certBase64)


# import OpenSSL
# #读取本地证书
# with open("C:\\Users\\zhangjuan\\Downloads\\topUkeyCert.cer","rb") as fp:
#     crt_data = fp.read()
# certData = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1,(crt_data))
# print(certData.get_issuer())
# print(certData.get_issuer().get_components())
# print(certData.get_notAfter())


#读取本地二进制文件
# with open("F:\\test\\pkm2","rb") as fp:
#     crt_data = fp.read()
# fp.close()
# wf= open("F:\\test\\pkmtttt","wb")
# wf.write(crt_data)
# wf.close()

import binascii

hex_str = "557365723a20746573740d0a50617373776f72643a206f7073313233210d0a"

hex = hex_str.encode('utf-8')
str_bin = binascii.unhexlify(hex)
str = str_bin.decode('utf-8')

print(str)
print('zzzz5555')




