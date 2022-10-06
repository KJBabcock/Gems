from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('gems/', views.GemList.as_view(), name="gem_list"),
    path('gems/new/', views.GemCreate.as_view(), name="gem_create"),
    path('gems/<int:pk>/', views.GemDetail.as_view(), name="gem_detail"),
    path('gems/<int:pk>/update',views.GemUpdate.as_view(), name="gem_update"),
    path('gems/<int:pk>/delete',views.GemDelete.as_view(), name="gem_delete"),
    path('gems/<int:pk>/attributes/new/', views.AttributeCreate.as_view(), name="attribute_create"),
    path('chains/<int:pk>/attributes/<int:attribute_pk>/', views.ChainAttributeAssoc.as_view(), name="chain_attribute_assoc"),
]