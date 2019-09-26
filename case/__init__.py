import json,time,random
timestamp = (str(time.time()).replace('.', ''))[:-4]
nowTime = time.strftime("%Y-%m-%d", time.localtime())
# # bb='a=b&c=d&f=e'
# # aa=bb.replace("=",':')
# # # cc=bb.replace(":",'":"')
# # dd=aa.split('&')
# # print(json.dumps(dd))
#
# print(json.dumps([0,2,3,4]))
# carList = {}
# carList["contractNo"] = "timetamps"
# carList["title"] = "testContract"
# carList["contractUrl"] = "http://qiniu.hsbro.cn/1567666941167_C3-1V2.0.pdf"
# temp_i = '{"C4":' + json.dumps(carList, ensure_ascii=False) + '}'

# newCarList = str(carList)
# newCarList = newCarList.replace("'", "")

# print(temp_i)

# list = {"resultCode":200,"message":"\u8bf7\u6c42\u6210\u529f","data":{"list":[{"id":59907,"orderNo":"HS2019090609015223","logisticsId":0,"status":501,"pay4sState":null,"reason":"","carName":"test","color":"\u73cd\u73e0\u767d","interiorColor":"\u9ed1\u8272","gearbox":"\u81ea\u52a8","guidePrice":"153800.00","paidDeposit":"800.00","produceYear":"2019-07","type":"\u6807\u914d","remark":"","frameNumber":"LNAA2AA18K5003270","purchasePrice":"140800.00","price":"0.00","voucher":"","amount":"1000.00","number":1,"overdueFee":"0.00","deadline":1570204800,"voucherTime":"","payRemark":"","operateId":0,"operateName":"","createTime":"2019-09-06 09:01:52","contractUrl":"","verifyCarId":""},{"id":59908,"orderNo":"HS2019090609015223","logisticsId":0,"status":501,"pay4sState":null,"reason":"","carName":"test","color":"\u73cd\u73e0\u767d","interiorColor":"\u9ed1\u8272","gearbox":"\u81ea\u52a8","guidePrice":"153800.00","paidDeposit":"800.00","produceYear":"2019-07","type":"\u6807\u914d","remark":"","frameNumber":"LNAA2AA10K5003263","purchasePrice":"140800.00","price":"0.00","voucher":"","amount":"1000.00","number":1,"overdueFee":"0.00","deadline":1570204800,"voucherTime":"","payRemark":"","operateId":0,"operateName":"","createTime":"2019-09-06 09:01:52","contractUrl":"","verifyCarId":""},{"id":59909,"orderNo":"HS2019090609015223","logisticsId":0,"status":501,"pay4sState":null,"reason":"","carName":"test","color":"\u73cd\u73e0\u767d","interiorColor":"\u9ed1\u8272","gearbox":"\u81ea\u52a8","guidePrice":"153800.00","paidDeposit":"800.00","produceYear":"2019-07","type":"\u6807\u914d","remark":"","frameNumber":"LNAA2AA13K5003256","purchasePrice":"140800.00","price":"0.00","voucher":"","amount":"1000.00","number":1,"overdueFee":"0.00","deadline":1570204800,"voucherTime":"","payRemark":"","operateId":0,"operateName":"","createTime":"2019-09-06 09:01:52","contractUrl":"","verifyCarId":""},{"id":59910,"orderNo":"HS2019090609015223","logisticsId":0,"status":501,"pay4sState":null,"reason":"","carName":"test","color":"\u73cd\u73e0\u767d","interiorColor":"\u9ed1\u8272","gearbox":"\u81ea\u52a8","guidePrice":"153800.00","paidDeposit":"800.00","produceYear":"2019-07","type":"\u6807\u914d","remark":"","frameNumber":"LNAA2AA16K5002912","purchasePrice":"140800.00","price":"0.00","voucher":"","amount":"1000.00","number":1,"overdueFee":"0.00","deadline":1570204800,"voucherTime":"","payRemark":"","operateId":0,"operateName":"","createTime":"2019-09-06 09:01:52","contractUrl":"","verifyCarId":""}],"total":4,"page":1,"rows":50}}
# m = []
# while True:
#     try:
#         n = 0
#         a = list["data"]["list"]
#         c = a[n]["id"]
#         m.append(c)
#         n = n+1
#         continue
#     except Exception:
#         print(m)
#         break

# list = []
# i = {}
# i["name"] = "1"
# i["phone"] = "1"
# i["relation"] = "1"
# list.append(i)
# list.append(i)
# print(list)
# carList = self.s.json()["data"]
# newCarList = []
# for i in carList:
#     i["doing"] = "false"
#     # 使用dumps将list转化为json字符串
#     # 并且拼接上父节点的内容
#     temp_i = '{"carsInfo":' + json.dumps(i, ensure_ascii=False) + '}'


#     newCarList.append(temp_i)
# newCarList = str(newCarList)
# newCarList = newCarList.replace("'", "")
# # print(newCarList)
# from common import base
# b = base.Base()
# a = "2019-09-08"
# c = str(b.Caltime(a,nowTime))[0]
# d = int(c) + 1
# print(d)

# def get_two_float(f_str, n):
#     f_str = str(f_str) # f_str = '{}'.format(f_str) 也可以转换为字符串
#     a, b, c = f_str.partition('.')
#     c = (c+"0"*n)[:n] # 如论传入的函数有几位小数，在字符串后面都添加n为小数0
#     return ".".join([a, c])
#
# num = 123.4567
# print(get_two_float(num, 2))
#
# num2 = 123.4
# print(get_two_float(num2, 2))
maritalStatus = random.choice(["未婚", "已婚无子女", "已婚有子女", "离异", "丧偶", "其他"])

print(maritalStatus)