from django.http import Http404

class SendUserChangePermissionMixin:
    def has_permissions(self):
        return self.get_object().send_user.username.username == self.request.user.username

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404
        return super().dispatch(request, *args, **kwargs)