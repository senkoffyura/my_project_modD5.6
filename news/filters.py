from django_filters import FilterSet,  DateTimeFilter
from django.forms import DateTimeInput
from .models import Post

class PostFilter(FilterSet):

    added_after = DateTimeFilter(
        field_name='time_creates',
        lookup_expr='gt',
        label='Поиск публикации после указанной даты',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},

        ),
    )

    class Meta:
        model = Post
        fields = {
           'heading': ['icontains'],
           'category': ['exact'],
       }
