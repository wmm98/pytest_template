import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
import os
from Common.Log import *

log = MyLog()


# 用邮箱实现带附件邮件发送
class Email():

    def __init__(self):
        self.smtp_host = "smtp.126.com"  # 发送邮件的smtp服务器(从QQ邮箱中取得)
        self.smtp_user = "mingmingwu1998@126.com"  # 用于登录smtp服务器的用户名，也就是发送者的邮箱
        self.smtp_pwd = "CGIXAVDEHBHZOOXZ"  # 授权码，和用户名user一起，用于登录smtp，非邮箱密码，可以使用Foxmail生成
        self.smtp_port = 465  # smtp服务器SSL端口号，默认是465
        self.sender = "mingmingwu1998@126.com"

    def sendeamil(self, tolist, subject, body, lasteamil_path, lasteamil_path2):
        """
        发送邮件
        :param tolist:收件人的邮箱列表
        :param subject: 邮件标题
        :param body: 邮件内容
        :param lasteamil_path: 邮件附件所在路径
        :return:
        """
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['Form'] = Header(self.sender, 'utf-8')  # 发件人
        # message['To'] = Header(tolist, 'utf-8')
        message['To'] = Header(",".join(tolist), 'utf-8')  # 收件人列表
        # print("****************************************************")
        # print(",".join(tolist))
        # print("****************************************************")
        message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

        # 邮件正文内容
        message.attach(MIMEText(body, 'plain', 'utf-8'))  # 邮件内容，格式，编码

        # 构造附件1
        # 获取最新的email路径，如果存在说明有报错，构造附件，发送email路径下的excel文件
        att1 = MIMEApplication(open(lasteamil_path, 'rb').read())
        att1['Content-Type'] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么邮件就显示什么名字
        att1.add_header('Content-Disposition', 'attachment', filename="Test_send_email.html")
        message.attach(att1)

        # 构造附件2
        att2 = MIMEApplication(open(lasteamil_path2, 'rb').read())
        att2['Content-Type'] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么邮件就显示什么名字
        att2.add_header('Content-Disposition', 'attachment', filename="Test_send_email.xlsx")
        message.attach(att2)

        try:
            smtpSSLClient = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)  # 实例化一个SMTP_SSL对象

            # 220：服务就绪。
            # 250：请求动作正确完成（HELO、MAIL
            # FROM、RCPT
            # TO、QUIT指令执行成功会返回此信息）。
            # 235：认证通过。
            # 221：正在处理。
            # 354：开始发送邮件内容，提示以特殊行.结束邮件内容。
            # 500：语法错误，命令不能识别。
            # 552：中断处理。

            loginRes = smtpSSLClient.login(self.smtp_user, self.smtp_pwd)  # 登录smtp服务器
            # print("登录结果：loginRes=", loginRes)
            log.info("登录结果：loginRes=" + str(loginRes))
            if loginRes and loginRes[0] == 235:
                log.info("登陆成功，code = " + str(loginRes[0]))
                smtpSSLClient.sendmail(self.sender, tolist, message.as_string())
                log.info(f"mail has been send successful. message:{message.as_string()}")
            else:
                log.error("登录失败，code=" + str(loginRes[0]))
        except Exception as e:
            log.error("邮件发送失败，Exception：e=" + str(e))


if __name__ == "__main__":
    # 当前目录
    attachment_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    lasteamil_path = attachment_path + '/index.html'  # 此函数用于获取最新邮件附件的路径，例如#F:/email\20220210144217\异常通知.xlsx
    lasteamil_path2 = attachment_path + '/testDemo.xlsx'
    if lasteamil_path:
        emailSenderClient = Email()
        content = '异常数据如附件所示'
        tolist = ['792545884@qq.com', '920691848@qq.com']  # 收件人邮箱
        subject = '政通传媒异常数据通知'
        emailSenderClient.sendeamil(tolist, subject, content, lasteamil_path, lasteamil_path2)

