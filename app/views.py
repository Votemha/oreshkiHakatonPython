from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Note
from django.db.models import Count

# Главная страница
def index(request):
    users = User.objects.annotate(note_count=Count('notes'))
    return render(request, 'index.html', {'users': users})


# ---------- USERS ----------
def user_create(request):
    if request.method == 'POST':
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('index')
    return render(request, 'user_form.html')


def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('index')


# ---------- NOTES ----------
def notes_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'notes_list.html', {'user': user})


def note_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        Note.objects.create(
            user=user,
            title=request.POST['title'],
            text=request.POST['text'],
            tags=request.POST['tags']
        )
        return redirect('notes_list', user_id=user.id)
    return render(request, 'note_form.html', {'user': user})


def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    user_id = note.user.id
    note.delete()
    return redirect('notes_list', user_id=user_id)