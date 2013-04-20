from django.conf import settings

def googleanalytics(request):
    return {
        'google_tracking_id' : settings.GOOGLE_TRACKING_ID,
    }