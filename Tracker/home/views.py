import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect, reverse
import joblib
from .forms import EntryForm

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect(reverse('login'))

def home_form(request):
        return render(request, "home_form.html")

def facts(request):
    return render(request, "facts.html")

def stats(request):
    return render(request, "stats.html")

def home_view(request):
    if request.user.is_authenticated:
        loaded_model = joblib.load("model.pkl")
        
        
        age = int(request.POST['age'])
        country = request.POST['country']
        sex = request.POST['sex']
        diffBreathe = int(request.POST['diffBreathe'])
        #sore = int(request.POST['sore'])
        bodyPain = int(request.POST['bodyPain'])
        runnyNose = int(request.POST['runnyNose'])
        nasal = int(request.POST['nasal'])
        diarrhea = int(request.POST['diarrhea'])
        #tired = int(request.POST['tired'])
        fever = int(request.POST['fever'])
        dry = float(request.POST['dry'])
        #contact = request.POST['contact']
        #severe = request.POST['severe']
        """
        age = request.POST['age']
        country = request.POST['country']
        sex = int(request.POST['sex'])
        breathe = int(request.POST['breathe'])
        sore = int(request.POST['sore'])
        pain = int(request.POST['pain'])
        nose = int(request.POST['nose'])
        nasal = int(request.POST['nasal'])
        diarrhea = int(request.POST['diarrhea'])
        tired = int(request.POST['tired'])
        fever = int(request.POST['fever'])
        dry = float(request.POST['dry'])
        contact = request.POST['contact']
        severe = request.POST['severe']
        
       
        """
        lst = [fever,bodyPain,age, runnyNose, diffBreathe]
        #lst = [age, country,sex, breathe, sore, pain, nose, nasal, diarrhea, tired, fever, dry, contact, severe]
        print(lst)
        df =pd.DataFrame([lst])
        df.columns=['fever','bodyPain','age', 'runnyNose', 'diffBreathe']
        #df.columns =['age','country','sex',' breathe', 'sore', 'pain', 'nose', 'nasal', 'diarrhea', 'tired', 'fever', 'dry', 'contact', 'severe']
        result= loaded_model.predict_proba(df)[0][1]
        print(result)
        context={"result":result}
        df = pd.read_csv('data.csv')
        if result <0.5:
            return render(request, "mild.html",context)

        elif result >=0.3 and result < 0.7:
            return render(request, "severe.html",context)

        else:
            return render(request, "severe.html",context)
        
    else:
        return redirect(reverse('login'))
