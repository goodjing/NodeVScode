# postman断言
## 常见断言方法
### 状态码断言
- 判断接口响应的状态码：Status code: code is 200
```
pm.test("Status code is 200",function(){
    //断言内容，可以修改
    pm.respons.to.have.status(200);
    //200是预期结果
});
```
- 判断接口响应码是否与预期集合中的某个值一致
  
```
pm.test("Successful POST request", function () {
    pm.expect(pm.response.code).to.be.oneOf([201,202]);
    //检查响应码是否为201或者202
});
```

- 判断状态码名称(也就是状态码后面的描述)是否包含某个字符串：Status code：code name has string

```
pm.test("Status code name has string", function () {
    pm.response.to.have.status("OK");
    //断言响应状态消息包含OK
});
```
### 响应内容断言
- 断言响应体中包含XXX字符串：Response body:Contains string

```
pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("string_you_want_to_search");
});
```

- 响应结果如果是json，断言响应体(json)中某个键名对应的值：Response body : JSON value check

```
pm.test("Your test name", function () {
    var jsonData = pm.response.json();
    //获取响应体，以json显示，赋值给jsonData .注意：该响应体必须返会是的json，否则会报错  
    pm.expect(jsonData.value).to.eql(100);
    //获取jsonData中键名为value的值，然后和100进行比较
});
```
【示例】
```
pm.test("msg", function () {
    var jsonDate = pm.response.json();
    pm.expect(jsonDate.msg).to.eql("订单分配负责人出错!");
});
```

- 断言响应体等于XXX字符串：Response body : is equal to a string

```
pm.test("Body is correct", function () {
    pm.response.to.have.body("response_body_string");
    //获取响应体等于response_body_string
});
```

### 响应头断言
- 断言响应头包含：Response headers:Content-Type header check

```
pm.test("Content-Type is present", function () {
    pm.response.to.have.header("Content-Type");
    //断言响应头存在"Content-Type"
});
```

### 响应速度断言
- 判断实际响应时间是否与低于预期时间：Response time is less than 200ms

```
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```

### 任何响应需要转为JsonData 对象  

- 多层json嵌套，获取user_id的值
```
{
    "code": 0,
    "message": "请求成功！",
    "data": {
        "user_id": "1252163151781167104"
    }
}
```
```
// 获取json体数据
var jsonData = pm.response.json();
// 获取user_id的值,通过.获取
var user_id = jsonData.data.user_id
```  

- json中存在列表，获取points中的第二个元素  
```json
{
    "code": 0,
    "message": "请求成功！",
    "data": {
        "roles": {
            "api": [
                "API-USER-DELETE"
            ],
            "points": [
                "point-user-delete",
                "POINT-USER-UPDATE",
                "POINT-USER-ADD"
            ]
        },
        "authCache": null
    }
}
```
```
//获取json体数据
var jsonData = pm.response.json()
// 获取user_id的值,通过下标获取列表中某个元素
var user_id = jsonData.data.roles.points[1]
```  

- 列表中取最后一个元素  
```json
{
    "code": 0,
    "message": "请求成功！",
    "data": {
        "total": 24,
        "rows": [
           
            {
                "id": "1066370498633486336",
                "mobile": "15812340003",
                "username": "zbz"
            },
            {
                "id": "1071632760222810112",
                "mobile": "16612094236",
                "username": "llx"
            },
            {
                "id": "1075383133106425856",
                "mobile": "13523679872",
                "username": "test001",
       
            }]
}
```
```
//获取json体数据
var jsonData = pm.response.json()
// 获取id的值,通过slice(-1)获取列表中最后一个元素。
var id = jsonData.data.rows.slice(-1)[0]
```
## 常用断言对应的脚本

### 清除一个环境变量

```
postman.clearEnvironmentVariable("variable_key");
```
### 断言响应数据中是否存在某个元素

```
tests["//断言返回的数据中是否存在__pid__这个元素"] = responseBody.has("pid");
```

