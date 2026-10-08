from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from event_app.models import*


def register_page(request):
    if request.method =='POST':
        username = request.POST.get ('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        
        user_exist = EventUserModel.objects.filter(username = username).exists()
        if user_exist:
            messages.warning(request, 'User already exists.')
            return redirect('register_page')
        

        if password == conf_password:
            EventUserModel.objects.create_user(
                username = username,
                password = password,
                email = email,
                full_name = full_name,
                phone = phone,
            )
            messages.success(request, 'User created successfully')
        else:
            messages.warning(request, 'Password doesnot match.')
            return redirect(login_page)  
    return render(request, 'auth/register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, 'User login successfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('login_page')

    return render(request, 'auth/login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required
def dashboard(request):

    events = EventModel.objects.all()
    search = request.GET.get('search', '')

    if search:
        events = events.filter(
            Q(event_title__icontains=search) |
            Q(event_type__icontains=search) |
            Q(location__icontains=search)
        )

    context = {
        'events': events,
        'search': search,
    }
    return render(request,'pages/dashboard.html',context)

@login_required
def event_page(request):

    events = EventModel.objects.filter(user=request.user)
    status = request.GET.get('status', '')

    if status:
        events = events.filter(status=status)

    context = {
        'events': events,
        'status': status,
    }
    return render(request,'pages/event_page.html',context)

@login_required
def event_details(request, e_id):
    event = get_object_or_404(EventModel,id=e_id)
    
    context = {
        'event': event
    }
    return render(request,'pages/event_details.html',context)



@login_required
def event_create(request):

    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_type = request.POST.get('event_type')
        event_description = request.POST.get('event_description')
        event_date = request.POST.get('event_date')
        status = request.POST.get('status')
        location = request.POST.get('location')

        EventModel.objects.create(
            user=request.user,
            event_title=event_title,
            event_type=event_type,
            event_description=event_description,
            event_date=event_date,
            status=status,
            location=location,
        )
        messages.success(request, 'Event Create successfully')
        return redirect('event_page')
    return render(request, 'pages/event_create.html')


def event_update(request,e_id):
    
    event_data = EventModel.objects.get(id = e_id)
    if request.method == 'POST':
        event_title = request.POST.get ('event_title')
        event_type = request.POST.get ('event_type')
        event_description = request.POST.get ('event_description')
        event_date = request.POST.get ('event_date')
        status = request.POST.get ('status')
        location = request.POST.get ('location')

        event_data.event_title = event_title
        event_data.event_type = event_type
        event_data.event_description = event_description
        event_data.event_date = event_date
        event_data.status = status
        event_data.location = location
        event_data.save()
        messages.success(request, 'Event Update successfully')
        return redirect('event_page')
    
    context ={
        'event_data':event_data
    }
    return render(request ,'pages/event_update.html',context)


def event_delete(request,e_id):
    
    EventModel.objects.get(id = e_id).delete()
    messages.success(request,'Event deleted successfully.')
    
    return redirect('my_events')




