# -*- coding: utf-8 -*-
import os
import time
import hashlib
from src.visualization_output import output

from flask import Flask, render_template, redirect, url_for, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField, TextField

from geopy.geocoders import Nominatim
import geopy.geocoders as geocoders
import gmaps
import os
import pickle
from ipywidgets.embed import embed_minimal_html

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image Only!'), FileRequired(u'Choose a file!')])
    location = TextField("Location")
    submit = SubmitField(u'Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        for filename in request.files.getlist('photo'):
            location = request.form["location"]
            # saves the photos
            photos.save(filename, name=location + '.')
            for file in os.listdir(os.getcwd() + '/static'):
                if file.endswith('.png'):
                    fname = os.getcwd() + '/static/' + file
                    prediction(fname, location)
                    os.remove(fname)

        success = True
        return render_template('next.html')
    else:
        success = False
    return render_template('index.html', form=form, success=success)

def prediction(filename, location):
    output_list = []
    image_file = filename
    location_input = location
    predicted_word = output(image_file)

    geolocator = Nominatim(user_agent="Natural Disaster")
    location = geolocator.geocode(location_input)
    print(("Location Latitude, Longitude",location.latitude, location.longitude))
    print("predicted_word",predicted_word)
    latitude = location.latitude
    longitude = location.longitude


    if os.path.isfile("run_demo.pickle"):
        output_list = pickle.load(open("run_demo.pickle", "rb"))
        
    output_list.append((image_file,location.latitude,location.longitude,predicted_word))
                
    gmaps.configure(api_key="AIzaSyA8QY3k_68BaSlDTehnWd0Kf73h5z7cIjA")
    fig = gmaps.figure(map_type="SATELLITE")
    for image,lat,lon,prediction in output_list:
        color = ""
        if(prediction=="severe"):
            color = 'red'
        elif(prediction=="mild"):
            color = "yellow"
        else:
            color = "green"
        layer = gmaps.symbol_layer([(lat,lon)], fill_color=color, stroke_color=color)
        fig.add_layer(layer)

    pickle.dump(output_list,open( "run_demo.pickle", "wb" ) )

    new_name = os.getcwd() + '/templates/' + 'export.html'
    embed_minimal_html(new_name, views=[fig])


@app.route('/manage')
def manage_file():
    return render_template('manage.html')

@app.route('/map')
def get_map():
    return render_template('export.html')
                

@app.route('/open/<filename>')
def open_file(filename):
    file_url = photos.url(filename)
    return render_template('browser.html', file_url=file_url)



if __name__ == '__main__':
    app.run(debug=True)
