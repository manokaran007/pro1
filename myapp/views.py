from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required




def register(request):
    if (request.method == 'POST'):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pword = request.POST.get('password')
        cuser=User.objects.create_user(uname,email,pword)
        cuser.save()
        
        
        return redirect('user_login')
        
    return render(request,"register.html")

def user_login(request):
    if (request.method == 'POST'):
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        users = authenticate(request,username=uname,password=pword)
        print(uname,pword)
        print(users)
        if users is not None:
            login(request,users)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    
    return render(request,'home.html')
def course(request):
    
    return render(request,'course.html')
def computer(request):
    return render(request,'computer/computer.html')

def com1(request):
    return render(request,'computer/1.html')


def com2(request):
    return render(request,'computer/2.html')

def com3(request):
    return render(request,'computer/3.html')

def com4(request):
    return render(request,'computer/4.html')

def com5(request):
    return render(request,'computer/5.html')

def com6(request):
    return render(request,'computer/6.html')

def com7(request):
    return render(request,'computer/7.html')

def com8(request):
    return render(request,'computer/8.html')

def comtest(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Computer.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        if request.user.is_authenticated:
            save_quiz_result(user_name=request.user.username, score=score)
        
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=Computer.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'computer/quiz.html',context)
    

def maths(request):
    return render(request,'maths/maths.html')
def mat1(request):
    return render(request,'maths/1.html')
def mat2(request):
    return render(request,'maths/2.html')
def mat3(request):
    return render(request,'maths/3.html')
def mat4(request):
    return render(request,'maths/4.html')
def mat5(request):
    return render(request,'maths/5.html')
def mat6(request):
    return render(request,'maths/6.html')
def mat7(request):
    return render(request,'maths/7.html')
def mat8(request):
    return render(request,'maths/8.html')

def mattest(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Maths.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        if request.user.is_authenticated:
            save_quiz_result(user_name=request.user.username, score=score)
        
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=Maths.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'maths/quiz.html',context)


def english(request):
    return render(request,'english/english.html')
def eng1(request):
    return render(request,'english/1.html')
def eng2(request):
    return render(request,'english/2.html')
def eng3(request):
    return render(request,'english/3.html')
def eng4(request):
    return render(request,'english/4.html')
def eng5(request):
    return render(request,'english/5.html')
def eng6(request):
    return render(request,'english/6.html')
def eng7(request):
    return render(request,'english/7.html')
def eng8(request):
    return render(request,'english/8.html')

def engtest(request):
    if request.method == 'POST':
        print(request.POST)
        questions=English.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        if request.user.is_authenticated:
            save_quiz_result(user_name=request.user.username, score=score)
        
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=English.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'english/quiz.html',context)
    
def tamil(request):
    return render(request,'tamil/tamil.html')
def tam1(request):
    return render(request,'tamil/1.html')
def tam2(request):
    return render(request,'tamil/2.html')
def tam3(request):
    return render(request,'tamil/3.html')
def tam4(request):
    return render(request,'tamil/4.html')
def tam5(request):
    return render(request,'tamil/5.html')
def tam6(request):
    return render(request,'tamil/6.html')
def tam7(request):
    return render(request,'tamil/7.html')
def tam8(request):
    return render(request,'tamil/8.html')

def tamtest(request):
    if request.method == 'POST':
        print(request.POST)
        questions=English.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        if request.user.is_authenticated:
            save_quiz_result(user_name=request.user.username, score=score)
        
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=English.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'tamil/quiz.html',context)

def save_quiz_result(user_name, score):
    try:
        quiz_result = QuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except QuizResult.DoesNotExist:
        QuizResult.objects.create(user_name=user_name, score=score)

def leaderboard(request):
    top_results = QuizResult.objects.order_by('-score')[:10]

    context = {
        'top_results': top_results
    }

    return render(request, 'leaderboard.html', context)

def game(request):
    return render(request,'game.html')

