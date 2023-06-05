from rest_framework.response import Response;
from rest_framework.decorators import api_view;
from django.http import HttpResponseBadRequest;
from django.shortcuts import HttpResponse;
from django.shortcuts import render;
from django.shortcuts import redirect;
from urllib.parse import urlencode;
import json;
from django.contrib.auth import authenticate;
'''
from django.contrib.auth.models import User, Group, Permission;
from school_app.models import Filiere;
from school_app.models import Domaine;
'''

@api_view(['GET'])
def getForm(request):
    #return HttpResponse("Form login...");
    #return render(request, 'api_login/login_form.html');
    if( 'is_connected' in request.session ):
#        return redirect("{}{}".format(base_url, encoded_params));
#        print('connecté');
        #checkLoginData(request);
        return HttpResponse(f'{request} DEJA CONNECTE !');
    else:
        return render(request, 'api_login/login_form2.html');

@api_view(['POST'])
def postLoginData(request):
    return HttpResponse(f'{request} well received!');

@api_view(['POST'])
def checkLoginData(request):
    print(" + + ++ + + + + + + + + + + + + + +");
    message = 'non';
    if(request.method == 'POST'):
        data = json.load(request);
        username = data.get('username');
        password = data.get('password');
        logged_user = authenticate(username=username, password=password);

        #if(username == 'u' and password == 'p'):
        if(logged_user is not None):
            message = 'oui';
            #return render(request, 'api_logged_user_pages/');
            #return redirect('/api_logged_user_pages/', message);
            #base_url = '/api_logged_user_pages/';
            base_url = '/api_logged_user_pages/' + '?';
            url_params = {'user':username, 'prenoms':password};
            #url_params = {'user':'arisTo', 'prenoms':'samaT'};
            url_params['page1'] = 'LR';
            #url_params = {'user':'aris'};#, 'prenoms':'sama'};
            encoded_params = urlencode(url_params);  
            print(encoded_params);
            print(url_params);
            request.session['is_connected'] = True;
            request.session.modified = True;
            return redirect("{}{}".format(base_url, encoded_params));

        print(data);
        print(" - - -- - PARAMS- - - - - - -");
    return HttpResponse(message);

