from django.shortcuts import (render, get_object_or_404, redirect,)
from django.urls import reverse_lazy
from .models import Order, OrderedPizza, Payment
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .forms import OrderModelForm
from .calculation_utils import calculate_sum_all_products_in_order
# from pizzeria import models


class OrderedPizzaView(DetailView):
    template_name = 'order_system/ordered_pizzas_list.html'
    context_object_name = 'pizzas'
    paginated_by = 15
    model = OrderedPizza
    #  tu trzeba przechwycic numer id order i wyswietlic dla niego wszystkie pizze

    def get_queryset(self):
        pass
        # OrderedPizza.objects.filter(order__pk=id)
        # Order.objects.get(id=4).ordered_pizza_set.all()
        # return OrderedPizza.objects.filter().order_by('name')  tu trzeba napisać query, które zwroci dla konkretnego
        # nr obiektu order te pizze zamowione dla tego zamowienia tylko


class CreateOrderView(CreateView):
    template_name = 'order_system/create_order.html'
    form_class = OrderModelForm
    # queryset = Order.objects.all()
    success_url = reverse_lazy('order_system:order-successed')
    # where will be save line to create finally order then it should after that execute function
    # calculate_total_price_products_order(order1.orderedpizza_set.all())
    # and after that use method  order.set_total( tutaj_podaj_wynik_funkcji)

    def form_valid(self, form):
        print('to jest cleaned data \n', form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_dict = {}
        form_dict.update(
            total=0,
        )
        context['form'] = OrderModelForm(initial=form_dict)
        return context


class OrderSuccessView(TemplateView):
    template_name = 'order_system/order_success.html'


class IndexOrderView(ListView):
    template_name = 'order_system/index.html'


class OrderDetailView(DetailView):
    template_name = 'order_system/order_detail.html'
    context_object_name = 'order'
    paginated_by = 15
    model = Order

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Order, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("id")
        current_order = get_object_or_404(Order, id=id_)
        products_in_order = current_order.orderedpizza_set.all()
        context['products_in_order'] = products_in_order
        context['total'] = calculate_sum_all_products_in_order(products_in_order)
        return context


class CreateOrderedProductView(CreateView):
    # orderedpizza2 = OrderedPizza(pizza_name=pizza2.name, amount=3, price=pizza2.price, order=order1)
    pass


class CreatePaymentView(CreateView):
    pass
    # payment1.get_payment_confirm()


