# Generated by Django 5.1.2 on 2024-11-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='comment2',
            field=models.TextField(blank=True, null=True, verbose_name='コメント2'),
        ),
    ]
