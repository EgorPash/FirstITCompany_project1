from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'dds/transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'dds/transaction_form.html', {'form': form})

def transaction_edit(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'dds/transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect('transaction_list')
