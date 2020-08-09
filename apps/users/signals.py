from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save,sender=User)  # 指定接收信号，从哪个model传递过来的。
def create_auth_password(sender,instance=None,created=False,**kwargs):
    # instance代表models的对象，create代表该信号是否为新建操作
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()