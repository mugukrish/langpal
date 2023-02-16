from django.shortcuts import render, redirect

def portfolio_home_view(request):
    return render(request, 'portfolio/portfolio_home.html')