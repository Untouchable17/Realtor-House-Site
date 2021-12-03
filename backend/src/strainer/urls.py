from django.urls import path

from src.strainer import views


app_name = "strainer"

urlpatterns = [
    path('', views.HousesAPIView.as_view(), name="all_houses"),
    # path('search/', views.SearchView.as_view(), name="search_house"),
    path('<slug:slug>/', views.HouseAPIView.as_view(), name="house_detail"),
]