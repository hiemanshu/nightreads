from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import SubscribeForm
from . import user_service


class SubscribeView(View):
    form_class = SubscribeForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SubscribeView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            tags = form.cleaned_data['tags']
            user = user_service.get_user(email=email)
            user_service.update_user_tags(user=user, tags=tags)
            return JsonResponse({'success': True})