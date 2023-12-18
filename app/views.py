from django.shortcuts import render
from rest_framework.response import Response
# Correct import statement
from rest_framework.views import APIView

# Your view class
class Appview(APIView):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        return Response({'data':'hello world from post'})