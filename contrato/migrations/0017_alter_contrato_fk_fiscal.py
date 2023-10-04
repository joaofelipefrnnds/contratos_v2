# Generated by Django 4.1 on 2023-06-26 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contrato', '0016_remove_novoevento_anexo_contrato_anx_empenho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fk_fiscal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
