# Generated by Django 2.0.7 on 2018-07-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='data')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('description', models.TextField(verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'tarefa',
                'verbose_name_plural': 'tarefas',
                'ordering': ['-date'],
            },
        ),
    ]