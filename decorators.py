from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy

def swagger_viewset(summary, description, tags=None):
    """Auto schema viewset by adding a summary and description."""
    d = description
    t = tags
    def add_title_desc(method, summary, desc, tags):
        return method_decorator(
            name=method,
            decorator=swagger_auto_schema(
                operation_summary=summary, operation_description=desc, tags=tags))

    def add_schema(*arg_tups):
        def wrapper(func):
            def recur(args):
                length = len(args)
                if length == 1:
                    method, summary = args[-1]
                    return add_title_desc(method, summary, d, t)(func)
                else:
                    m, s = args[-1]
                    return add_title_desc(m, s, d, t)(recur(args[:length - 1]))

            return recur(arg_tups)

        return wrapper

    return add_schema(
        ('list', format_lazy('{}-{}', summary, _('List'))),
        ('retrieve', format_lazy('{}-{}', summary, _('Retrieve'))),
        ('create', format_lazy('{}-{}', summary, _('Create'))),
        ('partial_update', format_lazy('{}-{}', summary, _('Partial-Update'))),
        ('destroy', format_lazy('{}-{}', summary, _('Destroy')))
    )