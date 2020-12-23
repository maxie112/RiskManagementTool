# Generated by Django 3.1.1 on 2020-09-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200515_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RiskId', models.IntegerField(max_length=2)),
                ('description', models.CharField(max_length=500)),
                ('riskName', models.CharField(max_length=10)),
                ('businessProcess', models.CharField(max_length=20)),
                ('controlId', models.IntegerField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
