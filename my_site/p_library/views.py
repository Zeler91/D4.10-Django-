from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, Redaction, Friend
from django.shortcuts import redirect
from django.views.generic import FormView  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login, authenticate  
from p_library.forms import ProfileCreationForm  
from django.http.response import HttpResponseRedirect  
from django.urls import reverse_lazy  
# from p_library.models import UserProfile
from allauth.socialaccount.models import SocialAccount

def nav(request):
    context = {
        "username": " ",
        "age": " ",
        "github_url": ' ',
    }
    if request.user.is_authenticated:  
        context['username'] = request.user.username
        if not SocialAccount.DoesNotExist: 
            context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
    return render(request, 'nav.html', context)

def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def redactions(request):
    template = loader.get_template('redactions.html')
    redactions = Redaction.objects.all()
    books = Book.objects.all()
    redactions_data = {
        "redactions": redactions,
        "books": books,
    }
    return HttpResponse(template.render(redactions_data, request))

def friends(request):
    template = loader.get_template('friends.html')
    friends = Friend.objects.all()
    books = Book.objects.all()
    friends_data = {
        "friends": friends,
        "books": books,
    }
    return HttpResponse(template.render(friends_data, request))

class RegisterView(FormView):  
  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
  
  
class CreateUserProfile(FormView):  
    form_class = ProfileCreationForm  
    template_name = 'profile-create.html'  
    success_url = reverse_lazy('p_library:nav')  
  
    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('login'))  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)