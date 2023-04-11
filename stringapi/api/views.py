from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def string_reverse(request, input_string):
    reversed_string = input_string[::-1]
    output = {'reversed_string': reversed_string}
    return JsonResponse(output)
