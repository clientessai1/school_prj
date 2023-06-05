from django.http import HttpResponseBadRequest

def arisDecor_requireAjax(function):
    """
    Retrurn a bad request instance if the view is not using AJAX function -- the view
    """
    def wrap(request, *args, **kwargs):
        if not (request.headers.get('X-Requested-With') == 'XMLHttpRequest'):
            return HttpResponseBadRequest();
        return function(request, *args, **kwargs);

    wrap.__doc__ = function.__doc__;
    wrap.__name__ = function.__name__;
    return wrap;
