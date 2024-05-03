from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile

class UserInfoForm(forms.ModelForm):
	Numero = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Numero'}),required=False)
	Endereço1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Endereço1'}),required=False)
	Endereço2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Endereço2'}),required=False)
	Cidade = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Cidade'}),required=False)
	Estado = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Estado'}),required=False)
	CEP = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CEP'}),required=False)
	Pais = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'País'}),required=False)
	class Meta:
		model = Profile
		fields = ('Numero', 'Endereço1' ,'Endereço2','Cidade','Estado','CEP','Pais')

class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password', 'new_password2']
	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser parecida com outras informações do seu usuário.</li><li>Sua senha deve conter ao menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comum.</li><li>Sua senha não pode ser apenas números.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirmar Senha'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>' 


class UpdateUserForm(UserChangeForm):
	password = None
	# Vamo que vamo galerinha
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Deve conter: Menos de 150 caracteres e pelo menos um caractere especial (Ex.: _ % $ ! @ #)</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser parecida com outras informações do seu usuário.</li><li>Sua senha deve conter ao menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comum.</li><li>Sua senha não pode ser apenas números.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Insira a mesma senha de antes.</small></span>' 