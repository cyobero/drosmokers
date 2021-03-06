"""drosmokers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import strains.views
import drosmokers.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', strains.views.batches_view, name='index'),
    path('new/strain', strains.views.strain_form, name='strain-form'),
    path('batches/', strains.views.batches_view, name='batches'),
    path('new/batch', strains.views.batch_form, name='batch-form'),
    path('new/terpenes/<int:batch_id>',
         strains.views.terpenes_form, name='terpenes-form'),
    path('new/grower', strains.views.grower_form, name='grower-form'),
    path('terpenes/<int:batch_id>',
         strains.views.terpenes_view, name='terpene-profile'),
    path('new/rating', strains.views.rating_form, name='rating-form'),
    path('success/', drosmokers.views.success_view, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
