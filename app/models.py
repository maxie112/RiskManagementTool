# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

#commentaar test
#nog een commentaar test
# Create your models here.
MAIN_RISKS = (
    ("Regulatory changes", "Regulatory changes"),
    ("Economic and Political environment", "Economic and Political environment"),
    ("Distribution channel", "Distribution channel"),
    ("Consumer Preferences", "Consumer Preferences"),
    ("Management Capabilities", "Management Capabilities"),
    ("Industry Consolidation", "Industry Consolidation"),
    ("Health and Safety", "Health and Safety"),
    ("Product Safety and Integrity", "Product Safety and Integrity"),
    ("Supply Chain Continuity", "Supply Chain Continuity"),
    ("Information Securitty", "Information Securitty"),
    ("Digital Media", "Digital Media"),
    ("Execution and Change Management", "Execution and Change Management"),
    ("Reporting", "Reporting"),
    ("Non-Compliance", "Non-Compliance")
)

GLOBAL_FUNCTIONS = (
                       ('GP','GP'),
                       ('GA&R','GA&R'),
                       ('GLA','GLA'),
                       ('GAP','GAP'),
                       ('GSP&BC','GSP&BC'),
                       ('IPM?','IPM?'),
                       ('GFP&CI','GFP&CI'),
                       ('GC','GC'),
                       ('GT&FM','GT&FM'),
                       ('GCA','GCA'),
                       ('GBD','GBD'),
                       ('GHR','GHR'),
                       ('IPMO','IPMO'),
                       ('PROSECO','PROSECO'),
                       ('GI','GI'),
                       ('GIS','GIS'),
                       ('Regional MT','Regional MT'),
                       ('OpCo China','OpCo China'),
                       ('GT  ','GT  '),
                       ('GFP&IC','GFP&IC')
)

MAIN_RESPONSES = (
    ("Mitigate", "Mitigate"),
    ("Ignore", "Ignore"),
    ("Avoid", "Avoid"),
    ("Transfer", "Transfer"),
    ("Accept", "Accept"),
    ("Share", "Share"),
    ("Contingecy", "Contingency"),
    ("Enhance", "Enhance"),
    ("Exploit", "Exploit")
)

RISK_CLASSIFICATION = (
    ("4", "Extreme Risk"),
    ("3", "High Risk"),
    ("2", "Medium Risk"),
    ("1", "Low Risk")
)

IMPACT_CLASSIFICATION = (
    ("4", "Catastrophic"),
    ("3", "Critical"),
    ("2", "Moderate"),
    ("1", "Negligible")
)


RISK_TYPE = (
    ("Operational", "Operational"),
    ("Strategic", "Strategic"),
    ("Compliance", "Compliance")

)

RISK_APPETITE = (
    ("1", "Hungry"),
    ("2", "Open"),
    ("3", "Cautious"),
    ("4", "Minimal"),
    ("5", "Averse"),
)

TESTING_CHOICES = (
    ("1", "HeiRules CSA 08 Health and Safety"),
    ("2", "HeiRules CSA 14 TAX"),
    ("3", "HeiRules CSA xx XX"),
)

SIZE_CHOICES = (
    ("1", "Small OPCO"),
    ("2", "Medium OPCO"),
    ("3", "Large OPCO"),
)

FREQUENCY_CHOICES = (
    ("1", "Weekly"),
    ("2", "Monthly"),
    ("3", "Quarterly"),
    ("4", "Annually")
)

API_OPTIONS = (
    ("1", "WHO"),
    ("2", "World Risk Index"),
    ("3", "WorldBank"),
    ("4", "Bloomberg"),
)

API_FREQUENCY = (
    ("1", "Hourly"),
    ("2", "Daily"),
    ("3", "Weekly"),
    ("4", "Monthly")
)

OPCO_SIZES = (
    ("1","Small"),
    ("2","Medium"),
    ("3","Large"),
)

COUNTRY_CHOICES = (
    ("Netherlands", "Netherlands"),
    ("Germany", "Germany"),
    ("France", "France")
)


