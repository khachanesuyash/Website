from django.shortcuts import render
from .models import Game
from django.http import HttpResponse, HttpResponseRedirect

import mysql.connector as con
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


conn = con.connect(host="localhost", user="root", password="Pranav", database="pranav")
cur = conn.cursor()

def index(request):
    all_games = Game.objects.all()
    context = {'all_games': all_games}
    return render(request, 'games/index.html', context)


def home(request):
    return render(request, 'games/home.html')


def result(request):
    text = request.GET.get('name')
    values = Game.objects.filter(name=text)
    context = {'values': values}
    return render(request, 'games/result.html', context)


def search(request):
    if request.method == 'GET':
        text = request.GET.get("search", None).title()
        values = Game.objects.filter(name=text)
        value = Game.objects.filter(name=text).exists()
        context = {'values': values}
        # all_games = Game.objects.all()
        # for game in all_games:
        # if game.name == text:
        #     return HttpResponse('Found')
        # else:
        #     return HttpResponse('Not Found')
        if value == True:
            return render(request, 'games/result.html', context)
        else:
            return HttpResponse('<h1 align = "center" >404 Error</h1><br><h1 align = "center" >Requested Game Not Found</h1>')
    else:
        return HttpResponse('')


def redirect(request):
    if request.method == 'GET':
        text = request.GET.get("search", None).title()
        text = text.title()
        return HttpResponseRedirect("/searches/?search="+text)


def plot(request):
    text = request.GET.get('name')
    value = Game.objects.get(name=text)

    left = [1, 2, 3, 4]
    height = [value.NA_Sales, value.EU_Sales, value.JP_Sales, value.Other_Sales]
    tick_label = ['America', 'Europe', 'Japan', 'Other']



    fig, ax = plt.subplots()
    ax.bar(left, height, tick_label=tick_label,
           width=0.8, color=['red', 'green'])

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bar Graph of Sales in Country(in Millions)')

    canvas = FigureCanvasAgg(fig)
    canvas.print_jpg('games/static/games/image/bar.jpeg')

    labels = tick_label
    sizes = height
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Pie Chart of Sales')
    plt.legend(loc="upper left")

    canvas1 = FigureCanvasAgg(fig1)
    canvas1.print_jpg('games/static/games/image/pie.jpeg')

    return render(request, 'games/graph.html')


