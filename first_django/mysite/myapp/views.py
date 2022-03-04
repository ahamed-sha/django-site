from django.shortcuts import render
from .forms import NewForm
from .models import AccessRecord, Topic, Webpage

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    
    my_dict = {
        'a_list': webpages_list,
        "hello": "hello_there",
    }
    return render(request, 'index.html', context=my_dict)

def newform_view(request):
    form = NewForm()

    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            print("validation success!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, "forms.html", {"form": form})
