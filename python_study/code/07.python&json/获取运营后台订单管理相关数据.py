import requests
import json

url = "http://10.10.27.210/manager/order/queryOrderList"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuaWNrIjoiMTM0MDAw5p2O6Z2Z5Liq5Lq654mIIiwiY3VycmVudFR5cGUiOjEsImV4cGlyZSI6MTY3Mzg2NDk0NDQ0OSwiaXNzIjoiNzQ0NTU4ODk2MDI2MjIyNTkyIiwidGVuYW50SWQiOiIxMDAzODEiLCJpZCI6Ijc0NDU1ODg5NjAyNjIyMjU5MiIsInVzZXJJZCI6IjE2MDgzNzMzMDI2NTc0NzA0NjYifQ.b2WGaOlZJWDN6bxKxyCFRGlmst-yCU_A_3GpXoZ5kQY'
}
data = {
    "queryType": 2,  # 0:我的;1:我团队的;2:全部
    "tenantId": "",  # 客户ID
    "isMakeInvoice": -1,  # 发票状态(-1:全部;0:未开票;1:开票中;2:已开票)
    "isMakeContract": -1,  # 合同状态(-1:全部;0:未开具;1:开具中;2:已开具)
    "startTime": "",
    "endTime": "",
    "orderNo": "",  # 订单编号
    "status": -1,  # 订单状态(-1:全部;0:未支付;1:已支付;2:已取消;3:已退款;5:凭证待审核)
    "managerId": "",
    "isAssigned": -1,  # 分配状态(-1:全部;0:未分配;1:已分配)
    "currentPage": 1,
    "pageSize": 100
}
response = requests.post(url, json=data, headers=headers)  # 接口返回值
r = json.dumps(response.json(), indent=2, ensure_ascii=False)  # 将返回值转为json格式
r_py = json.loads(r)

# 循环输出第0-10条订单的客户名称（buyerName）
for num in range(0, data['pageSize']):
    r_buyerName = r_py['data']['dataList'][num]['buyerName']
    r_orderSource = r_py['data']['dataList'][num]['orderSource']
    print(r_buyerName, r_orderSource)

# print(r)
# print(r_py)
