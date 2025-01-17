from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from GWG.models import *
from django.template import loader
import random


def welcome(request):
    res = render(request, "welcome.html")
    return res


def aboutus(request):
    res = render(request, "aboutus.html")
    return res


def registrationForm(request):
    res = render(request, "registration.html")
    return res


def registered(request):
    if request.method == "POST":
        username = request.POST["username"]
        if len(User.objects.filter(username=username)):
            userStatus = 1
        else:
            user = User()
            user.username = username
            user.password = request.POST["password"]
            user.name = request.POST["name"]
            user.classTh = request.POST["classTh"]
            user.mobileNo = request.POST["mobile"]
            user.email = request.POST["email"]
            user.save()
            userStatus = 2
    else:
        userStatus = 3
    context = {
        "userStatus": userStatus,
    }
    res = render(request, "registered.html", context)
    return res


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.filter(username=username, password=password)
        if len(user) == 0:
            loginError = "Invalid Username or password"
            res = render(request, "login.html", {"loginerror": loginError})
        else:
            request.session["username"] = user[0].username
            request.session["name"] = user[0].name
            request.session["firstLetter"] = (user[0].name)[0]
            res = HttpResponseRedirect("home")
    else:
        res = render(request, "login.html")
    return res


def homePage(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        res = render(request, "home.html")
    return res


def profile(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        user = User.objects.filter(username=request.session["username"])
        context = {"user": user}
        res = render(request, "profile.html", context)
    return res

def deleteUser(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            username = request.POST["username"]
            if len(User.objects.filter(username=username)):
                user = User.objects.filter(username=request.POST["username"])
                user.delete()
                userStatus = 1
                res = render(request, "deleteuser.html", context)
            else:
                userStatus = 2
            context = {"userStatus": userStatus}
            res = render(request, "deleteuser.html",context)
        else:
            res = render(request, "deleteuser.html")
    return res


def userDetails(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            username = request.POST["username"]
            if len(User.objects.filter(username=username)):
                user = User.objects.filter(username=request.session["username"])
                results = Result.objects.filter(username_id=user[0].username)
                userStatus=1
                context = {"user": user[0], "results": results,'userStatus':userStatus}
                res = render(request, "userDetails.html", context)
            else:
                userStatus = 2
                context = {'userStatus':userStatus}
            res = render(request, "userDetails.html",context)
        else:
            res = render(request, "userDetails.html")
    return res


def deleteQue(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            qid = request.POST["qid"]
            if len(Question.objects.filter(qid=qid)):
                question = Question.objects.filter(qid=request.POST["qid"])
                question.delete()
                questionStatus = 1
            else:
                questionStatus = 2
            context = {"questionStatus": questionStatus}
            res = render(request, "deleteQue.html",context)
        else:
            res = render(request, "deleteQue.html")
    return res


def allProfile(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        users = User.objects.all()
        context = {"users": users}
        res = render(request, "allProfile.html", context)
    return res


def editProfile(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            user = User()
            user.username = request.session["username"]
            user.test_attempted = request.POST["test_attempted"]
            user.points = request.POST["points"]
            user.password = request.POST["password"]
            user.name = request.POST["name"]
            user.classTh = request.POST["classTh"]
            user.email = request.POST["email"]
            user.mobileNo = request.POST["mobile"]
            user.save()
            res = res = HttpResponseRedirect("profile")
        else:
            user = User.objects.filter(username=request.session["username"])
            context = {"user": user}
            res = render(request, "editProfile.html", context)
    return res


def setQuestions(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        questionStatus = 1
        if request.method == "POST":
            question = Question()
            question.classTh = request.POST["classTh"]
            question.que = request.POST["question"]
            question.a = request.POST["optionA"]
            question.b = request.POST["optionB"]
            question.c = request.POST["optionC"]
            question.d = request.POST["optionD"]
            question.ans = request.POST["currectOption"]
            question.save()
            questionStatus = 2
        context = {"questionStatus": questionStatus}
        res = render(request, "setQuestions.html", context)
    return res


def showQuestions(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        if request.method == "POST":
            questions = Question.objects.filter(classTh=request.POST["classTh"])
            context = {
                "questions": questions,
            }
            res = render(request, "showQuestions.html", context)
        else:
            res = render(request, "showQuestions.html")
    return res


def testPaper(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        user = User.objects.filter(username=request.session["username"])
        classth = user[0].classTh
        n = int(request.GET["n"])
        question_pool = list(Question.objects.filter(classTh=classth))
        random.shuffle(question_pool)
        questions_list = question_pool[:n]
        context = {
            "questions": questions_list,
        }
        res = render(request, "test_paper.html", context)
    return res


def calculateTestResult(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        total_attempt = 0
        total_right = 0
        total_wrong = 0
        qid_list = []
        for k in request.POST:
            if k.startswith("qno"):
                qid_list.append(int(request.POST[k]))
        for n in qid_list:
            question = Question.objects.get(qid=n)
            try:
                if question.ans == request.POST["q" + str(n)]:
                    total_right += 1
                else:
                    total_wrong += 1
                total_attempt += 1
            except:
                pass
        points = (total_right - total_wrong) / len(qid_list) * 10
        # store result in result table
        result = Result()
        result.username = User.objects.get(username=request.session["username"])
        result.attempt = total_attempt
        result.right = total_right
        result.worng = total_wrong
        result.points = points
        result.save()
        # Update user Table
        user = User.objects.get(username=request.session["username"])
        user.test_attempted += 1
        user.points = (
            user.points * (user.test_attempted - 1) + points
        ) / user.test_attempted
        user.save()
        res = HttpResponseRedirect("result")
    return res


def showAllResult(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        user = User.objects.filter(username=request.session["username"])
        results = Result.objects.filter(username_id=user[0].username)
        context = {"user": user[0], "results": results}
        res = render(request, "showAllResult.html", context)
    return res


def showTestResult(request):
    if "name" not in request.session.keys():
        res = HttpResponseRedirect("login")
    else:
        # fect lastest result from Result table
        result = Result.objects.filter(
            resultid=Result.objects.latest("resultid").resultid,
            username_id=request.session["username"],
        )
        context = {"result": result}
        res = render(request, "result.html", context)
    return res


def logout(request):
    if "name" in request.session.keys():
        del request.session["username"]
        del request.session["name"]
    res = HttpResponseRedirect("login")
    return res
