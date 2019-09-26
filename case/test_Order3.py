# coding:utf-8
import unittest,json,random,time,warnings,re
from common.logger import Log
from common.page import requestMethod
from config import readConfig as r
from common.base import Base
timestamp = (str(time.time()).replace('.', ''))[:-4]
nowTime = time.strftime("%Y-%m-%d", time.localtime())
orgName = "广东亲友游戏网络有限公司"
licenseCode = "91440101MA5APDD34P"
corporation = "林晓婷"
# signName = "吴晓雯"
# signPhone = 13822148475
# signIdCard = 440785199309030027
signName = "吴宇超"
signPhone = 13822148475
signIdCard = 440785199309030027
# signName = "刘嘉达"
# signPhone = 18826416507
# signIdCard = "44078119920506151X"
image = "http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg"
images = "http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg"
email = "550535582@qq.com"
phone = "15976427940"
idCard = "440981199602164628"
Excel = "http://qiniu.hsbro.cn/1564122444913_中山珠峰汽车维修有限公司资质审核表.xlsx"
rar = "http://qiniu.hsbro.cn/1564558039473_1561341162079_%E8%B4%A7%E7%89%A9%E4%BF%9D%E9%99%A9%E5%90%88%E5%90%8C.rar"
address = "安徽省合肥市巢湖市安徽省合肥市滨湖区万达未来塔B座3303-3308室工号155"
carName = "2018款MAXU V80 2.5T 6挡傲运通长轴高顶6座"
remark = "审核通过"

