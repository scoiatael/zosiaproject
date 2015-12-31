from django.shortcuts import render_to_response, HttpResponse
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
    return render_to_response('bye.html', locals())


@login_required
def password_change(request):
    user = request.user
    title = "Change password"
    pc_form = ValidatedPasswordChangeForm(request.user, request.POST or None)
    if pc_form.is_valid():
        pc_form.save()
        return HttpResponseRedirect("done/")
    return render_to_response("change_password.html", locals())

@login_required
def password_change_done(request):
    user = request.user
    title = "Change password"
    return render_to_response("change_password_done.html", locals())

