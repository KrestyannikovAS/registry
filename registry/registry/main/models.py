from django.db import models
from datetime import date


class Documents(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField('Название документа', max_length=512)
    doc_author = models.CharField('Автор', max_length=50)
    doc_author_department = models.CharField('Отдел', max_length=50, default="СПАК")
    approval_date = models.DateField('Дата утверждения', default=date.today)
    revision_date = models.DateField('Дата утверждения', default=date.today)
    doc_source = models.CharField('Источник', max_length=50, default="АСДОУ")
    doc_url = models.CharField('Ссылка на документ', max_length=250)
    note = models.CharField('Комментарий', max_length=250, default="НЕТ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
