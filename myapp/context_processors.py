from myapp.forms import CallbackRequestForm

def callback_form(request):
    return {
        "callback_form": CallbackRequestForm()
    }
