# Generated by Django 2.1.4 on 2018-12-28 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_mae', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('grupo_amigo', models.CharField(choices=[('E', 'Escola'), ('P', 'Prédio')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('etiqueta', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(auto_now_add=True)),
                ('data_devolucao', models.DateField()),
                ('amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revistas.Amigo')),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_edicao', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revistas.Caixa')),
                ('colecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revistas.Colecao')),
            ],
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='revista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revistas.Revista'),
        ),
        migrations.AddField(
            model_name='amigo',
            name='revista',
            field=models.ManyToManyField(through='Revistas.Emprestimo', to='Revistas.Revista'),
        ),
    ]
