# Generated by Django 3.2.24 on 2024-07-31 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsuapp', '0021_auto_20240731_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='femalestudent',
            name='Gender',
            field=models.CharField(default=True, max_length=350),
        ),
    ]