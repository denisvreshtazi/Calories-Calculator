from flask.views import MethodView
from flask import Flask, request, render_template
from wtforms import  SubmitField, StringField, Form
from calorie import Calories
from temperature import Temperature


app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                               caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(city=calories_form.city.data,
                                  country=calories_form.country.data).get()

        calorie = Calories(weight=float(calories_form.weight.data),
                           height=float(calories_form.height.data),
                           age=float(calories_form.age.data),
                           temperature=temperature).calculate()

        return render_template('calories_form_page.html',
                               caloriesform=calories_form,
                               calories=calorie,
                               result=True)


class CaloriesForm(Form):

    weight = StringField('Weight: ', default=80)
    height = StringField('Height: ', default=180)
    age = StringField('Age: ', default=28)
    country = StringField('Country: ', default='Italy')
    city = StringField('City: ', default='Firenze')
    button = SubmitField('Calculate')


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
