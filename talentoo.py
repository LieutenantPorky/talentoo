from flask import Flask, jsonify, request, render_template, url_for
import People
from data_utils import *

app = Flask(__name__, static_folder="./static", static_url_path='/static')
app.debug = True

@app.route('/')
def homePage():
    result = render_template("homepage.html",new_person_link = url_for("new_person"), lookup_people_link= url_for("people"))
    return result

@app.route('/people')
def people():
    peopleList = [{"name":person.name + " " + person.surname, "link":url_for("see_person", index=person.index)} for person in People.Person.select()]
    print(peopleList)
    result = render_template("list_people.html", people_list=peopleList)
    return result

@app.route('/new')
def new_person():
    result = render_template("new_person.html",add_url=url_for("add_person"))
    return result

@app.route('/person/<int:index>')
def see_person(index):
    person = People.Person.get(index=index)
    contact_info = [{"name":i[0] , "content":i[1]} for i in person.contact.items()]
    print(contact_info)
    result = render_template("view_person.html",name=person.name + " " + person.surname, contact_list=contact_info)
    return result

@app.route('/add', methods=['POST'])
def add_person():
    parsedData = parseJQUERY(request.json)
    print(parsedData)
    contact= {
    "email":parsedData["email"],
    "phone":parsedData["phone"]
    }
    People.addPerson(name=parsedData["fname"], surname=parsedData["lname"], contact=contact)
    print("Person added")
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=8080)
