from django.urls import path
from . import views

urlpatterns = [
    path("", views.liste_taches, name="liste_taches"),
    path("terminer/<int:tache_id>/", views.terminer_tache, name="terminer_tache"),
    path("supprimer/<int:tache_id>/", views.supprimer_tache, name="supprimer_tache"),
]
