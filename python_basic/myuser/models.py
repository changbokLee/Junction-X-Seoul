from django.db import models

# Create your models here.

class Myuser(models.Model):
    username = models.CharField(max_length=128, verbose_name='아이디' , unique = True)
    password = models.CharField(max_length=256, verbose_name='비밀번호')
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='가입일시')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'dls_myuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
