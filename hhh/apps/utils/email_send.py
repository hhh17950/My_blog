from users.models import EmailCode
from random import Random
from django.core.mail import send_mail
from hhh.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_email_type(email, send_type='register'):
    email_code = EmailCode()
    random_code = random_str(16)
    email_code.code = random_code
    email_code.email = email
    email_code.send_type = send_type
    email_code.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '橙子于渔注册激活链接'
        email_body = '请点击下面链接激活你的账号：http://127.0.0.1:8000/activate/{0}'.format(random_code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
