from flask import Flask,jsonify,render_template,request
from Project_app.utils import MedicalInsurance

app = Flask(__name__)

@app.route("/") 
def hello_flask():
    print("Welcome to Insurance Prediction System")   
    return render_template("index.html")

@app.route("/predict_charges", methods = ["GET", "POST"])
def insurance_charges():
    if request.method == "GET":
        print("We are in a GET Method")

        age = eval(request.args.get("age"))
        print ("after age")
        sex = (request.args.get("sex"))
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print("*********************** age, sex, bmi, children, smoker, region **********************\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.get_charges()
        return render_template("index.html", prediction = charges)

        print(f"Insurance charges are : {charges}")

app.run(host= "0.0.0.0", port= 5005, debug = False)
# http://192.168.0.104:5005

# if __name__ == "__main__":
# app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters