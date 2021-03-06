# Generated by Django 3.1.7 on 2021-02-28 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_produto', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço (R$)')),
                ('modelo_produto', models.CharField(max_length=200, verbose_name='Modelo')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
            ],
        ),
    ]
