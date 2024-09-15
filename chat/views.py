from django.shortcuts import render,redirect
from .models import Message
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.models import User


@login_required(login_url='user:login')
def check_unread_messages(request):
    unread_count = Message.objects.filter(receiver=request.user, read=False).count()
    return JsonResponse({'unread_count': unread_count})

@login_required(login_url='user:login')
def load_previous_chats(request):
    admin_user_id = 3  # Replace with actual admin user ID
    messages = Message.objects.filter(
        sender__id__in=[request.user.id, admin_user_id],
        receiver__id__in=[request.user.id, admin_user_id]
    ).order_by('timestamp')

    # Mark messages as read
    Message.objects.filter(receiver=request.user, read=False).update(read=True)
    return render(request, 'chat/previous_chats.html', {'messages': messages, 'user': request.user})

@csrf_exempt
@login_required(login_url='user:login')
def send_message(request):
    if request.method == "POST":
        content = request.POST.get('content')
        admin_user_id = 3  # Replace with actual admin user ID
        admin_user = User.objects.get(id=admin_user_id)
        if content:
        # Create a new message
            Message.objects.create(
                sender=request.user,
                receiver=admin_user,
                content=content,
                timestamp=timezone.now()
            )
        return redirect('order:profile')
    return redirect('order:profile')