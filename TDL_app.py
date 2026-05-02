import os
from datetime import date
from flask import Flask,request,render_template

app=Flask(__name__)
date1 = date.today().strftime("%m_%d_%y")
date2 = date.today().strftime("%d-%B-%y")
if 'tdl.txt' not in os.listdir("."):
    with open ('tdl.txt','w') as f:
        f.write('')

def tasks():
    with open('tdl.txt', 'r' ) as f:
        tasklist=f.readlines()
    return tasklist

def createlist():
    with open('tdl.txt','w') as f:
        f.write('')
def updatelist(tasklist):
    #os.remove('tdl.txt')
    with open('tdl.txt','w') as f:
        f.writelines(tasklist)

@app.route('/')
def home():
    return render_template('TDL.html', date2=date2, tasklist=tasks(), l=len(tasks()))
#To clear the list
@app.route('/clear')
def clear():
    createlist()
    return render_template('TDL.html', date2=date2, tasklist=tasks(), l=len(tasks()))

#To add task
@app.route('/addtask',methods=['POST'])
def Task_Add():
    task = request.form.get('newtask')
    with open('tdl.txt','a') as f:
        f.writelines(task + '\n')
    return render_template('TDL.html', date2=date2, tasklist=tasks(), l=len(tasks()))

#to Delete a task
@app.route('/deltask',methods=['GET'])
def remove_tasks():
    task_index=int(request.args.get('deltaskid'))
    tasklist=tasks()
    print(task_index)
    print(tasklist)
    if task_index<0 or task_index<len(tasklist):
        tasklist.pop(task_index)
        updatelist(tasklist)
        return render_template('TDL.html', date2=date2, tasklist=tasks(), l=len(tasks()))
    else:
        updatelist(tasklist)
        render_template('TDL.html', date2=date2, tasklist=tasks(), l=len(tasks()))
if __name__=="__main__":
    app.run(debug=True)