from django.db import models


# Create your models here.
class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    # 人性化显示对象信息
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Keyword(models.Model):
    # 1.id：int类型，是自增长的,主键
    key_id = models.AutoField(primary_key=True)
    # 2.name：varchar(100)，图书的名字,不能为空
    keyword = models.CharField(max_length=100, null=False)

class CrawResult(models.Model):
    craw_id = models.AutoField(primary_key=True)
    passage_name = models.CharField(max_length=100, null=False)
    craw_fk = models.ForeignKey('Keyword',to_field='key_id',on_delete='CASCADE')

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255, null=False)
    question_fk = models.ForeignKey('Keyword', to_field='key_id', on_delete='CASCADE')

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer = models.TextField()
    answer_fk1 = models.ForeignKey('Question', to_field='question_id', on_delete='CASCADE')
    answer_fk2 = models.ForeignKey('CrawResult', to_field='craw_id', on_delete='CASCADE')