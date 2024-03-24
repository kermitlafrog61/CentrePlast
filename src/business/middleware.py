from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


class PermissionDeniedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            messages.add_message(request, messages.ERROR,
                                 "You're not allowed to edit this report.")
            return HttpResponseRedirect(reverse('report-list'))
        return None
