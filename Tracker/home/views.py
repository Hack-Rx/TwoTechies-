import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect, reverse
import joblib

def home_form(request):
    if request.user.is_authenticated:
        return render(request, "home_form.html")
    else:
        return redirect(reverse('login'))

def home_view(request):
    if request.user.is_authenticated:
        loaded_model = joblib.load("model.pkl")
        
        
        age = int(request.POST['age'])
        #country = request.POST['country']
        #sex = int(request.POST['sex'])
        diffBreathe = int(request.POST['diffBreathe'])
        bodyPain = int(request.POST['bodyPain'])
        runnyNose = int(request.POST['runnyNose'])
        fever = int(request.POST['fever'])
        
        lst = [fever,bodyPain,age, runnyNose, diffBreathe]
        
        print(lst)
        df =pd.DataFrame([lst])
        df.columns=['fever','bodyPain','age', 'runnyNose', 'diffBreathe']
        
        result= loaded_model.predict_proba(df)[0][1]
        
        print(result)
        
        df = pd.read_csv('data.csv')
        
        context={"result":result}
        return render(request, "home.html",context)
        
    else:
        return redirect(reverse('login'))
