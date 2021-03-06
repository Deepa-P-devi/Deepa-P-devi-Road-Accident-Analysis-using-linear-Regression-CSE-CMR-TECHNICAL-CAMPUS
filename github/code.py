import tkinter as tk  from tkinter import ttk  from PIL import Image ,ImageTk  r=tk.Tk();  
r.geometry("1920x1080+30+30")  
r.title('Road Accident Analysis using Machine Learning')  
background_image=ImageTk.PhotoImage(Image.open('o-TRAFFIC-facebook.jpg') )  background_label = tk.Label(r, image=background_image)  background_label.image = background_image  
background_label.place(x=0, y=0, relwidth=1, relheight=1)  
tt1=tk.Label(r,text=' Road Accidents Analysis and Prediction',width=50) 
tt1.config(font=("Ariel",50))  
tt1.pack(padx=10,pady=100)  
import pandas as pd  
from matplotlib import pyplot as plt  
import numpy as np  from sklearn.linear_model import LinearRegression  from sklearn.model_selection import train_test_split  from sklearn.preprocessing import LabelEncoder,OneHotEncoder from 
sklearn.compose import ColumnTransformer  
new_data=pd.read_csv('time_Prepared data v1.csv')  
data = pd.read_csv('only_road_accidents_data3.csv')  e= []  
cnt2 = 0                                                                                                                        for year in data['YEAR'].unique():  for i in data.index:  if data.loc[i,'YEAR'] == year:  
cnt2 = cnt2 + data.loc[i,'Total']  year_acc = (year,cnt2)  cnt2=0  
e.append(year_acc)  
model = LinearRegression()  
X_data = np.array([t[0] for t in e])  Y_data = np.array([y[1] for y in e])  
model.fit(X_data.reshape(len(X_data),1),Y_data.reshape(len(Y_data),1))  
data = pd.read_csv('time_Prepared data v1.csv')  data =data.drop('Unnamed: 0',axis=1)  le1 = LabelEncoder()  le2 = LabelEncoder()  elif data.loc[i,'TIME']== '21-24 hrs (Night)':  data.loc[i,'TIME'] = 7  
def analysis():  
data3 = pd.read_csv('only_road_accidents_data3.csv')  top1=tk.Toplevel(r)  
top1.geometry("1920x1080+30+30")  
top1.title('Analysis')  
tt1=tk.Label(top1,text=' Analysis',width=80)  tt1.config(font=("Ariel",50))  tt1.pack(padx=10,pady=60)  
#to find the timespan of max and min accidents  c= []      cnt = 0  for time in data3.columns[2:10]:  for i in data3.index:  cnt = cnt + data3.loc[i,time]  
time_acc = (time,cnt)                                                                                          cnt=0  
c.append(time_acc)  #print(c)  x = c[0]  y = c[0]  for i in c:  
if i[1]>x[1]:  
x = i  if i[1] <y[1]:  y=i  
msg1="Timespan of maximum accidents"  
msg2="Timespan of minimum accidents"  
#print(str(x))  #print("\n" + str(y))  def ab_prints(msg,a):  txt=tk.Toplevel(top1)  txt.geometry("900x400+30+30")  
def ab3():  
data_month = pd.read_csv('only_road_accidents_data_month2.csv') count = 0;  mean_month =[]  mean_month_acc =[]  for month in data_month.columns[2:-1]:  for i in data_month.index :  
mean_month.append(data_month.loc[i,month])  acc = (month,np.mean(mean_month))  mean_month =[]  mean_month_acc.append(acc)  txt=tk.Toplevel(top1)          txt.geometry("1280x720+30+30")  def ab4():  
data_month = pd.read_csv('only_road_accidents_data_month2.csv') 
data_month.head()  
# accidents per month  
count = 0                                                                                                            month_acc =[]  for month in data_month.columns[2:-1]:  for i in data_month.index:  
count = count + data_month.loc[i,month]  acc = (month,count)  month_acc.append(acc)  count = 0  
#months of max and min accidents  
minvalue = month_acc[0]  maxvalue = month_acc[0]  for x in month_acc:  if x[1] < minvalue[1]:  
minvalue =x  if x[1] > maxvalue[1]:  
maxvalue =x  
msg='Month of minimum accidents'  ab_prints(msg,minvalue)  
def ab5():  
data_month = pd.read_csv('only_road_accidents_data_month2.csv') 
data_month.head()  
# accidents per month  count = 0  month_acc =[]      for month in data_month.columns[2:-1]:  for i in data_month.index:  count = count + data_month.loc[i,month]  acc = (month,count)  month_acc.append(acc)  count = 0  
#months of max and min accidents  
minvalue = month_acc[0]                                                                                  maxvalue = month_acc[0]  for x in month_acc:  if x[1] < minvalue[1]:  
minvalue =x  if x[1] > maxvalue[1]:  
maxvalue =x  
msg='Month of maximum accidents'  ab_prints(msg,maxvalue)  
def ab6():  
data = pd.read_csv('only_road_accidents_data3.csv')  e= []  cnt2 = 0  
for year in data['YEAR'].unique():  for i in data.index:  if data.loc[i,'YEAR'] == year:  cnt2 = cnt2 + data.loc[i,'Total']  year_acc = (year,cnt2)  cnt2=0  
e.append(year_acc)  #print(c)  x = e[0]  y = e[0]  for i in e:  if i[1]>x[1]:  
                x = i  if i[1] <y[1]:  y=i  
