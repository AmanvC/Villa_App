from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.VillaListView.as_view(), name='list'),
    path('<int:pk>/', views.VillaDetailView.as_view(), name='detail'),
    path('create_villa', views.VillaCreateView.as_view(), name='create_villa'),
    path('create_owner', views.OwnerCreateView.as_view(), name='create_owner'),
    path('update/<int:pk>/', views.OwnerUpdateView.as_view(), name='update_owner'),
    path('delete/<int:pk>/', views.OwnerDeleteView.as_view(), name='delete_owner'),

]
