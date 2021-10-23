from django.shortcuts import render,HttpResponse
from home3.models import Person
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def login(request):
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')
def validate(request):
    if(request.method == 'POST'):
        emails=[]
        email_get = request.POST.get('email')
        print(email_get)
        p=Person.objects.raw('SELECT id, email FROM home3_Person')
        for i in p:
            emails.append(i.email) 
        if(email_get in emails):
            return HttpResponse("You are loged in")
        else:
            content={"message":"Wrong Email"}
            return render(request,'login.html',content)
    #return HttpResponse("hello")        
            
def next(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email  = request.POST.get('email')
        #number = request.POST.get('number')
        send_mail(
            'Subject here',
            'Here is the message.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        Model1=Person(name=name,email=email)
        Model1.save()
        # p=Person.objects.raw('SELECT id, name, email FROM home3_Person')
        # for i in p:
        #     print(i.name,i.email)
    return HttpResponse("Successfully Registered!!!!!")
