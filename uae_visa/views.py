from django.shortcuts import get_object_or_404, render,  redirect
from django.core.paginator import Paginator
from uae_visa.forms import *
from uae_visa.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
from barcode import Code128
from .models import VisaInfo



@login_required
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        user = authenticate(username=uname, password=upass)
        if user:
            login(request, user)
            messages.success(request, 'You have been loged in')
            return redirect('home')
        else:
            return redirect('signin')

    context = {'title': 'signin'}
    return render(request, 'auth/signin.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def form_1_search(request):
    # Get the search keywords from the request
    visa_no = request.GET.get('keyword1')
    serial_id = request.GET.get('keyword2')

    # Initialize the querysets
    visa_infos = VisaInfo.objects.all()
    visa_applications = VisaApplication.objects.all()

    # Filter the VisaInfo and VisaApplication based on the search criteria
    if visa_no:
        visa_infos = visa_infos.filter(visa_no__icontains=visa_no)
    if serial_id:
        visa_infos = visa_infos.filter(serial_id__icontains=serial_id)

    # Pass the filtered results to the template
    context = {
        'visa_infos': visa_infos,
        'visa_applications': visa_applications,
    }

    return render(request, 'list/form1_v2.html', context)

@login_required
def form_1_list(request):
    visa_infos = VisaInfo.objects.all().order_by('-id')
    visa_applications = VisaApplication.objects.all().order_by('-id')

    # Paginate visa_applications
    paginator = Paginator(visa_applications, 15)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'visa_infos': visa_infos,
        'page_obj': page_obj,  # Use page_obj in the template
    }
    return render(request, 'list/form1_v2.html', context)

@login_required
def form_2_search(request):
    visa_no = request.GET.get('keyword1')
    serial_id = request.GET.get('keyword2')

    visa_infos = VisaInfo.objects.all()
    visa_applications = VisaApplication.objects.all()

    # Apply filtering based on keywords
    if visa_no:
        visa_infos = visa_infos.filter(visa_no__icontains=visa_no)
    if serial_id:
        visa_infos = visa_infos.filter(serial_id__icontains=serial_id)

    context = {
        'visa_infos': visa_infos,
        'visa_applications': visa_applications,
    }
    return render(request, 'list/form1_v2.html', context)

@login_required
def form_2_list(request):
    visa_infos = VisaInfo.objects.all().order_by('-id')
    visa_applications = VisaApplication.objects.all().order_by('-id')

    # Paginate visa_applications
    paginator = Paginator(visa_applications, 15)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'visa_infos': visa_infos,
        'page_obj': page_obj,  # Use page_obj in the template
    }
    return render(request, 'list/form2_v2.html', context)

@login_required
def visa_info(request):
    if request.method == 'POST':
        form = VisaInfoForm(request.POST)
        if form.is_valid():
            visa_info = form.save()

            if visa_info.visa_qnt:
                for i in range(1, visa_info.visa_qnt + 1):
                    VisaApplication.objects.create(
                        visa_info=visa_info,
                        serial_no=f"{visa_info.serial_id}.{i}",
                    )

            messages.success(request, 'Inserted successfully!')
            return redirect('visa_info')
    else:
        form = VisaInfoForm()
    
    if VisaInfo.objects.exists():
        serial_id = VisaInfo.objects.all().order_by('-id').first().serial_id
    else:
        serial_id = 0
    serial_id = int(serial_id) + 1
    # print(serial_id)

    context = {'form': form, 'serial_id': serial_id}
    return render(request, "visa/visaInfo.html", context)

@login_required
def visa_app(request):
    if request.method == 'POST':
        form = VisaApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Insert successfully!')
            return redirect('form_2_list')
    else:
        form = VisaApplicationForm()
    context = {'form': form}
    return render(request, "visa/visaApp.html", context)

# @login_required
# def edit(request, serial_no):
#     visa_application = get_object_or_404(VisaApplication, serial_no=serial_no)

#     if request.method == 'POST':
#         form = VisaApplicationForm(request.POST, instance=visa_application)
#         print(form.cleaned_data)
#         if form.is_valid():
#             print(form)
#             form.save()
#             return redirect('form_2_list')

#     data = VisaApplication.objects.get(serial_no=serial_no)
#     context = {
#         'data': data,
#     }
#     return render(request, 'visa/visaAppUpdate.html', context)



@login_required
def edit(request, serial_no):
    visa_application = get_object_or_404(VisaApplication, serial_no=serial_no)

    if request.method == 'POST':
        form = VisaApplicationForm(request.POST, instance=visa_application)
        
        if form.is_valid():
            # Accessing and printing the cleaned data only after validation
            # print(form.cleaned_data)
            
            form.save()
            return redirect('form_2_list')
        else:
            # Optionally print the form errors to understand why it's not valid
            print(form.errors)

    data = VisaApplication.objects.get(serial_no=serial_no)
    context = {
        'data': data,
    }
    return render(request, 'visa/visaAppUpdate.html', context)





@login_required
def edit_visa_info(request, serial_id):
    visa_info = get_object_or_404(VisaInfo, serial_id=serial_id)

    if request.method == 'POST':
        form = VisaInfoForm(request.POST, instance=visa_info)
        if form.is_valid():
            form.save()
            return redirect('form_1_list')

    data = VisaInfo.objects.get(serial_id=serial_id)
    print(data)
    context = {
        'data': data,
    }
    return render(request, 'visa/visaInfoUpdate.html', context)


















@login_required  
def pdf_application(request, serial_no):
    ml = VisaApplication.objects.get(serial_no=serial_no)

    # Generate barcode
    my_code = Code128(ml.visa_info.visa_no, writer=None)
    my_code.save(os.path.join('static/img/visa/') + str(ml.serial_no))

    passport_code = Code128(ml.passport_no, writer=None)
    passport_code.save(os.path.join('static/img/pp/') + str(ml.serial_no))

    context = {
        'member': {field.name: getattr(ml, field.name) or '' for field in VisaApplication._meta.fields},
    }
    return render(request, "pdf/pdf_for_visa_app.html", context)

@login_required  
def pdf_fly_air(request, serial_no):
    ml = VisaApplication.objects.get(serial_no=serial_no)
    context = {
        'member': {field.name: getattr(ml, field.name) or '' for field in VisaApplication._meta.fields},
    }
    return render(request, "pdf/pdf_for_fly_air.html", context)
    
@login_required 
def pdf_for_agreement(request, serial_no):
    ml=VisaApplication.objects.get(serial_no=serial_no)
    context = {
        'member': {field.name: getattr(ml, field.name) or '' for field in VisaApplication._meta.fields},
    }
    return render(request, 'pdf/pdf_for_agreement.html', context)

@login_required 
def pdf_for_visa_info(request, serial_id):
    ml = get_object_or_404(VisaInfo, serial_id=serial_id)
    context = {
        'member': {field.name: getattr(ml, field.name) or '' for field in VisaInfo._meta.fields},
    }
    return render(request, 'pdf/pdf_for_visa_info.html', context)



