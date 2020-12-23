from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .models import MAIN_RISKS, Risk, HeiRulesMonitoring, Actions, RiskPush, RiskInput, RiskAssesment
from .forms import RiskIdentified, RiskActions, HeiRulesMonitor, ApiConfiguration, CountryForm, RegionForm, PushRisk, RiskInputForm, RiskAssessmentForm
#from excel_response import ExcelResponse
from .serializer import RiskSerializer
from core.pagination import SmalllResultsSetPagination
from core.throttle import UserMinThrottle
from core.permissions import IsOwnerOrReadOnly
from core.generate_oath_tokens import generate_tokens
#Commentaar test
@login_required(login_url="/login/")
def index(request):
    try:
        generate_tokens(request)
    except Exception as e:
        error_message = e.__cause__
        print(error_message)
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:
        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def global_dashboard(request):
    return render(request, "global.html")


@login_required(login_url="/login/")
def opco_dashboard(request):
    risk_count = Risk.objects.all().count()

    return render(request, "opco.html", context={'newRisksCount': risk_count, 'totalRiskCount': risk_count + 20,
                                                 'pendingRiskCount': risk_count+6})


@login_required(login_url="/login/")
def region_dashboard(request):
    if request.method == "POST":
        _risk_push = PushRisk(request.POST)
        if _risk_push.is_valid():
            _risk_push.save()
    return render(request, "region.html")


@login_required(login_url="/login/")
def task_risk_form(request):
    #_risk_form_status =
    if request.method == "POST":
        _risk_form = RiskIdentified(request.POST)
        _risk_action = RiskActions(request.POST)
        _hei_monitoring = HeiRulesMonitor(request.POST)

        # print(risk_form)
        if _risk_action.is_valid():
            risk_action = _risk_action.save(commit=False)

            risk_action.save()
        if _hei_monitoring.is_valid():
            hei_monitoring = _hei_monitoring.save(commit=False)

            hei_monitoring.save()
        if _risk_form.is_valid():
            risk_form = _risk_form.save(commit=False)
            risk_form.action = risk_action
            risk_form.monitoring = hei_monitoring
            risk_form.status = "Pending"
            risk_form.save()


    _risks = list(Risk.objects.all().values('global_function',
                                            'risk_topic',
                                            'risk_type',
                                            'status').order_by('-created_at'))[:10]
    _new_risks = list(RiskPush.objects.all().order_by('-created_at'))
    _headers = ['Global Function', 'Topic', 'Type', 'Status']


    #TODO: Retrieve submitted risk responses from the database, list them ordered by modification date descending.
    return render(request, "riskform.html", {"newrisks": _new_risks,
                                             "risks": _risks,
                                             "headers": _headers})



@login_required(login_url="/login/")
def task_report(request):
    if request.method == "POST":
        objs = Risk.objects.select_related('action').all()
        return "1"

    rm_headers = ['id', 'description', 'created_at', 'updated_at', 'action', 'monitoring', 'status']
    _risks = list(Risk.objects.all().order_by('-created_at'))

    _headers = [f.name for f in Risk._meta.fields if f.name not in rm_headers]

    return render(request, "report.html", {
                                           'risks': _risks,
                                           'headers': _headers})


@login_required(login_url="/login/")
def task_edit(request):
    return render(request, "edit.html")


@login_required(login_url="/login/")
def push_riskresponse(request):

    return render(request, "pushriskresponse.html", {'risk': PushRisk,
                                                     'region': RegionForm,
                                                     'country': CountryForm})


@login_required(login_url="/login/")
def task_history(request):
    return render(request, "history.html")


@login_required(login_url="/login/")
def risk_assessment(request):
    print(request.user) #TODO: REGISTREER DEZE USER IN DE INPUT MODEL ZODAT WE ZIEN WIE WAT DOET

    if request.method == "GET":
        request.session["riskid"] = 1
        risk_item = RiskInput.objects.get(risk_id=request.session["riskid"])
        risk_info = RiskInputForm(initial={'risk_id': risk_item.risk_id,
        'risk_title': risk_item.risk_title, 
        'description': risk_item.description})
        risk_input = RiskAssessmentForm  
        return render(request, "riskassessmenttemplate.html", {'riskInfo': risk_info,
                                                 'riskInput': risk_input
                                                 })

    else:
        _risk_info_form = RiskInputForm(request.POST)
        _risk_input_form = RiskAssessmentForm(request.POST)
        if _risk_input_form.is_valid():
            #TODO: REGISTREER DE RISK ID IN DE INPUT MODEL ZODAT WE RESULTAAT AAN DE RISK ID KUNNEN KOPPELLEN..
            risk_assessment = _risk_input_form.save(commit=False)
            risk_assessment.save()
        
        request.session["riskid"] = request.session["riskid"] + 1
        try:
            risk_item = RiskInput.objects.get(risk_id=request.session["riskid"])
        except:
            #TODO: GEEF ANDERE PAGINA TERUG MET MELDING DAT HET KLAAR IS? MISSCHIEN OVERALL RESULT PAGE / POWER BI DASHBOARD EMBEDDEN?
            return render(request, "finishedRiskAssessment.html")
        risk_info = RiskInputForm(initial={'risk_id': risk_item.risk_id, 'description': risk_item.description})
        risk_input = RiskAssessmentForm
        return render(request, "riskassessmenttemplate.html", {'riskInfo': risk_info,
                                                 'riskInput': risk_input
                                                 })


@login_required(login_url="/login/")
def configure_api(request):
    # TODO: Possible risks:
    # Access Management Physical -> Entry to facilities
    api_form = ApiConfiguration
    return render(request, "configureapi.html", {'apiform': api_form})


@login_required(login_url="/login/")
def risk_response(request):

    if request.method == "GET":
        risk_form = RiskIdentified
        risk_action = RiskActions
        hei_monitoring = HeiRulesMonitor
        return render(request, "riskresponse.html", {'riskform': risk_form,
                                                 'riskaction': risk_action,
                                                 'heimonitoring': hei_monitoring})

@api_view(['GET', 'POST'])
def test_api(request):
    """
    API for demo puproses
    """
    if request.method == 'GET':
        
        _status = 200
        _response_payload = {
            'id': 1,
            'name': "Menno",
            'Company': "PwC"
        }

        return JsonResponse(_response_payload, status=_status)

