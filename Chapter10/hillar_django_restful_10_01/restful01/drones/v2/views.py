"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones import views


class ApiRootVersion2(generics.GenericAPIView):
	name = 'api-root'
	def get(self, request, *args, **kwargs):
		return Response({
			'vehicle-categories': reverse(views.DroneCategoryList.name,
				request=request),
			'vehicles': reverse(views.DroneList.name, request=request),
			'pilots': reverse(views.PilotList.name, request=request),
			'competitions': reverse(views.CompetitionList.name,
				request=request)
			})
