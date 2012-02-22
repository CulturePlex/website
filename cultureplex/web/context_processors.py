# -*- coding: utf-8 -*-
from django.conf import settings

def api_keys(request):
    return {'GOOGLE_ANALYTICS': getattr(settings, "GOOGLE_ANALYTICS", None),
            'GOOGLE_API_KEY': getattr(settings, "GOOGLE_API_KEY", None),
            'GOOGLE_MAPS_API_KEY': getattr(settings,
                                           "GOOGLE_MAPS_API_KEY", None)}

def project_name(request):
    return {'PROJECT_NAME': getattr(settings, "PROJECT_NAME", None)}

