# Generated by Django 3.2.12 on 2022-11-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_remove_comments_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description_1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
