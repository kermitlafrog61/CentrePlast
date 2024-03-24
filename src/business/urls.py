from django.urls import path
from .views import ReportListView, ReportCreateView, ReportUpdateView


urlpatterns = [
    path('reports/', ReportListView.as_view(), name='report-list'),
    path('reports/create/', ReportCreateView.as_view(), name='report-create'),
    path('reports/<int:pk>/edit/', ReportUpdateView.as_view(), name='report-edit'),
]