msg="Year with minimum accidents"  
ab_prints(msg,y)  
#print("Year with maximum accidents:"+ str(x))  #print("Year with minimum accidents:" + str(y))  
def ab7():  
data = pd.read_csv('only_road_accidents_data3.csv')  e= []  
cnt2 = 0                                                                                                              for year in data['YEAR'].unique():  for i in data.index:  if data.loc[i,'YEAR'] == year:  cnt2 = cnt2 + data.loc[i,'Total']  year_acc = (year,cnt2)  cnt2=0  
e.append(year_acc)  #print(c)  x = e[0]  y = e[0]  for i in e:  if i[1]>x[1]:  
x = i  if i[1] <y[1]:  
y=i  
msg="Year with maximum accidents"  
ab_prints(msg,x)  
def ab8():  txt=tk.Toplevel(top1)  txt.geometry("1280x720+30+30")  
img = ImageTk.PhotoImage(Image.open('india_heat.jpg'))  
panel = tk.Label(txt, image = img)  
        panel.image = img  panel.place(x=0,y=0)  
panel.pack(side = "bottom", fill = "both", expand = "yes")  txt.mainloop()  
def ab9():  
#to find state with min accidents occured  
data = pd.read_csv('road-accidents-in-india/only_road_accidents_data3.csv') d= []  cnt1 = 0  for state in data['STATE/UT'].unique():  for i in data.index:  if data.loc[i,'STATE/UT'] == state:  
cnt1 = cnt1 + data.loc[i,'Total']                                                              state_acc = (state,cnt1)  cnt1=0  
d.append(state_acc)  #print(c)  x = d[0]  y = d[0]  for i in d:  if i[1]>x[1]:  
x = i  if i[1] <y[1]:  
y=i  
ab_prints('State with Minimum number of Accidents',y)  
def ab10():  
#to find state with max accidents occured  
data = pd.read_csv('road-accidents-in-india/only_road_accidents_data3.csv') d= []  cnt1 = 0  for state in data['STATE/UT'].unique():  for i in data.index:  
                    if data.loc[i,'STATE/UT'] == state:  
cnt1 = cnt1 + data.loc[i,'Total']  state_acc = (state,cnt1)  cnt1=0  
d.append(state_acc)  #print(c)  x = d[0]  y = d[0]  for i in d:  if i[1]>x[1]:  
x = i  if i[1] <y[1]:  y=i  
ab_prints('State with Maximum number of Accidents',x)  
         ab1=tk.Button(top1,text='Timespan of maximum                                            accidents',width=50,height=1,command=lambda:ab_prints(msg1,x)) 
