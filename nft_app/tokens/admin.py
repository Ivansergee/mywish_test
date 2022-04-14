from django.contrib import admin

from .models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ['unique_hash', 'tx_hash', 'media_url', 'owner']


admin.site.register(Token, TokenAdmin)
