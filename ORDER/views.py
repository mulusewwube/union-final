from django.shortcuts import render,redirect
from .models import (editing,Website_project,Research,Thesis,Research_help,GraphicsDesignSubmission,ProgrammingProjectSubmission,VideoEditingSubmission,Transcription,Assignment,Business_plan)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
def utility(user):
    graphics = GraphicsDesignSubmission.objects.filter(user_name=user,status='completed').count()
    programming = ProgrammingProjectSubmission.objects.filter(user_name=user,status='completed').count()
    video = VideoEditingSubmission.objects.filter(user_name=user,status='completed').count()
    transcription = Transcription.objects.filter(user_name=user,status='completed').count()
    assignment = Assignment.objects.filter(user_name=user,status='completed').count()
    business_plans = Business_plan.objects.filter(user_name=user,status='completed').count()
    researches = Research.objects.filter(user_name=user,status='completed').count()
    theses = Thesis.objects.filter(user_name=user,status='completed').count()
    website = Website_project.objects.filter(user_name=user,status='completed').count()
    edit = editing.objects.filter(user_name=user,status='completed').count()
    research_help = Research_help.objects.filter(user_name=user,status='completed').count()

    total_completed_orders = research_help + graphics + programming + video + assignment + business_plans + researches + theses  + transcription + website + edit

    tgraphics = GraphicsDesignSubmission.objects.filter(user_name=user,status='pending').count()
    tprogramming = ProgrammingProjectSubmission.objects.filter(user_name=user,status='pending').count()
    tvideo = VideoEditingSubmission.objects.filter(user_name=user,status='pending').count()
    ttranscription = Transcription.objects.filter(user_name=user,status='pending').count()
    tassignment = Assignment.objects.filter(user_name=user,status='pending').count()
    tbusiness_plans = Business_plan.objects.filter(user_name=user,status='pending').count()
    tresearches = Research.objects.filter(user_name=user,status='pending').count()
    ttheses = Thesis.objects.filter(user_name=user,status='pending').count()
    twebsite = Website_project.objects.filter(user_name=user,status='pending').count()
    tedit = editing.objects.filter(user_name=user,status='pending').count()
    treserch_help = Research_help.objects.filter(user_name=user,status='pending').count()

    total_pending_orders = treserch_help + tgraphics + tprogramming + tvideo + tassignment + tbusiness_plans + tresearches + ttheses  + ttranscription + twebsite + tedit

    total = total_pending_orders + total_completed_orders 
    
    return total,total_pending_orders,total_completed_orders

@login_required(login_url='user:login')
def profile_page(request):
    total,pending,completed = utility(request.user)
    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,

    }
    return render(request,'order/profile.html',context)


@login_required
def user_orders(request):
    # Retrieve orders for the logged-in user
    graphics = GraphicsDesignSubmission.objects.filter(user_name=request.user)
    programming = ProgrammingProjectSubmission.objects.filter(user_name=request.user)
    video = VideoEditingSubmission.objects.filter(user_name=request.user)
    transcription = Transcription.objects.filter(user_name=request.user)
    assignment = Assignment.objects.filter(user_name=request.user)
    business_plans = Business_plan.objects.filter(user_name=request.user)
    researches = Research.objects.filter(user_name=request.user)
    theses = Thesis.objects.filter(user_name=request.user)
    web = Website_project.objects.filter(user_name=request.user)
    edit = editing.objects.filter(user_name=request.user)
    research_help = Research_help.objects.filter(user_name=request.user)
    
    total,pending,completed = utility(request.user)

    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,
        'business_plans': business_plans,
        'researches': researches,
        'theses': theses,
        'assignment':assignment,
        'transcriptions':transcription,
        'videos':video,
        'programmings':programming,
        'graphicss':graphics,
        'websites':web,
        'editings':edit,
        'research_help': research_help
    }

    return render(request, 'order/ordres.html', context)

