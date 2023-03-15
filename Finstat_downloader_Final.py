from tkinter import *
from tkinter import ttk
from datetime import datetime
import pprint
import requests
from bs4 import BeautifulSoup
from tkinter import filedialog
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
import pandas as pd
import os


pp = pprint.PrettyPrinter(indent=4)
df = pd.DataFrame()
folder_name = []
input_ico = []
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), '')
folder_name.append(desktop)
root = Tk()
e = Entry(root,width = 100)
var = IntVar()
input_questions = []


def sel():
    selection =  str(var.get())
    try:
        options.pop()
    except:
        Exception
    input_questions.append( str(var.get()))

R1 = Radiobutton(root, text="2014 mode", variable=var, value=3,
                  command=sel)
R1.pack( anchor = W )
R3 = Radiobutton(root, text="micro", variable=var, value=2,
                  command=sel)
R3.pack( anchor = W)
label = Label(root)
label.pack()

def display_text():
    global entry
    string= entry.get()
    try:
        input_ico.pop()
    except:
        pass
    input_ico.append(string)
    label.configure(text='Press Download')
    myButton['state'] = 'normal'
    
label=Label(root, text="Enter Ico", font=("Courier 22 bold"))
label.pack()

entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()

def browse_button():
    global folder_path
    folder_path = StringVar()
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(folder_path.get())
    folder_name.append(folder_path.get())

