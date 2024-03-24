from django.contrib import admin
from django.urls import path, include

from . import views
from business.views import monthly_revenue_report


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/monthly-revenue-report/',
         monthly_revenue_report, name='monthly-revenue-report'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('business/', include('business.urls')),
]
