from django.shortcuts import render
from rest_framework.views import(
    APIView
)
from rest_framework.response import Response
from rest_framework import status

from .serializers import TestSerializer


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
