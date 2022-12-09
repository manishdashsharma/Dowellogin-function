import json
from django.shortcuts import render ,redirect
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from dowelllogin.utils import dowellconnection


def redirect_to_login():
    return redirect(
        "https://100014.pythonanywhere.com/?redirect_url=http://127.0.0.1:8000/"
    )

@csrf_exempt
def home(request):
    session_id = request.GET.get("session_id", None)
    code=request.GET.get('id',None)
    if session_id:
        url="https://100014.pythonanywhere.com/api/userinfo/"
        response=requests.post(url,data={"session_id":session_id}) 
        profile_detais= json.loads(response.text)
        request.session["userinfo"]=profile_detais["userinfo"]
        request.session["user_name"]=profile_detais["userinfo"]["username"]
        request.session["portfolio_info"]=profile_detais["portfolio_info"]
        request.session["role"]=profile_detais["portfolio_info"]["role"]
        return redirect('/page')
    elif code == '100093':
        url="https://100093.pythonanywhere.com/api/userinfo/"
        response=requests.post(url,data={"session_id":session_id}) 
        profile_detais= json.loads(response.text)
        request.session["userinfo"]=profile_detais["userinfo"]
        request.session["user_name"]=profile_detais["userinfo"]["username"]
        request.session["portfolio_info"]=profile_detais["portfolio_info"]
        request.session["role"]=profile_detais["portfolio_info"]["role"]
        return redirect("/page")
    else:
      return redirect_to_login()  


def page(request):
    if request.session.get("userinfo"):
        username= request.session["user_name"]
        role = request.session["role"]
        return render(request,'index.html', context={"user_name":username , "role":role} )
    else:
        return redirect_to_login()

def logout(request):
    del request.session["userinfo"]
    del request.session["user_name"]
    del request.session["portfolio_info"]
    del request.session["role"]
    return redirect("https://100014.pythonanywhere.com/sign-out")
