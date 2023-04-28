from flask import Flask, render_template, request
from storage import *

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('index.html')

@app.route('/new_student', methods = ["GET"])
def add_student():
    return render_template('student.html',
                           page_type = 'new',
                           form_meta = {"action":"/confirm_student", "method":"post"}, form_data={"NRIC":"", "student_name":"", "student_age":"","year_enrolled":"","graduating_year":"", "student_class":""})

@app.route('/confirm_student', methods = ["POST"])
def confirm_student():
    if request.method == "POST":
        nric = request.form["NRIC"]
        student_name = request.form["student_name"]
        student_age = request.form["student_age"]
        year_enrolled = request.form["year_enrolled"]
        graduating_year = request.form["graduating_year"]
        student_class = request.form["student_class"]
        
        return render_template('student.html',
                           page_type = 'confirm',
                           form_meta = {"action":"/student_success", "method":"post"}, form_data={"NRIC":nric, "student_name":student_name, "student_age":student_age,"year_enrolled":year_enrolled,"graduating_year":graduating_year, "student_class":student_class})

@app.route('/student_success', methods = ["POST"])
def student_success():
    if request.method == "POST":
        nric = request.form["NRIC"]
        student_name = request.form["student_name"]
        student_age = request.form["student_age"]
        year_enrolled = request.form["year_enrolled"]
        graduating_year = request.form["graduating_year"]
        student_class = request.form["student_class"]

        record = {"nric":nric,
                  "student_name":student_name,
                 "student_age":student_age,
                 "year_enrolled":year_enrolled,
                 "graduuating_year":graduating_year,
                 "student_class":student_class}
        
        return render_template('student.html',
                           page_type = 'success')



@app.route('/new_cca', methods = ["GET"])
def new_cca():
    return render_template('cca.html', 
                    page_type = 'new', 
                    form_meta = {'action':'/select_category','method':'post'},       
                    form_data = {'student_name': ''})




@app.route('/select_category', methods = ["POST"])
def select_category():
    if request.method == "POST":
        student_name = request.form['student_name']
        #append from database to categories
        categories = []
        
        return render_template('cca.html',
                              page_type = 'select_category',
                              form_meta = {'action' : '/select_cca', 'method' : 'post'},
                              form_data = {'category': '', 
                            'student_name': student_name}, categories = categories)




@app.route('/select_cca', methods = ["POST"])
def select_cca():
    if request.method == "POST":
        category = request.form['category']
        student_name = request.form['student_name']
        ccas = []

        if category == 'Sports':
            #append all the sport ccas to ccas
            pass
        elif category == 'Aesthetics':
            #append all aesthetics ccas to ccas
            pass
        elif category == 'Clubs':
            #append all clubs ccas to ccas
            pass

        return render_template('cca.html', page_type = 'select_cca', form_meta = {"action":"/confirm_cca","method":"post"}, form_data = {"student_name" : student_name, "category" : category}, ccas = ccas)


@app.route('/confirm_cca', methods = ["POST"])
def confirm_cca():
    if request.method == "POST":
        student_cca = request.form["student_cca"]
        student_name = request.form["student_name"]

        return render_template('cca.html',
                              page_type = "confirmation",
                              form_meta = {'action' : '/cca_success', 'method' : 'post'},
                              form_data = {'student_name' : student_name, 'student_cca' : student_cca})



@app.route('/cca_success', methods = ["POST"])
def cca_success():
    if request.method == "POST":
        student_cca = request.form["student_cca"]
        student_name = request.form["student_name"]

        #Now we must add the stuff to the database here

        return render_template('cca.html',
                              page_type = "success")


@app.route('/add_activity', methods = ["GET"])
def add_activity():
    return render_template("activity.html",
                          page_type = "new",
                          form_meta = {"action" : "/display_info_for_activity", "method" : "post"},
                          form_data = {"student_name":""})

