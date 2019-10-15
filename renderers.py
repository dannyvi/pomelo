from rest_framework.renderers import JSONRenderer

class PomeloRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        success=True
        try:
            response = renderer_context['response']
            status_code = response.status_code

            if status_code >= 300:
                success = False
        except:
            pass
        data = {'success': True, 'data': data}

        return super().render(data, accepted_media_type, renderer_context)

