from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# Home url
def home_view(request):
    return JsonResponse({"message":"Welcome to the Kiranawala API service."})