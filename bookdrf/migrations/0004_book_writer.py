# Generated by Django 3.2.12 on 2022-04-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdrf', '0003_auto_20220417_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.CharField(default='无名氏', max_length=30),
        ),
    ]
