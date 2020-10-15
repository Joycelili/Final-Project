from flask import Flask, request
import image_prep as ip
import pickle
import matplotlib.pyplot as plt 


app= Flask(__name__)

# necesario en pythonanywhere
#PATH=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home ():
    cover = open('template/unindex.html', 'r', encoding='utf-8').read() 
    return cover

@app.route("/predict",methods=['GET', 'POST'])
def prediccion():
    if request.method== "POST":
        animal=request.form.get("buscador")
    else:
        animal=request.args.get("buscador")
    
    model = pickle.load(open("output/LogisticRegression3.sav", 'rb'))
    predic_show= ip.show_image_prediction(animal)
    return predict_show._repr_hmtl_()


if __name__=="__main__":
    app.run(debug=False)
