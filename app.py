import os
import random #for game data

from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for) 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")       
app.secret_key = os.environ.get("SECRET_KEY")               


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
            "honey_production": efficiency(),
            "health": health()
            }
    return db_template


def wasp_db():
    db_template = { 
            "category_name": "TEST",
            "task_name": "Ok, you got me, I'm a Wasp",
            "honey_production": "🍯🍯🍯🍯🍯 excellent",
            "health": "🩸🩸🩸🩸🩸 healthy"
            }
    return db_template


def plant_database():
    for i in range(20): #creates database on load of page, 20 is number of bees in hive
        mongo.db.tasks.insert_one(automated_db())
    mongo.db.tasks.insert_one(wasp_db()) #Need at least one wasp in the db!


#GAME START 
@app.route("/") 
@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST": 
        existing_user = mongo.db.users.find_one( 
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists") 
            return redirect(url_for("start")) 

        register = { 
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "full_name": request.form.get("full_name").lower(),
            "phone": request.form.get("phone"),
            "address": request.form.get("address").lower()
        }
        mongo.db.users.insert_one(register) 

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower() 
        flash("Registration Successful!")
        return redirect(url_for("welcome", username=session["user"]))
        
    return render_template("start.html")


@app.route('/welcome', methods=["GET", "POST"])
def welcome():
    progress_value = 0
    plant_database()

    if request.method == "POST":
        task = { #get all the values the user has typed
            "task_name": request.form.get("task_name"),
            "honey_production": request.form.get("honey_production"),
            "health": request.form.get("health"),
        }
        mongo.db.tasks.insert_one(task) 
        return redirect(url_for("get_tasks"))

    return render_template('welcome_task.html', progress_value=progress_value)


#UI TASKS ORDERED
def ui_tasks():
    any_wasps = list(mongo.db.tasks.find({"$text": {"$search": "wasp"}}))
    any_poor = list(mongo.db.tasks.find({"$text": {"$search": "poor"}}))
    any_diseased = list(mongo.db.tasks.find({"$text": {"$search": "diseased"}}))

    if any_diseased:
        flash("🩸 diseased = " + str(len(any_diseased)) + " bees")

    if (len(any_diseased)) == 0:
        if any_poor:
            flash("🍯  poor productivity = " + str(len(any_poor)) + " bees")
    
        if (len(any_poor)) == 0:
            if any_wasps:
                flash("'wasp' = " + str(len(any_wasps)))

            if (len(any_wasps)) == 0:
                flash("Purge Complete!")

'''
# HELLO EXAMINER! Try this, comment out above '#UI TASKS ORDERED' and use this code instead.
# Better or Worse? I couldn't decide.

#UI TASKS ALL AT ONCE
def ui_tasks():
    any_wasps = list(mongo.db.tasks.find({"$text": {"$search": "wasp"}}))
    any_poor = list(mongo.db.tasks.find({"$text": {"$search": "poor"}}))
    any_diseased = list(mongo.db.tasks.find({"$text": {"$search": "diseased"}}))

    if any_poor:
        flash("🍯  poor productivity = " + str(len(any_poor)))

    if any_diseased:
        flash("🩸 diseased = " + str(len(any_diseased)))
    
    if any_wasps:
        flash("Surname 'wasp' = " + str(len(any_wasps)))

    if (len(any_wasps)) == 0 and (len(any_poor)) == 0 and (len(any_diseased)) == 0:
        flash("Purge Complete!")
'''

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
            progress_value = 100

    return progress_value


#MAIN GAME SCREEN
@app.route("/get_tasks")
def get_tasks():
    session.pop('_flashes', None) # <-- Not my code
    progress_value = progress_bar()
    ui_tasks()
    tasks = list(mongo.db.tasks.find())

     #.tasks inside this is referencing the tasks on mongo
    return render_template("tasks.html", tasks=tasks, progress_value=progress_value)


#SEARCH
@app.route("/search/", methods=["GET", "POST"]) 
def search():
    progress_value = progress_bar()
    ui_tasks()
    query = request.form.get("search") 
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}})) 
    return render_template("tasks.html", tasks=tasks, progress_value=progress_value) 


#ADD TASK
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    progress_value = progress_bar()
    ui_tasks()
    if request.method == "POST":
        task = { 
            "task_name": request.form.get("task_name"),
            "honey_production": request.form.get("honey_production"),
            "health": request.form.get("health"),
        }
        mongo.db.tasks.insert_one(task) 
        return redirect(url_for("get_tasks"))

    return render_template("add_task.html", progress_value=progress_value) 


#EDIT TASK
@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    progress_value = progress_bar()
    ui_tasks()
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = { 
            "task_name": request.form.get("task_name"),
            "honey_production": request.form.get("honey_production"),
            "health": request.form.get("health"),
        }
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": submit}) #code fix for tutorial error
        return redirect(url_for("get_tasks"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, progress_value=progress_value) 


#DELETE TASK
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for("get_tasks"))


#DELETE MULTIPLE TASKS
@app.route("/delete_multiple", methods=["GET", "POST"])
def delete_multiple():
        list = request.form.getlist('mycheckbox') #getlist returns []
        length_of_list = len(list)
        for i in range(length_of_list):
            mongo.db.tasks.delete_one({"_id": ObjectId(list[i])})
        return redirect(url_for("get_tasks"))


#END / DESTROY ALL DATA 
@app.route("/end")
def end():
    mongo.db.tasks.delete_many({}) #deletes GAME database

    mongo.db.users.delete_one(  #deletes all USER data
        {"username": session["user"]}) 
    
    session.pop("user") # deletes user from session cookie

    return render_template("end.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), 
            )