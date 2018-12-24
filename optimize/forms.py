from django import forms
from optimize.models import Image

class ImageModelForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = [
			'picture',
		]