### 断言response等于预期内容

```
tests["Body is correct"] = responseBody === "response_body_string";
```

### 断言json解析后的key的值等于预期内容

```
tests["Args key contains argument passed as url parameter"] = 'test' in responseJSON.args
```

### 检查response的header信息是否有被测字段

```
tests["Content-Type is present"] = postman.getResponseHeader("Content-Type");
```

### 校验响应数据中，返回的数据类型

```
var jsonData = JSON.parse(responseBody);
//第一步先转化为json字符串。其中变量(jsonData)可以自行定义......
tests["//data.category.name__valuse的值的类型是不是string"] = typeof(jsonData.data.category[0].name) == "string";
```

### 响应时间判断

```
tests["Response time is less than 200ms"] = responseTime < 200;
```

### 设置环境变量

```
postman.setEnvironmentVariable("variable_key", "variable_value");
```

### 断言状态码

```
tests["Status code is 200"] = responseCode.code != 400;
```

### 检查响应码name

```
tests["Status code name has string"] = responseCode.name.has("Created");
```

### 断言成功的post请求返回码

```
tests["Successful POST request"] = responseCode.code === 201 || responseCode.cod
```

## 预处理
### 去除json参数注释
```
//  去除json参数注释方法
GlobalJsonMinify = function (json) {

    var tokenizer = /"|(\/\*)|(\*\/)|(\/\/)|\n|\r|\[|]/g,
        in_string = false,
        in_multiline_comment = false,
        in_singleline_comment = false,
        tmp, tmp2, new_str = [], ns = 0, from = 0, lc, rc,
        prevFrom
    ;

    tokenizer.lastIndex = 0;

    while ( tmp = tokenizer.exec(json) ) {
        lc = RegExp.leftContext;
        rc = RegExp.rightContext;
        if (!in_multiline_comment && !in_singleline_comment) {
            tmp2 = lc.substring(from);
            if (!in_string) {
                tmp2 = tmp2.replace(/(\n|\r|\s)*/g,"");
            }
            new_str[ns++] = tmp2;
        }
        prevFrom = from;
        from = tokenizer.lastIndex;

        // found a " character, and we're not currently in
        // a comment? check for previous `\` escaping immediately
        // leftward adjacent to this match
        if (tmp[0] === "\"" && !in_multiline_comment && !in_singleline_comment) {
            // limit left-context matching to only go back
            // to the position of the last token match
            //
            // see: https://github.com/getify/JSON.minify/issues/64
            lc.lastIndex = prevFrom;

            // perform leftward adjacent escaping match
            tmp2 = lc.match(/(\\)*$/);
            // start of string with ", or unescaped " character found to end string?
            if (!in_string || !tmp2 || (tmp2[0].length % 2) === 0) {
                in_string = !in_string;
            }
            from--; // include " character in next catch
            rc = json.substring(from);
        }
        else if (tmp[0] === "/*" && !in_string && !in_multiline_comment && !in_singleline_comment) {
            in_multiline_comment = true;
        }
        else if (tmp[0] === "*/" && !in_string && in_multiline_comment && !in_singleline_comment) {
            in_multiline_comment = false;
        }
        else if (tmp[0] === "//" && !in_string && !in_multiline_comment && !in_singleline_comment) {
            in_singleline_comment = true;
        }
        else if ((tmp[0] === "\n" || tmp[0] === "\r") && !in_string && !in_multiline_comment && in_singleline_comment) {
            in_singleline_comment = false;
        }
        else if (!in_multiline_comment && !in_singleline_comment && !(/\n|\r|\s/.test(tmp[0]))) {
            new_str[ns++] = tmp[0];
        }
    }
    new_str[ns++] = rc;
    return new_str.join("");
};

pm.request.body.raw = GlobalJsonMinify(pm.request.body.raw)
```
### 日志输出
```
console.log("这是log级别的日志")
console.info("这是info级别的日志")
console.warn("这是warning级别的日志")
console.error("这是error级别的日志")
console.debug("这是debug级别的日志")
```

