from django.shortcuts import (render, get_object_or_404, redirect,)
from .models import PizzeriaLocal, Pizza, Topping
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .forms import RestaurantModelForm
from django.urls import reverse_lazy


class IndexRestaurantsView(ListView):
    template_name = 'pizzeria/index.html'
    context_object_name = 'locals'
    paginated_by = 10
    model = PizzeriaLocal

    def get_queryset(self):
        return PizzeriaLocal.objects.all().order_by('name')


class RestaurantDetailView(DetailView):
    template_name = 'pizzeria/restaurant_detail.html'
    # context_object_name = 'local'
    # model = PizzeriaLocal

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(PizzeriaLocal, id=id_)


class MenuRestaurantDetailView(DetailView):
    template_name = 'pizzeria/menu_restaurant_detail.html'
    model = PizzeriaLocal

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(PizzeriaLocal, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu = get_object_or_404(PizzeriaLocal, id=self.kwargs.get("id"))
        menu = menu.pizza_set.all()
        print(menu)
        print('a to juz sam lokal z context obj name', context['object'])
        context['menu'] = menu
        print(context)
        return context


class CreateRestaurantView(CreateView):
    template_name = 'pizzeria/create_restaurant.html'
    form_class = RestaurantModelForm
    queryset = PizzeriaLocal.objects.all()
    success_url = reverse_lazy('pizzeria:index')

    def form_valid(self, form):
        print('to jest cleaned data \n', form.cleaned_data)
        return super().form_valid(form)











