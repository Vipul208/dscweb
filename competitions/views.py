from django.shortcuts import get_object_or_404, render
from .models import Competition


# Create your views here.
def home_view(request):
    competitions = Competition.objects.all()
    context = {
        "competitions": competitions,
    }
    template_name = 'competitions/home.html'
    return render(request, template_name, context)


def competition_view(request, slug):
    competition = get_object_or_404(Competition, slug=slug)
    template_name = 'competitions/detail.html'
    context = {"competition": competition}
    return render(request, template_name, context)
