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
signName = "吴宇超"
signPhone = 15976427940
signIdCard = 440785199202226310
account = 6212262012002653779
image = "http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg"
images = "http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg,http://qiniu.hsbro.cn/1568087953840_%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_201909091529361.jpg"
email = "550535582@qq.com"
phone = "15976427940"
idCard = "440981199602164628"
Excel = "http://qiniu.hsbro.cn/1564122444913_中山珠峰汽车维修有限公司资质审核表.xlsx"
rar = "http://qiniu.hsbro.cn/1564558039473_1561341162079_%E8%B4%A7%E7%89%A9%E4%BF%9D%E9%99%A9%E5%90%88%E5%90%8C.rar"
address = "安徽省合肥市巢湖市安徽省合肥市滨湖区万达未来塔B座3303-3308室工号155"
carName = "2018款MAXU V80 2.5T 6挡傲运通长轴高顶6座"
remark = "审核通过"
rate = 0.080

class test_01_Order1(unittest.TestCase,requestMethod):
    log = Log()
    purchasePrice = random.randint(1000,200000) # 采购价
    paidDeposit = random.randint(100,2000) # 已付订金
    bond = purchasePrice * 0.2 # 应付保证金
    amount = purchasePrice * 0.8 - paidDeposit # 垫资总额
    carInfo = {}
    carInfo["carName"] = "本田 思域 2016款 1.5L"
    carInfo["style"] = "豪华版"
    carInfo["frameNumber"] = "LNAA2AA13K5003256"
    carInfo["produceYear"] = nowTime
    carInfo["gearbox"] = "自动"
    carInfo["interiorColor"] = "黄色"
    carInfo["type"] = "标配"
    carInfo["number"] = 1
    carInfo["color"] = "炫耀黑"
    carInfo["amount"] = amount
    carInfo["guidePrice"] = random.randint(1000,200000) # 指导价
    carInfo["purchasePrice"] = purchasePrice
    carInfo["price"] = random.randint(1000,200000) # 销售价
    carInfo = json.dumps(carInfo, ensure_ascii=False)
    def test_01_Shop_Submit_Order(self):
        print(" ")
        self.log.info("-------SHOP下单保理1-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="login_v2/index",account=r.shopAccount,password=r.shopPassword)
        # 提交订单
        if self.s.json()["resultCode"]==200:

            self.post(address="frontend_v2/order/create",params=
            {
                "act":"add", # add提交，draft草稿
                "paidDeposit":self.paidDeposit, # 已交订金（汽贸店给4S店）
                "deposit":self.paidDeposit,# 支付订金（客户给汽贸店）
                "voucher":image,# 定金支付凭证
                "contractUrl":image,# 购车合同
                "period":30,# 融资期限
                "bond":self.bond,# 应付保证金
                "pickUpTime":nowTime,# 提车日期
                "carsInfo":self.carInfo,
                "userName":signName,# 上牌方
                "phone":signPhone,
                "address":address,
                "idCard":signIdCard,
                "shopName":orgName,
                "orgAddress":address,
                "orgLink":signName,# 4S联系人
                "orgPhone":phone,
                "account":account,
                "reAccount":account,
                "payRemark":"替xx付款",
                "provinceName":"广东省",
                "cityName":"深圳市",
                "areaName":"南山区",
                "bankName":"广发银行",
                "bankBranch":"南山支行",
                "accept":1,
            })

        else:
            print("未知错误")
    def test_02_Admin_Verify_Order(self):
        self.log.info("-------ADMIN审核订单-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:

            # 保理1订单列表
            self.get(address="work_v2/order/index")
            self.orderId = self.s.json()["data"]["list"][0]["id"]
            # 保理1详情
            self.get(address="work_v2/order/detail",params={"orderId":self.orderId})
            self.B3Title = self.s.json()["data"]["contractList"]["B3"]["Title"]
            self.B3Url = self.s.json()["data"]["contractList"]["B3"]["Template"]
            self.B4Title = self.s.json()["data"]["contractList"]["B4"]["Title"]
            self.B4Url = self.s.json()["data"]["contractList"]["B4"]["Template"]
            # 调整融资金额以及利率
            self.post(address="work_v2/order/adjustAmount",params=
            {
                "orderId":self.orderId,
                "amount":self.amount, # 垫资总额
                "rate":rate,# 利率
            })
            # 审核订单
            # 合同参数
            B3 = {}
            B3["loading"] = "false"
            B3["isUpload"] = 0 # 0：合同非上传
            B3["type"] = 3 # 合同类型
            B3["title"] = self.B3Title # 合同名称
            B3["contractUrl"] = self.B3Url # 合同模板
            B4 = {}
            B4["loading"] = "false"
            B4["isUpload"] = 0
            B4["type"] = 3
            B4["title"] = self.B4Title
            B4["contractUrl"] = self.B4Url
            contractList = {}
            contractList["B3"] = B3
            contractList["B4"] = B4
            contractList = json.dumps(contractList,ensure_ascii=False)
            self.post(address="work_v2/order/verify",params=
            {
                "orderId":self.orderId,
                "state":2,
                "reason":remark,
                "attachment":image,
                "contractList":contractList
            })
            # 总经理审核，发起合同签署
            self.get(address="h5_v2/contract/confirmSign",params=
            {
               "type":2,
                "id":self.orderId,
                "signType":0,
            })
        else:
            print("未知错误")
class test_02_Order1(unittest.TestCase,requestMethod):
    def test_01_Admin_ConfirmLoan(self):
        print(" ")
        self.log.info("-------ADMIN收到保证金-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:

            # 保理1订单列表
            self.get(address="work_v2/order/index")
            self.orderId = self.s.json()["data"]["list"][0]["id"]
            # 确认收到保证金
            self.post(address="work_v2/order/confirmLoan",params=
            {
                "orderId":self.orderId,
                "type":1,
                "voucher":image,
                "remark":remark
            })
            # 录入物流信息
            self.post(address="work_v2/order/logisticsInfo",params=
            {
                "orderId":self.orderId,
                "name":orgName,
                "plateNumber":licenseCode,
                "pickUpName":signName,
                "idCardOn":image,
                "idCardOff":image,
                "checkName":signName,
                "checkIdCardOn":image,
                "checkIdCardOff":image,
                "idCard":signIdCard,
                "remark":remark,
                "checkIdCard":signIdCard,
                "logisticsTime":nowTime,
                "contract":image
            })
            # 录入验车信息
            self.post(address="work_v2/order/checkCar",params=
            {
                "orderId":self.orderId,
                "frameNumber":"LNAA2AA13K50032561",
                "image":image,
                "contract":image,
                "transportList":image,
                "remark":remark,
            })
        else:
            print("未知错误")
    def test_02_Shop_AllowPickUp(self):
        print(" ")
        self.log.info("-------SHOP验车-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="login_v2/index",account=r.shopAccount,password=r.shopPassword)
        if self.s.json()["resultCode"]==200:

            # 订单列表
            self.get(address="frontend_v2/order/index")
            self.orderId =self.s.json()["data"]["list"][0]["id"]
            # 同意验车
            self.get(address="frontend_v2/order/allowPickUp",params=
            {
                "orderId":self.orderId,
                "scheme":1,
                "remark":remark
            })
        else:
            print("未知错误")
    def test_03_Admin_VerifyLoan(self):
        print(" ")
        self.log.info("-------ADMIN同意放款-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:

            # 保理1订单列表
            self.get(address="work_v2/order/index")
            self.orderId = self.s.json()["data"]["list"][0]["id"]
            # 总经理同意放款
            self.post(address="h5_v2/order/verifyLoan",params=
            {
                "orderId":self.orderId,
                "code":8432,
                "remark":remark,
            })
            # 财务确认线下放款
            self.post(address="work_v2/order/confirmLoan",params=
            {
                "orderId":self.orderId,
                "type":3,
                "voucher":image,
                "remark":remark,
            })
            # 确认收齐票证
            self.post(address="work_v2/order/verifyTicket",params=
            {
                "orderId":self.orderId,
                "ticketDate":nowTime,
                "remark":remark,
                "image":image,
            })
            # 录入装车信息
            self.post(address="work_v2/order/loadCar",params=
            {
                "orderId":self.orderId,
                "image":image,
                "handover":image,
                "remark":remark,
            })
            # 录入入库信息
            self.post(address="work_v2/order/unStock",params=
            {
                "orderId":self.orderId,
                "image":images,
                "stockSheet":images,
                "stockAddress":address,
                "logisticsFee":random.randint(100,2000),
                "remark":remark
            })
        else:
            print("未知错误")
    def test_04_Shop_SettlementApply(self):
        print(" ")
        self.log.info("-------SHOP提车申请-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="login_v2/index",account=r.shopAccount,password=r.shopPassword)
        if self.s.json()["resultCode"]==200:
            # 订单列表
            self.get(address="frontend_v2/order/index")
            self.orderId =self.s.json()["data"]["list"][0]["id"]
            # 提车申请
            self.post(address="frontend_v2/order/settlementApply",params=
            {
                "orderId":self.orderId,
                "userName":signName,
                "phone":signPhone,
                "idCard":signIdCard,
                "settleDate":nowTime,
                "idCardOn":image,
                "idCardOff":image,
                "remark":remark,
            })
        else:
            print("未知错误")
    def test_05_Admin_LaunchB7(self):
        print(" ")
        self.log.info("-------ADMIN审核结算-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:
            # 保理1订单列表
            self.get(address="work_v2/order/index")
            # 取列表第一个订单ID
            self.orderId = self.s.json()["data"]["list"][0]["id"]
            # 订单详情
            self.get(address="work_v2/order/detail",params={"orderId":self.orderId})
            self.reduceFee = random.randint(1,10)
            self.totalAmount = float(self.s.json()["data"]["totalAmount"]) - self.reduceFee
            self.serviceCharge = self.s.json()["data"]["serviceCharge"]
            self.totalFee = self.s.json()["data"]["interests"]
            # 审核通过，发起B7签署
            self.get(address="work_v2/order/launchB7",params={"orderId":self.orderId})
            # 业务支持审核结算
            self.post(address="work_v2/order/verifyAmount",params=
            {
                "orderId":self.orderId,
                "totalAmount":self.totalAmount,# 回款金额
                "ticketFee":0,# 票证滞纳金
                "ticketDate":nowTime,# 票证日期
                "settleDate":nowTime,# 结算日期
                "otherFee":random.randint(100,2000),# 其他费用
                "serviceCharge":self.serviceCharge,# 服务费
                "reduceFee":self.reduceFee,# 减免金额
                "remark":remark,
                "contractNo":licenseCode, # 合同编号
                "keyCount":random.randint(1,10), # 车钥匙数量
                "remarkImage":image, # 附件
                "state":1,# 1：提交
            })
            # 运营总监审核减免
            self.post(address="work_v2/order/verifyReduce",params=
            {
                "state":1,
                "orderId":self.orderId,
                "reduceFee":self.reduceFee,
                "reason":remark,
            })
            # 财务确认结算金额
            self.post(address="work_v2/order/confirmSettle",params=
            {
                "state": 1,
                "orderId": self.orderId,
                "reason": remark,
            })
            # 财务收到回款金额
            self.post(address="work_v2/order/confirmLoan",params=
            {
                "orderId":self.orderId,
                "type":2,
                "voucher":image,
                "remark":remark,
            })
            # 总经理同意放车
            self.get(address="h5_v2/order/allowCar",params=
            {
                "state": 1,
                "orderId": self.orderId,
                "reason": remark,
                "code":8432,
            })
            # 业务支持录入票证
            self.post(address="work_v2/order/ticket",params=
            {
                "orderId":self.orderId,
                "logisticsNo":licenseCode,
                "image":image,
                "remark":remark
            })
        else:
            print("未知错误")
if __name__=="__main__":
    unittest.main()