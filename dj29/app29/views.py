from django.shortcuts import render
from .models import table_30, table_34


# Create your views here.
def demo(request):
    obj=table_30.objects.all()
    obj2 = table_34.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
