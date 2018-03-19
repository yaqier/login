# import os
# from django.core.mail import send_mail, EmailMultiAlternatives
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
# if __name__ == '__main__':
#
#     # send_mail(
#     #     "来自上天的测试邮件",
#     #     "欢迎来天上玩",
#     #     'angelc1011@sina.com',
#     #     ['angelc1011@163.com'],
#     # )
#
#     subject, from_email, to = "来自天堂的测试邮件", 'angelc1011@sina.com', '834961506@qq.com'
#     text_content = '欢迎来到天堂'
#     html_content = '<p>欢迎来<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>到天堂</p>'
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
