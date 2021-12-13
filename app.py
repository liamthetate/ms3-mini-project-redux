import os
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




@app.route("/profile2", methods=["GET", "POST"]) #two different address's will lead to the same place
def profile2():
    if request.method == "POST": 
        num = 1
        flash("YOU HAVE COMPLETED " + str(num) + "out of 10 TASKS")
        return redirect(url_for("profile2"))

    return render_template("profile2.html") #takes the taks found in the db and displyas them on page



#once a user has logged in they can press a button to access the database, this will fill it
@app.route("/fill_db", methods=["GET", "POST"]) 
def fill_db():
    if request.method == "POST":
        db_entry = { 
                "category_name": "Worker Bees",
                "task_name": "Ms Flaps",
                "task_description": "filling the database",
                "is_urgent": "off",
                "due_date": "null",
                "created_by": session["user"],
                "honey_production": "good",
                "health": "diseased"
            }, { 
                "category_name": "Worker Bees",
                "task_name": "Lady McFlaps",
                "task_description": "balls",
                "is_urgent": "off",
                "due_date": "null",
                "created_by": session["user"],
                "honey_production": "poor",
                "health": "healthy"
            }, { 
                "category_name": "Worker Bees",
                "task_name": "Miss Buzzer",
                "task_description": "more bllas",
                "is_urgent": "off",
                "due_date": "null",
                "created_by": session["user"],
                "honey_production": "good",
                "health": "healthy"
            }, { 
                "category_name": "Worker Bees",
                "task_name": "Miss Wasp",
                "task_description": "bla bla bla",
                "is_urgent": "off",
                "due_date": "null",
                "created_by": session["user"],
                "honey_production": "good",
                "health": "healthy"
            }
            
        mongo.db.tasks.insert_many(db_entry)
        return redirect(url_for("fill_db"))

    return render_template("fill_db.html")


@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        return redirect(url_for("register"))

    return render_template("start.html")

@app.route("/start2", methods=["GET", "POST"])
def start2():
    if request.method == "POST":
        return redirect(url_for("register"))

    return render_template("start2.html")

@app.route("/") #two different address's will lead to the same place
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find()) #.tasks inside this is referencing the tasks on mongo
    return render_template("tasks.html", tasks=tasks) #takes the taks found in the db and displyas them on page


@app.route("/search", methods=["GET", "POST"]) #GET happens by default so we don't have to write it, unless we want POST
def search():
    query = request.form.get("query") #what the user wrote
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}})) #what the database has / 
    return render_template("tasks.html", tasks=tasks) #page render of results


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST": #has use tried to post info? then...
        existing_user = mongo.db.users.find_one( # look at 'users' on db and see if they are there
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists") #settings for this to be found on base.html
            return redirect(url_for("register")) #basically try again

        register = { #gets values from users form
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register) #adds those values into the db

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower() #gets username
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"])) #takes user to own page url

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: #yikes this one hurts my brain
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower() #session is referencing a cookie
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = { #get all the values the user has typed
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "honey_production": request.form.get("honey_production"),
            "health": request.form.get("health"),
        }
        mongo.db.tasks.insert_one(task) 
        flash("Task Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories) #display the catgeoires on the page that are in db


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = { #get all the values the user has typed
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "honey_production": request.form.get("honey_production"),
            "health": request.form.get("health"),
        }
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": submit}) #code fix for tutorial error
        flash("Task Successfully Updated")
        return redirect(url_for("get_tasks"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories) #display task & cats fround in db


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Thank you! The Bee is under investigation by authorities")
    return redirect(url_for("get_tasks"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories) #first is passed into the template, second is the function one


@app.route('/add_category', methods=["GET", "POST"]) #responses to actions taken by user on add_category.html
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New category added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit}) #update on error in tutorial code
        flash("category updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Deleted!")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)