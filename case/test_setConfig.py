# coding:utf-8
import unittest, time
from common.page import requestMethod
from common.base import Base
from config import readConfig as r


class editConfig(unittest.TestCase,requestMethod,Base):

    # 时间戳
    ticks = str(time.time()).replace('.', '')
    timestamp = ticks[:-4]

    def testContract(self):

        self.login(address="work_v2/login",account=r.adminAccount, password=r.adminPassword)
        # image：接口参数
        file = {'image':('B3.pdf',open('D:\\sysContract\\B3.pdf','rb'),'pdf'),}
        # 上传文件接口
        if self.s.json()["resultCode"]==200:
            self.upload("publics_v2/upload", file)
            self.ContractUrl = self.s.json()["data"]["url"]
            # 上传文件到法大大
            self.postNotNeedToken("publics_v2/uploadTemplate",
                                  {"template": self.ContractUrl, "timestamp": self.timestamp}, )
            self.TemplateId = self.s.json()["data"]
            # 修改合同配置
            self.post("work_v2/config/create", {
                "name": "Contract",
                "key": "B3",
                "subkey[Title]": "B3保理融资服务合同",
                "subkey[TemplateId]": self.TemplateId,
                "subkey[Template]": self.ContractUrl,
                "remark": "B3保理融资服务合同",
                # "subkey[SignKeyword]":u"签章处",
            })
        else:
            print("未知错误")

    def testSendSms(self):
        self.login(address="work_v2/login",account=r.adminAccount, password=r.adminPassword)
        self.post("work_v2/config/create", {
            "name": "send_sms",
            "key": "risk_control",
            "subkey[0]": "18811103837",
            # "subkey[1]": "18811103837",
            # "subkey[2]": "18811103837",
            "remark": "这是给风控发送短信配置",            # "subkey[3]": "13556823051",

        })

if __name__ == "__main__":
    editConfig().testSendSms()

