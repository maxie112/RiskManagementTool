# Generated by Django 3.0.3 on 2020-04-09 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_opco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='risk_type',
            field=models.CharField(choices=[('Operational', 'Operational'), ('Strategic', 'Strategic'), ('Compliance', 'Compliance')], default='Operational', max_length=200),
        ),
        migrations.CreateModel(
            name='Opco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opco_name', models.CharField(max_length=250)),
                ('opco_size', models.CharField(choices=[('1', 'Small'), ('2', 'Medium'), ('3', 'Large')], default='medium', max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Country')),
            ],
        ),
    ]
