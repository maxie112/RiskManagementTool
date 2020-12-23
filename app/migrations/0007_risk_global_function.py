# Generated by Django 3.0.3 on 2020-04-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200409_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='global_function',
            field=models.CharField(choices=[('GP', 'GP'), ('GA&R', 'GA&R'), ('GLA', 'GLA'), ('GAP', 'GAP'), ('GSP&BC', 'GSP&BC'), ('IPM?', 'IPM?'), ('GFP&CI', 'GFP&CI'), ('GC', 'GC'), ('GT&FM', 'GT&FM'), ('GCA', 'GCA'), ('GBD', 'GBD'), ('GHR', 'GHR'), ('IPMO', 'IPMO'), ('PROSECO', 'PROSECO'), ('GI', 'GI'), ('GIS', 'GIS'), ('Regional MT', 'Regional MT'), ('OpCo China', 'OpCo China'), ('GT  ', 'GT  '), ('GFP&IC', 'GFP&IC')], default='GP', max_length=200),
        ),
    ]