from django.urls import path

from .views import ListCreateTokenView, TotalSupplyView


urlpatterns = [
    path('tokens/create/', CreateTokenView.as_view(), name='create_token'),
    path('tokens/list/', ListTokensView.as_view(), name='tokens_list'),
    path('tokens/total_supply/', TotalSupplyView.as_view(), name='tokens_list'),

]