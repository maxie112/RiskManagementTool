# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Risk, Actions, HeiRulesMonitoring, Region, Country, Organization, RiskMapping, \
    ApiConfiguration, Opco, RiskAssesment, RiskInput

# Register your models here.

admin.site.register(Risk)

admin.site.register(Actions)

admin.site.register(HeiRulesMonitoring)

admin.site.register(Region)

admin.site.register(Country)

admin.site.register(Opco)

admin.site.register(Organization)

admin.site.register(RiskMapping)

admin.site.register(ApiConfiguration)

admin.site.register(RiskInput)

admin.site.register(RiskAssesment)


