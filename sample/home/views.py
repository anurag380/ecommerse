from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages,auth
from . forms import Register,Productform
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProductFilter
import json
from urllib.parse import urlencode


# Create your views here.

def home(request):
    # return HttpResponse("WELCOME TO DJANGO")
    if request.user.username != '':
        if Order.objects.filter(customer__user = request.user, status = 'Pending').exists():
            order = Order.objects.get(customer__user = request.user, status = 'Pending')
            count = order.get_cart_items
        else:
            count = 0
    else:
        count = 0


    product_list = Products.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list, )
    # return render(request, 'home.html', {'filter': product_filter})

    product_list = Products.objects.all()
    paginator = Paginator(product_filter.qs, 2)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        paginator = paginator.page(page_number)
    except PageNotAnInteger:
        paginator = paginator.page(1)

    # except EmptyPage:
    #     paginator = paginator.page(paginator.num_pages)

    category = Category.objects.all()
    tag = Tag.objects.all()


    products = { 
        'products' : paginator,
        'count' : count,
        'page_obj' : page_obj,
        'category' : category,
        'tag' : tag,
        'filter': product_filter
        }
    return render(request,'home.html', products)
    

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['name']
#         email = request.POST['email']
#         phno = request.POST['phno']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if Customer.objects.filter(email = email).exists():
#                 messages.info(request,"E-mail already taken") 
#                 return redirect('signup')
#             else:
#                 customer = Customer.objects.create(name=username,email=email,phno=phno,password=password1)
#                 customer.save()
#                 messages.info(request, "User created")
#                 return redirect('signin')
#         else: 
#             messages.info(request,"Passwod is not match") 
#             return redirect('signup')
#     else:
#         return render(request,'signup.html')



def signup(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "User created")
            return ('signin')
    form = { 'form' : form }
    return render(request, 'signup.html', form)



# def signin(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         try :
#             check_user = Customer.objects.get(email=email, password=password)
#             request.session['email'] = check_user.email
#             request.session['password'] = check_user.password
#             return redirect('home')
#         except Customer.DoesNotExist:
#             messages.error(request, "Invalid User..!")
#             return render(request,'signin.html')
#     else:
#         return render(request, 'signin.html')


def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username = name, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid User name or Password')
    return render(request, 'signin.html')

 

def logout(request):
    auth.logout(request)
    return redirect('home')


# def forgot(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         if Customer.objects.filter(name=name).exists():
#             if password1 == password2:
#                 Customer.objects.filter(name=name).update(password=password1)
#                 return redirect('signin')
#             else:
#                 messages.error(request, "Password didn't match")
#                 return redirect('forgot')
#         else:
#             messages.error(request, "User name does not exist")
#             return render(request,'forgot.html')
#     return render(request,'forgot.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        if name is not None and phno is not None:
            cont = Contact.objects.create(name=name, email=email, phno=phno)
            cont.save()
            val_pass = {
                'name' : name,
                'output' : 1 
            }
        return render(request,'contact.html', val_pass)
    else:
        return render(request,'contact.html')


def add_cart(request):
    if request.user.username is not None:
        pro = request.GET['p']
        item = Products.objects.get(id = pro)
        print(item)

        name=request.user.username
        user = Customer.objects.get(name=name)
        print(user)
        
        # user_id = user.id
        # print(user_id)

        # try:
        #     order = Order.objects.get(customer = user )
        #     if (order.status == 'Pe'):
        #         order = Order.objects.get(customer = user )
        #     else:
        #         pass
        # except : 
        #     order = Order(customer = user )
        #     order.save()
        # print(order)

        if Order.objects.filter(customer = user, status = 'Pending').exists() :
            print("iugucwiufhwieuhfiwunfefrghjkl")
            # a = Order.objects.get(customer = user, status = 'Pending' )
            # if a.status == 'Pending':
            order = Order.objects.get(customer = user, status = 'Pending' )
            # else:
            #     order = Order.objects.create(customer = user )
        else:
            order = Order.objects.create(customer = user )
            order.save()
        order.save()

        # prod = Orderline.objects.filter(product = item).exists()
        print('.................')
        if ( Orderline.objects.filter(product = item, is_order = False).exists() ):
            # orderline = Orderline.objects.get(product = item)

            # print('***************************8')
            # orderline.quantity += 1
            # print(orderline.quantity)
            # orderline.total = orderline.unit_price * orderline.quantity
            # orderline.save()
            # order.amount += orderline.total
            # order.save()
            # print(order.amount)
            pass
            print("here....")
            print(Orderline.objects.filter(product = item, is_order = False))
        else:
            orderline = Orderline()

            orderline.order = order
            orderline.product = item
            orderline.unit_price = item.price
            orderline.total = orderline.unit_price * orderline.quantity
            orderline.save()
            order.amount += orderline.total
            order.save()
            print(order.amount)
        
        url = request.META.get('HTTP_REFERER')
        return redirect(url)
    else:
        return render(request,'home.html')


