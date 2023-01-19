from django.db import models
# from django.db.models import CharField
from apps.bases.models import FactSchema


class User(FactSchema):
    name = models.CharField(max_length=128, verbose_name='用户中文名')
    username = models.CharField(max_length=64, unique=True, verbose_name='用户编码')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    telephone = models.CharField(max_length=20, verbose_name='电话号码')
    type = models.IntegerField(default=1, verbose_name='身份',
                               choices=((1, '用户'), (2, '管理员')))


    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

