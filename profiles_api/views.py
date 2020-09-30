from django.shortcuts import render
from rest_framework.views import(
    APIView
)
from rest_framework.response import Response

# Create your views here.

class TestAPIView(APIView):
    """test API View"""

    def get(self, request, formate=None):
        """Return a list of APIView features"""
        

        return Response({'message': 'Hello'})
