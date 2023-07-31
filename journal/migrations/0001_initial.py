# Generated by Django 4.0.6 on 2023-07-31 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('descricao', models.CharField(blank=True, max_length=200, verbose_name='Descrição')),
                ('data', models.DateTimeField(verbose_name='Data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome e sobrenome')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('data_pub', models.DateTimeField(verbose_name='Data de publicação')),
                ('edicao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.edicao')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='edicao',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=100, verbose_name='Conteúdo')),
                ('data_pub', models.DateTimeField(verbose_name='Data de publicação')),
                ('noticia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.noticia')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.usuario')),
            ],
        ),
    ]
