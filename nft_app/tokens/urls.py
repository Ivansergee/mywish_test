from django.urls import path

from .views import CreateTokenView, TotalSupplyView, ListTokenView


urlpatterns = [
    path('tokens/create/', CreateTokenView.as_view(), name='create_token'),
    path('tokens/list/', ListTokenView.as_view(), name='tokens_list'),
    path('tokens/total_supply/', TotalSupplyView.as_view(), name='tokens_list'),
]
