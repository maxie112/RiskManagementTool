from django import forms
from .models import Risk, Actions, HeiRulesMonitoring, ApiConfiguration, Region, Country, RiskAssesment, RiskPush, RiskInput


class RiskIdentified(forms.ModelForm):
    class Meta:
        widgets = {'description': forms.TextInput(attrs={'size': 50})}
        model = Risk
        fields = ['global_function', 'risk_topic', 'risk_classification', 'impact_classification', 'risk_response', 'risk_type',
                  'risk_appetite', 'description']


class RiskActions(forms.ModelForm):
    class Meta:
        widgets = {'action_title': forms.TextInput(attrs={'size': 50}),
                   'action_description': forms.TextInput(attrs={'size': 50})}
        model = Actions
        fields = ['action_title', 'action_description']


class HeiRulesMonitor(forms.ModelForm):
    class Meta:
        widgets = {'way_of_testing': forms.TextInput(attrs={'size': 50})}
        model = HeiRulesMonitoring
        fields = ['testing_procedure', 'size', 'frequency', 'way_of_testing']


class ApiConfiguration(forms.ModelForm):
    class Meta:
        widgets = {'custom_url': forms.TextInput(attrs={'size': 50})}
        widgets = {'short_description': forms.TextInput(attrs={'size': 50})}
        model = ApiConfiguration
        fields = ['long_name', 'frequency', 'custom_url', 'short_description']


class PushRisk(forms.ModelForm):
    class Meta:
        widgets = {'description': forms.TextInput(attrs={'size': 50})}
        model = RiskPush
        fields = ['global_function', 'risk_topic', 'risk_classification', 'impact_classification', 'risk_response',
                  'risk_type', 'risk_appetite', 'description']


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['region_short', 'region_long']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_long']


class RiskInputForm(forms.ModelForm):
    class Meta:
        model = RiskInput
        widgets = {
        'risk_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        'risk_title': forms.TextInput(attrs={'readonly': 'readonly'}),
        'description': forms.TextInput(attrs={'readonly': 'readonly', 'size': 100}),
    }
        fields=['risk_id', 'risk_title', 'description', ]


class RiskAssessmentForm(forms.ModelForm):
    class Meta:
        model = RiskAssesment
        widgets = {'open_entry': forms.TextInput(attrs={'size': 50})}
        fields=['relevance', 'open_entry']