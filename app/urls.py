from django.urls import path, re_path
from app import views
from django.conf.urls import url
from rest_framework import routers
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
# router.register(r'package', views.PackageViewSet)


urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('group', views.global_dashboard, name='global_dashboard'),
    path('opco', views.opco_dashboard, name='opco_dashboard'),
    path('region', views.region_dashboard, name='region_dashboard'),
    path('region', views.region_dashboard, name='region_dashboard'),
    path('history', views.task_history, name='history'),
    path('riskform', views.task_risk_form, name='riskform'),
    path('edit', views.task_edit, name='edit'),
    path('report', views.task_report, name='report'),
    path('riskassessment', views.risk_assessment, name='riskassessment'),
    path('riskresponse', views.risk_response, name='riskresponse'),
    path('configureapi', views.configure_api, name='configureapi'),
    path('push_riskresponse', views.push_riskresponse, name='pushriskresponse'),
    path('apitest', views.test_api, name='dacaAPI'),
   # The home page
    path('', views.index, name='home'),
]
