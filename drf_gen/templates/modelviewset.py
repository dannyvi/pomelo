
__all__ = ['MODEL_URL', 'MODEL_VIEW']


MODEL_URL = """from pomelo.settings import api_settings
from . import views


RouterClass = api_settings.DEFAULT_ROUTER
router = RouterClass()


{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}

urlpatterns = router.urls
"""


MODEL_VIEW = """from pomelo.modelviewset import ModelViewSet
from pomelo.decorators import swagger_viewset
from pomelo.filterfields import get_filterset_fields
from django.utils.translation import gettext_lazy as _
from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

@swagger_viewset(_('{{ model }}'), _('{{ model }}'), [_('{{ model }}')])
class {{ model }}ViewSet(ModelViewSet):
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer
    filterset_fields = get_filterset_fields(queryset.model)
{% endfor %}"""
