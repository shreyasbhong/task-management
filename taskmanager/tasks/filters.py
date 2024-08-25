import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Task.status_choices)
    priority = django_filters.ChoiceFilter(choices=Task.priority_choices)
    due_date = django_filters.DateFilter(lookup_expr='exact')

    class Meta:
        model = Task
        fields = ['status', 'priority', 'due_date']
