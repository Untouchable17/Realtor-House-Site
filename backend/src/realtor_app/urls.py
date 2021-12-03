from django.urls import path

from src.realtor_app import views


app_name = "realtors"

urlpatterns = [
    path('', views.RealtorListAPIView.as_view(), name="all_realtors"),
    path('<int:pk>/', views.RealtorAPIView.as_view(), name="retrieve_realtor"),
    path('top_realtor/', views.RatingTopAPIView.as_view(), name="top_realtor"),
]