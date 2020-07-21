from django.shortcuts import render,redirect
from .models import Entery,Balance


# Create your views here.

def validateNumber(request):
	if request.method == "POST":
		no = request.POST['number']
		a = Entery.objects.filter(card_no=no)
		if a:
			return render(request,'pin.html',{'k':1})
		return render(request,'index.html',{"error":"Please Enter the Valid Card Number"})
	return render(request,'index.html')

def withdrawmoney(request):
	if request.method == "POST":
		pin = request.POST['number']
		k = request.POST['no']
		a = Entery.objects.filter(pin=pin)
		print(k)
		if a:
			for i in a:
				return render(request,'withdraw.html',{'name':i.name})
				break
		elif int(k)==3:
			return render(request,'face.html',{"error":"you enter pin 3 times. PLease reset it."})
		else:
			k = int(k)+1
			return render(request,'pin.html',{"error":"Try Again",'k':k})
		# return render(request,'pin.html',{"error":"Please Enter Correct pin"})
	return redirect('/')
	# return render(request,'index.html')


def balancemoney(request,name):
	a = Balance.objects.filter(Entery__name = name)
	print(a)
	if a:
		for i in a:
			return render(request,'balance.html',{'balance':i.balance,'name':name})
			break
	return redirect('/')

def debitmoney(request,name):
	if request.method == "POST":
		no = request.POST['number']
		a = Balance.objects.filter(Entery__name = name)
		if a:
			for i in a:
				actuall = int(i.balance) - int(no)
				print(actuall)
				Balance.objects.filter(Entery__name = name).update(balance=actuall)
				return render(request,'balance.html',{'balance':actuall})
				break
	return render(request,'debit.html',{'name':name})

def depositmoney(request,name):
	if request.method == "POST":
		no = request.POST['number']
		a = Balance.objects.filter(Entery__name = name)
		if a:
			for i in a:
				actuall = int(i.balance) + int(no)
				print(actuall)
				Balance.objects.filter(Entery__name = name).update(balance=actuall)
				return redirect('/')
				break
	return render(request,'deposit.html',{'name':name})

def updatepinmoney(request,name):
	if request.method == "POST":
		no = request.POST['number']
		if no:
			Entery.objects.filter(name = name).update(pin=no)
			return redirect('/')
	return render(request,'update.html',{'name':name})


from .face_recognition import return_id
def resetpin(request):
	ids = return_id()
	data = Entery.objects.filter(face_id = ids)
	if data:
		for i in data:
			name = i.name
			return render(request,'reset.html',{'name':name})
	else:
		return redirect('/',{"error":"Your face in not recognize"})
		# return render(request,'index.html',{"error":"Your face in not recognize"})

def cardpageshow(request):
	if request.method == "POST":
		no = request.POST['number']
		a = Entery.objects.filter(card_no=no)
		if a:
			return render(request,'face.html',{'k':1})
		return render(request,'index.html',{"error":"Please Enter the Valid Card Number"})
	return render(request,'cardpage.html')