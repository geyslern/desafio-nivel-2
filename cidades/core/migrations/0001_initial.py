# Generated by Django 3.0.6 on 2020-05-14 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=35)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
            ],
        ),
    ]
