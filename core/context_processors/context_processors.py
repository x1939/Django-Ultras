from core.models import Information, Logo

def info(request):
    return {
        'information': Information.objects.first(),
        'logo': Logo.objects.first(),
    }