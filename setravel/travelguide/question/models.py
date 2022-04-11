from django.db import models


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    qid = models.CharField(max_length=100, verbose_name='qid')
    answer1 = models.CharField(max_length=100, verbose_name='answer1', default=None)
    answer2 = models.CharField(max_length=100, verbose_name='answer2', default=None)
    answer3 = models.CharField(max_length=100, verbose_name='answer3', default=None)
    answer4 = models.CharField(max_length=100, verbose_name='answer4', default=None)
    answer5 = models.CharField(max_length=100, verbose_name='answer5', default=None)
    answer6 = models.CharField(max_length=100, verbose_name='answer6', default=None)
    answer7 = models.CharField(max_length=100, verbose_name='answer7', default=None)


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100, verbose_name="question")
    answer = models.ForeignKey(
        Answer, verbose_name="answer", on_delete=models.CASCADE)
