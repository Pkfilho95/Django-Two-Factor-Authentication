from django.shortcuts import redirect
from django.conf import settings
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model

from .forms import TwoFactorAuthForm

USER_MODEL = get_user_model()

class AuthView(FormView):
    """
    First authentication view.
    """
    
    template_name = 'auth.html'
    form_class = AuthenticationForm
    success_url = '/verify/'

    def form_valid(self, form):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        user = authenticate(request=self.request, username=username, password=password)
        
        self.request.session['id'] = user.id
        
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):

        # Redirect to LOGIN_REDIRECT_URL if user is authenticated
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        
        return super().dispatch(request, *args, **kwargs)

class TwoAuthView(FormView):
    """
    Second authentication view.
    """

    template_name = 'two_auth.html'
    form_class = TwoFactorAuthForm
    success_url = settings.LOGIN_REDIRECT_URL

    def get(self, request, *args, **kwargs):
        user = USER_MODEL.objects.get(id=self.request.session.get('id'))
        user_token = user.twofactorauthmodel

        # Update the token
        user_token.save()

        # Put here the code that will send the token to the user
        # I put print just for test and show the token
        print(f'Token: {user_token.token}')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = USER_MODEL.objects.get(id=self.request.session.get('id'))
        user_token = user.twofactorauthmodel.token

        token = form.cleaned_data.get('token')

        if token == user_token:
            login(request=self.request, user=user)
        
        else:
            logout(request=self.request)
            return redirect('/')
        
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):

        # Return to login page
        if not self.request.session.get('id'):
            return redirect('/')

        # Redirect to success_url if user is authenticated
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        
        return super().dispatch(request, *args, **kwargs)