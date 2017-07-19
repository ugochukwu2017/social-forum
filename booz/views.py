from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .models import Booz,Comment
from .forms import BoozForm,CommentForm,LikeForm


def booz_list(request):
    boozs = Booz.public.select_related('owner').all()
    if request.GET.get('tag'):
        boozs = boozs.select_related('owner').filter(tags__name=request.GET['tag'])
    context = {'boozs': boozs}
    return render(request, 'booz/booz_list.html', context)


def booz_detail(request, pk):
    booz = get_object_or_404(Booz, pk=pk)
    return render(request, 'booz/booz_detail.html', {'booz': booz})


@login_required
def booz_user(request, username):
    user = get_object_or_404(User, username=request.user.username)
    if request.user == user:
        boozs = user.boozs.select_related('owner').all()
    else:
        boozs = Booz.public.select_related('owner').filter(owner__username=username)
    if request.GET.get('tag'):
        boozs = boozs.select_related('owner').filter(tags__name=request.GET['tag'])
    context = {'boozs': boozs, 'owner': user}
    return render(request, 'booz/booz_user.html', context)


@login_required
def booz_create(request):
    if request.method == 'POST':
        form = BoozForm(data=request.POST)
        if form.is_valid():
            booz = form.save(commit=False)
            booz.owner = request.user
            booz.save()
            return redirect('booz_user',
                username=request.user.username)
    else:
        form = BoozForm()
    context = {'form': form, 'create': True}
    return render(request, 'booz/form.html', context)


@login_required
def booz_edit(request, pk):
    booz = get_object_or_404(Booz, pk=pk)
    if booz.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = BoozForm(instance=booz, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('booz_user',
                username=request.user.username)
    else:
        form = BoozForm(instance=booz)
    context = {'form': form, 'create': False}
    return render(request, 'booz/form.html', context)


def add_comment_to_booz(request, pk):
    booz = get_object_or_404(Booz, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.booz = booz
            comment.save()
            return redirect('booz_detail', pk=booz.pk)
    else:
        form = CommentForm()
    return render(request, 'booz/add_comment_to_booz.html', {'form': form})


def add_like_to_booz(request, pk):
    booz = get_object_or_404(Booz, pk=pk)
    if request.method == "POST":
        form = LikeForm(request.POST)
        like = form.save(commit=False)
        like.booz = booz
        like.save()
        return redirect('booz_detail', pk=booz.pk)

    else:
        form = LikeForm()
    return render(request, 'booz/add_like_to_booz.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('booz_detail', pk=comment.booz.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('booz_detail', pk=comment.booz.pk)
