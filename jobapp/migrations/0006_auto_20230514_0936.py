# Generated by Django 3.1.3 on 2023-05-14 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_auto_20230514_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
