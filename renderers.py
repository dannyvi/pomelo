from rest_framework.renderers import JSONRenderer

def _expand_list_or_dict_recursively(data):
    if isinstance(data, dict):
        return ' '.join([f'{key}: {_expand_list_or_dict_recursively(value)}'
                          if key != 'detail' else
                          f'{_expand_list_or_dict_recursively(value)}' for
                          key, value in data.items() ])
    elif isinstance(data, list):
        return '     '.join([_expand_list_or_dict_recursively(d) for d in data])
    else:
        return data


class PomeloRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        success=True
        status_code=200
        try:
            response = renderer_context['response']

            if int(response.status_code) >= 300:
                success = False
                if int(response.status_code) == 401 and data['detail'].code == 'not_authenticated':
                    status_code = 208
                else:
                    status_code = response.status_code
                #print(status_code, data, data['detail'].code)
        except:
            pass
        if success:
            data = {'status':status_code, 'data': data}
        else:
            data = {'status': status_code, 'message': _expand_list_or_dict_recursively(data)}
        return super().render(data, accepted_media_type, renderer_context)

