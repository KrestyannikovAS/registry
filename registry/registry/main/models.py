from django.db import models
from datetime import date


class Documents(models.Model):
    objects = None
    title = models.CharField('Название документа', max_length=250)
    doc_author = models.CharField('Автор', max_length=50)
    approval_date = models.DateField('Дата утверждения', default=date.today)
    doc_url = models.CharField('Ссылка на документ', max_length=250)
    note = models.CharField('Описание', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
