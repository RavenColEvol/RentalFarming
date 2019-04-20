from django.core.exceptions import PermissionDenied


def renter_only(view_func):
    def wrap(*args, **kwargs):
        if str(args[0].request.user) == 'AnonymousUser' or not args[0].request.user.is_renter:
            raise PermissionDenied

        return view_func(*args, **kwargs)

    return wrap
