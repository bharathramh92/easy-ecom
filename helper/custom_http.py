def get_from_request_GET(request):
    return '?' + ''.join([str(k + '=' + v + '&') for k,v in request.GET.items()])[:-1]