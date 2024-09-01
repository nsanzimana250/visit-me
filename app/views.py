from django.shortcuts import render
from .models import Contact, Project

def index(request):
    if request.method == 'POST':
        # Extract form data from the request
        fullname = request.POST.get('Name')
        phone_number = request.POST.get('tel')
        email = request.POST.get('email')
        message = request.POST.get('Message')

        # Save the data to the Contact model
        contact = Contact(fullname=fullname, phone_number=phone_number, email=email, message=message)
        contact.save()

        # Optionally, you can pass a success message back to the template
        return render(request, "index.html", {'success': True})
    
    # Retrieve all project data from the Project model
    projects = Project.objects.all()
    
    return render(request, "index.html", {'projects': projects})