class test_01_Order3(unittest.TestCase,requestMethod):
    log = Log()
    # 参数
    sex = ["男", "女"]
    maritalStatus = random.choice(["未婚", "已婚无子女", "已婚有子女", "离异", "丧偶", "其他"])
    if maritalStatus == "已婚无子女":
        spousePiccCreditPhoto=image,  # 配偶人保征信授权书照片
        spousePiccCreditSignPhoto=image,  # 配偶人保征信授权书签字照
        spousePiccCreditHandPhoto=image,  # 配偶手持人保征信授权书和签字照片
        spouseBankCreditPhoto=image,  # 配偶银行征信授权书照片
        spouseBankCreditSignPhoto=image,  # 配偶银行征信授权书签字照
        spouseBankCreditHandPhoto=image,  # 配偶手持银行征信授权书和签字照片
        spouseIdCard = signIdCard # 配偶身份证
        spouseName = signName # 配偶姓名
        spousePhone = signPhone # 配偶手机号码
        spouseIdCardOn = image # 配偶身份证正反面
        spouseIdCardOff = image # 配偶身份证正反面
        spouseFontPhoto = image # 配偶正面照片
        spousePiccCreditPhoto=image,  # 配偶人保征信授权书照片
        spousePiccCreditSignPhoto=image,  # 配偶人保征信授权书签字照
        spousePiccCreditHandPhoto=image,  # 配偶手持人保征信授权书和签字照片
        spouseBankCreditPhoto=image,  # 配偶银行征信授权书照片
        spouseBankCreditSignPhoto= image,  # 配偶银行征信授权书签字照
        spouseBankCreditHandPhoto= image,  # 配偶手持银行征信授权书和签字照片
        marriageCertificate = image # 结婚证
        singleCertificate ="" # 单身说明照片，已婚传空

    elif maritalStatus =="已婚有子女":
        spousePiccCreditPhoto=image,  # 配偶人保征信授权书照片
        spousePiccCreditSignPhoto=image,  # 配偶人保征信授权书签字照
        spousePiccCreditHandPhoto=image,  # 配偶手持人保征信授权书和签字照片
        spouseBankCreditPhoto=image,  # 配偶银行征信授权书照片
        spouseBankCreditSignPhoto=image,  # 配偶银行征信授权书签字照
        spouseBankCreditHandPhoto=image,  # 配偶手持银行征信授权书和签字照片
        spouseIdCard = signIdCard # 配偶身份证
        spouseName = signName # 配偶姓名
        spousePhone = signPhone # 配偶手机号码
        spouseIdCardOn = image # 配偶身份证正反面
        spouseIdCardOff = image # 配偶身份证正反面
        spouseFontPhoto = image # 配偶正面照片
        spousePiccCreditPhoto=image,  # 配偶人保征信授权书照片
        spousePiccCreditSignPhoto=image,  # 配偶人保征信授权书签字照
        spousePiccCreditHandPhoto=image,  # 配偶手持人保征信授权书和签字照片
        spouseBankCreditPhoto=image,  # 配偶银行征信授权书照片
        spouseBankCreditSignPhoto= image,  # 配偶银行征信授权书签字照
        spouseBankCreditHandPhoto= image,  # 配偶手持银行征信授权书和签字照片
        marriageCertificate = image # 结婚证
        singleCertificate ="" # 单身说明照片，已婚传空空
    else:
        spousePiccCreditPhoto="",  # 配偶人保征信授权书照片
        spousePiccCreditSignPhoto="",  # 配偶人保征信授权书签字照
        spousePiccCreditHandPhoto="",  # 配偶手持人保征信授权书和签字照片
        spouseBankCreditPhoto="",  # 配偶银行征信授权书照片
        spouseBankCreditSignPhoto="",  # 配偶银行征信授权书签字照
        spouseBankCreditHandPhoto="",  # 配偶手持银行征信授权书和签字照片
        spouseIdCard = "" # 配偶身份证
        spouseName = "" # 配偶姓名
        spousePhone = "" # 配偶手机号码
        spouseIdCardOn = "" # 配偶身份证正反面
        spouseIdCardOff = "" # 配偶身份证正反面
        spouseFontPhoto = "" # 配偶正面照片
        spousePiccCreditPhoto="",  # 配偶人保征信授权书照片
        spousePiccCreditSignPhoto="",  # 配偶人保征信授权书签字照
        spousePiccCreditHandPhoto="",  # 配偶手持人保征信授权书和签字照片
        spouseBankCreditPhoto="",  # 配偶银行征信授权书照片
        spouseBankCreditSignPhoto= "",  # 配偶银行征信授权书签字照
        spouseBankCreditHandPhoto= "",  # 配偶手持银行征信授权书和签字照片
        marriageCertificate = "" # 结婚证
        singleCertificate =image # 单身说明照片，已婚传空空

    livingCondition = ["商品按揭购房", "无按揭购房", "公积金按揭购房", "自建房", "租用", "暂住", "亲属购房"]
    occupation = ["一般职业", "农牧业", "渔业", "木材森林业", "矿业", "采石业", "交通、运输业", "建筑、工程业", "制造业", "新闻出版、广告业", "卫生", "娱乐业", "文教",
                  "宗教", "公共事业", "商业", "金融、保险业", "服务业", "家庭教育", "餐饮、保洁", "保姆、护理", "特殊护理、室外高空作业", "家政其他", "家庭管理", "治安人员",
                  "体育", "其他"]
    position = ["高级领导", "中级领导", "一般员工", "其他", "未知"]
    companyNature = ["事业机关", "国有股份", "外资", "合资", "民营", "私营", "个体", "社会团体"]
    mainSourceIncome = ["经营、租赁所得", "工资", "投资、佣金", "无", "其他"]
    carType = ["新车", "二手车"]
    powerSystemType = ["新能源", "传统动力"]
    netVehiclePrice = random.randrange(100000, 100000000, 10000)
    relation = ["家人", "朋友", "同事"]
    if random.choice(carType) == "新车":
        downPayment = netVehiclePrice * 0.2
        loanAmount = netVehiclePrice * 0.8
    else:
        downPayment = netVehiclePrice * 0.2
        loanAmount = netVehiclePrice * 0.7

    # m = random.randrange(1, 100000000)
    # if m % 2 == 0:
    #     spouseName = "舒淇"
    #     spousePhone = phone
    #     spouseOtherContactMode = "住我家楼下"
    #     immediateFamilyName = ""
    #     immediateFamilyPhone = ""
    #     immediateFamilyRelation = ""
    #     otherContactName = ""
    #     otherContactPhone = ""
    #     otherContactRelation = ""
    # elif m % 3 == 0:
    #     spouseName = ""
    #     spousePhone = ""
    #     spouseOtherContactMode = ""
    #     immediateFamilyName = "舒淇"
    #     immediateFamilyPhone = phone
    #     immediateFamilyRelation = "兄弟"
    #     otherContactName = ""
    #     otherContactPhone = ""
    #     otherContactRelation = ""
    # else:
    #     spouseName = ""
    #     spousePhone = ""
    #     spouseOtherContactMode = ""
    #     immediateFamilyName = ""
    #     immediateFamilyPhone = ""
    #     immediateFamilyRelation = ""
    #     otherContactName = "舒淇"
    #     otherContactPhone = phone
    #     otherContactRelation = "兄弟"
    # def test_03_ShopSubmitOrder3(self):
    #
    #     # 登录
    #     self.login(address="login_v2/index",account="13800138000",password="e10adc3949ba59abbe56e057f20f883e")
    #     # 提交保理三订单
    #     self.post(address="frontend_v2/insuranceorder/saveOrder",params={
    #         "name":"吴宇超",
    #         "phone":phone,
    #         "sex":random.choice(self.sex),
    #         "birthday":nowTime,
    #         "age":18,
    #         "idCard":"440785199202226310",
    #         "idCardEffectiveDate":nowTime,
    #         "idCardBelongAddress":address,
    #         "maritalStatus":random.choice(self.maritalStatus),
    #         "familyPeopleNum":3,
    #         "householdAddress":address,
    #         "livingCondition":random.choice(self.livingCondition),
    #         "livingAddress":address,
    #         "jobCompanyName":"宝鸡有一群怀揣着梦想的少年相信在牛大叔的带领下会创造生命的奇",
    #         "occupation":random.choice(self.occupation),
    #         "position":random.choice(self.position),
    #         "companyNature":random.choice(self.companyNature),
    #         "companyAddress":address,
    #         "companyPhone":"0755-8888888888",
    #         "entryDate":nowTime,
    #         "mainSourceIncome":random.choice(self.mainSourceIncome),
    #         "monthlyIncome":1000000000,
    #         "natureVehicleUse":" 固定自用汽车",
    #         "brandModel":carName,
    #         "carType":random.choice(self.carType),
    #         "powerSystemType":random.choice(self.powerSystemType),
    #         "netVehiclePrice":self.netVehiclePrice,
    #         "downPayment":self.downPayment,
    #         "loanAmount":self.loanAmount,
    #         "loanInstallment":36,
    #         "spouseName":self.spouseName,
    #         "spousePhone":self.spousePhone,
    #         "spouseOtherContactMode":self.spouseOtherContactMode,
    #         "contactInfo":"",
    #     })
    def test_01_ShopsOrder3SaveDraft(self):
        contactInfo = []
        i = {}
        i["name"] = corporation
        i["phone"] = phone
        i["relation"] = random.choice(self.relation)
        contactInfo.append(json.dumps(i,ensure_ascii=False))
        contactInfo.append(json.dumps(i,ensure_ascii=False))
        contactInfo = str(contactInfo)
        contactInfo = contactInfo.replace("'", '')
        # 登录
        self.login(address="login_v2/index",account=r.shopAccount,password=r.shopPassword)
        if self.s.json()["resultCode"]==200:

            # 提交大数据
            self.post(address="frontend_v2/insuranceorder/saveOrder",params={
                "name": signName,  # 借款人姓名
                "phone": signPhone,  # 借款人手机号码
                "idCard": signIdCard,  # 借款人身份证
                "sex": random.choice(self.sex),
                "birthday": nowTime,
                "age": 18,
                "natureVehicleUse": " 固定自用汽车",
                "borrowerFrontPhoto": image,  # 借款人正面照
                "borrowerIdCardOn": image,  # 借款人身份证
                "borrowerIdCardOff": image, # 借款人身份证
                "driverLicenseOn": image,   # 驾照
                "driverLicenseOff": image,  # 驾照
                "repaymentBankPhotoOn": image,  # 还款银行卡
                "singleCertificate":self.singleCertificate, # 单身说明
                "spouseIdCardOn": self.spouseIdCardOn,
                "spouseIdCardOff": self.spouseIdCardOff,
                "borrowerJobCertificate": image,  # 工作证明
                "houseRegisterBookHomePage": image,  # 户口本主页
                "houseRegisterBookSelfPage": image,  # 户口本本人
                "piccCreditPhoto": image,  # 征信授权书照片
                "piccCreditSignPhoto": image,  # 征信授权书签字照
                "piccCreditHandPhoto": image,  # 手持征信授权书及身份证照片
                "bankCreditPhoto": image,  # 银行授权书照片
                "bankCreditSignPhoto": image,  # 银行授权书签字照
                "bankCreditHandPhoto": image,  # 手持银行授权书及身份证照片
                "maritalStatus": self.maritalStatus,
                "spouseIdCard": self.spouseIdCard,  # 配偶身份证
                "spouseName" :self.spouseName, # 配偶姓名
                "spousePhone" : self.spousePhone, # 配偶手机号码

                "repaymentBankPhotoOff": image,
                "spouseFontPhoto":self.spouseFontPhoto,
                "marriageCertificate": self.marriageCertificate,  # 结婚证
                "spousePiccCreditPhoto": self.spousePiccCreditPhoto,  # 配偶人保征信授权书照片
                "spousePiccCreditSignPhoto": self.spousePiccCreditSignPhoto,  # 配偶人保征信授权书签字照
                "spousePiccCreditHandPhoto": self.spousePiccCreditHandPhoto,  # 配偶手持人保征信授权书和签字照片
                "spouseBankCreditPhoto": self.spouseBankCreditPhoto,  # 配偶银行征信授权书照片
                "spouseBankCreditSignPhoto": self.spouseBankCreditSignPhoto,  # 配偶银行征信授权书签字照
                "spouseBankCreditHandPhoto": self.spouseBankCreditHandPhoto,  # 配偶手持银行征信授权书和签字照片

                # "idCardEffectiveDate": nowTime,
                # "idCardBelongAddress": address,
                # "familyPeopleNum": 3,
                # "householdAddress": address,
                # "livingCondition": random.choice(self.livingCondition),
                # "livingAddress": address,
                # "jobCompanyName": orgName,
                # "occupation": random.choice(self.occupation),
                # "position": random.choice(self.position),
                # "companyNature": random.choice(self.companyNature),
                # "companyAddress": address,
                # "companyPhone": "0755-8888888888",
                # "entryDate": nowTime,
                # "mainSourceIncome": random.choice(self.mainSourceIncome),
                # "monthlyIncome": 1000000000,
                # "brandModel": carName,
                # "carType": random.choice(self.carType),
                # "powerSystemType": random.choice(self.powerSystemType),
                # "netVehiclePrice": self.netVehiclePrice,
                # "downPayment": self.downPayment,
                # "loanAmount": self.loanAmount,
                # "loanInstallment": 36,
                # "spouseName": self.spouseName,
                # "spousePhone": self.spousePhone,
                # "spouseOtherContactMode": self.spouseOtherContactMode,
                # "contactInfo": contactInfo,
                "dataType":2,
            })
            # 提交人保保单
            # self.post(address="frontend_v2/insuranceorder/saveOrder", params={
            #     "name": signName,  # 借款人姓名
            #     "phone": signPhone,  # 借款人手机号码
            #     "idCard": signIdCard,  # 借款人身份证
            #     "sex": random.choice(self.sex),
            #     "birthday": nowTime,
            #     "age": 18,
            #     "natureVehicleUse": " 固定自用汽车",
            #     "borrowerFrontPhoto": image,  # 借款人正面照
            #     "borrowerIdCardOn": image,  # 借款人身份证
            #     "borrowerIdCardOff": image,  # 借款人身份证
            #     "driverLicenseOn": image,  # 驾照
            #     "driverLicenseOff": image,  # 驾照
            #     "repaymentBankPhotoOn": image,  # 还款银行卡
            #     "singleCertificate": self.singleCertificate,  # 单身说明
            #     "spouseIdCardOn": self.spouseIdCardOn,
            #     "spouseIdCardOff": self.spouseIdCardOff,
            #     "borrowerJobCertificate": image,  # 工作证明
            #     "houseRegisterBookHomePage": image,  # 户口本主页
            #     "houseRegisterBookSelfPage": image,  # 户口本本人
            #     "piccCreditPhoto": image,  # 征信授权书照片
            #     "piccCreditSignPhoto": image,  # 征信授权书签字照
            #     "piccCreditHandPhoto": image,  # 手持征信授权书及身份证照片
            #     "bankCreditPhoto": image,  # 银行授权书照片
            #     "bankCreditSignPhoto": image,  # 银行授权书签字照
            #     "bankCreditHandPhoto": image,  # 手持银行授权书及身份证照片
            #     "maritalStatus": self.maritalStatus,
            #     "spouseIdCard": self.spouseIdCard,  # 配偶身份证
            #     "spouseName": self.spouseName,  # 配偶姓名
            #     "spousePhone": self.spousePhone,  # 配偶手机号码
            #     "repaymentBankPhotoOff": image,
            #     "spouseFontPhoto": self.spouseFontPhoto,
            #     "marriageCertificate": self.marriageCertificate,  # 结婚证
            #     "spousePiccCreditPhoto": self.spousePiccCreditPhoto,  # 配偶人保征信授权书照片
            #     "spousePiccCreditSignPhoto": self.spousePiccCreditSignPhoto,  # 配偶人保征信授权书签字照
            #     "spousePiccCreditHandPhoto": self.spousePiccCreditHandPhoto,  # 配偶手持人保征信授权书和签字照片
            #     "spouseBankCreditPhoto": self.spouseBankCreditPhoto,  # 配偶银行征信授权书照片
            #     "spouseBankCreditSignPhoto": self.spouseBankCreditSignPhoto,  # 配偶银行征信授权书签字照
            #     "spouseBankCreditHandPhoto": self.spouseBankCreditHandPhoto,  # 配偶手持银行征信授权书和签字照片
            #     # 保单资料
            #     "idCardEffectiveDate": nowTime,
            #     "idCardBelongAddress": address,
            #     "familyPeopleNum": 3,
            #     "householdAddress": address,
            #     "livingCondition": random.choice(self.livingCondition),
            #     "livingAddress": address,
            #     "jobCompanyName": orgName,
            #     "occupation": random.choice(self.occupation),
            #     "position": random.choice(self.position),
            #     "companyNature": random.choice(self.companyNature),
            #     "companyAddress": address,
            #     "companyPhone": "0755-8888888888",
            #     "entryDate": nowTime,
            #     "mainSourceIncome": random.choice(self.mainSourceIncome),
            #     "monthlyIncome": 1000000000,
            #     "officialGuidePrice":random.randint(10000,1000000),
            #     "brandModel": carName,
            #     "carType": random.choice(self.carType),
            #     "powerSystemType": random.choice(self.powerSystemType),
            #     "netVehiclePrice": self.netVehiclePrice,
            #     "downPayment": self.downPayment,
            #     "loanAmount": self.loanAmount,
            #     "isPlusFinance":1,
            #     "plusFinanceAmount":random.randint(1000,20000),
            #     "loanInstallment": 36,
            #     "spouseOtherContactMode": signPhone,
            #     "contactInfo": contactInfo,
            #     "dataType": 1,
            # })
            # 保理3列表
            self.get(address="frontend_v2/insuranceorder/index")
            self.orderId = self.s.json()["data"]["list"][0]["id"]
            # 订单详情
            self.get(address="frontend_v2/insuranceorder/details",params={"id":self.orderId})
            newContactInfo = []
            i = {}
            i["name"] = corporation
            i["phone"] = phone
            i["relation"] = random.choice(self.relation)
            # i["id"] = self.s.json()["data"]["otherContactData"][0]["id"]
            o = {}
            o["name"] = corporation
            o["phone"] = phone
            o["relation"] = random.choice(self.relation)
            # o["id"] = self.s.json()["data"]["otherContactData"][1]["id"]
            newContactInfo.append(json.dumps(i,ensure_ascii=False))
            newContactInfo.append(json.dumps(o,ensure_ascii=False))
            newContactInfo = str(newContactInfo)
            newContactInfo = newContactInfo.replace("'", '')
        else:
            print("未知错误")
        # 编辑订单
        # self.post(address="frontend_v2/insuranceorder/saveOrder",params=
        # {
        #     "id":self.orderId,
        #     "name": signName,  # 借款人姓名
        #     "phone": "18888866666",  # 借款人手机号码
        #     "idCard":signIdCard,  # 借款人身份证
        #     "borrowerIdCardOn": images,
        #     "borrowerIdCardOff": images,
        #     "spouseIdCard": signIdCard,  # 配偶身份证
        #     "spouseIdCardOn": images,
        #     "spouseIdCardOff": images,
        #     "driverLicenseOn": images,
        #     "driverLicenseOff": images,  # 驾照
        #     "borrowerJobCertificate": images,  # 工作证明
        #     "repaymentBankOn": images,  # 还款银行卡
        #     # "repaymentBankOff": images,
        #     "houseRegisterBookHomePage": images,  # 户口本主页
        #     "houseRegisterBookSelfPage": images,  # 户口本本人
        #     "marriageCertificate": images,  # 结婚证
        #     "borrowerFrontPhoto": images,  # 借款人正面照
        #     "piccCreditPhoto": images,  # 征信授权书照片
        #     "piccCreditSignPhoto": images,  # 征信授权书签字照
        #     "piccCreditHandPhoto": images,  # 手持征信授权书及身份证照片
        #     "bankCreditPhoto": images,  # 银行授权书照片
        #     "bankCreditSignPhoto": images,  # 银行授权书签字照
        #     "bankCreditHandPhoto": images,  # 手持银行授权书及身份证照片
        #     "spousePiccCreditPhoto": images,  # 配偶人保征信授权书照片
        #     "spousePiccCreditSignPhoto": images,  # 配偶人保征信授权书签字照
        #     "spousePiccCreditHandPhoto": images,  # 配偶手持人保征信授权书和签字照片
        #     "spouseBankCreditPhoto": images,  # 配偶银行征信授权书照片
        #     "spouseBankCreditSignPhoto": images,  # 配偶银行征信授权书签字照
        #     "spouseBankCreditHandPhoto": images,  # 配偶手持银行征信授权书和签字照片
        #     "sex": random.choice(self.sex),
        #     "birthday": "2018-08-08",
        #     "age": 19,
        #     "idCardEffectiveDate": "2018-08-08",
        #     "idCardBelongAddress": orgName,
        #     "maritalStatus": random.choice(self.maritalStatus),
        #     "familyPeopleNum": 2,
        #     "householdAddress": orgName,
        #     "livingCondition": random.choice(self.livingCondition),
        #     "livingAddress": orgName,
        #     "jobCompanyName": address,
        #     "occupation": random.choice(self.occupation),
        #     "position": random.choice(self.position),
        #     "companyNature": random.choice(self.companyNature),
        #     "companyAddress": orgName,
        #     "companyPhone": "0755-1234567",
        #     "entryDate": "2018-08-08",
        #     "mainSourceIncome": random.choice(self.mainSourceIncome),
        #     "monthlyIncome": 10002220,
        #     "natureVehicleUse": " 固定自用汽车",
        #     "brandModel": orgName,
        #     "carType": random.choice(self.carType),
        #     "powerSystemType": random.choice(self.powerSystemType),
        #     "netVehiclePrice": "88888",
        #     "downPayment": "800",
        #     "loanAmount": "1000",
        #     "loanInstallment": 36,
        #     "spouseName": signName,
        #     "spousePhone": signPhone,
        #     "spouseOtherContactMode": self.spouseOtherContactMode,
        #     "contactInfo": newContactInfo,
        #     "dataType":2,
        # })
        # # 订单详情
        # self.get(address="frontend_v2/insuranceorder/details",params={"id":self.orderId})
