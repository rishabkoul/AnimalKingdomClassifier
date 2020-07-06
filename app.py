from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
# Load the Model back from file
with open("zoomodel.pkl", 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        if request.form['hair'] == 'Yes':
            hair = 1
        else:
            hair = 0
        if request.form['feathers'] == 'Yes':
            feathers = 1
        else:
            feathers = 0
        if request.form['eggs'] == 'Yes':
            eggs = 1
        else:
            eggs = 0
        if request.form['milk'] == 'Yes':
            milk = 1
        else:
            milk = 0
        if request.form['airborne'] == 'Yes':
            airborne = 1
        else:
            airborne = 0
        if request.form['aquatic'] == 'Yes':
            aquatic = 1
        else:
            aquatic = 0
        if request.form['predator'] == 'Yes':
            predator = 1
        else:
            predator = 0
        if request.form['toothed'] == 'Yes':
            toothed = 1
        else:
            toothed = 0
        if request.form['backbone'] == 'Yes':
            backbone = 1
        else:
            backbone = 0
        if request.form['breathes'] == 'Yes':
            breathes = 1
        else:
            breathes = 0
        if request.form['venomous'] == 'Yes':
            venomous = 1
        else:
            venomous = 0
        if request.form['fins'] == 'Yes':
            fins = 1
        else:
            fins = 0

        if request.form['tail'] == 'Yes':
            tail = 1
        else:
            tail = 0
        if request.form['domestic'] == 'Yes':
            domestic = 1
        else:
            domestic = 0
        if request.form['catsize'] == 'Yes':
            catsize = 1
        else:
            catsize = 0

        # hair = int(request.form['hair'])
        # feathers = int(request.form['feathers'])
        # eggs = int(request.form['eggs'])
        # milk = int(request.form['milk'])
        # airborne = int(request.form['airborne'])
        # aquatic = int(request.form['aquatic'])
        # predator = int(request.form['predator'])
        # toothed = int(request.form['toothed'])
        # backbone = int(request.form['backbone'])
        # breathes = int(request.form['breathes'])
        # venomous = int(request.form['venomous'])
        # fins = int(request.form['fins'])
        legs = int(request.form['legs'])
        # tail = int(request.form['tail'])
        # domestic = int(request.form['domestic'])
        # catsize = int(request.form['catsize'])
        prediction = model.predict([[hair, feathers, eggs, milk, airborne, aquatic, predator,
                                     toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize]])
        # output = round(prediction[0], 2)
        # if output < 0:
        #     return render_template('index.html', prediction_texts="Sorry you cannot sell this car")
        # else:
        #     return render_template('index.html', prediction_text="You Can Sell The Car at {}".format(output))
        if(prediction[0] == 1):
            output = 'Mammal'
        elif prediction[0] == 2:
            output = 'Bird'
        elif prediction[0] == 3:
            output = 'Reptile'
        elif prediction[0] == 4:
            output = 'Fish'
        elif prediction[0] == 5:
            output = 'Amphibian'
        elif prediction[0] == 6:
            output = 'Bug'
        elif prediction[0] == 7:
            output = 'Invertebrate'
        return render_template('index.html', prediction_text="Your animal is a {}".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
