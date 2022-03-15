# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path('api/v1/commons/', include('apps.commons.urls')),
    path('', include('apps.accounts.urls')),
    path('api/', include('library.urls')),
    # Auth routes - login / register
    path("", include("apps.authentication.urls")),
    path("", include("apps.home.urls")),  # UI Kits Html files

]
