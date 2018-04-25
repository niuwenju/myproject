# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
#qq邮箱smtp服务器

#smtp.login(sender_qq, pwd)
def send_regist_success_mail(userinfo):
    mail_title = u'注册成功'
    mail_content = u'''你好！<b>%s</b><br />
    你已经成功注册成为Tmitter用户<br />
    以下是您的信息：<br />
    <ul>
        <li>用户名：%s </li>
        <li>密码:%s</li>
    </ul>''' % (userinfo['realname'],userinfo['username'],userinfo['password'])
    recipient_list = userinfo['email']
    send(mail_title,mail_content,recipient_list)
#ssl登录

def send(mail_title,mail_content,recipient_list):
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = '*5933'
    # pwd为qq邮箱的授权码
    pwd = '***'
    # 发件人的邮箱
    sender_qq_mail = '*5933@qq.com'
    smtp = SMTP_SSL(host_server, 465)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    #smtp.set_debuglevel(1)
    #smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    msg = MIMEText(mail_content, "html", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = recipient_list
    smtp.sendmail(sender_qq_mail, recipient_list, msg.as_string())
    smtp.quit()
