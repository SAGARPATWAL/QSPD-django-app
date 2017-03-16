from django.shortcuts import render
from django.views.generic import TemplateView
from pylibs import qts
from .forms import movieform
# Create your views here.
class HomePageView(TemplateView):
    def get(self,request, **kwargs):
        return render(request,'index.html',context=None)

class AnsPageView(TemplateView):
	def post(self,request,**kwargs):
		if request.method=="POST":
			form=movieform(request.POST)
			if form.is_valid():
				moviename=request.POST.get('moviename')
				s_obj=qts.searching_for_quote(moviename)
				searchterm=request.POST.get('searchterm')
				result=s_obj.getdialouge(searchterm)
		else: form=movieform()
		return render(request,'ans.html',{'form':form, 'result':result})



