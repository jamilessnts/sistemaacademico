# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistemaacademico', '0006_auto_20161012_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.DecimalField(decimal_places=2, max_digits=4)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaacademico.Disciplina')),
            ],
        ),
        migrations.AlterModelOptions(
            name='avaliacoes',
            options={},
        ),
    ]
