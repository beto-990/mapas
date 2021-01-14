from django.shortcuts import render
from .models import Estado
# Create your views here.


def post_list(request):
    estados = Estado.objects.filter(sigla='SC').order_by('pop')
    return render(request, 'mapito/post_list.html', {'estados': estados})