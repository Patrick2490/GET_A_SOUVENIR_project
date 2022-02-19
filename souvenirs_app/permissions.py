from urllib import request
from django.http import Http404


class SendUserChangePermissionsMixin:
    def has_permissions(self):
        print(self.get_object().send_user.username.username == self.request.user.username)
        return self.get_object().send_user.username.username == self.request.user.username

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class ReceiveUserChangePermissionsMixin:
    def has_permissions(self):
        print(self.get_object().receive_user.username.username == self.request.user.username)
        return self.get_object().receive_user.username.username == self.request.user.username

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)