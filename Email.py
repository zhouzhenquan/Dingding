"""
-- coding: utf-8 --
@Time : 2020/8/6 16:05
@Author : 周振全
@Site :
@File : k.py
@Software: PyCharm

"""

import datetime
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import Screenshot


def send_email(title):

    # 连接邮箱的smtp服务器，并登录
    smtp = smtplib.SMTP_SSL(host="smtp.qq.com",port="465")
    smtp.login(user="1275470984@qq.com",password="rlaxoxvdubrsfjdh")

    # 构建一封邮箱
    msg = MIMEMultipart()

    #正文-图片 只能通过html格式来放图片
    htmlFile = """\
    <html>
        <head></head>
        <body>
            <pre style="font-family:arial;margin:left;">
            亲爱的周振全:
                    打卡成功！！！
            <img src="cid:image1">
            </pre>
        </body>
    </html>
    """

    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    N_H = now_time+htmlFile

    # 创建邮文本内容
    test_msg = MIMEText(N_H,_subtype="html",_charset='utf-8')
    # 添加到多组邮件的附件中
    msg.attach(test_msg)


    # 主题
    msg["Subject"] = title
    # 发件人
    msg["From"] = "1275470984@qq.com"
    # 收件人
    msg["To"] = "17764509133@163.com"

    img_folders = Screenshot.screenshot()
    files = img_folders
    image = MIMEImage(open(files, 'rb').read(), files.split('.')[-1])
    # 定义图片 ID，在 HTML 文本中引用
    image.add_header('Content-ID','<image1>')
    msg.attach(image)

    # #附件
    # img_folder = Screenshot.screenshot()
    # file = open(img_folder, "rb")
    # img = MIMEImage(file.read())
    # file.close()
    # img.add_header('Content-ID', 'dns_config')
    # msg.attach(img)

    # 发送邮箱
    smtp.send_message(msg,from_addr="1275470984@qq.com",to_addrs="17764509133@163.com")

