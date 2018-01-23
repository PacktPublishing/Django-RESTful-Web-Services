"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('drones.urls', namespace='v1')),
    url(r'^v1/api-auth/', include('rest_framework.urls',
        namespace='rest_framework_v1')),
    url(r'^v2/', include('drones.v2.urls', namespace='v2')),
    url(r'^v2/api-auth/', include('rest_framework.urls',
        namespace='rest_framework_v2')),
    ]
