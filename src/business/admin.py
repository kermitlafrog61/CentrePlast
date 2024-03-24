from django.contrib import admin
from .models import DailyReport


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ['manager_first_name', 'address', 'revenue', 'date']

    def manager_first_name(self, obj):
        return obj.manager.first_name
    manager_first_name.admin_order_field = 'manager__first_name'
    manager_first_name.short_description = 'Manager First Name'
