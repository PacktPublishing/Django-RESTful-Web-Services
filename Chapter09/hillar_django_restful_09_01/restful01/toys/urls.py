"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('drones.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
