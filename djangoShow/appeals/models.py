import datetime
from django.db import models
from django.utils import timezone


class Complaint(models.Model):
    text = models.CharField('вопрос', max_length=200)
    answer = models.CharField('ответ', max_length=200)

    def __str__(self):
        return f"{self.text} | {self.answer}"

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
