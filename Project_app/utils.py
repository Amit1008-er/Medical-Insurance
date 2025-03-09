import numpy as np
import pandas as pd
import json
import pickle
import config



class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_" + region

    def load_models(self):
        with open (config.Model_file_path, "rb") as f:
            self.model=pickle.load(f)    
        
        with open (config.Json_file_path,"r") as f:
            self.json_data=json.load(f)

    def get_charges(self):
        self.load_models()

        self.region_index=self.json_data["columns"].index(self.region)

        test_array=np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.age
        test_array[1] = self.json_data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data["smoker"][self.smoker]
        test_array[self.region_index] = 1

        print(test_array)
        charges = self.model.predict([test_array])[0]
        return charges


if __name__== "__main__":
    age = 32
    sex = "male"
    bmi = 24
    children = 1
    smoker = "no"
    region = "northwest"

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_charges()
    print(f"Medical Ins charges are {charges}")


        


    