# Generated by Django 3.2.12 on 2022-11-15 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20221115_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='item',
        ),
    ]
