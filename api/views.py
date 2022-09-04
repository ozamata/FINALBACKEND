from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics



from .models import *
from .serializers import *


class IndexView(APIView):

    def get(self,request):
        context = {
            'status':True,
            'message':'api de miembros listo'
        }

        return Response(context)


class NoticiasView(generics.ListAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer


class NoticiasCreateView(generics.CreateAPIView):
    serializer_class = NoticiasSerializer


class TestimonioView(generics.ListAPIView):
    queryset = Testimonio.objects.all()
    serializer_class = TestimonioSerializer


class TestimonioCreateView(generics.CreateAPIView):
    serializer_class = TestimonioSerializer