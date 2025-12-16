from django.shortcuts import render,redirect
from django.core.mail import send_mail
# Create your views here.
from django.views import View
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class AboutView(View):
    def get(self,request):
        return render(request,'about.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Build the full message with name & email
        full_message = f"""
        You have received a new message from your website contact form:

        Name: {name}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """


        send_mail(
            subject,
            full_message,
            email,
            ['ismathilyas786@gmail.com'],
            fail_silently=True
        )

        return redirect('home')
class ServicesView(View):
    def get(self,request):
        return render(request,'services.html')
class Internship(View):
    def get(self,request):
        return render(request,'internship.html')
from myapp.forms import CallbackRequestForm
from django.contrib import messages
from django.conf import settings


def callback_request(request):
    if request.method == "POST":
        form = CallbackRequestForm(request.POST)
        if form.is_valid():
            obj = form.save()

            # Send email to admin
            try:
                subject = "New Callback Request"
                message = (
                    f"A new callback request has been submitted:\n\n"
                    f"Name: {obj.name}\n"
                    f"Phone: {obj.phone}\n"
                )
                from_email = settings.EMAIL_HOST_USER
                recipient_list = ["ismathilyas786@gmail.com"]  # your email

                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, "Your request was submitted! We will call you soon.")
            except Exception as e:
                messages.error(request, "Saved, but email notification failed.")
                print("Email error:", e)

        else:
            messages.error(request, "Please correct the errors and submit again.")

    return redirect(request.META.get("HTTP_REFERER", "/"))
