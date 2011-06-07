from django.contrib.sites.models import Site

def site(request):
    #TODO: caching here
    return {'current_site': Site.objects.get_current() }

