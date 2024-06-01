from django.shortcuts import render, HttpResponse, redirect
# from home.models import Contact
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
# from blog.models import Post
# Create your views here.
def base(request):
    return render(request,'base.html')
# signup view
def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse('password not match')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        





    return render(request,'signup.html')


# login view 

def Login(request):
    if request.method == 'POST':
        loginUname = request.POST.get('loginUsername')
        loginPass = request.POST.get('loginPassword')
        user = authenticate(username=loginUname, password=loginPass)
        if user is not None:
            login(request, user)
            messages.success(request, 'User successfully logged in')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')  # Redirect back to the login page
    return render(request, 'login.html')


# homepage view
@login_required
def Homepage(request):
    return render(request,'homepage.html')
    # return render(request,'homepage.html')

#base page
@login_required
def PrimaryGroup(request):
    return render(request,'Primary-group.html')

@login_required
def AccountGroup(request):
    return render(request,'Account-group.html')

@login_required
def AccountLedger(request):
    return render(request,'Account-ledger.html')

@login_required
def Customer(request):
    return render(request,'Customer.html')

@login_required
def Supplier(request):
    return render(request,'Supplier.html')

@login_required
def PurchaseOrders(request):
    return render(request,'Purchase-order.html')

@login_required
def PurchaseInvoice(request):
    return render(request,'Purchase-invoice.html')

@login_required
def PurchaseReturn(request):
    return render(request,'Purchase-return.html')

@login_required
def Invoice(request):
    return render(request,'invoice.html')

@login_required
def SaleQuotations(request):
    return render(request,'Sale-quotations.html')

@login_required
def CreateOrder(request):
    return render(request,'Create-orders.html')

@login_required
def CreateQuotation(request):
    return render(request,'Create-quotation.html')

@login_required
def AcceptedOrders(request):
    return render(request,'Accepted-orders.html')

@login_required
def PendingAllocation(request):
    return render(request,'Pending-allocation.html')

@login_required
def AddPayment(request):
    return render(request,'Add-payment.html')

@login_required
def ViewPayment(request):
    return render(request,'View-payment.html')

@login_required
def AddReciept(request):
    return render(request,'Add-reciept.html')

@login_required
def ViewReciept(request):
    return render(request,'View-reciept.html')

@login_required
def GeneralLedger(request):
    return render(request,'General-ledger.html')

@login_required
def GeneralLedger2(request):
    return render(request,'General-ledger2.html')

@login_required
def JournalEntries(request):
    return render(request,'Journal-entries.html')

@login_required
def ProductCreation(request):
    return render(request,'Product-creation.html')

@login_required
def ProductCreation2(request):
    return render(request,'Product-creation2.html')

@login_required
def AddMaterialToPProduct(request):
    return render(request,'Add-material-to-product.html')

@login_required
def BrandandCategory(request):
    return render(request,'Brand-and-category.html')

@login_required
def AddServices(request):
    return render(request,'Add-services.html')

@login_required
def CreateProductStock(request):
    return render(request,'Create-product-stock.html')

@login_required
def CreateMaterialStock(request):
    return render(request,'Create-material-stock.html')

@login_required
def MaterialStockEntries(request):
    return render(request,'Material-stock-entries.html')

@login_required
def ProductStockEntries(request):
    return render(request,'Product-stock-entries.html')

@login_required
def JobList(request):
    return render(request,'Job-list.html')

@login_required
def SalesOrderInformation(request):
    return render(request,'Sales-order-info.html')
