# Generated by Django 2.2.22 on 2021-06-02 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20210602_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estoque.Produto'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='status',
            field=models.CharField(blank=True, choices=[('AB', 'Aberta'), ('FC', 'Fechada'), ('PC', 'Processando'), ('DC', 'Desconhecido')], default='DC', max_length=2, null=True),
        ),
    ]
