# Generated by Django 4.1 on 2023-05-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0003_rename_cnpj_empresa_cnpj_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj_empresa',
            field=models.CharField(max_length=11),
        ),
    ]
