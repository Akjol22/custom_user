from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    message = f'Congratulations! Вы зарегистрировались на нашем сайте Активируйте аккаунт отправив нам этот код {activation_code}'
    send_mail(
        'Ативация аккаунта',
        message,
        'akzolkanaev81@gmail.com',
        [email]
    )