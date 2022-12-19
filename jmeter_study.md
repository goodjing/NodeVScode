## 迅速调试接口
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

## 接口测试案例一
以小e为例。
### 配置元件：用户定义的变量
可以存储发送请求的公共变量：
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
还可以存储测试用的语料所在位置：
| 名称 | 值 | 描述 |
| --- | ---- | --- |
| pathofBin | C:\Users\Administrator\Desktop\标准场景 | 语料所在的位置 |

### 线程组
**配置元件：HTTP请求默认值**
Web服务器：（可使用公共变量）
- 协议：${protocol}
- 服务器名称或IP：${GetIP}

HTTP请求：（可使用公共变量）
- 路径：${path}

参数：（同请求一起发送参数）
| 名称 | 值 |
| --- | ---- |
| reqSource | ${reqSource} |
| appId | ${appId} |
| userId | ${userId} |
| sign | ${sign} |
| timestamp | ${timestamp} |
| isVoiceInput | ${isVoiceInput} |

**配置元件：CSV数据文件设置**
- 文件名：${pathofBin}/考勤管理/打卡/签到.csv
- 文件编码：UTF-8
- 变量名称：query

**固定定时器**
- 线程延迟（毫秒）：5000

**取样器**
- HTTP请求：GET
- 参数：test=${query}
【Response返回BeanShell后置处理程序】
```
import java.util.Collection;
import java.util.Iterator;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

//获取获取请求的返回值
String response_data =prev.getResponseDataAsString();
//日志打印获取请求的返回值
log.info("response_data:"+response_data);

//转换成JSON串
JSONObject json = JSONObject.parseObject(response_data);

//获取data的json串
JSONObject data = json.getJSONObject("data");
log.info("data:"+data.toString());

//获取data的意图intentInfo
String intentInfo_name  =data.getJSONObject("intentInfo").getString("name");
String intentInfo_title =data.getJSONObject("intentInfo").getString("title");
log.info("intentInfo_name:"+intentInfo_name);
log.info("intentInfo_title:"+intentInfo_title);
vars.put("intentInfo_name",intentInfo_name);
vars.put("intentInfo_title",intentInfo_title);

//获取data的纠错算法后的text
String errorRecovery_text =data.getString("text");
log.info("errorRecovery_text:"+errorRecovery_text);
vars.put("errorRecovery_text",errorRecovery_text);

//获取data的后台的参数creater\action
String creater = data.getJSONObject("invoker").getJSONObject("params").getString("creater");
String action  = data.getJSONObject("invoker").getString("action");
log.info("creater:"+creater);
log.info("action:"+action);
vars.put("creater",creater);
vars.put("action",action);


JSONArray sceneRecommendArray = (JSONArray) data.get("sceneRecommendList");
log.info("sceneRecommendArray:"+sceneRecommendArray.toString());
List sceneRecommendList = new ArrayList();
 if (sceneRecommendArray.size() > 0)
 {
    for (int i = 0; i < sceneRecommendArray.size(); i++) {
    // 遍历 jsonarray 数组，把每一个对象转成 json 对象
    JSONObject job = sceneRecommendArray.getJSONObject(i);  
    //获取user串中的superior
	String corpus = job.get("corpus");
	log.info("corpus:"+corpus);  
	sceneRecommendList.add(corpus);
     }
     
log.info("sceneRecommendList:"+sceneRecommendList.toString());
vars.put("sceneRecommendList",sceneRecommendList.toString());
}
```