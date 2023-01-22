from django.shortcuts import render

def error_404(request, exception):
    return render(request, '../templates/404.html', status=404)


def error_500(request):
    return render(request, '../templates/500.html', status=500)