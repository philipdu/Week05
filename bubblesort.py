import csv

from flask import Flask, redirect, render_template, request, url_for

user_input = []
app = Flask(__name__)
app.config["SECRET_KEY"] = "Highly secret key"    

@app.route("/", methods=["GET", "POST"])
def index():
    user_input.clear() #Clears memory - can also do global user_input
    if request.method == "POST":
        li = list(map(int,request.form["li"].split(","))) # ["3", "2", "1"]
        sort(li)
        user_input.append(li)

        return redirect(url_for("hello"))
    return render_template("index.html")

def sort(li):
    n = len(li)
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(n-1): #need n-1 so we can compare i to i+1
            if li[i] > li[i+1]:
                swap(li, i, i+1)
                swapped = True
                #print(li)

def swap(li,i,j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp
    user_input.append(li.copy()) 
    #Appends a copy of li so we see the iterations of the bubble sort

@app.route("/Hello")
def hello():
    return render_template("hello.html", all_users=user_input)

if __name__ == "__main__":
    app.run(debug=True)