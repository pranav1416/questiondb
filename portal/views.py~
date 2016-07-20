from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .models import Info,Question
from django.contrib.auth import authenticate, login, logout
#import os,subprocess,sys
#from datetime import datetime,timedelta,date
from django.http import HttpResponse
#import tempfile			
#import time			
#from random import random
#from questiondb import settings
#base=settings.BASE_DIR
# Create your views here.


            
def home(request):
    return render (request,'Signup.html')

#signup html has called signup function
def signup(request):
    if (request.method == "POST") :
        if (User.objects.filter(username=str(request.POST['username']))).exists():
            return render (request,'Signup.html',{'message':'The username already exists'})   
        else:
            username=request.POST['username']
            password=request.POST['password']
            temp=User.objects.create_user(username=username,password=password,first_name=request.POST['first_name'])
            user=authenticate(username=username,password=password)
            login(request,user)
            Info.objects.create(user=request.user)
            return render(request,'Question_page.html')
    else:
        return render (request,'Signup.html') 
              
#another form in the sign up page will call the following function
def login_function(request):
    if(request.method == "POST") :
        username = request.POST['username']
        password = request.POST['password']
        if((username=="seniorlogin") and (password=="forcelogin")) :
            q = Question.objects.get(pk=1)
            return render(request,'seniorpage.html',{'question':q})######################################################Senior page for upvotes 
        else:
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return render(request,'Question_page.html')
            else :
                return render(request,'Signup.html',{'message1':'Invalid Username or password'})
    else :
        return render(request,'Signup.html')
#submit button in Question_page.html will call the following function
def question_store(request):
    if (request.method == "POST"):
        questiontext= str(request.POST['question_text'])
        Question.objects.create(question_text=str(questiontext),option_a=str(request.POST['option_a']),option_b=str(request.POST['option_b']),option_c=str(request.POST['option_c']),option_d=str(request.POST['option_d']),correct_option=str(request.POST['correct_option'] ),user=request.user)
        q = Info()
        q = Info.objects.get(user = request.user)
        #print q.roll_no
        q.total = q.total + 1
        q.save()
        return render(request,'Question_page.html')
    else:
        return render(request,'Question_page.html')

def questionpage(request):
    return render(request,'Question_page.html')
def leaderboard(request):
    userdata = Info.objects.all()
    for i in userdata:
        q = Question.objects.filter(user = i.user)
        i.upvotes_senior = 0
        i.upvotes_junior = 0
        for j in q:
            i.upvotes_senior = i.upvotes_senior+j.upvotes_senior
            i.upvotes_junior = i.upvotes_junior+j.upvotes_junior
        i.save()
    board = Info.objects.all().order_by('-upvotes_senior','-upvotes_junior','-total')
    return render (request,'Leaderboard.html',{'object':board})
def question_list(request):
    q = Question.objects.filter(user = request.user)
    return render(request,'question_list.html',{'question_data':q})

def next_question(request):     ####################################################
    if request.method == "POST" :
        qid = int(request.POST['qid'])
        upvotes_senior = request.POST['upvotes_senior']
        upvotes_junior = request.POST['upvotes_junior']
        q = Question.objects.get(pk = qid)
        if(upvotes_senior=='1') :
            q.upvotes_senior = q.upvotes_senior+1
            print 'here'
        if(upvotes_junior=='1') :
            q.upvotes_junior = q.upvotes_junior+1
        print upvotes_senior
        #q.upvotes_senior = q.upvotes_senior+upvotes_senior
        #q.upvotes_junior = q.upvotes_junior+upvotes_junior
        q.save()
        qid = qid+1
        try:
            q = Question.objects.get(pk = qid)
        except:
            qid=qid-1
            q = Question.objects.get(pk = qid)
        return render(request,'seniorpage.html',{'question':q})
            
    else:
        return render(request,'Signup.html')

def go_question(request):       ##################################################
    if request.method == "POST":
        qid = request.POST['qid']
        try:
            q = Question.objects.get(pk=qid)
        except:
            q = Question.objects.get(pk=1)
        return render(request,'seniorpage.html',{'question':q})
    else:
        return render(request,'Signup.html') 

def leaderboard_redirect(request):
    q = Question.objects.get(pk=1)
    return render(request,'seniorpage.html',{'question':q}) 

def senior_leaderboard(request):
    userdata = Info.objects.all()
    for i in userdata:
        q = Question.objects.filter(user = i.user)
        i.upvotes_senior = 0
        i.upvotes_junior = 0
        for j in q:
            i.upvotes_senior = i.upvotes_senior+j.upvotes_senior
            i.upvotes_junior = i.upvotes_junior+j.upvotes_junior
        i.save()
    board = Info.objects.all().order_by('-upvotes_senior','-upvotes_junior','-total')
    return render (request,'leaderboard.html',{'object':board})
def log_out(request):
    logout(request)
    return render(request,'Signup.html')



