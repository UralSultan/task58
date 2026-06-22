from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Task, Project
from .forms import TaskModelForm, ProjectModelForm


class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        projects = Project.objects.all()
        query = self.request.GET.get('q')
        if query:
            projects = projects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.filter(is_deleted=False)
        return context


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectModelForm
    template_name = 'project_create.html'
    success_url = reverse_lazy('index')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectModelForm
    template_name = 'project_update.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('index')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(is_deleted=False)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'task_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['project_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.project.pk})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'task_update.html'

    def get_queryset(self):
        return Task.objects.filter(is_deleted=False)

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'

    def get_queryset(self):
        return Task.objects.filter(is_deleted=False)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})

    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())
