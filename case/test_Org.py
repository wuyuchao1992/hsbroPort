# coding:utf-8
import unittest,json,random,time,warnings,re
from common.logger import Log
from common.page import requestMethod
from config import readConfig as r

timestamp = (str(time.time()).replace('.', ''))[:-4]
nowTime = time.strftime("%Y-%m-%d", time.localtime())
orgName = "湖南游戏狗电竞文化发展有限公司"
licenseCode = "91430104MA4L65624C"
corporation = "常凌"
signName = "吴晓雯"
signPhone = 13822148475
signIdCard = 440785199309030027
# signName = "吴宇超"
# signPhone = 15976427940
# signIdCard = 440785199202226310
# signName = "刘嘉达"
# signPhone = 18826416507
# signIdCard = "44078119920506151X"
image = "http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg"
email = "550535582@qq.com"
phone = "15976427940"
idCard = "440981199602164628"
Excel = "http://qiniu.hsbro.cn/1564122444913_中山珠峰汽车维修有限公司资质审核表.xlsx"
rar = "http://qiniu.hsbro.cn/1547967789476_1111.rar"
address = "安徽省合肥市巢湖市安徽省合肥市滨湖区万达未来塔B座3303-3308室工号155"
carName = "2018款MAXU V80 2.5T 6挡傲运通长轴高顶6座"
other = "[{\"title\": \"这是资料标题1\",\"remark\":\"这是资料说明1\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"},{\"title\": \"这是资料标题2\",\"remark\":\"这是资料说明2\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"}]"
class TEST_01_ADMIN_SUBMIT_PERSONAL_ORG(unittest.TestCase,requestMethod):

    # 随机生成手机号码
    userAccount = 19667890000 + random.randint(1001, 9999)
    log = Log()
    # 个人
    def test_Personal_Submit_Info(self):
        print(" ")
        # 后台登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:
            # 提交个人认证
            self.post(address="work_v2/organization/create",params={
               "userAccount":self.userAccount, # 门店登录账号
               "type":"persecdelar",# org：汽贸店 agent：中介 4store：4s店 secdealer：二手车商 persecdelar：个人二手车商
               "netType":"2",# 入网类型：1企业 2个人
               "name": signName,  # 个人姓名
               "securities": image,  # 产权证明或租赁合同、租金凭证
               "image": image,  # 公司照片
               "address": "粤海街道高新南九道10号深圳湾科技生态园10栋A座11层1109室",  # 公司地址
               "account": "621226201200669865",  # 对公账号
               "bankName": "工商银行",  # 银行名称
               "bankBranch": "罗湖分行",  # 支行名称
               "rentPaymentVoucher":image, # 近三月租金凭证
               "phone": signPhone,  # 法人手机
               "idCard": signIdCard,  # 法人身份证
               "idCardOn": image,  # 法人身份证正面
               "idCardOff": image,  # 法人身份证反面
               "isShareHolder": "0",  # 法人是否大股东 0：不是 1：是
               "signPhone": signPhone,  # 签署人手机号码
               "signIdCard": signIdCard,  # 签署人身份证号码
               "signIdCardOn": image,  # 签署人身份证正面
               "signIdCardOff": image,  # 签署人身份证反面
               "certificate": image,  # CA证书照片
               "verifyAccount": "sam",  # 征信账号
               "verifyPwd": "abc`1234",  # 征信密码
               "verifyCode": "886",  # 征信验证码
               "verifyReport": rar,  # 征信报告
               "other": other,# 其他资料
               "provinceId": "440000",  # 省ID
               "cityId": "440300",  # 市ID
               "areaId": "440305",  # 区ID
               "provinceName": "广东省",
               "cityName": "深圳市",
               "areaName": "南山区",
               "payroll": image,  # 银行流水
               "businessId": "0",  # 业务ID  不填写或为0：保理一业务  2：保理二业务
               "utilityBill": image,  # 水电单
               "maritalStatus":"已婚无子女", # 婚姻状况
               "spouseName":"赵敏", # 配偶姓名
               "spouseIdCard":idCard, # 配偶身份证
               "spouseIdCardOn":image, # 配偶身份证正面
               "spouseIdCardOff":image, # 配偶身份证反面
               "salesContract":rar, # 销售合同
                })
            # 门店列表
            self.orgList(params={"keywords": signName})
            # 门店详情
            self.get(address="work_v2/organization/detail", params={"orgId": self.orgId})
            # 获取详情参数
            self.caId = self.s.json()["data"]["caInfo"]["caId"]
            self.companyName = self.s.json()["data"]["name"]
            self.licenseCode = self.s.json()["data"]["licenseCode"]
            self.corporation = self.s.json()["data"]["corporation"]
            self.phone = self.s.json()["data"]["phone"]
            self.idCard = self.s.json()["data"]["idCard"]
            # self.businessLicense = self.s.json()["data"]["license"][0]
            self.idCardOn = self.s.json()["data"]["idCardOn"]
            self.idCardOff = self.s.json()["data"]["idCardOff"]
            self.authorizationUrl = self.s.json()["data"]["certificate"]
            self.authorizationLink = r.H5URL + "ca/auth?_plat=shop&auth=sms"
            self.signName = self.s.json()["data"]["signName"]
            self.signPhone = self.s.json()["data"]["signPhone"]
            self.signIdCard = self.s.json()["data"]["signIdCard"]
            self.signIdCardOn = self.s.json()["data"]["signIdCardOn"]
            self.signIdCardOff = self.s.json()["data"]["signIdCardOff"]
            # 区域经理列表
            self.get("work_v2/user/clerkList")
            self.clerkId = self.s.json()["data"][0]["id"]
            self.clerkName = self.s.json()["data"][0]["userName"]
            # 框架合同列表
            self.get("work_v2/organization/businessContract")
            self.contractTitle01 = self.s.json()["data"][0]["contract"][0]["contractTitle"]
            self.contractUrl01 = self.s.json()["data"][0]["contract"][0]["contractUrl"]
            self.contractType01 = self.s.json()["data"][0]["contract"][0]["contractType"]
            self.businessId01 = self.s.json()["data"][0]["businessId"]
            self.contractTitle02 = self.s.json()["data"][1]["contract"][0]["contractTitle"]
            self.contractUrl02 = self.s.json()["data"][1]["contract"][0]["contractUrl"]
            self.contractType02 = self.s.json()["data"][1]["contract"][0]["contractType"]
            self.businessId02 = self.s.json()["data"][1]["businessId"]
            self.businessIds = str(re.findall('"businessId":(\d+)', self.s.text))
            self.businessIds = self.businessIds.replace("'", "")
            self.businessIds = self.businessIds.replace("[", "")
            self.businessIds = self.businessIds.replace("]", "")
            self.businessIds = self.businessIds.replace(" ", "")

            # 发送CA授权
            self.post(address="work_v2/systemconfig/createCa",params= {
                "type": 2,  # 1企业 2个人
                "orgId": self.orgId,
                "companyName": self.companyName,
                "licenseCode": self.licenseCode,
                "corporation": self.corporation,
                "phone": self.phone,
                "idCard": self.idCard,
                # "businessLicense": self.businessLicense,
                "idCardOn": self.idCardOn,
                "idCardOff": self.idCardOff,
                "authorizationUrl": self.authorizationUrl,
                "authorizationLink": self.authorizationLink,
                "caId": self.caId,
                "signName": self.signName,
                "signPhone": self.signPhone,
                "signIdCard": self.signIdCard,
                "signIdCardOn": self.signIdCardOn,
                "signIdCardOff": self.signIdCardOff,
            })
            # 短信授权申请CA
            self.postNotNeedToken(address="publics_v2/shortMessAuth",params= {
                            "caId": self.caId,
                            "phone": self.phone,
                            "code": "8432",
                            "timestamp": self.timestamp,
                        })
            # 合同参数
            self.contractList = json.dumps([{"contractTitle": self.contractTitle01,
                                        "contractUrl": self.contractUrl01,
                                        "contractType": self.contractType01,
                                        "guid": self.create_uid(),
                                        "businessId": self.businessId01,
                                        "visible": "false",
                                        "contractNo": "",
                                        "isUpload": 0,
                                        "signMethod": 0,
                                        "caIds": self.caId
                                        },{
                                        "contractTitle": self.contractTitle02,
                                        "contractUrl": self.contractUrl02,
                                        "contractType": self.contractType02,
                                        "guid": self.create_uid(),
                                        "businessId": self.businessId02,
                                        "visible": "false",
                                        "contractNo": "",
                                        "isUpload": 0,
                                        "signMethod": 0,
                                        "caIds": self.caId
                                       }])
            # 业务审核
            self.post(address="work_v2/organization/verify",params={
                          "orgId": self.orgId,
                          "clerkId": self.clerkId,
                          "clerkName": self.clerkName,
                          "contract": self.contractList,
                          "state": 1,  # -1  拒绝  1：通过
                          "remark": u"审核通过",
                          "attachment": "",
                          "amount": "0",
                          "sort": "",
                          "businessIds":self.businessIds,
                            })
            # 风控审核
            self.post(address="work_v2/organization/riskVerify",params= {

                                "orgId": self.orgId,
                                "state": "1",
                                "remark": "审核通过",
                                "attachment": Excel,
                              })
            # 风控总监审核
            self.post(address="work_v2/organization/riskDirectorVerify",params={
                            "orgId": self.orgId,
                            "state": "1",
                            "remark": "审核通过",
                            "attachment": Excel,
                            "amount": 1000000
                         })
            # 运营总监审核
            self.post(address="work_v2/organization/operationDirectorVerify",params= {
                "orgId": self.orgId,
                "state": "1",
                "remark": "审核通过",
                "attachment": Excel,
                "amount": 1000000
            })
            # 总经理审核
            self.post(address="h5_v2/organization/managerVerify",params={"orgId": self.orgId,
                "state": "1",
                "remark": "审核通过",
                "attachment": Excel,
                "amount": 1000000
            })
        else:
            print("未知错误")
