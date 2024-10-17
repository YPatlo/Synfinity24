from django.http import HttpResponse

# Create your views here.
def sitemap(request):
    return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')
