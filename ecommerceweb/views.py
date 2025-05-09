from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm, UserRegistrationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

@login_required
def product_list(request):
    # Ensure the Customer model has a ForeignKey to the User model
    products = Customer.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user  # Link product to logged-in user
            customer.save()
            return redirect('product_list')  # Correct redirect after form submission
    else:
        form = CustomerForm()
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    # Ensure that the customer belongs to the logged-in user
    customer = get_object_or_404(Customer, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    # Ensure that the customer belongs to the logged-in user
    customer = get_object_or_404(Customer, pk=pk, user=request.user)
    if request.method == 'POST':
        customer.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'customer': customer})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')  # Correct redirect after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