class TEST_02_ADMIN_SUBMIT_ENTERPRISE_ORG(unittest.TestCase, requestMethod):
    # 随机生成手机号码
    userAccount = 19667890000 + random.randint(1001, 9999)
    log = Log()
    # 企业
    def test_Org_Submit_Info(self):
        print(" ")
        # 后台登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:

            # 提交企业认证
            self.post(address="work_v2/organization/create",params={

                "userAccount": self.userAccount,  # 门店登录账号
                "businessIds":"0,2,3,4",
                "type": "secdealer",  # org：汽贸店 agent：中介 4store：4s店 secdealer：二手车商 persecdelar：个人二手车商
                 "netType": 1,  # 入网类型：1企业 2个人
                 "name":orgName, # 公司名字
                 "licenseCode":licenseCode,# 工商号码
                 "corporation":corporation,# 法人姓名
                 "securities":image,# 产权证明或租赁合同、租金凭证
                 "license":image,# 营业执照
                 "image":image,# 公司照片
                 "address":"粤海街道高新南九道10号深圳湾科技生态园10栋A座11层1109室", # 公司地址
                 "account":"621226201200669865",# 对公账号
                 "bankName":"工商银行",# 银行名称
                 "bankBranch":"罗湖分行", #支行名称
                 "phone":phone,# 法人手机
                 "email":email, # 法人邮箱
                 "idCard":"130635198510286167",# 法人身份证
                 "idCardOn":image, # 法人身份证正面
                 "idCardOff":image,# 法人身份证反面
                 "isShareHolder":"1", # 法人是否大股东 0：不是 1：是
                 "shareHolder":"王五",# 大股东名字
                 "shareHolderPhone":"15976427940", # 大股东电话
                 "shareHolderEmail":email, # 大股东邮箱
                 "shareHolderIdCard":"130635198510286167",# 大股东身份证
                 "shareHolderIdCardOn":image, # 大股东身份证正面
                 "shareHolderIdCardOff":image, # 大股东身份证反面
                 "hasAgent":"1",# 签署人0：法人  1：代理人   为1，则以下字段必填
                 "signName":signName,# 签署人姓名
                 "signPhone":signPhone, # 签署人手机号码
                 "signIdCard":signIdCard, # 签署人身份证号码
                 "signEmail":email,# 签署人邮箱
                 "signIdCardOn":image,# 签署人身份证正面
                 "signIdCardOff":image,# 签署人身份证反面
                 "certificate":image,# CA证书照片
                 "accountType":"0",# 0：委托人账号  1：对公账号
                 "bankList":"[{\"account\": \"6222021907005281742\",""\"bankBranch\": \"罗湖分行\",\"userName\": \"aupl0401\",\"phone\": \"18675343438\",\"bankName\": \"18675343438\"}]",# 委托人银行卡信息
                 "consignName":u"余待永",# 委托人姓名
                 "consignIdCard":"45032619840627183x", # 委托人身份证
                 "consignBankBranch":"罗湖分行",
                 "consignAccount":"91310115695751424K",
                 "consignPhone":phone,# 委托人手机号码
                 "verifyAccount":"sam",# 征信账号
                 "verifyPwd":"abc`1234",# 征信密码
                 "verifyCode":"886",# 征信验证码
                 "verifyReport":"http://qiniu.hsbro.cn/1547967789476_1111.rar",# 征信报告
                 "other":"[{\"title\": \"这是资料标题1\",\"remark\":\"这是资料说明1\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"},{\"title\": \"这是资料标题2\",\"remark\":\"这是资料说明2\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"}]",# 其他资料
                 "provinceId": "440000",# 省ID
                 "cityId":"440300", # 市ID
                 "areaId":"440305",# 区ID
                 "provinceName":"广东省",
                 "cityName":"深圳市",
                 "areaName":"南山区",
                 "payroll":image,# 银行流水
                 "businessId":"0",# 业务ID  不填写或为0：保理一业务  2：保理二业务
                 "utilityBill":image,# 水电单
                 "rentPaymentVoucher": image,  # 近三月租金凭证
                 "salesContract": rar,  # 销售合同

            })
            # 门店列表
            self.orgList()
            # 门店详情
            self.get(address="work_v2/organization/detail", params={"orgId": self.orgId})
            # 获取详情参数
            self.caId = self.s.json()["data"]["caInfo"]["caId"]
            self.companyName = self.s.json()["data"]["name"]
            self.licenseCode = self.s.json()["data"]["licenseCode"]
            self.corporation = self.s.json()["data"]["corporation"]
            self.phone = self.s.json()["data"]["phone"]
            self.idCard = self.s.json()["data"]["idCard"]
            # self.businessLicense = self.s.json()["data"]["license"][0]
            self.idCardOn = self.s.json()["data"]["idCardOn"]
            self.idCardOff = self.s.json()["data"]["idCardOff"]
            self.authorizationUrl = self.s.json()["data"]["certificate"]
            self.authorizationLink = r.H5URL + "ca/auth?_plat=shop&auth=sms"
            self.signName = self.s.json()["data"]["signName"]
            self.signPhone = self.s.json()["data"]["signPhone"]
            self.signIdCard = self.s.json()["data"]["signIdCard"]
            self.signIdCardOn = self.s.json()["data"]["signIdCardOn"]
            self.signIdCardOff = self.s.json()["data"]["signIdCardOff"]
            # 区域经理列表
            self.get("work_v2/user/clerkList")
            self.clerkId = self.s.json()["data"][0]["id"]
            self.clerkName = self.s.json()["data"][0]["userName"]
            # 框架合同列表
            self.get("work_v2/organization/businessContract")
            self.contractTitle01 = self.s.json()["data"][0]["contract"][0]["contractTitle"]
            self.contractUrl01 = self.s.json()["data"][0]["contract"][0]["contractUrl"]
            self.contractType01 = self.s.json()["data"][0]["contract"][0]["contractType"]
            self.businessId01 = self.s.json()["data"][0]["businessId"]
            self.contractTitle02 = self.s.json()["data"][1]["contract"][0]["contractTitle"]
            self.contractUrl02 = self.s.json()["data"][1]["contract"][0]["contractUrl"]
            self.contractType02 = self.s.json()["data"][1]["contract"][0]["contractType"]
            self.businessId02 = self.s.json()["data"][1]["businessId"]
            self.businessIds = str(re.findall('"businessId":(\d+)', self.s.text))
            self.businessIds = self.businessIds.replace("'", "")
            self.businessIds = self.businessIds.replace("[", "")
            self.businessIds = self.businessIds.replace("]", "")
            self.businessIds = self.businessIds.replace(" ", "")

            # 发送CA授权
            self.post(address="work_v2/systemconfig/createCa", params={
                "type": 2,  # 1企业 2个人
                "orgId": self.orgId,
                "companyName": self.companyName,
                "licenseCode": self.licenseCode,
                "corporation": self.corporation,
                "phone": self.phone,
                "idCard": self.idCard,
                # "businessLicense": self.businessLicense,
                "idCardOn": self.idCardOn,
                "idCardOff": self.idCardOff,
                "authorizationUrl": self.authorizationUrl,
                "authorizationLink": self.authorizationLink,
                "caId": self.caId,
                "signName": self.signName,
                "signPhone": self.signPhone,
                "signIdCard": self.signIdCard,
                "signIdCardOn": self.signIdCardOn,
                "signIdCardOff": self.signIdCardOff,
            })
            # 短信授权申请CA
            self.postNotNeedToken(address="publics_v2/shortMessAuth", params={
                "caId": self.caId,
                "phone": self.phone,
                "code": "8432",
                "timestamp": self.timestamp,
            })
            # 合同参数
            self.contractList = json.dumps([{"contractTitle": self.contractTitle01,
                                             "contractUrl": self.contractUrl01,
                                             "contractType": self.contractType01,
                                             "guid": self.create_uid(),
                                             "businessId": self.businessId01,
                                             "visible": "false",
                                             "contractNo": "",
                                             "isUpload": 0,
                                             "signMethod": 0,
                                             "caIds": self.caId
                                             }, {
                                                "contractTitle": self.contractTitle02,
                                                "contractUrl": self.contractUrl02,
                                                "contractType": self.contractType02,
                                                "guid": self.create_uid(),
                                                "businessId": self.businessId02,
                                                "visible": "false",
                                                "contractNo": "",
                                                "isUpload": 0,
                                                "signMethod": 0,
                                                "caIds": self.caId
                                            }])
            # 业务审核
            self.post(address="work_v2/organization/verify", params={
                "orgId": self.orgId,
                "clerkId": self.clerkId,
                "clerkName": self.clerkName,
                "contract": self.contractList,
                "state": 1,  # -1  拒绝  1：通过
                "remark": u"审核通过",
                "attachment": "",
                "amount": "0",
                "sort": "",
                "businessIds": self.businessIds,
            })
            # 风控审核
            self.post(address="work_v2/organization/riskVerify", params={

                "orgId": self.orgId,
                "state": "1",
                "remark": "审核通过",
                "attachment": Excel,
            })
            # 风控总监审核
            self.post(address="work_v2/organization/riskDirectorVerify", params={
                "orgId": self.orgId,
                "state": "1",
                "remark": "审核通过",
                "attachment": Excel,
                "amount": 1000000
            })
            # 运营总监审核
            self.post(address="work_v2/organization/operationDirectorVerify", params={
                "orgId": self.orgId,
                "state": "1",
                "remark": "审核通过",
                "attachment": Excel,
                "amount": 1000000
            })
            # 总经理审核
            self.post(address="h5_v2/organization/managerVerify", params={"orgId": self.orgId,
                                                                          "state": "1",
                                                                          "remark": "审核通过",
                                                                          "attachment": Excel,
                                                                          "amount": 1000000
                                                                          })
        else:
            print("未知错误")
