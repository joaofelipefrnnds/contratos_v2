# Generated by Django 4.1 on 2023-05-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0005_alter_empresa_email_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='email_empresa',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone_empresa',
            field=models.CharField(max_length=11),
        ),
    ]
