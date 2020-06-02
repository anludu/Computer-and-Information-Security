from .models import Application, User
from .forms import ApplicationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            app = Application(
                name=form.cleaned_data.get('name'),
                secret_password=User.objects.make_random_password(length=12),
                user=request.user
            )
            app.save()
            messages.success(request, 'Se creo una nueva appliación!!')
            return redirect('apps:view_application')
    else:
        form = ApplicationForm
        context = {
            'form': form,
        }
        return render(request, '../templates/apps/create_spass.html', context)


@login_required
def view_applications(request):
    user = Application.objects.get(id=request.user.id)
    applications = Application.objects.filter(user=user).order_by('-id')

    context = {
        'applications': applications,
        'form': Application,
    }

    return render(request, '../templates/apps/view_spass.html', context)
