# Generated by Django 3.2.11 on 2022-02-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='nm_calculadora', max_length=255, unique=True)),
                ('descricao', models.TextField(blank=True, db_column='ds_calculadora', null=True)),
                ('expressao', models.TextField(blank=True, db_column='ds_expressao')),
            ],
            options={
                'verbose_name': 'Calculadora',
                'ordering': ['id'],
            },
        ),
    ]