def home_plot(request):

    yearSet = set()
    curSet = []
    cur.execute('select year from game_data')
    curSet = cur.fetchall();
    for each in curSet:
        yearSet.add(each[0])
    # print(yearSet)
    
    cur.execute('select year, sum(global_sales) from game_data group by year')
    saleList = cur.fetchall();
    saleDict = {}
    for each in saleList:
        saleDict[each[0]] = each[1]

    keys = []
    for each in list(saleDict.keys()):
        keys.append(each)
    
    # print(saleDict.values())
    left = range(1,38)
    height = saleDict.values()
    tick_label = keys

    fig, ax = plt.subplots(figsize=(30,23))
    ax.bar(left, height, tick_label=tick_label,
           width=0.8, color=['red'])

    plt.xlabel('Years', fontsize=30)
    plt.ylabel('Global Sales', fontsize=30)
    ax.tick_params(axis="x", labelsize=23, rotation=90)
    ax.tick_params(axis="y", labelsize=23)
    plt.title('Bar Graph of Global Sales in Years(in Millions)', fontsize=30)

    canvas = FigureCanvasAgg(fig)
    canvas.print_jpg('games/static/games/image/gsbar.jpeg')
    # print(saleDict)
    
    image_data = open("games/static/games/image/gsbar.jpeg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def home_plot2(request):

    cur.execute('select sum(NA_Sales),sum(EU_Sales),sum(JP_Sales) from game_data;')
    saleList = cur.fetchall()

    # print(saleSet)
    # left = range(1,4)
    height = [saleList[0][0], saleList[0][1], saleList[0][2]]
    tick_label = ['America', 'Europe', 'Japan']

    fig, ax = plt.subplots(figsize=(30,23))
    # ax.bar(left, height, tick_label=tick_label,
    #        width=0.2, color=['red', 'green'])
    ax.scatter(tick_label, height, s=20**2.5)

    plt.xlabel('Country', fontsize=35)
    plt.ylabel('Total Sales', fontsize=30)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=23)
    plt.title('Scatter Plot  of Country Wise Sales(in Millions)', fontsize=30)


    canvas = FigureCanvasAgg(fig)
    canvas.print_jpg('games/static/games/image/csbar.jpeg')
    # print(saleDict)
    
    image_data = open("games/static/games/image/csbar.jpeg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def home_plot3(request):
   
    cur.execute('select genre, count(genre) from game_data group by genre')
    saleList = cur.fetchall();
    saleDict = {}
    for each in saleList:
        saleDict[each[0]] = each[1]

    keys = []
    for each in list(saleDict.keys()):
        keys.append(each)

    left = range(1,13)
    height = saleDict.values()
    tick_label = keys

    fig, ax = plt.subplots(figsize=(30,23))
    ax.bar(left, height, tick_label=tick_label,
           width=0.8, color=['red', 'green'])

    plt.xlabel('Genre', fontsize=30)
    plt.ylabel('Count', fontsize=30)
    ax.tick_params(axis="x", labelsize=23, rotation=90)
    ax.tick_params(axis="y", labelsize=23)
    plt.title('Bar Graph of Frequency of a genre', fontsize=30)

    canvas = FigureCanvasAgg(fig)
    canvas.print_jpg('games/static/games/image/gcbar.jpeg')
    # print(saleDict)

    # return HttpResponse('htppss')
    image_data = open("games/static/games/image/gcbar.jpeg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")\

def home_plot4(request):
   
    cur.execute('select genre, sum(global_sales) from game_data group by genre')
    saleList = cur.fetchall();
    saleDict = {}
    for each in saleList:
        saleDict[each[0]] = each[1]

    keys = []
    for each in list(saleDict.keys()):
        keys.append(each)
    
    # print(saleDict.values())
    left = range(1,13)
    height = saleDict.values()
    tick_label = keys

    fig, ax = plt.subplots(figsize=(30,23))
    ax.bar(left, height, tick_label=tick_label,
           width=0.8, color=['red', 'green'])
    # ax.plot(tick_label, height)

    plt.xlabel('Genre', fontsize=30)
    plt.ylabel('Global Sales', fontsize=30)
    ax.tick_params(axis="x", labelsize=23, rotation=90)
    ax.tick_params(axis="y", labelsize=23)
    plt.title('Global Sales(in Millions) per Genre', fontsize=30)

    canvas = FigureCanvasAgg(fig)
    canvas.print_jpg('games/static/games/image/ggbar.jpeg')
    # print(saleDict)
    
    image_data = open("games/static/games/image/ggbar.jpeg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def home_plot5(request):
  
    cur.execute('select platform, count(platform) from game_data group by platform;')
    saleList = cur.fetchall();
    saleDict = {}
    for each in saleList:
        saleDict[each[0]] = each[1]

    keys = []
    for each in list(saleDict.keys()):
        keys.append(each)
    
    # print(saleDict.values())
    left = range(1,25)
    height = saleDict.values()
    tick_label = keys

    fig, ax = plt.subplots(figsize=(30,23))
    ax.bar(left, height, tick_label=tick_label,
           width=0.8, color=['red', 'green'])
    # ax.plot(tick_label, height)

    plt.xlabel('Platform', fontsize=30)
    plt.ylabel('Count', fontsize=30)
    ax.tick_params(axis="x", labelsize=23, rotation=90)
    ax.tick_params(axis="y", labelsize=23)
    plt.title('Count of games per Platform', fontsize=30)

    canvas = FigureCanvasAgg(fig)
    canvas.print_jpg('games/static/games/image/ggbar.jpeg')
    # print(saleDict)
    
    image_data = open("games/static/games/image/ggbar.jpeg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")