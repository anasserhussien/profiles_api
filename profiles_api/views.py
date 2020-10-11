from django.shortcuts import render
from rest_framework.views import(
    APIView
)
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .permissions import *
from .serializers import *
from .models import *


# Create your views here.

class TestAPIView(APIView):
    """test API View"""
    serializer_class = TestSerializer

    def get(self, request, formate=None):
        """Return a list of APIView features"""

        return Response({'message': 'Hello'})

    def post(self, request):
        """Create a post method view"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = 'Hello {}'.format(name)
            return Response(
                {
                    'message':message
                }
            )
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        pass

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        pass

    def delete(self, request, pk=None):
        """Delete an object"""
        pass


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
    # specify which fields to search for using filter backend


class UserLoginAPIView(ObtainAuthToken):
    """Generating authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # to be able to test it in the browser version
