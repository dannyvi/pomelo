from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.compat import coreapi, coreschema
from django.utils.encoding import force_str

class Pagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size=32
    page_param = 'no_page'
    page_title = 'No paging'
    page_description = 'Cancel paging'

    def paginate_queryset(self, queryset, request, view=None):
        if 'no_page' in request.query_params:
            return None

        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'current': self.page.number,
            'total': self.page.paginator.num_pages,
            'results': data
        })

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        fields = super().get_schema_fields(view)

        fields.append(
            coreapi.Field(
                name=self.page_param,
                required=False,
                location='query',
            )
        )

        return fields

    def get_schema_operation_parameters(self, view):
        params = super().get_schema_operation_parameters(view)
        params.append(
            {
                'name': self.page_param,
                'required': False,
                'in': 'query',
                'description': force_str(self.page_description),
                'schema': {
                    'type': 'string',
                },
            },
        )
        return params
