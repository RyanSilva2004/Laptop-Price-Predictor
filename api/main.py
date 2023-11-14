from flask import Flask, render_template, request
import pickle
import numpy as np

#Install Libraries Using The Terminal Flask,Pickle,Numpy,Pandas and SKLearn (for some usual way might not work : use pip install -U scikit-learn)


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    price_prediction = 0
    if request.method == 'POST':
        price_prediction = 0
        ram = request.form['ram']
        weight = request.form['weight']
        company = request.form['company']
        typename = request.form['typename']
        opsys = request.form['opsys']
        cpu = request.form['cpuname']
        gpu = request.form['gpuname']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')

        lap_feature_list =[]

        lap_feature_list.append(int(ram))
        lap_feature_list.append(float(weight))
        lap_feature_list.append(len(touchscreen))
        lap_feature_list.append(len(ips))


        #One Hot Encoded Lists In The Model

        company_list = ['acer','apple','asus','dell','hp','lenovo','msi','other','toshiba']
        typename_list = ['2in1convertible','gaming','netbook','notebook','ultrabook','workstation']
        opsys_list = ['linux','mac','other','windows']
        cpu_list = ['amd','intelcorei3','intelcorei5','intelcorei7','other']
        gpu_list = ['amd','intel','nvidia']

        ## Testing Whether The Feature List Is Correctly Appended
        #for item in company_list:
        #    if item == company:
        #        lap_feature_list.append(1)
        #    else :
        #        lap_feature_list.append(0)

        #print(lap_feature_list)

        #Using A Function Since Its much more easier
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    lap_feature_list.append(1)
                else:
                    lap_feature_list.append(0)

        traverse_list(company_list, company)
        traverse_list(typename_list, typename)
        traverse_list(opsys_list, opsys)
        traverse_list(cpu_list, cpu)
        traverse_list(gpu_list, gpu)

        #Method To Call The Model An Predict The Price
        def predict(list):
            filename = 'model/laptop_price_predictor.pickle'
            with open(filename,'rb') as file:
                model = pickle.load(file)
            pred_price = model.predict([list])
            return pred_price

        price_prediction = predict(lap_feature_list) #To Save The Predicted Price
        price_prediction = np.round(price_prediction[0],2)

                
       
    return render_template("index.html",price_prediction = price_prediction) #Renders The Html and Returns The Predicted Price
    
if __name__ == '__main__':
    app.run(debug=False)

