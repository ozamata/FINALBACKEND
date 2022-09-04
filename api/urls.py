from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('noticias',views.NoticiasView.as_view()),
    path('noticias/create',views.NoticiasCreateView.as_view()),
    path('testimonio',views.TestimonioView.as_view()),
    path('testimonio/create',views.TestimonioCreateView.as_view()),
    ]