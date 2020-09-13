import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # check if data contains errors object in body.
        errors = data.get('errors',None)

        if errors is not None:
            # Let default JSONRenderer handle the error cases
            return super(UserJSONRenderer, self).render(data)

        # If we receive a `token` key as part of the response, it will be a
        # byte object. Byte objects don't serialize well, so we need to
        # decode it before rendering the User object.
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        # Insert data inside a user object for better visibility
        return json.dumps({
            'user': data
        })