# Generated by Django 2.1.4 on 2018-12-27 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=20)),
                ('complemento', models.CharField(max_length=256)),
                ('bairro', models.CharField(max_length=60)),
                ('cidade', models.CharField(max_length=60)),
                ('uf', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=9)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='ItemTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Itens Tema',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_aluguel', models.FloatField()),
                ('cor_toalha', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('data_festa', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_termino', models.TimeField()),
                ('valor_cobrado', models.FloatField()),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Festas.Endereco')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festas.Cliente')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festas.Tema')),
            ],
            options={
                'verbose_name_plural': 'Alugeis',
            },
        ),
        migrations.AddField(
            model_name='itemtema',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festas.Tema'),
        ),
    ]
