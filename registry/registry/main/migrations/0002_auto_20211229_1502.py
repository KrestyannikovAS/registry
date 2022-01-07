# Generated by Django 3.2.5 on 2021-12-29 08:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='doc_author_department',
            field=models.CharField(default='СПАК', max_length=50, verbose_name='Отдел'),
        ),
        migrations.AddField(
            model_name='documents',
            name='doc_source',
            field=models.CharField(default='АСДОУ', max_length=50, verbose_name='Источник'),
        ),
        migrations.AddField(
            model_name='documents',
            name='revision_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата утверждения'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='note',
            field=models.CharField(default='НЕТ', max_length=250, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='title',
            field=models.CharField(max_length=512, verbose_name='Название документа'),
        ),
    ]