@login_required(login_url='user:login')
def completed_orders(request):
    # Retrieve orders for the logged-in user
    graphics = GraphicsDesignSubmission.objects.filter(user_name=request.user,status='completed')
    programming = ProgrammingProjectSubmission.objects.filter(user_name=request.user,status='completed')
    video = VideoEditingSubmission.objects.filter(user_name=request.user,status='completed')
    transcription = Transcription.objects.filter(user_name=request.user,status='completed')
    assignment = Assignment.objects.filter(user_name=request.user,status='completed')
    business_plans = Business_plan.objects.filter(user_name=request.user,status='completed')
    researches = Research.objects.filter(user_name=request.user,status='completed')
    theses = Thesis.objects.filter(user_name=request.user,status='completed')
    web = Website_project.objects.filter(user_name=request.user,status='completed')
    edit = editing.objects.filter(user_name=request.user,status='completed')
    research_help = Research_help.objects.filter(user_name=request.user,status='completed')

    total,pending,completed = utility(request.user)

    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,
        'business_plans': business_plans,
        'researches': researches,
        'theses': theses,
        'assignment':assignment,
        'transcriptions':transcription,
        'videos':video,
        'programmings':programming,
        'graphicss':graphics,
        'websites':web,
        'editings':edit,
        'research_help': research_help
    }

    return render(request, 'order/completed_ordres.html', context)

@login_required(login_url='user:login')
def pending_orders(request):
    # Retrieve orders for the logged-in user
    graphics = GraphicsDesignSubmission.objects.filter(user_name=request.user,status='pending')
    programming = ProgrammingProjectSubmission.objects.filter(user_name=request.user,status='pending')
    video = VideoEditingSubmission.objects.filter(user_name=request.user,status='pending')
    transcription = Transcription.objects.filter(user_name=request.user,status='pending')
    assignment = Assignment.objects.filter(user_name=request.user,status='pending')
    business_plans = Business_plan.objects.filter(user_name=request.user,status='pending')
    researches = Research.objects.filter(user_name=request.user,status='pending')
    theses = Thesis.objects.filter(user_name=request.user,status='pending')
    web = Website_project.objects.filter(user_name=request.user,status='pending')
    edit = editing.objects.filter(user_name=request.user,status='pending')
    total,pending,completed = utility(request.user)

    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,
        'business_plans': business_plans,
        'researches': researches,
        'theses': theses,
        'assignment':assignment,
        'transcriptions':transcription,
        'videos':video,
        'programmings':programming,
        'graphicss':graphics,
        'websites':web,
        'editings':edit
    }

    return render(request, 'order/pending_ordres.html', context)



