# Generated by Django 3.0.4 on 2020-03-30 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interval', '0003_auto_20200326_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='most_common',
            new_name='test_type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_rating',
        ),
        migrations.RemoveField(
            model_name='test',
            name='xp_gain',
        ),
        migrations.AddField(
            model_name='question',
            name='question_index',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='right_answer',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='question_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='user_answer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='test',
            name='rightanswers',
            field=models.IntegerField(null=True),
        ),
    ]