from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin, CreateView
from .forms import ActivateForm, GenerationForm, TransactionForm
from .models import Card, Balance
from .generation import GenerationCards


class CardListView(ListView):
    """List of all cards"""
    model = Card
    paginate_by = 10
    queryset = Card.objects.all()
    context_object_name = 'all_card'
    template_name = 'index.html'


class TransactionListView(ListView):
    """ all receipts for this card """
    model = Balance
    paginate_by = 10
    context_object_name = 'trans_list'
    template_name = 'transaction_list.html'

    def get_queryset(self, *args, **kwargs):
        query = Balance.objects.filter(card__id=self.kwargs['pk'])
        return query


class TransactionCreateView(CreateView):
    """Creating a bank card transaction"""
    model = Balance
    form_class = TransactionForm
    template_name = 'transaction.html'

    def form_valid(self, form):
        card_id = get_object_or_404(Card, id=self.kwargs['pk'])
        form.instance.card = card_id
        return super(TransactionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail-card', kwargs={'pk': self.kwargs['pk']})


class CardDetailView(FormMixin, DetailView):
    """Detailed information on a bank card"""
    model = Card
    form_class = ActivateForm
    context_object_name = 'detail_card'
    template_name = 'detail.html'


class StatusView(UpdateView):
    """Activation and deactivation of a bank card"""
    model = Card
    form_class = ActivateForm
    context_object_name = 'form'
    template_name = 'detail_update.html'

    def get_success_url(self):
        return reverse('detail-card', kwargs={'pk': self.kwargs['pk']})


class CardDeleteView(DeleteView):
    """Removing a bank card"""
    model = Card
    template_name = 'delete_card.html'
    success_url = 'card'

    def get_success_url(self):
        return reverse('card')


class GenerationCardView(CreateView):
    """Generation of bank cards"""
    model = Card
    template_name = 'generation_card.html'
    form_class = GenerationForm

    def post(self, request, *args, **kwargs):
        gen = GenerationCards(request)
        gen.set_up()
        return redirect('/list-card/')

    def get_success_url(self):
        return reverse('card')


class SearchView(ListView):
    """Map search by database model fields"""
    model = Card
    context_object_name = 'result_search'
    template_name = "search.html"

    def get_queryset(self):
        value = self.request.GET.get('q')
        if value:
            result = Card.objects.filter(
                Q(number__contains=value) |
                Q(series__name__contains=value) |
                Q(status__contains=value) |
                Q(start_date__contains=value) |
                Q(end_date__contains=value)
            )
            return result
        return []
