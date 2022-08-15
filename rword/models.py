from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WordList(models.Model):
    word = models.CharField(max_length=64, verbose_name='단어')

    def __str__(self):
        return self.word

    class Meta:
        db_table = 'rword'

class SentenceList(models.Model):
    sentence = models.CharField(max_length=100, verbose_name='문장')
    contents = models.TextField(verbose_name='설명', null=True)
    writer = models.ForeignKey(User, verbose_name='작성자', null=True, on_delete=models.CASCADE)
    write_dttm = models.DateTimeField(auto_now_add=True, null=True, verbose_name='글 작성일')

    def __str__(self):
        return self.sentence
    
    class Meta:
        db_table = 'rwordsent'