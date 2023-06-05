from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseBadRequest
from .decorators import arisDecor_requireAjax; 

@arisDecor_requireAjax
@api_view(['GET'])
def getData(request):
    print(" = = = = = = BEGIN = = = = = ");
    #print(dir(request));
    #print(request.META.get('HTTP_X_REQUESTED_WITH'));
    #print(request.META.get('REQUEST_METHOD'));
    print(request.headers.get('X-Requested-With'));
    print(" = = = = = = = ON GOING= = = = ");
    """
    if not (request.headers.get('X-Requested-With') == 'XMLHttpRequest'):
        return HttpResponseBadRequest();
    else:
        person = {'name':'Elijah', 'age':15};
        return Response(person);
    """

    person = {'name':'Elijah', 'age':15};
    return Response(person);

