from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length= 128, verbose_name = '제목')
    contents = models.TextField(verbose_name = '내용')
    writer = models.ForeignKey('myuser.Myuser', on_delete =models.CASCADE)
    register_dttm = models.DateTimeField(auto_now_add =True, verbose_name ='등록일시')

    def _str_(self):
        return self.title

    class Meta:
        db_table = 'dls_board'
        verbose_name = '게시글'
        verbose_name_plural ='게시글'