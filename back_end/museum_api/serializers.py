from rest_framework import serializers
from .models import Image
from django.db.models import Q

class ImageSerializer(serializers.ModelSerializer):
	image = serializers.ImageField(use_url=True)
	created_on = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
	class Meta:
		model = Image
		fields = ('id', 'input_text', 'created_on', 'image')
	# def validate_name(self, value):
	# 	if len(value) <= 1:
	# 		raise serializers.ValidationError("キーワードは必ず2文字以上で設定してください")
	# 	return value