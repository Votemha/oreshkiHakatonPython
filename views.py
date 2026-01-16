from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Note
from .forms import NoteForm, AdminUserCreateForm, AdminUserUpdateForm


def home(request):
    users = User.objects.annotate(notes_count=Count("note"))
    return render(request, "notes/home.html", {"users": users})


@login_required
def note_list(request):
    q = request.GET.get("q", "")
    notes = Note.objects.filter(user=request.user)

    if q:
        notes = notes.filter(
            Q(title__icontains=q) |
            Q(text__icontains=q) |
            Q(tags__icontains=q)
        )

    return render(request, "notes/note_list.html", {"notes": notes, "q": q})


@login_required
def note_create(request):
    form = NoteForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        n = form.save(commit=False)
        n.user = request.user
        n.save()
        return redirect("note_list")

    return render(request, "notes/note_form.html", {"form": form, "mode": "create"})


@login_required
def note_edit(request, pk):
    n = get_object_or_404(Note, pk=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=n)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("note_list")

    return render(request, "notes/note_form.html", {"form": form, "mode": "edit"})


@login_required
def note_delete(request, pk):
    n = get_object_or_404(Note, pk=pk, user=request.user)

    if request.method == "POST":
        n.delete()
        return redirect("note_list")

    return render(request, "notes/note_delete.html", {"note": n})


@staff_member_required
def admin_user_list(request):
    users = User.objects.annotate(notes_count=Count("note"))
    return render(request, "notes/admin_user_list.html", {"users": users})


@staff_member_required
def admin_user_create(request):
    form = AdminUserCreateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("admin_user_list")

    return render(request, "notes/admin_user_form.html", {"form": form, "mode": "create"})


@staff_member_required
def admin_user_edit(request, pk):
    u = get_object_or_404(User, pk=pk)
    form = AdminUserUpdateForm(request.POST or None, instance=u)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("admin_user_list")

    return render(request, "notes/admin_user_form.html", {"form": form, "mode": "edit"})


@staff_member_required
def admin_user_delete(request, pk):
    u = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        u.delete()
        return redirect("admin_user_list")

    return render(request, "notes/admin_user_confirm_delete.html", {"u": u})
