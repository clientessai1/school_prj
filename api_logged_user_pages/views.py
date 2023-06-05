from rest_framework.response import Response;
from rest_framework.decorators import api_view;
from django.http import HttpResponseBadRequest;
from django.shortcuts import HttpResponse;
from django.shortcuts import render;
import json;
from django.contrib.auth.models import User;

@api_view(['GET'])
#def getIndex(request, user, prenoms):
def getIndex(request):
    data = request.GET;
    #data = json.load(request);
    print("- - - -api_logged_user_pages GETINDEX - - - -");
    print(data);
    user_name = data['user'];      
    connected_user = User.objects.get(username=user_name);
    permissions_list = connected_user.get_group_permissions();
    print(permissions_list);
    """
    print(user);
    print(prenoms);
    """
    #return HttpResponse("Form login...");
    #return render(request, 'api_login/login_form.html');
    return render(request, 'api_logged_user_pages/index.html');

@api_view(['GET'])
def getPage1(request):
    return render(request, 'api_logged_user_pages/page1.html');

@api_view(['GET'])
def getPage2(request):
    return render(request, 'api_logged_user_pages/page2.html');

"""
@api_view(['POST'])
def postLoginData(request):
    return HttpResponse(f'{request} well received!');
"""
