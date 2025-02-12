from django.shortcuts import render,redirect
from django.http import HttpResponse

from . import myquery
# Create your views here.


def home(request):

    return HttpResponse('HI')

def calculator(request):

    a = request.POST.get('1st')
    b = request.POST.get('2nd')
    d = {}

    if a!=None and b!=None:
        s = int(a) + int(b)
        d = {'ad' : s}
        
    return render(request,'calc.html',d)

def navbar(request):
    return render(request,'navbar.html')

def landingpage(request):
    return render(request,'navbar.html')


def userdata(request):

    a = request.POST.get('nm')
    b = request.POST.get('em')
    c = request.POST.get('ph')


    if a!=None and b!=None and c!=None:
        print(a,b,c)
        myquery.insertuserdata(a,b,c)

        return render(request,'userform.html',{'stat': "Data Inserted"})
    else:
        return render(request,'userform.html',{'stat' : "Data Not Inserted"})

def fetchdata(request):
    data = myquery.fetchuserdata()
    print(data)

    return render(request, 'table_details.html', {'details': data})     



def update_userdata(request):
    id = request.GET.get('v')
    print(id)
    data = myquery.fetchuser_details(id)

    user_data = {

    'name' : data[0][1],
    'mail' : data[0][2],
    'phone' : data[0][3]
    }

    a = request.POST.get('nm')
    b = request.POST.get('em')
    c = request.POST.get('ph')


    if a!=None and b!=None and c!=None:
        print(a,b,c)
        myquery.update_userdata(a,b,c,id)

        return redirect('fetchdata') 

    return render(request,'update.html', {'data':user_data})


 


def deleteuserdata(request):

    id = request.GET.get('v')

    myquery.deluserdata(id)

    return redirect('fetchdata')


import joblib
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse

# Load the saved model
model = joblib.load("userdata/new_credit_card_fraud_model.pkl")

def predict_fraud(request):
    result = None
    if request.method == 'POST':
        try:

            print("Received POST data:", request.POST)

            # Extract features from the form
            feature1 = float(request.POST.get('Transaction Amount'))
            feature2 = float(request.POST.get('Transaction Frequency'))
            feature3 = float(request.POST.get('Account Age (Months)'))
            feature4 = float(request.POST.get('Location Mismatch'))
            feature5 = float(request.POST.get('Time of Transaction'))

            if None in (feature1, feature2, feature3, feature4, feature5):
                raise ValueError("All form fields are required.")
            
            # Add more features as per model requirements
            
            # Prepare data for prediction
            features = np.array([[feature1, feature2, feature3, feature4, feature5]])
            print("Features sent to model:", features)


            prediction = model.predict(features)
            print("Model Prediction:", prediction) 
            
            result = "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"
        except Exception as e:
            result = f"Error: {str(e)}"
    print("✅ Final Result Before Rendering:", result)
    return render(request, 'creditcard.html', {'result': result})