#seniorpage.html  upvotesection,questiondisplay,logout,leaderboard
###################################################################################to be continued
"""
def question_view(request):
    elif request.user.is_authenticated():
        q=Question.objects.all()
        return render(request,'Hub.html',{'questions':q})
                      # To display question hub
    else:
        return render(request,'Loginpage.html')
        
def question_list(request,question_id):
    if time_passed()<start_seconds_left:
        return render(request,'Index.html')
    elif time_passed()>end_seconds_left:
        return leaderboard(request)
    elif request.user.is_authenticated():
        q=Question.objects.get(pk=question_id)
        if(QuestionData.objects.filter(user=request.user,question=q)).exists():
            print "The QuestionData object already exists"
        else:
            os.mkdir(os.path.join(base,"judge","user",str(request.user.id),str(question_id)))
            QuestionData.objects.create(user=request.user,question=q)                                                                     
        return render(request,'Editor.html',{'question':q})	############
    else:
        return render(request,'Loginpage.html')
        
def return_editor_page(request,question_id):
    if time_passed()<start_seconds_left:
        return render(request,'Index.html')
    elif time_passed()>end_seconds_left:
        return leaderboard(request)
    elif request.user.is_authenticated():
        q = Question.objects.get(pk=question_id)
        return render(request,'Editor.html',{'question':q})   ##############
    else:
        return render(request,'Loginpage.html')
        
def code_test(request,question_id):
    if time_passed()<start_seconds_left:
        return render(request,'Index.html')
    elif time_passed()>end_seconds_left:
        return leaderboard(request)
    elif request.user.is_authenticated:
        if request.method == "POST" :
            language = request.POST['language']
            flag = request.POST['flag']
            print flag         
            try:    
                code = request.FILES['doc'].read()
            except:
                code = request.POST['user_code']	
        loadbuffer = ""
        reload(sys)
        sys.setdefaultencoding('utf-8')
        location = base+"/judge/user/"+str(request.user.id)+"/"+str(question_id)+"/"+str(request.user.id)+"_"+str(question_id)+"."+language
        if flag == "loadbuffer":
            print location
            if os.path.exists(location):
                if os.path.isfile(location):
                    fileobject = open(location,"r")
                    print location
                    loadbuffer = fileobject.read()
                    fileobject.close()
                else :
                    print "No file"
            else:
                print "path dosent exists"
            return HttpResponse(loadbuffer)
        
        if code != "":
            fileobject = open(location,"w")
            fileobject.write(code)
            fileobject.close()
        if flag == "save":
            return HttpResponse("Your file is saved")
        elif flag == "compile":
            if language == "c":
                cmd = ['gcc', location]
            else:
                cmd = ['g++', location]
            error = terminalfunc(cmd,location)
            if error == "":
                error = "Compilation Successful"
            return HttpResponse(error)
        elif flag=="run":
            if request.method == "POST":
                status = request.POST['status']
                custom = request.POST['custom']
            if status == '1':                       # Making the input file in case of custom input
                inputlocation = base+"/judge/input/"+str(request.user.id)+"/"+str(request.user.id)+"_"+str(question_id)+".in"
                fileobject = open(inputlocation, "w")
                fileobject.write(custom)
                fileobject.close()
            cmd=['python',base+'/judge/customj.py',str(request.user.id)+"_"+str(question_id)+"."+language,str(status)]
            outputfile = terminalfunc(cmd,location)
                                                    # call the judge and pass the input.Get the result and pass it to the html template
            if "Compile Time Error" in outputfile:               # If compile time error 
                if language == "c":
                    cmd = ['gcc', location]
                else:
                    cmd = ['g++', location]
                outputfile = terminalfunc(cmd,location)
                outputfile = "Compile Time Error<br>"+outputfile
            return HttpResponse(outputfile)
        else:
            tempuser = UserData.objects.get(user=request.user)
            tempuser.subid = tempuser.subid + 1
            cmd=['python',base+'/judge/jmain.py',str(request.user.id)+"_"+str(question_id)+"."+language]
            with tempfile.TemporaryFile() as tempf:
                output = subprocess.Popen(cmd, stdout=tempf, stderr=tempf, stdin=tempf)
                output.wait()
                tempf.seek(0)
                outputfile = tempf.read()
            score = outputfile.count('1')
            score = score*20
            print score 
            subdata = QuestionData.objects.get(user=request.user,question=Question.objects.get(pk=question_id))
            if subdata.score < score :           #if score obtained is more than the last time
                tempuser.totaltime = tempuser.totaltime-subdata.timereq
                timetaken = (datetime.now()-tempuser.start).seconds
                subdata.timereq = timetaken                         #update time
                tempuser.totaltime = tempuser.totaltime+subdata.timereq
                tempuser.score = tempuser.score-subdata.score
                subdata.score = score                               #update score
                tempuser.score = tempuser.score+subdata.score
                tempuser.save()
                subdata.save()
            print outputfile            #For testing purpose
            if "-9999" in outputfile:
                return render (request,'Submitpage.html',{'question':question_id,'out1':'C','out2':'C','out3':'C','out4':'C','out5':'C'})

            elif "7" in outputfile:
                return render (request,'Submitpage.html',{'question':question_id,'out1':'A','out2':'A','out3':'A','out4':'A','out5':'A'})
            else:
                outputfile = outputfile.replace('1','R')
                outputfile = outputfile.replace('-99','W')
                outputfile = outputfile.replace('5','T')
            outputfile = outputfile.replace(' ','')
            return render (request,'Submitpage.html',{'question':question_id,'out1':outputfile[1],'out2':outputfile[3],'out3':outputfile[5],'out4':outputfile[7],'out5':outputfile[9]})
    else:
        return render(request,'Loginpage.html')      
            
def leaderboard(request):
    board = UserData.objects.all().order_by('-score','totaltime')
    return render (request,'Leaderboard.html',{'object':board})
    
def log_out(request):
    logout(request)
    return leaderboard(request)
            
def terminalfunc(cmd,location):
    with tempfile.TemporaryFile() as tempf:
        output = subprocess.Popen(cmd, stdout=tempf, stderr=tempf, stdin=tempf)
        output.wait()
        tempf.seek(0)
        outputfile = tempf.read()
    outputfile = outputfile.replace(location, '<br>')
    outputfile = outputfile.replace("\n", "<br>")
    return outputfile
            
#R  right answer
#T  TLE
#W  Wrong answer
#C  Compile time error
#A  abnormal termination    
    """
