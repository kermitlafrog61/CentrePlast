from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import CreateView, ListView, UpdateView

from .forms import MonthYearForm
from .models import DailyReport


class ReportListView(LoginRequiredMixin, ListView):
    model = DailyReport
    template_name = 'reports/list.html'

    def get_queryset(self):
        return DailyReport.objects.filter(manager=self.request.user)


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = DailyReport
    fields = ['address', 'revenue']
    template_name = 'reports/create.html'
    success_url = reverse_lazy('report-list')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        form.instance.date = now()
        return super().form_valid(form)


class ReportUpdateView(UpdateView):
    model = DailyReport
    fields = ['address', 'revenue']
    template_name = 'reports/update.html'

    def get_object(self, queryset=None):
        """Ensure that only reports from the current month can be edited."""
        obj = super().get_object(queryset)
        if obj.date.month == now().month and obj.date.year == now().year:
            return obj
        else:
            raise PermissionDenied("The date has already passed")

    def get_queryset(self):
        """Ensure users can only edit their own reports."""
        return DailyReport.objects.filter(manager=self.request.user)

    def get_success_url(self):
        return reverse_lazy('report-list')


@staff_member_required
def monthly_revenue_report(request):
    if request.method == 'POST':
        form = MonthYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            total_revenue = DailyReport.objects.filter(
                date__month=month, date__year=year).aggregate(Sum('revenue'))['revenue__sum'] or 0
            return render(request, 'monthly_revenue_report.html', {'form': form, 'total_revenue': total_revenue})
    else:
        form = MonthYearForm()
    return render(request, 'monthly_revenue_report.html', {'form': form, 'total_revenue': None})
