# Generated by Django 3.1.1 on 2020-09-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20200917_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskassesment',
            name='risk',
        ),
        migrations.AddField(
            model_name='riskassesment',
            name='risk_id',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='riskinput',
            name='risk_id',
            field=models.CharField(max_length=10),
        ),
    ]