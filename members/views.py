from django.shortcuts import render
from .models import Member, Subs

# Create your views here.

def view_member(request):
    """ A view that renders the members page """

    return render(request, 'members/members.html')