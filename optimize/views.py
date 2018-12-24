from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView

from optimize.forms import ImageModelForm
from optimize.models import Image
# Create your views here.

class ImageView(View):
	template_name = "home.html"
	form_class = ImageModelForm
	def get(self,request, *args, **kwargs):
		form = self.form_class()
		return render(request,self.template_name,{'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST,request.FILES) 
		device=None
		if form.is_valid():
			form.save()
			url = form.cleaned_data["picture"]
			pic = Image.objects.all()
			# print(url)
			if request.user_agent.is_pc:
				height=540
				width=480
				# print("pc")

			if request.user_agent.is_mobile:
				# device="mobile"
				height=160
				width=120
				

			if request.user_agent.is_tablet:
				# device="tablet"
				height=320
				width=240
			
			print(height)
			print(width)
			context = {'pic':pic,'form':form, 'url':url,'height':height, 'width':width}
			return render(request,self.template_name,context)

		return render(request,self.template_name,{'form':form})