## 加密与解密
### ASE加密
比如要加密请求body中的test的值。
```
function AesEncrypt(data,secret_key){
    //将AES加密写成有一个方法
    var ECBOptions = {mode: CryptoJS.mode.ECB,padding: CryptoJS.pad.Pkcs7};//密码，文本，偏移量、模式等设置
    var AesSecert = CryptoJS.enc.Utf8.parse(secret_key);//加密密码
    var data_enc = CryptoJS.AES.encrypt(data, AesSecert, ECBOptions).toString()
    //CryptoJS.AES.encrypt()是AES加密方法，对应的还有AES解密方法CryptoJS.AES.decrypt()
    return data_enc //返回加密后的数据，格式为字符串
}
var test = pm.request.body.formdata.get('test') //获取接口参数，body中form-data格式的参数
pm.request.body.formdata.remove('test') //移除原参数
pm.request.body.formdata.add({'key':'test','value':AesEncrypt(test,'ABCDEFGHIjklmnop')}) //调用加密方法，并把加密后的结果作为test的value重新加入body中
```
### ASE解密
```
var body = responseBody
var AES_key= "QWERTYUIOPASDFGH" //设置秘钥
var ECBOptions = {mode: CryptoJS.mode.ECB,padding: CryptoJS.pad.Pkcs7};//设置偏移量、模式等设置
var AesSecert = CryptoJS.enc.Utf8.parse(AES_key);//秘钥为Utf-8格式，需要先解码为十六进制数
var data_dec = CryptoJS.AES.decrypt(body, AesSecert, ECBOptions)//调用crypto-js中解密的方法
var data_dec_str = data_dec.toString(CryptoJS.enc.Utf8)//再将解密后的结果转为字符串且为UTF-8格式
console.log("解密之后的结果:",data_dec_str)
```
### MD5加密
```
function Md5Encrypt(value){
    // MD5加密
    var val_md5 = CryptoJS.MD5(value).toString()
    return val_md5 //返回加密后的数据
}
var test = pm.request.body.formdata.get('test') //获取接口参数
pm.request.body.formdata.remove('test') //移除原参数
pm.request.body.formdata.add({'key':'test','value':Md5Encrypt(test)}) //添加加密后的参数
```
### 举例
对含参数文本处理思路：
1. 先获取原始文本
2. 通过替换方法修改参数变量
3. 再进行加密处理
4. 将加密后的文本替换进原来的请求body

**原始body**
```json
{
"loginUrl":"https://{{url_ip}}:7443/login.html",
"userName": "{{dandian_name}}",
"password": "{{dandian_password}}"
}
```
**加密处理**
```
/**
 * 加密
 * 当前不需要对秘钥与body进行
 */
function aesEncrypt(srcs,key){
    // var key  = CryptoJS.enc.Utf8.parse(keyStr);  无需进行解码
    // var srcs = CryptoJS.enc.Utf8.parse(date);
    // console.log('content srcs:'+srcs);
    // console.log('content key:'+key);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {mode:CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7});
    return encrypted.toString();
}
 
/**秘钥 */
const Vkey ="xded+=xdee239sdd";
var Vbody=pm.request.body.raw;
console.log('原始body:'+Vbody);
Vbody = Vbody.replace('{{url_ip}}',pm.environment.get("url_ip"));
Vbody = Vbody.replace('{{dandian_name}}',pm.environment.get("dandian_name"));
Vbody = Vbody.replace('{{dandian_password}}',pm.environment.get("dandian_password"));
console.log('处理参数:'+Vbody);
 
//加密
encryptDate=aesEncrypt(Vbody,Vkey);
console.log('body加密后:'+encryptDate);
 
//请求修改body
pm.request.body.update({mode: 'raw',raw:encryptDate});
 
//修改后的body
console.log('真实body:'+pm.request.body.raw);
```
