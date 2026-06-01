from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Profile


@login_required
def profile(request):

    profile = Profile.objects.get(
        user=request.user
    )

    context = {
        'profile': profile
    }

    return render(
        request,
        'users/profile.html',
        context
    )