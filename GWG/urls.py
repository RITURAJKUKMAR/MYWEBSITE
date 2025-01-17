from django.urls import path
from GWG.views import *

app_name = "GWG"


urlpatterns = [
    path("", welcome, name="welcome"),
    path("aboutus", aboutus, name="aboutus"),
    path("new-user", registrationForm, name="registrationForm"),
    path("store-user", registered, name="storeUser"),
    path("login", login, name="login"),
    path("home", homePage, name="home"),
    path("profile", profile, name="profile"),
    path("deleteUser", deleteUser, name="deleteUser"),
    path("userDetails", userDetails, name="userDetails"),
    path("deleteQue", deleteQue, name="deleteQue"),
    path("editProfile", editProfile, name="editProfile"),
    path("allProfile", allProfile, name="allProfile"),
    path("set-questions", setQuestions, name="setQuestions"),
    path("show-Questions", showQuestions, name="showQuestions"),
    path("test-Paper", testPaper, name="testPaper"),
    path("calculate-result", calculateTestResult, name="caculateTest"),
    path("showAllResult", showAllResult, name="showAllResult"),
    path("result", showTestResult, name="result"),
    path("logout", logout, name="logout"),
]
