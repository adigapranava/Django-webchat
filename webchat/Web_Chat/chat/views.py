from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Messages
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
from django.core import serializers
from datetime import datetime, timedelta
from django.utils import timezone

def home(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'chat/index.htm', context)

def chat(request, pk):
    if request.user.is_authenticated:
        try:
            if request.method == "POST":
                touser = User.objects.get(id=pk)
                msg = Messages(msg_from = request.user, msg_to=touser, msg_text = request.POST['chat-msg'])
                msg.save()
                return redirect('chat-page', pk)
            context = {
                'users': User.objects.all(),
                'touser': User.objects.get(id=pk)
            }
        except:
            return HttpResponseNotFound()
        
        return render(request, 'chat/chatwith.html', context)
    else:
        return redirect('login')

def chat_messages(request, pk):
    if request.user.is_authenticated:
        try:
            touser = User.objects.get(id=pk)
            messages = Messages.objects.filter(Q(msg_from = request.user, msg_to=touser)|Q(msg_from = touser, msg_to = request.user))
            messages= messages.order_by('date_postdate')
            response = serializers.serialize('json', messages)
        except:
            response = serializers.serialize('json', [])        
        return HttpResponse(response, content_type='application/json')
    else:
        response = serializers.serialize('json', {})
        return HttpResponse(response, content_type='application/json')

def latest_chat_messages(request, pk):
    if request.user.is_authenticated:
        try:
            touser = User.objects.get(id=pk)
            time_threshold = datetime.now() - timedelta(minutes=1)
            messages = Messages.objects.filter(date_postdate__gt=time_threshold)
            messages = messages.filter(Q(msg_from = request.user, msg_to=touser)|Q(msg_from = touser, msg_to = request.user))            
            messages= messages.order_by('date_postdate')
            response = serializers.serialize('json', messages)
        except:
            response = serializers.serialize('json', [])        
        return HttpResponse(response, content_type='application/json')
    else:
        response = serializers.serialize('json', {})
        return HttpResponse(response, content_type='application/json')