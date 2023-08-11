# Generated by Django 4.1 on 2023-08-10 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contrato', '0020_remove_novoevento_anx_empenho_contrato_anx_contrato_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='modificado_por',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Modificado_Por', to=settings.AUTH_USER_MODEL, verbose_name='Modificado Por'),
            preserve_default=False,
        ),
    ]
