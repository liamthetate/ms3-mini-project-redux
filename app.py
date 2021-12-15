import os
import random #for game data
from flask import (
    Flask, flash, render_template, #flash is the prompts for the user
    redirect, request, session, url_for) #request reads forms from the user
from flask_pymongo import PyMongo
from bson.objectid import ObjectId #used for finding stuff like -> category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") #stock values
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")       #stock values
app.secret_key = os.environ.get("SECRET_KEY")               #stock values


mongo = PyMongo(app)


# Generates the random data required for the game
def bee_name():
    first_name = [
        "Lady", "Stella", "Ms", "Beatrix", "Buzz", "Edith",
        "Ambrosia", "Abbee", "BEEthoven", "OBEE-Wan", "Bianca", "Chase"
        ]
    second_name = [
        "McFly", "Flaps", "Wasp", "Bee", "McBeeFace", "Window-Basher",
        "KenoBEE", "McBee", "Barnabee", "Bee", "McBeeFace", "Beelzebub"
    ]
    name = first_name[random.randint(0, 11)] + " " + second_name[random.randint(0, 11)]
    return name


def efficiency():
    honey_production = ["🍯 poor", "🍯🍯🍯 good", "🍯🍯🍯🍯🍯 excellent"]
    efficiency = honey_production[random.randint(0, 2)]
    return efficiency


def health():
    health = ["🩸 diseased", "🩸🩸🩸 ok", "🩸🩸🩸🩸🩸 healthy"]
    health_rating = health[random.randint(0, 2)]
    return health_rating


def automated_db():
    db_template = { 
            "category_name": "TEST",
            "task_name": bee_name(),
            "created_by": session["user"],
            "honey_production": efficiency(),
            "health": health()
            }
    return db_template

def wasp_db():
    db_template = { 
            "category_name": "TEST",
            "task_name": "Mr Wasp",
            "created_by": session["user"],
            "honey_production": efficiency(),
            "health": health()
            }
    return db_template




def plant_database():
    for i in range(20): #creates database on load of page, 20 is number of bees in hive
        mongo.db.tasks.insert_one(automated_db())
    
    for i in range(3): 
        mongo.db.tasks.insert_one(wasp_db()) 


#GAME START 
@app.route("/") 
@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST": 
        existing_user = mongo.db.users.find_one( 
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists") #settings for flash to be found on base.html
            return redirect(url_for("register")) #basically try again

        register = { #gets values from users form
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register) #adds those values into the db

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower() #gets username
        flash("Registration Successful!")
        return redirect(url_for("welcome", username=session["user"])) #takes user to own page url

    return render_template("start.html")


#REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST": #has use tried to post info? then...
        existing_user = mongo.db.users.find_one( # look at 'users' on db and see if they are there
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists") #settings for flash to be found on base.html
            return redirect(url_for("register")) #basically try again

        register = { #gets values from users form
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "full_name": request.form.get("full_name").lower(),
            "phone": request.form.get("phone"),
            "address": request.form.get("address").lower()
        }
        mongo.db.users.insert_one(register) #adds those values into the db

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower() #gets username
        flash("Registration Successful!")
        return redirect(url_for("welcome", username=session["user"])) #takes user to own page url

    return render_template("welcome_task.html")


@app.route('/welcome')
def welcome():
    progress_value = 0
    plant_database()
    return render_template('welcome_task.html', progress_value=progress_value)


#DEBUG TOOLS
@app.route("/fill-db-button", methods=["GET", "POST"]) 
def fill_db_button():
    for i in range(20): #number of bees in hive
        mongo.db.tasks.insert_one(automated_db())
    return redirect("get_tasks")
#DEBUG TOOLS
@app.route("/delete-all", methods=["GET", "POST"]) 
def delete_all():
    mongo.db.tasks.delete_many({})
    return redirect("get_tasks")
#AN ATTEMPT TO RETAIN SEARCH ENGINE RESULTS
def search_memory():
    query = request.form.get("query")
    print(query)
    return query


'''
def wasps_left():
    any_wasps = list(mongo.db.tasks.find({"$text": {"$search": "wasp"}}))
    if any_wasps:
        flash(str(len(any_wasps)))
'''



#UI TASKS ORDERED
def ui_tasks():
    any_wasps = list(mongo.db.tasks.find({"$text": {"$search": "wasp"}}))
    any_poor = list(mongo.db.tasks.find({"$text": {"$search": "poor"}}))
    any_diseased = list(mongo.db.tasks.find({"$text": {"$search": "diseased"}}))

    if any_poor:
        flash("🍯  poor productivity = " + str(len(any_poor)))

    if (len(any_poor)) == 0:
        if any_diseased:
            flash("🩸 diseased = " + str(len(any_diseased)))
    
        if (len(any_diseased)) == 0:
            if any_wasps:
                flash("surname 'wasp' = " + str(len(any_wasps)))

            #if (len(any_wasps)) == 0:
            #    flash("DONE!")



def progress_bar():
    progress_value = 10

    any_poor = list(mongo.db.tasks.find({"$text": {"$search": "poor"}}))
    if len(any_poor) == 0:
        progress_value = 33

        any_diseased = list(mongo.db.tasks.find({"$text": {"$search": "diseased"}}))
        if len(any_diseased) == 0:
            progress_value = 66

        any_wasps = list(mongo.db.tasks.find({"$text": {"$search": "wasp"}}))
        if len(any_wasps) == 0:
            progress_value = 99

    return progress_value


#MAIN GAME SCREEN
@app.route("/get_tasks")
def get_tasks():
    session.pop('_flashes', None)
    progress_value = progress_bar()
    ui_tasks() 
    if end_state() == "end":
        return redirect(url_for('end'))

    tasks = list(mongo.db.tasks.find()) #.tasks inside this is referencing the tasks on mongo
    return render_template("tasks.html", tasks=tasks, progress_value=progress_value) #takes the taks found in the db and displyas them on page


#SEARCH
@app.route("/search/", methods=["GET", "POST"]) #GET happens by default so we don't have to write it, unless we want POST
def search():
    progress_value = progress_bar()
    ui_tasks()
    query = request.form.get("search") #what the user wrote
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}})) #what the database has / 
    return render_template("tasks.html", tasks=tasks, progress_value=progress_value) #page render of results
    #return redirect(url_for("get_tasks"))




