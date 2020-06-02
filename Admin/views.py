from django.shortcuts import render
import mysql.connector as con
from django.http import HttpResponse
import pandas as pd

conn = con.connect(host="localhost", user="root", password="Pranav", database="pranav")
cur = conn.cursor()

# Create your views here.

def admin_page(request):

    return render(request, 'Admin/myadmin.html')

def AdminLogin(request):
    uname = request.GET.get('uname')
    psw = request.GET.get('psw')
    cur.execute('select * from admin;')
    content = cur.fetchall()
    # conn.commit()
    if content[0][0] == uname:
        if content[0][1] == psw:
            return render(request, 'Admin/AdminControl.html')
        else:
            return HttpResponse('Incorrect Pass')
    else:
        return HttpResponse('Incorrect Uname')

def ImportCSV(request): 

    # path = request.GET.get('text')
    path = request.GET.get("import", None).title()
    df = pd.read_csv(path)
    cur.execute('drop table if exists game_data')
    cur.execute('create table if not exists game_data(ID int(255),Name varchar(100) ,'
                    ' Platform varchar(50), Year int(4), Genre varchar(50), Publisher varchar(50),'
                    ' NA_Sales float(5), EU_Sales float(5),	JP_Sales float(5),'
                    ' Other_Sales float(5), Global_Sales float(5), img varchar(50),	info varchar(50),'
                    ' constraint Name check(Name not like %s));',['%[0-9]%'])
    conn.commit()
    for row in df.itertuples():
        cur.execute('insert into game_data(ID ,Name, Platform, Year, Genre, Publisher, '
                    ' NA_Sales, EU_Sales, JP_Sales , Other_Sales, Global_Sales, img, info ) '
                    ' values(%s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s);',[row.id, row.name,
                     row.platform, row.year, row.genre, row.publisher, row. NA_Sales, row.EU_Sales, row.JP_Sales,
                      row.Other_Sales, row.Global_Sales, row.img, row.info])
        conn.commit()
    

    return HttpResponse('<h1>Successfully Imported</h1>')

def disp_games(request):
   
    cur.execute('select Name from game_data;')
    tuple_games = cur.fetchall()
    all_games = []
    for row in tuple_games:
        all_games.append(row[0])


    context = {'all_games': all_games}
    return render(request, 'Admin/index.html', context)
    # return HttpResponse(all_games)

def update_delete(request):
    global oldName
    oldName = request.GET.get('name')
    # print(oldName)
    context = {'oldName' : oldName}
    return render(request, 'Admin/up_del.html', context)

def update_func(request):
    newname = request.GET.get('newName')
    # print(oldName)
    # print(newname)
    # newName.isNumeric() != True
    if (newname != "" and newname.isnumeric() != True):
        cur.execute('update game_data set game_data.name = %s where game_data.name = %s', [newname, oldName])
        conn.commit()
        return HttpResponse('Success')
    else:
       return HttpResponse('Enter Alphabetical Value!')
    
def delete_func(request):
    if (oldName != ""):
        cur.execute('delete from game_data where game_data.name = %s', [oldName])
        conn.commit()
        return HttpResponse('Success')
    else:
       return HttpResponse('Please Enter appropriate name')