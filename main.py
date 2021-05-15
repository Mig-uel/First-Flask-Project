from flask import Flask, render_template #Importing Flask module and creating Flask web server; Importing template

app = Flask(__name__) # Current file (__name__ = main.py) & creating instance calling it app

@app.route("/") #Default web page
def home(): #Default page
    return render_template("home.html"); #Returns our home.html

@app.route("/about")
def about():
    return render_template("about.html") #Returning our aboutme.html

if __name__ == "__main__": #Prevents other scripts from running
    app.run(debug=True) #Debug
