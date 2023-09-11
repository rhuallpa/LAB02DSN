from django.urls import path
from . import views


urlpatterns = [



    # URLs relacionadas con Persona y Dirección
    path('persona/', views.persona, name='persona'),
    path('registrar_persona/', views.registrar_persona, name='registrar_persona'),
    path('eliminar_persona/<str:id_persona>/', views.eliminar_persona, name='eliminar_persona'),
    path('editar_persona/<str:id_persona>/', views.editar_persona, name='editar_persona'),



    # URLs de autenticación
    path('signup/', views.signup, name='signup'),
    path('home/', views.homes, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
]
