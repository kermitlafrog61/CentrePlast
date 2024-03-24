from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return reverse_lazy('admin:index')
        return super().get_success_url()
