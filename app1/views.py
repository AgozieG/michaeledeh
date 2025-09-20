from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'app1/index.html')

def base(request):
    return render(request, 'app1/base.html')

def footer(request):
    return render(request, 'app1/footer.html')

def about(request):
    return render(request, 'app1/about.html')

def books(request):
    return render(request, 'app1/books.html')

def journals(request):
    return render(request, 'app1/journals.html')

def news(request):
    return render(request, 'app1/news.html')

def presentations(request):
    return render(request, 'app1/presentations.html')

def pics(request):
    return render(request, 'app1/pics.html')

def training(request):
    return render(request, 'app1/training.html')

def education(request):
    return render(request, 'app1/education.html')

def policy(request):
    return render(request, 'app1/policy.html')

def security(request):
    return render(request, 'app1/security.html')

def mentor(request):
    return render(request, 'app1/mentor.html')

def research(request):
    return render(request, 'app1/research.html')

def rec(request):
    return render(request, 'app1/rec.html')

def test(request):
    return render(request, 'app1/test.html')

def fliers(request):
    return render(request, 'app1/fliers.html')

def advid(request):
    return render(request, 'app1/advid.html')




from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FileUploadForm

def send_file_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['message']
            uploaded_file = request.FILES['attachment']
            

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=None,            # uses DEFAULT_FROM_EMAIL
                to=['michael.edeh@ebsu.edu.ng'],
            )
            # Attach the uploaded file
            email.attach(
                uploaded_file.name,
                uploaded_file.read(),
                uploaded_file.content_type
            )
            email.send(fail_silently=False)
            # ... attach & send email ...
            messages.success(request, "Your file was sent successfully!")
            return redirect('send_file')
    else:
        form = FileUploadForm()
    return render(request, 'app1/send_file.html', {'form': form})


# from django.contrib import messages

# def send_file_view(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # ... attach & send email ...
#             messages.success(request, "Your file was sent successfully!")
#             return redirect('send_file')
#     else:
#         form = FileUploadForm()
#     return render(request, 'app1/send_file.html', {'form': form})