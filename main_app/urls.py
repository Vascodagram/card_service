from django.urls import path
from .views import CardListView, CardDetailView, StatusView, \
    CardDeleteView, GenerationCardView, SearchView, \
    TransactionCreateView, TransactionListView

urlpatterns = [
    path('generation-card/', GenerationCardView.as_view(), name='generation-card'),
    path('list-card/', CardListView.as_view(), name='card'),
    path('card/<int:pk>/list-transaction/', TransactionListView.as_view(), name='list-transaction'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='detail-card'),
    path('card/<int:pk>/transaction/', TransactionCreateView.as_view(), name='transaction'),
    path('card/<int:pk>/edit/', StatusView.as_view(), name='edit'),
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='delete'),
    path('search/', SearchView.as_view(), name='search')

]