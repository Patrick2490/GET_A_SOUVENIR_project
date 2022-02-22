from rest_framework import permissions

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         """
#         :param request: Processing request from user.
#         :param view:
#         :param obj: Requested object.
#         :return: true or another action.
#         """
#         if request.method in permissions.SAFE_METHODS:  # The check of validation and security of the request.
#             return True
#         print(request.user)
#         return obj.username == request.user.username.username  # Comparison of the object's affiliation to the user.