# postman断言  
## 常见断言方法
### 状态码断言
- 判断接口响应的状态码：Status code: code is 200  
  
```json
pm.test("Status code is 200", function () {
    //Status code is 200是断言名称，可以自行修改
    pm.response.to.have.status(200);
    //这里填写的200是预期结果，实际结果是请求返回结果
});
```

- 判断接口响应码是否与预期集合中的某个值一致
  
```json
pm.test("Successful POST request", function () {
    pm.expect(pm.response.code).to.be.oneOf([201,202]);
    //检查响应码是否为201或者202
});
```

- 判断状态码名称(也就是状态码后面的描述)是否包含某个字符串：Status code：code name has string

```json
pm.test("Status code name has string", function () {
    pm.response.to.have.status("OK");
    //断言响应状态消息包含OK
});
```
### 响应内容断言
- 断言响应体中包含XXX字符串：Response body:Contains string

```json
pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("string_you_want_to_search");
});
```

- 响应结果如果是json，断言响应体(json)中某个键名对应的值：Response body : JSON value check

```json
pm.test("Your test name", function () {
    var jsonData = pm.response.json();
    //获取响应体，以json显示，赋值给jsonData .注意：该响应体必须返会是的json，否则会报错  
    pm.expect(jsonData.value).to.eql(100);
    //获取jsonData中键名为value的值，然后和100进行比较
});
```
【示例】
```json
pm.test("msg", function () {
    var jsonDate = pm.response.json();
    pm.expect(jsonDate.msg).to.eql("订单分配负责人出错!");
});
```

- 断言响应体等于XXX字符串：Response body : is equal to a string

```json
pm.test("Body is correct", function () {
    pm.response.to.have.body("response_body_string");
    //获取响应体等于response_body_string
});
```

### 响应头断言
- 断言响应头包含：Response headers:Content-Type header check

```json
pm.test("Content-Type is present", function () {
    pm.response.to.have.header("Content-Type");
    //断言响应头存在"Content-Type"
});
```

### 响应速度断言
- 判断实际响应时间是否与低于预期时间：Response time is less than 200ms

```json
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```

### 任何响应需要转为JsonData 对象
```json
{  
"reponse": {    
"person": {      
   "name": "hai",      
   "age": 18    
         }  
       }
}
```
若要获取age需要：
```json
//第一步将响应转为 jsonData 对象
jsonData = pm.response.json();
//第二步通过 . 获取到我们想要的 age 的值
var age = jsonData.reponse.person.age;
```

## 常用断言对应的脚本

### 清除一个环境变量

```json
postman.clearEnvironmentVariable("variable_key");
```
### 断言响应数据中是否存在某个元素

```json
tests["//断言返回的数据中是否存在__pid__这个元素"] = responseBody.has("pid");
```

### 断言response等于预期内容

```json
tests["Body is correct"] = responseBody === "response_body_string";
```

### 断言json解析后的key的值等于预期内容

```json
tests["Args key contains argument passed as url parameter"] = 'test' in responseJSON.args
```

### 检查response的header信息是否有被测字段

```json
tests["Content-Type is present"] = postman.getResponseHeader("Content-Type");
```

### 校验响应数据中，返回的数据类型

```json
var jsonData = JSON.parse(responseBody);
//第一步先转化为json字符串。其中变量(jsonData)可以自行定义......
tests["//data.category.name__valuse的值的类型是不是string"] = typeof(jsonData.data.category[0].name) == "string";
```

### 响应时间判断

```json
tests["Response time is less than 200ms"] = responseTime < 200;
```

### 设置环境变量

```json
postman.setEnvironmentVariable("variable_key", "variable_value");
```

### 断言状态码

```json
tests["Status code is 200"] = responseCode.code != 400;
```

### 检查响应码name

```json
tests["Status code name has string"] = responseCode.name.has("Created");
```

### 断言成功的post请求返回码

```json
tests["Successful POST request"] = responseCode.code === 201 || responseCode.cod
```