ab1.config(font=("Ariel",20))  ab1.pack(pady=10)  
def predict():  
year=0  time=0  state=0  top2=tk.Toplevel(r)  
top2.geometry("1920x1080+30+30")  
#background_image=ImageTk.PhotoImage(Image.open('maxresdefault.jpg')) 
#background_label = tk.Label(top2, image=background_image) 
#background_label.image = background_image  
#background_label.place(x=0, y=0, relwidth=1, relheight=1)  top2.title('Prediction')  
tt1=tk.Label(top2,text=' Prediction',width=80)  tt1.config(font=("Ariel",50))      tt1.pack(padx=10,pady=60)  def pb_prints(msg,a,b):  #tk.messagebox.showinfo(msg,a)  txt=tk.Toplevel(top2)  txt.geometry("640x400+30+30") 
tt1=tk.Message(txt,text=msg,relief=tk.RAISED,anchor=tk.W,width=1000) tt1.config(font=("Ariel",20))  
tt1.pack(padx=10,pady=5)  tt2=tk.Message(txt,text=a,relief=tk.RAISED,anchor=tk.W,width=800) 
tt2.config(font=("Ariel",20))  
tt2.pack(padx=10,pady=5)  c="Accuracy: "+str(b*100)+"%"  tt3=tk.Message(txt,text=c,relief=tk.RAISED,anchor=tk.W,width=800) 
tt3.config(font=("Ariel",20))  
tt3.pack(padx=10,pady=5)                                                                                 
b4=tk.Button(txt,text='Back',width=10,height=2,command=txt.destroy) 
b4.config(font=("Ariel",20))  
b4.pack(side='bottom',pady=2)  
#text=tk.Text(txt)  
#text.insert(tk.END,msg)  
#text.insert(tk.END,a)  
#text.pack()  
def entry(z):  
year = int(z.get())  acc_year=model.predict(year)          pb_prints('Predicted number of 
accidents',acc_year[0],model.score(X_data.reshape(len(X_data),1),Y_data.reshape 
(len(Y_data),1)))  
def ShowReg(top2):  txt=tk.Toplevel(top2)  txt.geometry("1280x720+30+30")  
img = ImageTk.PhotoImage(Image.open('reg.png'))  
panel = tk.Label(txt, image = img)  panel.image = img  panel.place(x=0,y=0)  
panel.pack(side = "bottom", fill = "both", expand = "yes")  txt.mainloop()  
def pb1():  
txt=tk.Toplevel(top2)  txt.geometry("1280x720+30+30")  tt1=tk.Message(txt,text='Enter the Year to Predict number of Accidents',relief=tk.RAISED,anchor=tk.W,width=1000)  tt1.config(font=("Ariel",20))  tt1.pack(padx=20,pady=20)  z = tk.Entry(txt,font =("Ariel",15))  z.pack()  
z.focus_set()  
b4=tk.Button(txt,text='Back',width=10,height=2,command=txt.destroy) 
b4.config(font=("Ariel",20))                                                                              b4.pack(side='bottom',pady=2) 
b=tk.Button(txt,text='Predict',command=lambda:entry(z),activeforeground='red',width
=50,height=2)  
b.config(font=("Ariel",20))  def entry1(comboboxTime,comboboxState,comboboxYear):  
year = int(comboboxYear.get())  state = comboboxState.get()  time = comboboxTime.get()  state1=le1.transform([state])  if time== '0-3 hrs. (Night)':  
time = 0  elif time== '3-6 hrs. (Night)':  
   time = 1  elif time== '6-9 hrs (Day)':  
time = 2  elif time== '9-12 hrs (Day)':  
time = 3  elif time== '12-15 hrs (Day)':  
time = 4  elif time== '15-18 hrs (Day)':  
time = 5  elif time== '18-21 hrs (Night)':  
time = 6  elif time== '21-24 hrs (Night)':  time = 7  
cal = ohe.transform([[state1,year,time]])  res=model1.predict(cal)  if res[0] < 0:  
res[0]=0  
pb_prints('Predicted number of  
accidents',res[0],model1.score(X_train,y_train))  
def entry2(comboboxMonth,comboboxState,comboboxYear):  
year = int(comboboxYear.get())  
state = comboboxState.get()  
month = comboboxMonth.get()                                                                     
state = le_month_1.transform([state])  month = le_month_2.transform([month])  cal = ohe_month.transform([[state,year,month]])  res=model3.predict(cal)  if res[0] < 0:  res[0]=0  
        pb_prints('Predicted number of  
accidents',res[0],model3.score(X_train_month,y_train_month))  
def pb2():          txt=tk.Toplevel(top2) 19 txt.geometry("1280x720+30+30")  txt.title('Multipe Linear Regression???)           pb2=tk.Button(top2,text='Multiple Linear 
Regression(time)',width=50,height=1,command=pb2)  pb2.config(font=("Ariel",20))  pb2.pack(pady=15,padx=10)  
     pb3=tk.Button(top2,text='Multiple Linear  Regression(month)',width=50,height=1,command=pb3)  
pb3.config(font=("Ariel",20))  pb3.pack(pady=20,padx=10)  
pb0=tk.Button(top2,text='Back',width=10,height=2,command=top2.destroy) 
pb0.pack(pady=30,padx=10)  
top2.mainloop()  
button1 = tk.Button(r,text='Analysis',width=25,height=2,command=analysis) 
button1.config(font=("Ariel",20))  
button1.pack(pady=30)  
button2= tk.Button(r,text='Prediction',width=25,height=2,command=predict) button2.config(font=("Ariel",20))  
button2.pack(pady=30)                                                                                           
button3= tk.Button(r,text='Exit',width=25,height=2,command=r.destroy) 
button3.config(font=("Ariel",20))  
button3.pack(pady=30)  
r.mainloop() 
 
                                                                                                                                                                                                        
 
 
 
 
 
 
 
 
