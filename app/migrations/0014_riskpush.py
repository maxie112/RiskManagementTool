# Generated by Django 3.0.3 on 2020-04-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200410_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskPush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_function', models.CharField(choices=[('GP', 'GP'), ('GA&R', 'GA&R'), ('GLA', 'GLA'), ('GAP', 'GAP'), ('GSP&BC', 'GSP&BC'), ('IPM?', 'IPM?'), ('GFP&CI', 'GFP&CI'), ('GC', 'GC'), ('GT&FM', 'GT&FM'), ('GCA', 'GCA'), ('GBD', 'GBD'), ('GHR', 'GHR'), ('IPMO', 'IPMO'), ('PROSECO', 'PROSECO'), ('GI', 'GI'), ('GIS', 'GIS'), ('Regional MT', 'Regional MT'), ('OpCo China', 'OpCo China'), ('GT  ', 'GT  '), ('GFP&IC', 'GFP&IC')], default='GP', max_length=200)),
                ('risk_topic', models.CharField(choices=[('Regulatory changes', 'Regulatory changes'), ('Economic and Political environment', 'Economic and Political environment'), ('Distribution channel', 'Distribution channel'), ('Consumer Preferences', 'Consumer Preferences'), ('Management Capabilities', 'Management Capabilities'), ('Industry Consolidation', 'Industry Consolidation'), ('Health and Safety', 'Health and Safety'), ('Product Safety and Integrity', 'Product Safety and Integrity'), ('Supply Chain Continuity', 'Supply Chain Continuity'), ('Information Securitty', 'Information Securitty'), ('Digital Media', 'Digital Media'), ('Execution and Change Management', 'Execution and Change Management'), ('Reporting', 'Reporting'), ('Non-Compliance', 'Non-Compliance')], default='Regulatory changes', max_length=200)),
                ('risk_response', models.CharField(choices=[('Mitigate', 'Mitigate'), ('Ignore', 'Ignore'), ('Avoid', 'Avoid'), ('Transfer', 'Transfer'), ('Accept', 'Accept'), ('Share', 'Share'), ('Contingecy', 'Contingency'), ('Enhance', 'Enhance'), ('Exploit', 'Exploit')], default='Mitigate', max_length=200)),
                ('risk_classification', models.CharField(choices=[('4', 'Extreme Risk'), ('3', 'High Risk'), ('2', 'Medium Risk'), ('1', 'Low Risk')], default='Low Risk', max_length=200)),
                ('risk_type', models.CharField(choices=[('Operational', 'Operational'), ('Strategic', 'Strategic'), ('Compliance', 'Compliance')], default='Operational', max_length=200)),
                ('impact_classification', models.CharField(choices=[('4', 'Catastrophic'), ('3', 'Critical'), ('2', 'Moderate'), ('1', 'Negligible')], default='Moderate', max_length=200)),
                ('risk_appetite', models.CharField(choices=[('1', 'Hungry'), ('2', 'Open'), ('3', 'Cautious'), ('4', 'Minimal'), ('5', 'Averse')], default='Averse', max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
