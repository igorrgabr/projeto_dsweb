# Generated by Django 4.0.6 on 2023-06-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_question_delete_alternativa_delete_questao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
    ]
