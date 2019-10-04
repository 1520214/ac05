# Generated by Django 2.2.5 on 2019-09-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_auto_20190911_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOrcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_unitario', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
            ],
        ),
    ]