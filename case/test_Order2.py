# coding:utf-8
import unittest,json,random,time,warnings,re
from common.logger import Log
from common.page import requestMethod
from config import readConfig as r
from common.base import Base
timestamp = (str(time.time()).replace('.', ''))[:-4]
nowTime = time.strftime("%Y-%m-%d", time.localtime())
orgName = "湖南游戏狗电竞文化发展有限公司"
licenseCode = "91430104MA4L65624C"
corporation = "常凌"
signName = "吴宇超"
signPhone = 15976427940
signIdCard = 440785199202226310
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
# 保理2
contractUrl = "http://qiniu.hsbro.cn/1567666941167_C3-1V2.0.pdf"
rate = 0.66
period = 20
class test_01_Order2(unittest.TestCase,requestMethod):
    log = Log()
    def test_01_ShopSubmitOrder2(self):
        print(" ")
        self.log.info("-------SHOP下单保理2-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="login_v2/index",account=r.shopAccount,password=r.shopPassword)
        if self.s.json()["resultCode"]==200:

            # 导入Excel
            self.upload(address="publics_v2/excelImport",files={'file':('1.xls',open('C:\\Users\\Tony\\Desktop\\1.xls','rb'),'xls'),})
            # Excel返回车辆信息
            carList = self.s.json()["data"]
            newCarList = []
            for i in carList:
                i["doing"] = "false"
                # 使用dumps将list转化为json字符串
                # 并且拼接上父节点的内容
                temp_i = '{"carsInfo":' + json.dumps(i,ensure_ascii=False) + '}'
                newCarList.append(temp_i)
            newCarList = str(newCarList)
            newCarList = newCarList.replace("'","")
            # print(newCarList)
            # 提交订单
            self.post(address="frontend_v2/orderbatch/create",params=
            {
                "act":"add",
                "carList":newCarList,
                "creditorList":json.dumps([{"name": "胡歌", "phone": phone, "idCard": idCard, "amount": "1000000000","contractName": "卖身契", "contractDate": nowTime,"contractUrl": image}],ensure_ascii=False),
                "companyName":orgName,
                "address":"广东省深圳市",
                "linkName":"谢天华",
                "linkPhone":phone,
                "account":"62122620120026537796212262012002653779",
                "reAccount":"62122620120026537796212262012002653779",
                "payRemark":"替xxx打款",
                "provinceName":"浙江省",
                "cityName":"杭州市",
                "bankName":"中国建设银行",
                "bankBranch":"国才支行",
                "accept":1,
                "other":json.dumps([{"title":"附件1","remark":"","images":rar},{"title":"附件2","remark":"","images":rar}],ensure_ascii=False),
                "totalAmount":4000,
                "creditAmount":1000000000
            })
        else:
            print("未知错误")
    def test_02_AdminAuditOrder2(self):
        self.log.info("------ADMIN保理2------")
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:
            # 保理2列表
            self.get(address="work_v2/batch/index")
            self.orderId = self.s.json()["data"]["list"][0]["id"]
            # 保理2详情
            self.get(address="work_v2/batch/detail",params={"id":self.orderId})
            self.amount = self.s.json()["data"]["adjustAmount"]
            # 业务支持审核
            i = {}
            i["contractNo"] = timestamp
            i["title"] = "testContract"
            i["contractUrl"] = contractUrl
            contractList = '{"C4":' + json.dumps(i, ensure_ascii=False) + '}'
            self.post(address="work_v2/batch/verify",params=
            {
                "orderId":self.orderId,
                "state":1, #  -1 ：拒绝  1：通过
                "contractList":contractList,
                "rate":rate,
                "period":period,
                "amount":self.amount,
                "remark":address,
                "attachment":image
            })
            # 运营总监审核
            self.post(address="work_v2/batch/operationDirectorVerify",params=
            {
                "orderId":self.orderId,
                "state":1,
                "rate":rate,
                "period":period,
                "remark":address,
                "attachment": image
            })
            # H5工作台统计
            self.get(address="h5_v2/matter/lists")
            # H5保理2列表
            self.get(address="h5_v2/batch/index",params={"state":0})
            self.h5OrderId = self.s.json()["data"]["list"][0]["id"]
            # H5保理2详情
            self.get(address="h5_v2/batch/detail",params={"id":self.h5OrderId})
            # 总经理审核
            self.post(address="h5_v2/batch/managerVerify",params=
            {
                "orderId":self.h5OrderId,
                "state":1,
                "rate":rate,
                "sort":0,
            })
        else:
            print("未知错误")
class test_02_Order2(unittest.TestCase,requestMethod):
    log = Log()
    b = Base()
    def test_01_AdminAuditOrder(self):
        print(" ")
        self.log.info("-------物流下单-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:

            # 保理2列表
            self.get(address="work_v2/batch/index")
            self.batchId = self.s.json()["data"]["list"][0]["id"]
            # 订单车列表
            self.get(address="work_v2/batch/carList",params={"id":self.batchId})
            self.orderId = str(re.findall('"id":(\d+)', self.s.text))
            self.orderId = self.orderId.replace("'", "")
            self.orderId = self.orderId.replace("[", "")
            self.orderId = self.orderId.replace("]", "")
            # 安排物流
            i = {}
            i["name"] = orgName
            i["idCard"] = idCard
            i["phone"] = phone
            i = json.dumps(i,ensure_ascii=False)
            self.post(address="work_v2/batch/logistics",params=
            {
                "remark":remark,
                "attachment":image,
                "batchId":self.batchId,
                "orderIds":self.orderId,
                "isSelectAll":1,
                "name":orgName,
                "licensePlate":licenseCode,
                "carCount":5,
                "loadTime":nowTime,
                "picker":i,
                "verifier":i,
            })
            # 一键验车
            self.post(address="work_v2/orderbatch/batchVerifyCar",params=
            {
                "remark":remark,
                "attachment":image,
                "batchId":self.batchId,
                "orderIds":self.orderId,
                "isSelectAll":1,
                "images":image,
            })
        else:
            print("未知错误")
    def test_02_ShopCheckCar(self):
        print(" ")
        self.log.info("-------SHOP确认验车-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="login_v2/index", account=r.shopAccount, password=r.shopPassword)
        if self.s.json()["resultCode"]==200:

            # 保理2列表
            self.get(address="frontend_v2/batch/index")
            self.batchId = self.s.json()["data"]["list"][0]["id"]
            # 订单车列表
            self.get(address="frontend_v2/batch/carList",params={"id":self.batchId})
            # 订单车列表
            self.get(address="frontend_v2/batch/carList",params={"id":self.batchId})
            self.orderId = str(re.findall('"id":(\d+)', self.s.text))
            self.orderId = self.orderId.replace("'", "")
            self.orderId = self.orderId.replace("[", "")
            self.orderId = self.orderId.replace("]", "")
            # 一键确认验车
            self.post(address="frontend_v2/orderbatch/checkCarVerifyBatch",params=
            {
                "remark": remark,
                "attachment": image,
                "batchId": self.batchId,
                "orderIds": self.orderId,
                "isSelectAll": 1,
                "state": 1,
            })
        else:
            print("未知错误")
    def test_03_AdminVerifyTicket(self):
        print(" ")
        self.log.info("-------确认收齐票证-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:

            # 保理2列表
            self.get(address="work_v2/batch/index")
            self.batchId = self.s.json()["data"]["list"][0]["id"]
            # 保理2车列表
            self.get(address="work_v2/batch/carList",params={"id":self.batchId})
            self.orderId = str(re.findall('"id":(\d+)', self.s.text))
            self.orderId = self.orderId.replace("'", "")
            self.orderId = self.orderId.replace("[", "")
            self.orderId = self.orderId.replace("]", "")
            # 确认收齐票证
            self.post(address="work_v2/orderbatch/verifyTicket",params=
            {
                "remark": remark,
                "attachment": image,
                "batchId": self.batchId,
                "orderIds": self.orderId,
                "isSelectAll": 1,
            })
        else:
            print("未知错误")
class test_03_Order2(unittest.TestCase,requestMethod):
    log = Log()
    b = Base()
    def test_01_H5VerifyLoan(self):
        print(" ")
        self.log.info("-------总经理同意放款-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:
            # 保理2列表
            self.get(address="h5_v2/batch/index")
            self.batchId = self.s.json()["data"]["list"][0]["id"]
            print(self.batchId )
            # 保理2车列表
            self.get(address="h5_v2/batch/carList",params={"id":self.batchId})
            self.orderId = str(re.findall('"id":(\d+)', self.s.text))
            self.orderId = self.orderId.replace("'", "")
            self.orderId = self.orderId.replace("[", "")
            self.orderId = self.orderId.replace("]", "")
            # 总经理同意放款
            self.post(address="h5_v2/orderbatch/verifyLoan",params=
            {
                "remark": remark,
                "attachment": image,
                "batchId": self.batchId,
                "orderIds": self.orderId,
                "isSelectAll": 1,
                "code": 8432
            })
            # 财务确认放款
            self.post(address="work_v2/orderbatch/confirmLoan",params=
            {
                "remark": remark,
                "attachment": image,
                "batchId": self.batchId,
                "orderIds": self.orderId,
                "isSelectAll": 1,
                "type":2,
            })
        else:
            print("未知错误")
    def test_02_ShopSettlementApply(self):
        print(" ")
        self.log.info("-------SHOP发起结算-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="login_v2/index", account=r.shopAccount, password=r.shopPassword)
        if self.s.json()["resultCode"]==200:
            # 保理2列表
            self.get(address="frontend_v2/batch/index")
            self.batchId = self.s.json()["data"]["list"][0]["id"]
            # 订单车列表
            self.get(address="frontend_v2/batch/carList",params={"id":self.batchId})
            # 订单车列表
            self.get(address="frontend_v2/batch/carList",params={"id":self.batchId})
            self.orderId = str(re.findall('"id":(\d+)', self.s.text))
            self.orderId = self.orderId.replace("'", "")
            self.orderId = self.orderId.replace("[", "")
            self.orderId = self.orderId.replace("]", "")
            # 发起结算
            i = {}
            i["name"] = orgName
            i["idCard"] = idCard
            i["phone"] = phone
            i["idCardOn"] = image
            i["idCardOff"] = image
            i = json.dumps(i,ensure_ascii=False)
            self.post(address="frontend_v2/orderbatch/settlementApply",params=
            {
                "remark": remark,
                "attachment": image,
                "batchId": self.batchId,
                "orderIds": self.orderId,
                "isSelectAll": 1,
                "settleDate":nowTime,
                "picker":i
            })
        else:
            print("未知错误")
    def test_03_AdminVerifyAmount(self):
        print(" ")
        self.log.info("-------结算审核-------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="work_v2/login", account=r.h5Account, password=r.adminPassword)
        if self.s.json()["resultCode"]==200:

        # 保理2列表
            self.get(address="work_v2/batch/index")
            self.batchId = self.s.json()["data"]["list"][0]["id"]
            # 结算列表
            self.get(address="work_v2/batch/carList",params={"id":self.batchId,"status":522})
            self.orderIds = self.s.json()["data"]["list"][0]["orderIds"]
            self.amount = float(self.s.json()["data"]["list"][0]["amount"])
            self.amount = float(self.s.json()["data"]["list"][0]["amount"])
            self.rate = self.s.json()["data"]["list"][0]["rate"]
            self.voucherTime = self.s.json()["data"]["list"][0]["list"][0]["voucherTime"]
            self.totalFee = float(self.s.json()["data"]["list"][0]["totalFee"])
            self.settleDate = self.s.json()["data"]["list"][0]["settleDate"]
            self.settleId = self.s.json()["data"]["list"][0]["id"]
            self.serviceCharge = float(self.b.getTwoFloat(self.totalFee*0.0336,2))+float(self.b.getTwoFloat(self.amount*0.00005,2))
            self.reduceFee = random.randint(10,100)
            self.totalAmount = self.amount + self.totalFee + self.serviceCharge - self.reduceFee
            # 业务支持审核结算
            self.post(address="work_v2/orderbatch/verifyAmount",params=
            {
                "settleDate":self.settleDate,
                "serviceCharge":self.serviceCharge,
                "otherFee":self.reduceFee,
                "reduceFee":self.reduceFee,
                "amount":self.totalAmount,
                "remark":remark,
                "attachment":image,
                "batchId":self.batchId,
                "settleId":self.settleId,
                "state":1,
            })
            # 运营总监审核减免
            self.post(address="work_v2/orderbatch/verifyReduce",params=
            {
                "settleDate":self.settleDate,
                "serviceCharge":self.serviceCharge,
                "otherFee":self.reduceFee,
                "reduceFee":self.reduceFee,
                "amount":self.totalAmount,
                "remark":remark,
                "attachment":image,
                "batchId":self.batchId,
                "settleId":self.settleId,
                "state":1,
            })
            # 财务确认结算
            self.post(address="work_v2/orderbatch/confirmSettle",params=
            {
                "settleDate":self.settleDate,
                "serviceCharge":self.serviceCharge,
                "otherFee":self.reduceFee,
                "reduceFee":self.reduceFee,
                "amount":self.totalAmount,
                "remark":remark,
                "attachment":image,
                "batchId":self.batchId,
                "settleId":self.settleId,
                "state":1,
            })
            # 财务确认收到回款
            self.post(address="work_v2/orderbatch/confirmLoan",params=
            {
                "settleDate":self.settleDate,
                "serviceCharge":self.serviceCharge,
                "otherFee":self.reduceFee,
                "reduceFee":self.reduceFee,
                "amount":self.totalAmount,
                "remark":remark,
                "attachment":image,
                "batchId":self.batchId,
                "settleId":self.settleId,
                "state":1,
                "type":1,
                "orderIds":self.orderIds,
            })
            # 总经理放车
            self.post(address="h5_v2/orderbatch/allowCar",params=
            {
                "batchId":self.batchId,
                "code":8432,
                "orderIds":self.orderIds,
                "isSelectAll":1,
                "remark":remark,
                "state":1
            })
            # 寄出票证
            self.post(address="work_v2/orderbatch/ticket",params=
            {
                "remark":remark,
                "attachment":image,
                "batchId":self.batchId,
                "orderIds":self.orderIds,
                "isSelectAll":1,

            })
        else:
            print("未知错误")
if __name__=="__main__":
    unittest.main()