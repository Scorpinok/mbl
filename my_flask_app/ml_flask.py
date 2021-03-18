from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import dill
import category_encoders
import sklearn
import catboost


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.form['filename']

        df = pd.read_csv(file, sep=",")
        data = df.drop(['id'], axis=1)

        with open("catboost_pipeline2.dill", "rb") as f:
            pipeline = dill.load(f)
        
        
        prediction = pipeline.predict(data)

        pd.DataFrame({'Id': [i for i,_ in enumerate(prediction)],'Preds':prediction}).to_csv("_predictions.csv", index=False)

        prediction = '_predictions.csv'


    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0')