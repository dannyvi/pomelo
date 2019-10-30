__all__ = ['SERIALIZER']


SERIALIZER = """from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from {{ app }}.models import {{ models | join:', ' }}
{% for model, foreign, manytomany in models_keys %}

class {{ model }}Serializer(ModelSerializer):

    class Meta:
        model = {{ model }}{% if depth != 0 %}
        depth = {{ depth }}{% endif %}
        fields = '__all__'
    {% if foreign != None %} {% for name, mdl in foreign %}
    
    {{ name }}_detail = serializers.SerializerMethodField(read_only=True)
    
    def get_{{ name }}_detail(self, obj):
        return {{ mdl }}Serializer(obj.{{ name }}).data
    
    {% endfor %} {% endif %}
    
{% endfor %}"""
