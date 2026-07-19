from django.shortcuts import render, redirect, get_object_or_404
from .models import Tache


def liste_taches(request):
    if request.method == "POST":
        titre = request.POST.get("titre")
        if titre:
            Tache.objects.create(titre=titre)
        return redirect("liste_taches")

    taches = Tache.objects.all().order_by("-date_creation")
    return render(request, "taches/liste.html", {"taches": taches})


def terminer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    tache.marquer_terminee()
    return redirect("liste_taches")


def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    tache.delete()
    return redirect("liste_taches")
