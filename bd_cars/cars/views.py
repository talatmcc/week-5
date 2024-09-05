from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.utils.decorators import method_decorator
from .models import Brand, Car, Purchase, Comment
from .forms import ProfileForm

class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        brand_id = self.request.GET.get('brand_id')
        if brand_id:
            return Car.objects.filter(brand_id=brand_id)
        return Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()  # Add all brands to the context
        return context


class CarListView(ListView):
    template_name = 'car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        brand_id = self.kwargs['brand_id']
        return Car.objects.filter(brand_id=brand_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = get_object_or_404(Brand, id=self.kwargs['brand_id'])
        context['brands'] = Brand.objects.all()
        return context

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('car_detail', pk=car.pk)
        return self.get(request, *args, **kwargs, form=form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(car=self.get_object())
        return context

@method_decorator(login_required, name='dispatch')
class PurchaseView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            Purchase.objects.create(user=request.user, car=car)
            return redirect('profile')
        return redirect('car_detail', pk=pk)

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchases'] = Purchase.objects.filter(user=self.request.user)
        return context


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})