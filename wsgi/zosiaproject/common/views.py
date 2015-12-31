from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .forms import *

from users.models import Participant

def thanks(request):
    user = request.user
    title = "Bye!"
    login_form = LoginForm()
    return render(request, 'bye.html', locals())


@login_required
def password_change(request):
    user = request.user
    title = "Change password"
    pc_form = ValidatedPasswordChangeForm(request.user, request.POST or None)
    if pc_form.is_valid():
        pc_form.save()
        return HttpResponseRedirect("done/")
    return render(request, "change_password.html", locals())

@login_required
def password_change_done(request):
    user = request.user
    title = "Change password"
    return render(request, "change_password_done.html", locals())

