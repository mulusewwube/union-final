from django.contrib import admin
from .models import Message
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()
class MessageAdmin1(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'read')
    list_filter = ('sender', 'receiver', 'read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    ordering = ('-timestamp',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sender=request.user) | qs.filter(receiver=request.user)

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('sender', 'receiver', 'content', 'timestamp', 'read')
        return ('receiver', 'content', 'timestamp', 'read')

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ('sender', 'receiver', 'read', 'timestamp')
        return ('receiver', 'read', 'timestamp')

    def get_search_fields(self, request):
        if request.user.is_superuser:
            return ('sender__username', 'receiver__username', 'content')
        return ('receiver__username', 'content')

    def changelist_view(self, request, extra_context=None):
        # Filter messages to only show conversations between admin and selected user
        if request.user.is_superuser and 'user_id' in request.GET:
            user_id = request.GET['user_id']
            try:
                user = User.objects.get(pk=user_id)
                extra_context = extra_context or {}
                extra_context['title'] = f'Chat with {user.username}'
                self.queryset = self.queryset.filter(
                    (Q(sender=user) & Q(receiver=request.user)) |
                    (Q(receiver=user) & Q(sender=request.user))
                )
            except User.DoesNotExist:
                pass
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Message, MessageAdmin1)
