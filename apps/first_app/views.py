from django.shortcuts import render,redirect
import random,datetime
# \n not working and when i use
# should every function return only render or redirect or etc
# def initialize(): can i write like tihis outside and return nothing
#should do this without hidden inputs
#no change even if i dont put post

def index(request):
    # request.session.flush()
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'message' in request.session:
        request.session['message'] = []
    return render(request,"first_app/index.html")
def logic(request):
    if request.POST['action'] =="farm":
        money = random.randint(10,20)
        request.session['gold'] +=money
        mymessage = "Earned "+ str (money)+ " golds from the farm "+str(datetime.datetime.now())
        request.session['message'].append(mymessage)
        # "Earned" , str (money), " golds from the farm" + str(datetime.datetime.now()))
    elif request.POST['action'] =="cave":
        money = random.randint(5,10)
        request.session['gold'] +=money
        mymessage = "Earned "+ str (money)+ " golds from the cave "+str(datetime.datetime.now())
        request.session['message'].append(mymessage)
    elif request.POST['action'] =="house":
        money = random.randint(2,5)
        request.session['gold'] +=money
        mymessage = "Earned "+ str (money)+ " golds from the house "+str(datetime.datetime.now())
        request.session['message'].append(mymessage)
    elif request.POST['action'] =="casino":
        test = random.randint(0,1)
        print test
        if test==1:
            money = random.randint(0,50)
            request.session['gold'] +=money
            mymessage = "Earned "+ str (money)+ " golds from the casino "+str(datetime.datetime.now())
        elif test==0:
            money = random.randint(0,50)
            request.session['gold'] -=money
            mymessage = "Lost "+ str (money)+ " golds from the casino "+str(datetime.datetime.now())
        request.session['message'].append(mymessage)
    elif request.POST['action'] =="reset":
        request.session.clear()


    return redirect('/')
