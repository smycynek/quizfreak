# Generated by Django 2.2.8 on 2020-09-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizfreak', '0002_quiz_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='index',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='index'),
        ),
    ]
