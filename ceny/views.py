from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Ceny
from .forms import AddCenyForm
from django.views.generic import DeleteView

# Create your views here.
def home_view(request):
    no_discounted = 0
    error = None
    
    form = AddCenyForm(request.POST or None)
    
    if request.method == 'POST':
        try: 
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "There is no name or price"
        except Exception as e:
            error = f"Unexpected error happened: {e}"
    
    form = AddCenyForm()
    
    quse = Ceny.objects.all()
    items_no = quse.count()
    
    if items_no > 0:
        discount_list = []
        for item in quse:
            if item.old_price > item.now_price:
                discount_list.append(item)
            no_discounted = len(discount_list)
            
    context = {
        'quse': quse,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
    }
    
    return render(request, 'ceny/main.html', context)

class CenyDeleteView(DeleteView):
    model = Ceny
    template_name = 'ceny/confirm_del.html'
    success_url = reverse_lazy('home')
    
def update_prices(request):
    quse = Ceny.objects.all()
    for link in quse:
        link.save()
    return redirect('home')       
    