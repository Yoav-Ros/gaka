# Generated by Django 3.0.4 on 2020-03-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200326_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='media/images/toast.jpeg', null=True, upload_to='media/images'),
        ),
    ]
