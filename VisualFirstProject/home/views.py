from turtle import color
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

# Create your views here.
def landpage(request):
    return render(request,'landpage.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def projects(request):
    return render(request,'projects.html')
def api(request):
    return render(request,'api.html')
def congratulation(request):
    firstname=request.POST['firstname']
    return render(request,'congratulation.html')

     
def videodownloader(request):
    videolink=str(request.GET['videolink'])
    if videolink=="":
        tk.Message("wrong input")
    else:
        videolink="https://www.youtube.com/watch?v=UtF6Jej8yb4"
    quality=str(request.GET['quality'])
    YouTube(videolink).streams.filter(res=quality).first().download('C:\dekstop')
    return messagebox("Done")

def covidData(request):