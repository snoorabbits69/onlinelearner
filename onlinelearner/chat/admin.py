from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
 list_display = ['sent_on', 'course', 'content']
 list_filter = ['sent_on', 'course']
 search_fields = ['content']
 raw_id_fields = ['user', 'course'] 
 list_filter = ['sent_on', 'course']
 search_fields = ['content']
 raw_id_fields = ['user', 'course']