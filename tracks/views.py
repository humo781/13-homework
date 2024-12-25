from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Music

def home(request):
    return render(request, 'index.html')

def music_list(request):
    musics = Music.objects.all()
    ctx = {'musics': musics}
    return render(request, 'music/music-list.html', ctx)

def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    ctx = {'music': music}
    return render(request, 'music/music-detail.html', ctx)

def music_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        image = request.FILES.get('image')
        audio_file = request.FILES.get('audio_file')
        if title and artist and album and genre and release_date and image and audio_file:
            Music.objects.create(
                title=title,
                artist=artist,
                album=album,
                genre=genre,
                release_date=release_date,
                image=image,
                audio_file=audio_file
            )
            return redirect('tracks:list')
    return render(request, 'music/form.html')

def music_update(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        image = request.FILES.get('image')
        audio_file = request.FILES.get('audio_file')
        if title and artist and album and genre and release_date:
            music.title = title
            music.artist = artist
            music.album = album
            music.genre = genre
            music.release_date = release_date
            if image:
                music.image = image
            if audio_file:
                music.audio_file = audio_file
            music.save()
            return redirect('tracks:list')
    ctx = {'music': music}
    return render(request, 'music/form.html', ctx)

def music_del_confirm(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        music.delete()
        return redirect('tracks:list')
    ctx = {'music': music}
    return render(request, 'music/music-delete-confirm.html', ctx)
