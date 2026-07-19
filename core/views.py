from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Task


class TaskListView(View):
    """Affiche la liste des taches et gere la creation."""

    template_name = "core/task_list.html"

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {"tasks": tasks})

    def post(self, request):
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
            messages.success(request, "Tache ajoutee.")
        else:
            messages.error(request, "Le titre est obligatoire.")
        return redirect("task_list")


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("task_list")
