# Generated by Django 3.2.12 on 2022-03-28 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publish',
        ),
    ]
