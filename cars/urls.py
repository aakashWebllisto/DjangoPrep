from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.CarListView.as_view(), name='all'),
    path('cars/<int:pk>/detail', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
]