class TEST_03_SHOP_SUBMIT_PERSONAL_ORG(unittest.TestCase,requestMethod):
    # 随机生成手机号码
    account = 19667890000 + random.randint(1001, 9999)
    # account = 13822148475
    password = "c4ca4238a0b923820dcc509a6f75849b"
    log = Log()
    # 个人
    def test_01_Personal_Submit_Org(self):
        print(" ")
        # 创建账号
        self.postNotNeedToken("login_v2/signin", {
            "account": self.account,
            "code": "8432",
            "password": self.password,
            "repassword": self.password,
            "timestamp": timestamp,
        })
        # 登录注册账号
        self.login("login_v2/index", self.account, self.password)
        # 门店提交认证
        self.post("frontend_v2/organization/verify",{
       "type":"persecdelar",# org：汽贸店 agent：中介 4store：4s店 secdealer：二手车商 persecdelar：个人二手车商
       "netType":2,# 入网类型：1企业 2个人
       "name": signName,  # 个人名字
       "securities": image,  # 产权证明或租赁合同、租金凭证
       "image": image,  # 公司照片
       "address": "粤海街道高新南九道10号深圳湾科技生态园10栋A座11层1109室",  # 公司地址
       "account": "621226201200669865",  # 对公账号
       "bankName": "工商银行",  # 银行名称
       "bankBranch": "罗湖分行",  # 支行名称
       "rentPaymentVoucher":image, # 近三月租金凭证
       "phone": signPhone,  # 手机号码
       "idCard": signIdCard,  # 身份证
       "idCardOn": image,  # 法人身份证正面
       "idCardOff": image,  # 法人身份证反面
       "isShareHolder": "0",  # 法人是否大股东 0：不是 1：是
       # "shareHolder": "王五",  # 大股东名字
       # "shareHolderPhone": "15976427940",  # 大股东电话
       # "shareHolderEmail": email,  # 大股东邮箱
       # "shareHolderIdCard": "130635198510286167",  # 大股东身份证
       # "shareHolderIdCardOn": image,  # 大股东身份证正面
       # "shareHolderIdCardOff": image,  # 大股东身份证反面
       # "hasAgent": "1",  # 签署人0：法人  1：代理人   为1，则以下字段必填
       # "signName": u"吴宇超",  # 签署人姓名
       "signPhone": phone,  # 签署人手机号码
       "signIdCard": signIdCard,  # 签署人身份证号码
       # "signEmail": email,  # 签署人邮箱
       "signIdCardOn": image,  # 签署人身份证正面
       "signIdCardOff": image,  # 签署人身份证反面
       "certificate": image,  # CA证书照片
       # "accountType": "1",  # 0：委托人账号  1：对公账号
       # "consign": "{\"consignIdCard\":\"450423197508186531\",\"account\": \"6222021907005281742\","
       #            "\"bankBranch\": \"工商银行\",\"consignName\": \"aupl0401\",\"consignPhone\": \"18675343438\"}",
       # # 委托人银行卡信息
       # "consignName": u"余待永",  # 委托人姓名
       # "consignIdCard": "45032619840627183x",  # 委托人身份证
       # "consignPhone": phone,  # 委托人手机号码
       "verifyAccount": "sam",  # 征信账号
       "verifyPwd": "abc`1234",  # 征信密码
       "verifyCode": "886",  # 征信验证码
       "verifyReport": "http://qiniu.hsbro.cn/1547967789476_1111.rar",  # 征信报告
       "other": other,# 其他资料
       # 其他资料
       "provinceId": "440000",  # 省ID
       "cityId": "440300",  # 市ID
       "areaId": "440305",  # 区ID
       "provinceName": "广东省",
       "cityName": "深圳市",
       "areaName": "南山区",
       "payroll": image,  # 银行流水
       "businessId": "0",  # 业务ID  不填写或为0：保理一业务  2：保理二业务
       "utilityBill": image,  # 水电单
       "maritalStatus":"已婚无子女", # 婚姻状况
       "spouseName":"赵敏", # 配偶姓名
       "spouseIdCard":idCard, # 配偶身份证
       "spouseIdCardOn":image, # 配偶身份证正面
       "spouseIdCardOff":image, # 配偶身份证反面
       "salesContract":rar, # 销售合同

        })
    def test_02_Verify_Org(self):
        # 后台登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        # 门店列表
        self.orgList()
        # 门店详情
        self.get(address="work_v2/organization/detail", params={"orgId": self.orgId})
        # 获取详情参数
        self.caId = self.s.json()["data"]["caInfo"]["caId"]
        self.companyName = self.s.json()["data"]["name"]
        self.licenseCode = self.s.json()["data"]["licenseCode"]
        self.corporation = self.s.json()["data"]["corporation"]
        self.phone = self.s.json()["data"]["phone"]
        self.idCard = self.s.json()["data"]["idCard"]
        # self.businessLicense = self.s.json()["data"]["license"][0]
        self.idCardOn = self.s.json()["data"]["idCardOn"]
        self.idCardOff = self.s.json()["data"]["idCardOff"]
        self.authorizationUrl = self.s.json()["data"]["certificate"]
        self.authorizationLink = r.H5URL + "ca/auth?_plat=shop&auth=sms"
        self.signName = self.s.json()["data"]["signName"]
        self.signPhone = self.s.json()["data"]["signPhone"]
        self.signIdCard = self.s.json()["data"]["signIdCard"]
        self.signIdCardOn = self.s.json()["data"]["signIdCardOn"]
        self.signIdCardOff = self.s.json()["data"]["signIdCardOff"]
        # 区域经理列表
        self.get("work_v2/user/clerkList")
        self.clerkId = self.s.json()["data"][0]["id"]
        self.clerkName = self.s.json()["data"][0]["userName"]
        # 框架合同列表
        self.get("work_v2/organization/businessContract")
        self.contractTitle01 = self.s.json()["data"][0]["contract"][0]["contractTitle"]
        self.contractUrl01 = self.s.json()["data"][0]["contract"][0]["contractUrl"]
        self.contractType01 = self.s.json()["data"][0]["contract"][0]["contractType"]
        self.businessId01 = self.s.json()["data"][0]["businessId"]
        self.contractTitle02 = self.s.json()["data"][1]["contract"][0]["contractTitle"]
        self.contractUrl02 = self.s.json()["data"][1]["contract"][0]["contractUrl"]
        self.contractType02 = self.s.json()["data"][1]["contract"][0]["contractType"]
        self.businessId02 = self.s.json()["data"][1]["businessId"]
        self.businessIds = str(re.findall('"businessId":(\d+)', self.s.text))
        self.businessIds = self.businessIds.replace("'", "")
        self.businessIds = self.businessIds.replace("[", "")
        self.businessIds = self.businessIds.replace("]", "")
        self.businessIds = self.businessIds.replace(" ", "")

        # 发送CA授权
        self.post(address="work_v2/systemconfig/createCa", params={
            "type": 2,  # 1企业 2个人
            "orgId": self.orgId,
            "companyName": self.companyName,
            "licenseCode": self.licenseCode,
            "corporation": self.corporation,
            "phone": self.phone,
            "idCard": self.idCard,
            # "businessLicense": self.businessLicense,
            "idCardOn": self.idCardOn,
            "idCardOff": self.idCardOff,
            "authorizationUrl": self.authorizationUrl,
            "authorizationLink": self.authorizationLink,
            "caId": self.caId,
            "signName": self.signName,
            "signPhone": self.signPhone,
            "signIdCard": self.signIdCard,
            "signIdCardOn": self.signIdCardOn,
            "signIdCardOff": self.signIdCardOff,
        })
        # 短信授权申请CA
        self.postNotNeedToken(address="publics_v2/shortMessAuth", params={
            "caId": self.caId,
            "phone": self.phone,
            "code": "8432",
            "timestamp": self.timestamp,
        })
        # 合同参数
        self.contractList = json.dumps([{"contractTitle": self.contractTitle01,
                                         "contractUrl": self.contractUrl01,
                                         "contractType": self.contractType01,
                                         "guid": self.create_uid(),
                                         "businessId": self.businessId01,
                                         "visible": "false",
                                         "contractNo": "",
                                         "isUpload": 0,
                                         "signMethod": 0,
                                         "caIds": self.caId
                                         }, {
                                            "contractTitle": self.contractTitle02,
                                            "contractUrl": self.contractUrl02,
                                            "contractType": self.contractType02,
                                            "guid": self.create_uid(),
                                            "businessId": self.businessId02,
                                            "visible": "false",
                                            "contractNo": "",
                                            "isUpload": 0,
                                            "signMethod": 0,
                                            "caIds": self.caId
                                        }])
        # 业务审核
        self.post(address="work_v2/organization/verify", params={
            "orgId": self.orgId,
            "clerkId": self.clerkId,
            "clerkName": self.clerkName,
            "contract": self.contractList,
            "state": 1,  # -1  拒绝  1：通过
            "remark": u"审核通过",
            "attachment": "",
            "amount": "0",
            "sort": "",
            "businessIds": self.businessIds,
        })
        # 风控审核
        self.post(address="work_v2/organization/riskVerify", params={

            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
        })
        # 风控总监审核
        self.post(address="work_v2/organization/riskDirectorVerify", params={
            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
            "amount": 1000000
        })
        # 运营总监审核
        self.post(address="work_v2/organization/operationDirectorVerify", params={
            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
            "amount": 1000000
        })
        # 总经理审核
        self.post(address="h5_v2/organization/managerVerify", params={"orgId": self.orgId,
                                                                      "state": "1",
                                                                      "remark": "审核通过",
                                                                      "attachment": Excel,
                                                                      "amount": 1000000
                                                                      })
