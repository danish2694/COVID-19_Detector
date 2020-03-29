from django.shortcuts import render
from django.http import HttpResponse
import pickle

file = open('./App/model.pkl','rb')
clf = pickle.load(file)
file.close()

def index(request):
	if request.method == "POST":
		# mydata = request.form
		fever = int(request.POST.get('fever'))
		age = int(request.POST.get('age'))
		pain = int(request.POST.get('pain'))
		runnyNose = int(request.POST.get('runnyNose'))
		diffBreath = int(request.POST.get('diffBreath'))
		#code for inference
		inputFeatures = [fever,age,pain,runnyNose,diffBreath]
		infoProbability = clf.predict_proba([inputFeatures])[0][1]
		infectionProbability=round((infoProbability)*100)
		params = {'infectionProbability':infectionProbability}
		return render(request,'show.html',params)
	else:
		return render(request,'index.html')

def contact(request):
	return render(request,'contactus.html')