STATUS_CHOICES = (
    ("Approved", "Approved"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected")
)

RELEVANCY_CHOICES = (
    ("Not relevant", "Not relevant"),
    ("Relevant", "Relevant"),
    ("High importance", "High importance")
)


REPUTATIONAL_RISKS = []
FINANCIAL_RISKS = []
BUSINESS_CONTINUITY_RISKS = []


class Region(models.Model):
    region_short = models.CharField(max_length=50)
    region_long = models.CharField(max_length=250)


class Country(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=5)
    country_long = models.CharField(max_length=250, choices=COUNTRY_CHOICES, default="Netherlands")


class Opco(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    opco_name = models.CharField(max_length=250)
    opco_size = models.CharField(max_length=50, choices=OPCO_SIZES, default="medium")


class Actions(models.Model):
    action_title = models.CharField(max_length=200)
    action_description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HeiRulesMonitoring(models.Model):
    testing_procedure = models.CharField(max_length=200, choices=TESTING_CHOICES, default="HeiRules CSA xx XX")
    size = models.CharField(max_length=200, choices=SIZE_CHOICES, default="Medium OPCO")
    frequency = models.CharField(max_length=200, choices=FREQUENCY_CHOICES, default="Quarterly")
    way_of_testing = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Risk(models.Model):
    global_function = models.CharField(max_length=200, choices=GLOBAL_FUNCTIONS, default="GP")
    risk_topic = models.CharField(max_length=200, choices=MAIN_RISKS, default="Regulatory changes")
    risk_response = models.CharField(max_length=200, choices=MAIN_RESPONSES, default="Mitigate")
    risk_classification = models.CharField(max_length=200, choices=RISK_CLASSIFICATION, default="Low Risk")
    risk_type = models.CharField(max_length=200, choices=RISK_TYPE, default="Operational")
    impact_classification = models.CharField(max_length=200, choices=IMPACT_CLASSIFICATION, default="Moderate")
    risk_appetite = models.CharField(max_length=200, choices=RISK_APPETITE, default="Averse")
    description = models.CharField(max_length=500)
    action = models.ForeignKey(Actions, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    monitoring = models.ForeignKey(HeiRulesMonitoring, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RiskPush(models.Model):
    global_function = models.CharField(max_length=200, choices=GLOBAL_FUNCTIONS, default="GP")
    risk_topic = models.CharField(max_length=200, choices=MAIN_RISKS, default="Regulatory changes")
    risk_response = models.CharField(max_length=200, choices=MAIN_RESPONSES, default="Mitigate")
    risk_classification = models.CharField(max_length=200, choices=RISK_CLASSIFICATION, default="Low Risk")
    risk_type = models.CharField(max_length=200, choices=RISK_TYPE, default="Operational")
    impact_classification = models.CharField(max_length=200, choices=IMPACT_CLASSIFICATION, default="Moderate")
    risk_appetite = models.CharField(max_length=200, choices=RISK_APPETITE, default="Averse")
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="New")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Organization(models.Model):
    short_description = models.CharField(max_length=50)
    long_description = models.CharField(max_length=250)


class RiskMapping(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    action = models.ForeignKey(Actions, on_delete=models.CASCADE)
    monitoring = models.ForeignKey(HeiRulesMonitoring, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class ApiConfiguration(models.Model):
    api_id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=50)
    custom_url = models.CharField(max_length=500)
    long_name = models.CharField(max_length=200, choices=API_OPTIONS, default="WHO")
    frequency = models.CharField(max_length=500, choices=API_FREQUENCY, default="Daily")
    short_description = models.CharField(max_length=500)

class RiskInput(models.Model):
    risk_id = models.CharField(max_length=10)
    risk_title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RiskAssesment(models.Model):
    risk_id = models.CharField(max_length=10, blank=True)
    impact = models.IntegerField(null=True)
    likelyhood = models.IntegerField(null=True)
    relevance = models.CharField(max_length=20, choices=RELEVANCY_CHOICES, default="Relevant")
    open_entry = models.TextField(max_length=1000, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