class TEST_04_SHOP_SUBMIT_ENTERPRISE_ORG(unittest.TestCase, requestMethod):
    # 随机生成手机号码
    account = 19667890000 + random.randint(1001, 9999)
    # account = 13822148475
    password = "c4ca4238a0b923820dcc509a6f75849b"
    log = Log()
    # 企业
    def test_03_Enterprise_Submit_Org(self):
        # 创建账号
        self.postNotNeedToken(address="login_v2/signin",params={
            "account":self.account,
            "code":"8432",
            "password":self.password,
            "repassword":self.password,
            "timestamp":timestamp,
        })

        # 登录注册账号
        self.login(address="login_v2/index",account=self.account,password=self.password)

        # 门店提交认证
        self.post("frontend_v2/organization/verify",{
         "type": "secdealer",  # org：汽贸店 agent：中介 4store：4s店 secdealer：二手车商 persecdelar：个人二手车商
         "netType": 1,  # 入网类型：1企业 2个人
         "name":orgName, # 公司名字
         "licenseCode":licenseCode,# 工商号码
         "corporation":corporation,# 法人姓名
         "securities":image,# 产权证明或租赁合同、租金凭证
         "license":image,# 营业执照
         "image":image,# 公司照片
         "address":"粤海街道高新南九道10号深圳湾科技生态园10栋A座11层1109室", # 公司地址
         "account":"621226201200669865",# 对公账号
         "bankName":"工商银行",# 银行名称
         "bankBranch":"罗湖分行", #支行名称
         "phone":phone,# 法人手机
         "email":email, # 法人邮箱
         "idCard":idCard,# 法人身份证
         "idCardOn":image, # 法人身份证正面
         "idCardOff":image,# 法人身份证反面
         "isShareHolder":"1", # 法人是否大股东 0：不是 1：是
         "shareHolder":"王五",# 大股东名字
         "shareHolderPhone":"15976427940", # 大股东电话
         "shareHolderEmail":email, # 大股东邮箱
         "shareHolderIdCard":"130635198510286167",# 大股东身份证
         "shareHolderIdCardOn":image, # 大股东身份证正面
         "shareHolderIdCardOff":image, # 大股东身份证反面
         "hasAgent":"1",# 签署人0：法人  1：代理人   为1，则以下字段必填
         "signName":signName,# 签署人姓名
         "signPhone":signPhone, # 签署人手机号码
         "signIdCard":signIdCard, # 签署人身份证号码
         "signEmail":email,# 签署人邮箱
         "signIdCardOn":image,# 签署人身份证正面
         "signIdCardOff":image,# 签署人身份证反面
         "certificate":image,# CA证书照片
         "accountType":"0",# 0：委托人账号  1：对公账号
         "bankList":"[{\"account\": \"6222021907005281742\","
                   "\"bankBranch\": \"罗湖分行\",\"userName\": \"aupl0401\",\"phone\": \"18675343438\",\"bankName\": \"工商银行\"}]",# 委托人银行卡信息
         "consignName":u"余待永",# 委托人姓名
         "consignIdCard":"45032619840627183x", # 委托人身份证
         "consignBankBranch":"罗湖分行",
         "consignAccount":"91310115695751424K",
         "consignPhone":phone,# 委托人手机号码
         "verifyAccount":"sam",# 征信账号
         "verifyPwd":"abc`1234",# 征信密码
         "verifyCode":"886",# 征信验证码
         "verifyReport":"http://qiniu.hsbro.cn/1547967789476_1111.rar",# 征信报告
         "other":"[{\"title\": \"这是资料标题1\",\"remark\":\"这是资料说明1\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"},{\"title\": \"这是资料标题2\",\"remark\":\"这是资料说明2\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"}]",# 其他资料
         "provinceId": "440000",# 省ID
         "cityId":"440300", # 市ID
         "areaId":"440305",# 区ID
         "provinceName":"广东省",
         "cityName":"深圳市",
         "areaName":"南山区",
         "payroll":image,# 银行流水
         "businessId":"0",# 业务ID  不填写或为0：保理一业务  2：保理二业务
         "utilityBill":image,# 水电单
         "rentPaymentVoucher": image,  # 近三月租金凭证
         "salesContract": rar,  # 销售合同
        })
    def test_04_Verify_Org(self):
        # 后台登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        # 门店列表
        self.orgList()
        # 门店详情
        self.get(address="work_v2/organization/detail", params={"orgId": self.orgId})
        # 获取详情参数
        self.caId = self.s.json()["data"]["caInfo"]["caId"]
        self.companyName = self.s.json()["data"]["name"]
        self.licenseCode = self.s.json()["data"]["licenseCode"]
        self.corporation = self.s.json()["data"]["corporation"]
        self.phone = self.s.json()["data"]["phone"]
        self.idCard = self.s.json()["data"]["idCard"]
        # self.businessLicense = self.s.json()["data"]["license"][0]
        self.idCardOn = self.s.json()["data"]["idCardOn"]
        self.idCardOff = self.s.json()["data"]["idCardOff"]
        self.authorizationUrl = self.s.json()["data"]["certificate"]
        self.authorizationLink = r.H5URL + "ca/auth?_plat=shop&auth=sms"
        self.signName = self.s.json()["data"]["signName"]
        self.signPhone = self.s.json()["data"]["signPhone"]
        self.signIdCard = self.s.json()["data"]["signIdCard"]
        self.signIdCardOn = self.s.json()["data"]["signIdCardOn"]
        self.signIdCardOff = self.s.json()["data"]["signIdCardOff"]
        # 区域经理列表
        self.get("work_v2/user/clerkList")
        self.clerkId = self.s.json()["data"][0]["id"]
        self.clerkName = self.s.json()["data"][0]["userName"]
        # 框架合同列表
        self.get("work_v2/organization/businessContract")
        self.contractTitle01 = self.s.json()["data"][0]["contract"][0]["contractTitle"]
        self.contractUrl01 = self.s.json()["data"][0]["contract"][0]["contractUrl"]
        self.contractType01 = self.s.json()["data"][0]["contract"][0]["contractType"]
        self.businessId01 = self.s.json()["data"][0]["businessId"]
        self.contractTitle02 = self.s.json()["data"][1]["contract"][0]["contractTitle"]
        self.contractUrl02 = self.s.json()["data"][1]["contract"][0]["contractUrl"]
        self.contractType02 = self.s.json()["data"][1]["contract"][0]["contractType"]
        self.businessId02 = self.s.json()["data"][1]["businessId"]
        self.businessIds = str(re.findall('"businessId":(\d+)', self.s.text))
        self.businessIds = self.businessIds.replace("'", "")
        self.businessIds = self.businessIds.replace("[", "")
        self.businessIds = self.businessIds.replace("]", "")
        self.businessIds = self.businessIds.replace(" ", "")

        # 发送CA授权
        self.post(address="work_v2/systemconfig/createCa", params={
            "type": 2,  # 1企业 2个人
            "orgId": self.orgId,
            "companyName": self.companyName,
            "licenseCode": self.licenseCode,
            "corporation": self.corporation,
            "phone": self.phone,
            "idCard": self.idCard,
            # "businessLicense": self.businessLicense,
            "idCardOn": self.idCardOn,
            "idCardOff": self.idCardOff,
            "authorizationUrl": self.authorizationUrl,
            "authorizationLink": self.authorizationLink,
            "caId": self.caId,
            "signName": self.signName,
            "signPhone": self.signPhone,
            "signIdCard": self.signIdCard,
            "signIdCardOn": self.signIdCardOn,
            "signIdCardOff": self.signIdCardOff,
        })
        # 短信授权申请CA
        self.postNotNeedToken(address="publics_v2/shortMessAuth", params={
            "caId": self.caId,
            "phone": self.phone,
            "code": "8432",
            "timestamp": self.timestamp,
        })
        # 合同参数
        self.contractList = json.dumps([{"contractTitle": self.contractTitle01,
                                         "contractUrl": self.contractUrl01,
                                         "contractType": self.contractType01,
                                         "guid": self.create_uid(),
                                         "businessId": self.businessId01,
                                         "visible": "false",
                                         "contractNo": "",
                                         "isUpload": 0,
                                         "signMethod": 0,
                                         "caIds": self.caId
                                         }, {
                                            "contractTitle": self.contractTitle02,
                                            "contractUrl": self.contractUrl02,
                                            "contractType": self.contractType02,
                                            "guid": self.create_uid(),
                                            "businessId": self.businessId02,
                                            "visible": "false",
                                            "contractNo": "",
                                            "isUpload": 0,
                                            "signMethod": 0,
                                            "caIds": self.caId
                                        }])
        # 业务审核
        self.post(address="work_v2/organization/verify", params={
            "orgId": self.orgId,
            "clerkId": self.clerkId,
            "clerkName": self.clerkName,
            "contract": self.contractList,
            "state": 1,  # -1  拒绝  1：通过
            "remark": u"审核通过",
            "attachment": "",
            "amount": "0",
            "sort": "",
            "businessIds": self.businessIds,
        })
        # 风控审核
        self.post(address="work_v2/organization/riskVerify", params={

            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
        })
        # 风控总监审核
        self.post(address="work_v2/organization/riskDirectorVerify", params={
            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
            "amount": 1000000
        })
        # 运营总监审核
        self.post(address="work_v2/organization/operationDirectorVerify", params={
            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
            "amount": 1000000
        })
        # 总经理审核
        self.post(address="h5_v2/organization/managerVerify", params={"orgId": self.orgId,
                                                                      "state": "1",
                                                                      "remark": "审核通过",
                                                                      "attachment": Excel,
                                                                      "amount": 1000000
                                                                      })
if __name__ == "__main__":
    unittest.main()
