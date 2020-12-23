from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin_menno/', admin.site.urls),
    path("", include("authentication.urls")),  
    path("", include("app.urls"))  
]