def cart(request):
    user = request.user

    # order = Order.objects.get(customer = user)
    # try:
    #     order = Order.objects.get(customer = user )
    # except : 
    #     order = Order(customer = user )
    #     order.save()
    # print(order )

    # ord = Orderline.objects.get(order = order)
    # orderline = Orderline()

    items = Orderline.objects.filter(order__customer__user=user, is_order = False)
    # items = Orderline.objects.all()
    products = { 'products' : items }
    return render(request, 'cart.html' ,products)

def remove(request):
    # if request.user.username is not None:
        pro = request.GET['p']
        item = Orderline.objects.get(id = pro)

        # name=request.user.username
        # user = Customer.objects.get(name=name)
       
        # user.products.remove(cart)
        # Orderline.objects.get(product = item)
        name=request.user.username
        user = Customer.objects.get(name=name)
        order = Order.objects.get(customer = user, status = 'Pending' )
        order.amount -= item.total
        item.delete()
        order.save()

        return redirect('cart')
    # else:
        # return render(request,'cart.html')

def empty(request):
    return render(request, 'cart.html')

def itemadd(request):
    name=request.user.username
    user = Customer.objects.get(name=name)
    order = Order.objects.get(customer = user, status = 'Pending' )
    pro = request.GET['p']
    item = Orderline.objects.get(id = pro)
    qty = request.GET['q']
    if item.quantity < int(qty):
        order.amount += item.unit_price
    else:
        order.amount -= item.unit_price
    order.save()
    item.quantity = qty 
    item.total = item.unit_price * int(qty)
    item.save()
    # order.amount += item.total
    # order.save()
    # print(order.amount)
    data = {
            'total' : item.total,
            'amount' : order.amount
        }
    # print(data)
    return JsonResponse(data)
    # print("*****helloword")
    # print(request.GET['p'])
    # print(request.GET['q'])
    # print(request.GET['qty'])
    # return redirect('cart')

def itemremove(request):
    pro = request.GET['p']
    item = Orderline.objects.get(id = pro)
    item.quantity -= 1
    item.total = item.unit_price * item.quantity
    item.save()
    return redirect('cart')


def checkout(request):
    name=request.user.username
    user = Customer.objects.get(name=name)
    print(user)

    for i in Order.objects.filter(customer = user):
        
        if i.status == 'Ordered':
            pass
        elif i.status == 'Pending':
            order = Orderline.objects.filter(order=i.id)
            for qr in order:
                print(qr.is_order)
                qr.is_order=True
                print(qr.is_order)
                qr.save()
            # print(order[0])
            # order.is_order=True
            # order.save()
            i.status = 'Ordered'
            # user = request.user
            # Orderline.objects.filter(order__customer__user=user).delete()
            # order = Orderline.objects.get(order__customer__user=user, order__status='Pending')
            # print(order.is_order)
            i.save()



    # order = Order.objects.get(customer = user )
    # order.status = 'or'
    # user = request.user
    # Orderline.objects.filter(order__customer__user=user).delete()
    # order.save()
    # print(order)
    return render(request, 'checkout.html')

def edit(request):
    form = Productform()
    pr_id = request.GET['p']
    item = Products.objects.get(id = pr_id)
    # old_price = old_name.price
    # # old_image = old_name.image
    # # 'image' : old_image
    # print(old_name)
    # print(old_price)
    form = Productform(instance=item)
    if request.method == 'POST':
        form = Productform(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Updated")
            return redirect('home')
    form = { 'form' : form }
    return render(request, 'edit.html', form)
    

def delete(request):
    if request.user.is_superuser:
        pr_id = request.GET['p']
        Products.objects.get(id=pr_id).delete()
        messages.success(request, "Product Removed")
        return redirect('home')
    else:
        messages.success(request, "You don't have permission to delete..!")
        return redirect('home')

def make(request):
    form = Productform()
    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Products.objects.create(request.POST,request.FILES)
            messages.info(request, "Product created")
            return redirect('home')
    form = { 'form' : form }
    return render(request, 'edit.html', form)


def myorders(request):
    name=request.user.username
    user = Customer.objects.get(name=name)
    order = Order.objects.filter(customer__name = user, status = 'Ordered')
    print(order)
    form = { 'form' : order }
    return render(request, 'myorders.html', form)


def showorder(request,id):
    print(id)
    order = Order.objects.get(id = id)
    items = Orderline.objects.filter(order=order)
    # items = Orderline.objects.all()
    products = { 'products' : items }
    return render(request, 'showorder.html' ,products)


def search(request):

    prod = json.loads(request.GET['data'])

    print(prod)
    category = prod.get('category')
    tag = prod.get('tag')
    name = prod.get('name')

    product_list = Products.objects.all()
   
    product_filter = ProductFilter({"category":category, "tag":tag , 'name':name}, queryset=product_list, )
   
    product_list = Products.objects.all()
    paginator = Paginator(product_filter.qs, 2) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        paginator = paginator.page(page_number)
    except PageNotAnInteger:
        paginator = paginator.page(1)

    category = Category.objects.all()
    tag = Tag.objects.all()

    url = urlencode(prod).replace('%5B%27','')
    url = url.replace('%27%5D','')
    url = url.replace('%27%2C+%27','&tag=')


    products = { 
        'products' : paginator,
        'page_obj' : page_obj,
        'category' : category,
        'tag' : tag,
        'filter': product_filter,
        "url" : url
        }
    return render(request,'products.html', products)