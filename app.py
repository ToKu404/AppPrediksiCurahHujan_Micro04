from flask import Flask, render_template, request
import pickle
import preprocess

app = Flask(__name__, static_url_path='/static')

# Load Pickle
model = pickle.load(open("prediction.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods = ["POST"])
def result():
    if request.method == 'POST':
        sun = request.form["sun"] if request.form["sun"]!="" else 0
        avg_temp = request.form["avg_temp"] if request.form["avg_temp"]!="" else 0
        humidity = request.form["humidity"] if request.form["humidity"]!="" else 0
        day = request.form["day"] if request.form["day"]!="" else 0
        
        if(sun == 0 or avg_temp == 0 or humidity == 0 or day == 0):
            rain = "-"
        else:
            r = preprocess.preprocessing([sun, avg_temp, humidity, day])
            rain = model.predict(r)
            rain = "{0:,.2f}".format(rain[0])
    return render_template("result.html", ret = rain, s=sun, t=avg_temp,h=humidity,d=day)

if __name__ == '__main__':
    app.run(debug=True)