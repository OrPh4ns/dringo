from django.urls import path

from emergency import views

urlpatterns = [
    path('notfalls', views.get_emergs, name='notfalls'),
    path('neuer_notfall', views.new_emerg, name='neuer_notfall'),
    # path('info', views.get_info, name='info'),
]