@app.route('/display_info_for_activity', methods = ["POST"])
def display_info_for_activity():
    if request.method == 'POST':
        student_name = request.form["student_name"]
        student_class = ...
        student_cca = ...
        
        return render_template("activity.html",
                              page_type = "display",
                              form_meta = {"action" : "/select_activity", "method" : "post"},
                                form_data = {"student_name" : student_name, "student_class" : student_class, "student_cca" : student_cca})


@app.route('/select_activity', methods = ["POST"])
def select_activity():
    if request.method == "POST":
        student_name = request.form["student_name"]
        student_cca = request.form["student_cca"]

        #Find out all the activities by THAT CCA
        #to create a dropdown of the list of activities

        return render_template('/activity.html', page_type = "select", form_meta = {"actions" : "/input_activity", "method" : "post"}, form_data = {"student_name" : student_name , "selected_activity" : ""})

@app.route("/input_activity", methods = ["POST"])
def edit_activity():
    if request.method == "POST":
        student_name = request.form["student_name"]
        selected_activity = request.form["selected_activity"]

        if selected_activity == "Create new activity":
            return render_template("activity.html",
                              page_type = "input",
                              form_meta = {"action" : "/new_activity_success", "method" : "post"},
                              form_data = {"student_name" : student_name, "start_date" : "", "end_date" : "", "activity_description" : "", "category": "", "role": "", "award": "", "hours": ""})

        else:
            return render_template("activity.html",
                              page_type = "input",
                              form_meta = {"action" : "/exisiting_activity_success", "method" : "post"},
                              form_data = {"student_name" : student_name, "category": "", "role": "", "award": "", "hours": ""})
            
@app.route("/new_activity_success", methods = ["POST"])
def new_activity_success():
    if request.method == "POST":
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        activity_description = request.form["activity_description"]
        
        student_name = request.form["student_name"]
        category = request.form["category"]
        role = request.form["role"]
        award = request.form["award"]
        hours = request.form["hours"]
    #Add the activity to the database

        return render_template("activity.html", page_type = "success")


@app.route("/exisiting_activity_success", methods = ["POST"])
def existing_activity_success():
    if request.method == "POST":
        student_name = request.form["student_name"]
        category = request.form["category"]
        role = request.form["role"]
        award = request.form["award"]
        hours = request.form["hours"]
    #Add the activity to the database

        return render_template("activity.html", page_type = "success")


@app.route('/view_student', methods = ["GET"])
def view_student():
    return render_template('view_student.html', page_type = "new", form_meta = {"action":"/display_student","method":"post"},form_data = {"student_name":""})


@app.route('/display_student', methods = ["POST"])
def display_student():

    if request.method == "POST":
        student_name = request.form["student_name"]
        student_class = ...
        student_cca = ...
    
        return render_template('view_student.html', page_type = "display", form_meta = {"action":"/display_student","method":"post"},form_data = {"student_name":student_name, "student_class": student_class, "student_cca":student_cca})

@app.route('/view_classes', methods = ["GET"])
def view_classes():
    return render_tempalate('view_classes.html', page_type = "new", form_meta = {"action":"/display_class","method":"post"}, form_data = {"student_class":""})

@app.route('/display_class', methods = ["POST"])
def display_class():

    if request.method == "POST":
        student_class = request.form["student_class"]

        #Get student and cca from database
    
        return render_template('view_student.html', page_type = "display", form_meta = {"action":"/display_student","method":"post"},form_data = {...})


@app.route('/view_cca', methods = ["GET"])
def view_cca():        
        return render_template('view_cca.html',
                              page_type = 'new',
                              form_meta = {'action' : '/select_cca_to_view', 'method' : 'post'},
                              form_data = {'category': ''})

@app.route('/select_cca_to_view', methods = ["POST"])
def select_cca_to_view():
    pass


if __name__ == '__main__':
    app.run('0.0.0.0')

