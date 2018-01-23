"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import serializers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
import drones.views


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
	drones = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='drone-detail')
	
	class Meta:
		model = DroneCategory
		fields = (
		'url',
		'pk',
		'name',
		'drones')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
	# Display the category name
	drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(),
		slug_field='name')
	
	class Meta:
		model = Drone
		fields = (
			'url',
			'name',
			'drone_category',
			'manufacturing_date',
			'has_it_competed',
			'inserted_timestamp')


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
	# Display all the details for the related drone
	drone = DroneSerializer()

	class Meta:
		model = Competition
		fields = (
			'url',
			'pk',
			'distance_in_feet',
			'distance_achievement_date',
			'drone')


class PilotSerializer(serializers.HyperlinkedModelSerializer):
	competitions = CompetitionSerializer(many=True, read_only=True)
	gender = serializers.ChoiceField(
	choices=Pilot.GENDER_CHOICES)
	gender_description = serializers.CharField(
		source='get_gender_display',
		read_only=True)
	
	class Meta:
		model = Pilot
		fields = (
			'url',
			'name',
			'gender',
			'gender_description',
			'races_count',
			'inserted_timestamp',
			'competitions')


class PilotCompetitionSerializer(serializers.ModelSerializer):
	# Display the pilot's name
	pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')
	# Display the drone's name
	drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')
	
	class Meta:
		model = Competition
		fields = (
			'url',
			'pk',
			'distance_in_feet',
			'distance_achievement_date',
			'pilot',
			'drone')


