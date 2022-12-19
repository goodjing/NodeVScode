## HTTP信息头管理器
用于存储登录信息等
| 名称 | 值 |
| --- | ---- |
| Authorization | xxxxxxxxxxxxx |
| Connection | keep-alive |
| Content-Type | application/json |

## 线程组
可配置线程属性，比如：
- 线程数：30
- Rame-Up时间（秒）：1
- 循环次数：1

### 取样器
常用的是`HTTP请求`，填写一些基本信息，比如Web服务器：
- 协议：http
- 服务器名称或IP：10.10.27.210
- 端口号：80
比如HTTP请求：
- post或者get
- 路径：/order/order/createOrder
- 消息体数据：一般是json

### 监听器
常用的是`查看结果树`、`汇总报告等`
