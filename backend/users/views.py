from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm

from .models import Profile


@login_required
def profile(request):

    profile = Profile.objects.get(
        user=request.user
    )

    context = {
        'profile': profile,
        'tickets_count': request.user.tickets.count()
    }

    return render(
        request,
        'users/profile.html',
        context
    )

@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return redirect('profile')

    else:

        form = ProfileForm(
            instance=profile
        )

    context = {
        'form': form
    }

    return render(
        request,
        'users/edit_profile.html',
        context
    )