@login_required(login_url='user:login')
def create_research(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'

        if user_name and firstname and lastname and email and phone_number and gender and titles and number_of_pages and abstract and description and accept_terms:
            Research.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,abstract=abstract,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            
            return redirect(reverse_lazy('order:order'))
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect(reverse_lazy('order:order'))
        # Replace with your success URL

    return render(request, 'order/research.html')


@login_required(login_url='user:login')
def research_help(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'

        if user_name and firstname and lastname and email and phone_number and gender and titles and number_of_pages and abstract and description and accept_terms:
            Research_help.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,abstract=abstract,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            
            return redirect(reverse_lazy('order:research_help'))
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect(reverse_lazy('order:research_help'))
        # Replace with your success URL

    return render(request, 'order/research_help.html')


@login_required(login_url='user:login')
def create_thesis(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'

        if user_name and firstname and lastname and email and phone_number and gender and titles and number_of_pages and abstract and description and accept_terms:

            Thesis.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,abstract=abstract,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')

            return redirect('order:thesis')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect(reverse_lazy('order:thesis'))
    return render(request, 'order/thesis.html')


@login_required(login_url='user:login')
def graphics_design_submission(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        service = request.POST.get('service')
        design_file = request.FILES.get('design_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')

        # You can add validation and error handling here

        # Save the submission to the database
        if user_name and firstname and lastname and email and phone_number and gender and service and design_file and description and accept_terms:

            submission = GraphicsDesignSubmission(
            user_name=user_name,
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            gender=gender,
            service=service,
            design_file=design_file,
            description=description,
            accept_terms=accept_terms == 'on'
        )
            submission.save()
            messages.success(request,'order submitted successfully you can see it in the dashboard ')

            return redirect('order:graphics-design')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect(reverse_lazy('order:graphics-design'))
        

    return render(request, 'order/graphics_design.html')

@login_required(login_url=('user:login'))
def programming_project_submission(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        title = request.POST.get('title')
        programming_language = request.POST.get('programming_language')
        specific_work_area = request.POST.get('specific_work_area')
        project_file = request.FILES.get('project_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')

        if user_name and firstname and lastname and email and phone_number and gender and title and programming_language and specific_work_area and project_file and description and accept_terms:
        # Save the submission to the database
            submission = ProgrammingProjectSubmission(
                user_name = user_name,
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                gender=gender,
                title=title,
                programming_language=programming_language,
                specific_work_area=specific_work_area,
                project_file=project_file,
                description=description,
                accept_terms=accept_terms == 'on'
            )
            submission.save()
            messages.success(request,'order submitted successfully you can see it in the dashboard ')

            return redirect('order:program-project')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect('order:program-project')  # Replace with your success URL


    return render(request, 'order/programming.html')


@login_required(login_url='user:login')
def video_editing_submission(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        title = request.POST.get('title')
        video_length = request.POST.get('video_length')
        video_format = request.POST.get('video_format')
        project_file = request.FILES.get('project_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')

        if user_name and firstname and lastname and email and phone_number and gender and title and video_format and video_length and project_file and description and accept_terms:
       
        # Save the submission to the database
            submission = VideoEditingSubmission(
                user_name=user_name,
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                gender=gender,
                title=title,
                video_length=video_length,
                video_format=video_format,
                project_file=project_file,
                description=description,
                accept_terms=accept_terms == 'on'
            )
            submission.save()
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            return redirect('order:video-project')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect('order:video-project')
    return render(request, 'order/video_editing.html')
@login_required(login_url='user:login')
def transcription(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        transcribed_file = request.POST.get('file')
        accept_terms = request.POST.get('accept_terms')
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')
        description = request.POST.get('description')

        if user_name and firstname and lastname and email and phone_number and gender and transcribed_file and source_language and target_language and accept_terms:
        # Save the submission to the database
            submission = Transcription(
                user_name=user_name,
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                gender=gender,
                accept_terms=accept_terms == 'on',
                source_language=source_language,
                target_language=target_language,
                transcribed_file = transcribed_file,
                description=description
            )
            submission.save()
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            return redirect('order:transcription')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect('order:transcription')

    return render(request, 'order/transcription.html')

# ////////////////////////////////////////////////////

@login_required(login_url='user:login')
def assignment(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'

        if user_name and firstname and lastname and email and phone_number and gender and titles and number_of_pages and abstract and accept_terms:

            Assignment.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,abstract=abstract,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            return redirect('order:assignment')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect('order:assignment')  # Replace with your success URL
        
    return render(request, 'order/assignment.html')

@login_required(login_url='user:login')
def business_plan(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'
        
        if user_name and firstname and lastname and email and phone_number and gender and titles and number_of_pages and abstract and accept_terms:

            Business_plan.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,abstract=abstract,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            return redirect('order:business-plan')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect('order:business-plan')  # Replace with your success URL
          
    return render(request, 'order/business_plan.html')
@login_required(login_url='user:login')
def website_project(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        web_type = request.POST.get('web-type')
        framework = request.POST.get('framework')
        website_file = request.FILES.get('web_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'

        if user_name and firstname and lastname and email and phone_number and gender and titles and web_type and website_file and description and framework and accept_terms:

            Website_project.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,website_type = web_type, gender=gender,website_title=titles,framework=framework,website_file=website_file,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            return redirect('order:website-project')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect('order:website-project')  # Replace with your success URL

    return render(request, 'order/web_design.html')

@login_required(login_url='user:login')
def Writing_editing_project(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        edited_file = request.FILES.get('edited_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'

        if user_name and firstname and lastname and email and phone_number and gender and edited_file and description and accept_terms:

            editing.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number, gender=gender,edited_file=edited_file,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            return redirect('order:editing-project')  # Replace with your success URL
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect('order:editing-project')  # Replace with your success URL
          
    return render(request, 'order/writhing_editing.html')
