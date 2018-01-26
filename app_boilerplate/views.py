from knox.auth import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


# Endpoint to check token validity, just gives 200 or error.
class Token(APIView):

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        return Response()

# Example endpoint


class ViewBoilerplate(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        return Response({'example': True})