def myClick():
    myButton['state'] = 'disabled'
    myLabel = Label(root, text = "Stiahnute")
    myLabel.pack()

    df = pd.DataFrame()
    df2 = pd.DataFrame()

    if input_questions[-1] == str(3):
        
        df = pd.DataFrame()
        url = 'https://www.finstat.sk/' + input_ico[-1] +  '/suvaha?as=2014'
        print(url)
        browser = requests.get(url)  
        soup = BeautifulSoup(browser.text,'html.parser')
        tables = soup.find_all('table')
        soup 

        for z in range(1,146):
            lol = []
            i = 0
            for x in soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }]):


                i = i+1
                text = x.get_text()
                lol.append(text.replace('\n','').replace('\r','').replace('\xa0', ''))

                if i ==len(soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }])):
                    try:
                        df[str(z)] = lol
                    except:
                        continue

        df = df.transpose()

        list_polozka = []
        i = 0
        try:
            for x in range(0,1500):
                list_polozka.append(tables[0].findAll('div', {'class' : 'multiPinned-lg'})[i].get_text() )
                i = i+1
        except:
            pass
        names = [x.replace('\n','').replace('\r','') for x in list_polozka]


        i = 0
        years = []
        try:
            for x in range(0,20):
                years.append(soup.findAll('th', {'class' : 'text-right'})[i].get_text())
                i = i+1

        except:
            pass
        del df[0]    
        years = [x.replace('\n','').replace('\r','').strip() for x in years]
        df.columns = years
        df.index = names
       
        df2 = pd.DataFrame()
        url = 'https://www.finstat.sk/' + input_ico[-1] +  '/vykaz_ziskov_strat?as=2014'
        browser = requests.get(url)  
        soup = BeautifulSoup(browser.text,'html.parser')
        tables = soup.find_all('table')
        soup
        for z in range(1,62):
            lol = []
            i = 0
            for x in soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }]):


                i = i+1
                text = x.get_text()
                lol.append(text.replace('\n','').replace('\r','').replace('\xa0', ''))
                if i ==len(soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }])):
                    try:
                        df2[str(z)] = lol
                    except:
                        continue
        df2 = df2.transpose()

        list_polozka = []
        i = 0
        try:
            for x in range(0,1500):
                list_polozka.append(tables[0].findAll('div', {'class' : 'multiPinned-lg'})[i].get_text() )
                i = i+1
        except:
            pass
        names = [x.replace('\n','').replace('\r','') for x in list_polozka]
        i = 0
        years = []
        try:
            for x in range(0,20):
                years.append(soup.findAll('th', {'class' : 'text-right'})[i].get_text())
                i = i+1
        except:
            pass
        del df2[0]    
        years = [x.replace('\n','').replace('\r','').strip() for x in years]
        df2.columns = years
        df2.index = names
    
    elif input_questions[-1] == str(2):
        
        df = pd.DataFrame()
        url = 'https://www.finstat.sk/' + input_ico[-1] +  '/suvaha?as=micro_2014'
        print(url)
        browser = requests.get(url)  
        soup = BeautifulSoup(browser.text,'html.parser')
        tables = soup.find_all('table')
        soup 
        for z in range(1,46):
            lol = []
            i = 0
            for x in soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }]):
                i = i+1
                text = x.get_text()
                lol.append(text.replace('\n','').replace('\r','').replace('\xa0', ''))

                if i ==len(soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }])):
                    try:
                        df[str(z)] = lol
                    except:
                        continue
        df = df.transpose()
        list_polozka = []
        i = 0
        try:
            for x in range(0,1500):
                list_polozka.append(tables[0].findAll('div', {'class' : 'multiPinned-lg'})[i].get_text() )
                i = i+1
        except:
            pass
        names = [x.replace('\n','').replace('\r','') for x in list_polozka]
        i = 0
        years = []
        try:
            for x in range(0,20):
                years.append(soup.findAll('th', {'class' : 'text-right'})[i].get_text())
                i = i+1

        except:
            pass
        del df[0]    
        years = [x.replace('\n','').replace('\r','').strip() for x in years]
        df.columns = years
        df.index = names
        df2 = pd.DataFrame()
        url = 'https://www.finstat.sk/' + input_ico[-1] +  '/vykaz_ziskov_strat?as=micro_2014'
        browser = requests.get(url)  
        soup = BeautifulSoup(browser.text,'html.parser')
        tables = soup.find_all('table')
        soup
        for z in range(1,39):
            lol = []
            i = 0
            for x in soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }]):
                i = i+1
                text = x.get_text()
                lol.append(text.replace('\n','').replace('\r','').replace('\xa0', ''))
                if i ==len(soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }])):
                    try:
                        df2[str(z)] = lol
                    except:
                        continue
        df2 = df2.transpose()
        list_polozka = []
        i = 0
        try:
            for x in range(0,1500):
                list_polozka.append(tables[0].findAll('div', {'class' : 'multiPinned-lg'})[i].get_text() )
                i = i+1
        except:
            pass
        names = [x.replace('\n','').replace('\r','') for x in list_polozka]
        i = 0
        years = []
        try:
            for x in range(0,20):
                years.append(soup.findAll('th', {'class' : 'text-right'})[i].get_text())
                i = i+1
        except:
            pass
        del df2[0]    
        years = [x.replace('\n','').replace('\r','').strip() for x in years]
        df2.columns = years
        df2.index = names

    elif input_questions[-1] == str(1):

        df = pd.DataFrame()
        url = 'https://www.finstat.sk/' + input_ico[-1] +  '/suvaha'
        print(url)
        browser = requests.get(url)  
        soup = BeautifulSoup(browser.text,'html.parser')
        tables = soup.find_all('table')
        soup 
        for z in range(1,127):
            lol = []
            i = 0
            for x in soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }]):


                i = i+1
                text = x.get_text()
                lol.append(text.replace('\n','').replace('\r','').replace('\xa0', ''))

                if i ==len(soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }])):
                    try:
                        df[str(z)] = lol
                    except:
                        continue
        df = df.transpose()

        list_polozka = []
        i = 0
        try:
            for x in range(0,1500):
                list_polozka.append(tables[0].findAll('div', {'class' : 'multiPinned-lg'})[i].get_text() )
                i = i+1
        except:
            pass
        names = [x.replace('\n','').replace('\r','') for x in list_polozka]


        i = 0
        years = []
        try:
            for x in range(0,20):
                years.append(soup.findAll('th', {'class' : 'text-right'})[i].get_text())
                i = i+1

        except:
            pass
        del df[0]    
        years = [x.replace('\n','').replace('\r','').strip() for x in years]
        df.columns = years
        df.index = names
        df2 = pd.DataFrame()
        url = 'https://www.finstat.sk/' + input_ico[-1] +  '/vykaz_ziskov_strat'
        browser = requests.get(url)  
        soup = BeautifulSoup(browser.text,'html.parser')
        tables = soup.find_all('table')
        soup
        for z in range(1,63):
            lol = []
            i = 0
            for x in soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }]):


                i = i+1
                text = x.get_text()
                lol.append(text.replace('\n','').replace('\r','').replace('\xa0', ''))
                if i ==len(soup.findAll('tr', {'data-id' : 'row-' + str(z)})[0].findAll(['td', {'class' : 'nowrap text-right' },{'class' : 'nowrap text-right negative' }])):
                    try:
                        df2[str(z)] = lol
                    except:
                        continue
        df2 = df2.transpose()
    
        list_polozka = []
        i = 0
        try:
            for x in range(0,1500):
                list_polozka.append(tables[0].findAll('div', {'class' : 'multiPinned-lg'})[i].get_text() )
                i = i+1
        except:
            pass
        names = [x.replace('\n','').replace('\r','') for x in list_polozka]

        i = 0
        years = []
        try:
            for x in range(0,20):
                years.append(soup.findAll('th', {'class' : 'text-right'})[i].get_text())
                i = i+1

        except:
            pass
        del df2[0]    
        years = [x.replace('\n','').replace('\r','').strip() for x in years]
        df2.columns = years
        df2.index = names

    else:
        print('error')

    def dfs_tabs(df_list, sheet_list, file_name):
        file_name = folder_name[-1] +'/' + str(input_ico[-1]) +'.xlsx'
        writer = pd.ExcelWriter(file_name,engine='xlsxwriter') 
        workbook  = writer.book
        sheet_name = "VZZ"
        sheet_name2 = "suvaha"
        
        for dataframe, sheet in zip(df_list, sheet_list):
            dataframe.to_excel(writer, sheet_name=sheet, startrow=1 , startcol=0) 

        worksheet = writer.sheets[sheet_name]
        worksheet = writer.sheets[sheet_name]
        worksheet.write(0, 0, 'Stiahnute z Finstatu    '+datetime.now().strftime('%d %b %Y'), workbook.add_format({'bold': True, 'color': '#E26B0A', 'size': 14}))
        worksheet = writer.sheets[sheet_name2]
        worksheet.write(0, 0, 'Stiahnute z Finstatu    '+datetime.now().strftime('%d %b %Y'), workbook.add_format({'bold': True, 'color': '#E26B0A', 'size': 14}))
        writer.save()
    dfs = [df, df2]
    sheets = ['suvaha','VZZ']    

    dfs_tabs(dfs, sheets, 'multi-test.xlsx')

myButton4 = Button(root, text= "Okay",width= 7, command= display_text)    
myButton = Button(root, text = "Download", command=myClick, state = 'disabled')
myButton3 = Button(root, text = "Directory", command = browse_button)
myButton2 = Button(root, text = "Exit", command = root.destroy)
myButton4.pack()
myButton3.pack()
myButton.pack()
myButton2.pack()
root.mainloop()
