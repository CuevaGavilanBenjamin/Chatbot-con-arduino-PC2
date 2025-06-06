from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('grafico/', views.grafico_humedad, name='grafico_humedad'),
    path('grafico_clasificacion/', views.grafico_clasificacion_humedad, name='grafico_clasificacion_humedad'),
    path('api/estadisticas/', views.estadisticas_humedad, name='api_estadisticas_humedad'), #benjamin
    path('estadisticas/', views.pagina_estadisticas, name='pagina_estadisticas'),#benjamin
    path('dashboard_estadisticas/', views.dashboard_estadisticas, name='estadisticas_humedad'), 

]