#ADD TASK
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    progress_value = progress_bar()
    ui_tasks()
    if request.method == "POST":
        task = { #get all the values the user has typed
            "task_name": request.form.get("task_name"),
            "honey_production": request.form.get("honey_production"),
            "health": request.form.get("health"),
        }
        mongo.db.tasks.insert_one(task) 
        return redirect(url_for("get_tasks"))

    #categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", progress_value=progress_value) #display the catgeoires on the page that are in db


#EDIT TASK
@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    progress_value = progress_bar()
    ui_tasks()
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = { #get all the values the user has typed
            "task_name": request.form.get("task_name"),
            "honey_production": request.form.get("honey_production"),
            "health": request.form.get("health"),
        }
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": submit}) #code fix for tutorial error
        #flash("Task Successfully Updated")
        return redirect(url_for("get_tasks"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, progress_value=progress_value) #display task & cats fround in db


#DELETE TASK
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    #flash("Thank you! The Bee is under investigation by authorities")
    #return render_template("tasks.html")
    return redirect(url_for("get_tasks"))



#DELETE MULTIPLE TASKS
@app.route("/delete_multiple", methods=["GET", "POST"])
def delete_multiple():
        test = request.form.get('mycheckbox')
        #test = request.form.getlist('task._id') #getlist returns []
        flash(test)
'''
    if request.method == "POST":
        test = request.form.get('mycheckbox')
        #test = request.form.getlist('task._id') #getlist returns []
        flash(test)
'''
    #for getid in request.form.getlist(format('mycheckbox')):
        #flash("TESTING")
        #mongo.db.tasks.delete_one({"_id": ObjectId(getid)})
    #return redirect(url_for("get_tasks"))


#CHECKS TO SEE IF GAME IS OVER
def end_state():
    any_wasps = list(mongo.db.tasks.find({"$text": {"$search": "wasp"}}))
    any_poor = list(mongo.db.tasks.find({"$text": {"$search": "poor"}}))
    any_diseased = list(mongo.db.tasks.find({"$text": {"$search": "diseased"}}))

    if (len(any_poor)) == 0:
        if (len(any_diseased)) == 0:
            if (len(any_wasps)) == 0:
                return "end"


#END / deletes game database
@app.route("/end", methods=["GET", "POST"])
def end():

    mongo.db.tasks.delete_many({}) #deletes game database

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("end.html", username=username)

    return render_template("end.html")


#LOGOUT / DESTROY ALL DATA
@app.route("/logout")
def logout():
    mongo.db.users.delete_one(
        {"username": session["user"]}) #destroys all data
    session.pop("user") # remove user from session cookie
    return render_template("logged_out.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), 
            debug=True) #DELETE