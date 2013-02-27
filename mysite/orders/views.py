# Create your views here.
from django.template import Context, loader, RequestContext
from orders.models import Order, OrderForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
# from orders.forms import OrderCreateForm

def index(request):
    return render_to_response('orders/index.html')

def new_prescription(request):
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
        else:
            return render_to_response('orders/new.html', {
            'form': form, },context_instance=RequestContext(request))
        return render_to_response('orders/index.html') # Redirect after POST
    else:
        form = OrderForm() # An unbound form
    
    return render_to_response('orders/new.html', {
            'form': form, },context_instance=RequestContext(request))
