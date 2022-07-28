from rest_framework import generics
from .serializers import ImageSerializer
import os
from .models import Image
# Create your views here.
# class CreateImageView(generics.CreateAPIView):

# 	queryset = Image.objects.all()
# 	serializer_class = ImageSerializer

# 	def os(self):
# 		return os.system("ls")

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
import subprocess
class ImageViewSet(viewsets.ModelViewSet):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer

	def get_queryset(self):
		return self.queryset.filter()

	@action(detail=False, methods=['GET'], name='OS')
	def os(self, gomi):
		gomi = 1
		cp = subprocess.run("ls", capture_output=True, text=True)
		response = cp.stdout
		return Response(response, status=status.HTTP_200_OK)
