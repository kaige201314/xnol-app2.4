#xnol-app2.4 automation test

##本文档用于说明appium-xnol UI自动化测试框架
##环境：172.20.30.63，数据库：172.20.30.64


##一、框架主题说明：
####1、Data目录：用于存放测试数据，activatronCode.txt存放理财金券激活码、phoneNO.txt存放注册新用户时生成的手机号，idCardNO.txt存放绑卡时的身份证号码，login_password.txt存放注册时的登录密码，tradeCode.txt存放交易密码；
####2、Doc目录：用于存放说明文档；
####3、PageObject目录：用于存放页面基础类，封装常用的元素定位方法；
####4、Public目录：用于存放一些公共方法；
####5、Random目录：用于存放一些随机需要用的方法，文件等等；
####6、result目录：用于存放测试用例执行的结果，即测试报告；
####7、TestCase目录：用于存放已经实现好的测试用例；
####8、TestCase2目录：用于存放未实现的测试用例；

##二、测试用例说明：

### test_case001——》老用户登录——》退出

### test_case001——》注册新用户
    
### test_case002——》登录——》设置交易密码——》退出
    
### test_case003——》登录——》修改交易密码——》退出
    
### test_case004——》登录——》找回交易密码——》退出

### test_case005——》新用户登录——》绑卡——》充值——》退出

### test_case006——》登录——》提现——》退出

### test_case007——》登录——》设置——》修改——》关闭手势密码——》退出

### test_case008——》登录——》提取天天牛、月月牛——》退出

### test_case009——》登录——》添加理财金券——》购买天天牛——》购买月月牛——》购买安心牛——》购买散标——》购买富盈人生——》购买理财金体验标——》退出
    
### test_case010——》登录——》购买VIP专享标——》退出
    
### test_case011——》登录——》购买债权转让标——》退出（备注：由于63环境没有债权转让标，故此用例还未彻底完成，购买的流程和其他标的的购买大体相同）
    
### test_case012——》登录——》修改登录密码——》退出
    
### test_case013——》

### test_case014——》

### test_case015——》

### test_case016——》

### test_case017——》
    
### test_case018——》

##一、测试报告：

![test-report.png](http://upload-images.jianshu.io/upload_images/1464121-d2588976045a0254.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
