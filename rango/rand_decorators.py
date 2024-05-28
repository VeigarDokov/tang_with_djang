"""this is veigar random decorators"""
from django.core.exceptions import PermissionDenied


def permission_required(allowed_users=[]):
    """docstring for rand decorator"""
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if request.user is allowed_users:
                return func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator
