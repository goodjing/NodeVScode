## Web接口测试
### 配置元件：HTTP信息头管理器
用于存储登录信息等
| 名称 | 值 |
| --- | ---- |
| Authorization | xxxxxxxxxxxxx |
| Connection | keep-alive |
| Content-Type | application/json |

### 线程组
可配置线程属性，比如：
- 线程数：30
- Rame-Up时间（秒）：1
- 循环次数：1

**取样器**
常用的是`HTTP请求`，填写一些基本信息。
比如Web服务器：
- 协议：http
- 服务器名称或IP：10.10.27.210
- 端口号：80  

比如HTTP请求：
- post或者get
- 路径：/order/order/createOrder
- 消息体数据：一般是json

**监听器**
常用的是`查看结果树`、`用表格查看结果`等。

## vConsole接口测试
以小e为例。
### 配置元件：用户定义的变量
可以存储发送请求的公共变量
| 名称 | 值 |
| --- | ---- |
| protocol | https |
| GetIP | test-ai.easst.cn |
| PostIP | test-ai.easst.cn |
| path | /easst/semantic |
| reqSource | 2 |
| appId | k55frqcd |
| userId | 10634 |
| sign | xxxxxx |
| timestamp | xxxxxxxx |
| isVoiceInput | true |
| mobiletoken | "" |
| faqPath | /easst/faq/execute_easst?method=faq |
还可以存储测试用的语料所在位置
| 名称 | 值 | 描述 |
| --- | ---- | --- |
| pathofBin | C:\Users\Administrator\Desktop\标准场景 | 语料所在的位置 |