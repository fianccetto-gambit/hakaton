# Generated by Django 4.1.5 on 2023-01-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='photo',
            field=models.ImageField(blank=1, null=1, upload_to='images/', verbose_name='Изображение'),
            preserve_default=1,
        ),
    ]
