from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
        # Home page:
        path('', views.index, name='index'),
        path('pizzas/', views.pizzas, name='pizza_names'),

        # Details page for a single pizza:
        path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
        ]
