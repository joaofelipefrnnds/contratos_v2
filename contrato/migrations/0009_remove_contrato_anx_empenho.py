# Generated by Django 4.1 on 2023-05-30 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0008_contrato_anx_empenho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='anx_empenho',
        ),
    ]
