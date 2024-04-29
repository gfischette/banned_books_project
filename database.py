import pymysql
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField, SelectField


db = SQLAlchemy()
app = Flask(__name__)


if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.config['SECRET_KEY'] = 'NUIW8R28INHDIRH38'

db.init_app(app)


class Info(db.Model):
    __tablename__ = 'finaldetails'
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String)
    areas = db.Column(db.String)
    region = db.Column(db.String)
    number_books = db.Column(db.Integer)
    title_one = db.Column(db.String)
    cover_one = db.Column(db.String)
    author_one = db.Column(db.String)
    summary_one = db.Column(db.String)
    link_one = db.Column(db.String)
    title_two = db.Column(db.String)
    cover_two = db.Column(db.String)
    author_two = db.Column(db.String)
    summary_two = db.Column(db.String)
    link_two = db.Column(db.String)

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


class DistrictForm(FlaskForm):
    district = SelectField('Select District')
    submit = SubmitField('Submit')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/southfl')
def south():
    form = DistrictForm()
    sdistricts = Info.query.filter_by(region='South').order_by(Info.district).all()
    schoices = []
    for district in sdistricts:
        schoices.append((district.id, district.district))
    form.district.choices = schoices
    return render_template('region.html', form=form)
    
@app.route('/panhandlefl')
def panhandle():
    form = DistrictForm()
    pdistricts = Info.query.filter_by(region='Panhandle').order_by(Info.district).all()
    pchoices = []
    for district in pdistricts:
        pchoices.append((district.id, district.district))
    form.district.choices = pchoices
    return render_template('region.html', form=form)
    
@app.route('/northfl')
def north():
    form = DistrictForm()
    ndistricts = Info.query.filter_by(region='North').order_by(Info.district).all()
    nchoices = []
    for district in ndistricts:
        nchoices.append((district.id, district.district))
    form.district.choices = nchoices
    return render_template('region.html', form=form)
    
@app.route('/centralfl')
def central():
    form = DistrictForm()
    cdistricts = Info.query.filter_by(region='Central').order_by(Info.district).all()
    cchoices = []
    for district in cdistricts:
        cchoices.append((district.id, district.district))
    form.district.choices = cchoices
    return render_template('region.html', form=form)
    
@app.route('/otherfl')
def other():
    form = DistrictForm()
    odistricts = Info.query.filter_by(region='Other').order_by(Info.district).all()
    ochoices = []
    for district in odistricts:
        ochoices.append((district.id, district.district))
    form.district.choices = ochoices
    return render_template('region.html', form=form)

@app.route('/district', methods=['POST'])
def district_detail():
    district_id = request.form['district']
    info = Info.query.filter_by(id=district_id).first()
    return render_template('district.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)