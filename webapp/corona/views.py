from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Invitation, Memory


class IndexView(TemplateView):
    template_name = 'corona/index.html'

class EventView(TemplateView):
    template_name = 'corona/event.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'corona/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invitations = Invitation.objects.filter(user=self.request.user).select_related('event')
        context['events'] = {e.event:{} for e in invitations}
        for inv in invitations:
            context['events'][inv.event]['images'] = Memory.objects.filter(event=inv.event)
            context['events'][inv.event]['people'] = Invitation.objects.filter(event=inv.event).select_related('user').exclude(user=self.request.user)
        return context