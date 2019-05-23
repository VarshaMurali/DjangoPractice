from django.shortcuts import render,get_object_or_404
from accountsetup.models import Account
from accountsetup.forms import DepositForm,WithdrawForm
from django.views.generic import ListView,View
from django.http import HttpResponse
from accountsetup.mixins import SerializeMixin
import json
# Create your views here.
def index(request):
    my_dict={'insert_me':'Varsha',}
    return render(request,'accountsetup/home.html',context=my_dict)

class AccountList(ListView):
    context_object_name='accountlist'
    model=Account
    template_name='accountsetup/accountlist.html'

def depositamount(request,pk):
    acc = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form=DepositForm(request.POST,instance=acc)
        if form.is_valid():
            acc = form.save(commit=False)
            acc.balance=acc.balance+acc.amount
            acc.save()
            return render(request,'accountsetup/home.html',context={'insert_me':'Your transaction is complete',})
    else:
        form=DepositForm(instance=acc)
    return render(request,'accountsetup/deposit.html',{'form': form})

def withdrawamount(request,pk):
    acc=get_object_or_404(Account,pk=pk)
    if request.method == 'POST':
        form=WithdrawForm(request.POST,instance=acc)
        if form.is_valid():
            acc=form.save(commit=False)
            acc.balance=acc.balance-acc.amount
            acc.save()
            return render(request,'accountsetup/home.html',context={'insert_me':'Your transaction is complete',})
    else:
        form=WithdrawForm(instance=acc)
    return render(request,'accountsetup/withdraw.html',{'form': form})

class AccountApi(SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        acct=Account.objects.all()
        json_data=self.serialize(acct)
        return HttpResponse(json_data,status=205)

class Accountdetail(SerializeMixin,View):
    def get(request,id,*args,**kwargs):
        try:
            acct=Account.objects.get(id=id)
        except acct.DoesNotExist:
            json_data=json.dumps({'msg':'The account number is not valid'})
        else:
            json_data=self.serialize([acct,])
        return HttpResponse(json_data,status=205)
