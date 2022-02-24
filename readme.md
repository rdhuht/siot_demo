# 系统 windows

# siot
双击运行SIoT.exe 启动siot的mqtt服务（跳出的命令行窗口不要关闭）
打开localhost:8080
账号密码都是siot登录查看

# .py文件
.py文件使用python运行，不用安装编辑器，打开后会有提示信息；
farm_faculty_controller.py 模拟手机端，包含温湿度的判断逻辑，及执行器的处理逻辑；
fa……humidity.py 模拟湿度检测装置，发送数据到siot；
fa……temperature.py 模拟温度检测装置，发送数据到siot。