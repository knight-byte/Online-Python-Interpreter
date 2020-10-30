from django.conf import settings
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


class StaffRequiredMixin(AccessMixin):

    def redirect_to_login(self):
        return redirect_to_login(
            next=self.request.get_full_path(),
            login_url=self.get_login_url(),
            redirect_field_name=self.get_redirect_field_name()
        )

    def handle_no_permission(self, request):
        if not request.user.is_authenticated:
            return self.redirect_to_login()
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return HttpResponse(self.get_permission_denied_message(), status=403)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return self.handle_no_permission(request)
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
