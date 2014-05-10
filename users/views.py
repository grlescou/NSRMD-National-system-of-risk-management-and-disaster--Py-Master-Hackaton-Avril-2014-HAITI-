from django.shortcuts import render
from django.shortcuts import redirect,render_to_response
from django.contrib.auth.models import User, check_password, Group
from django.template import RequestContext
from users.forms import LoginForm
# from gestionR.models import HaitiAdm3Stats
from django.http import HttpResponse
# Create your views here.
def login(request):
    if 'userid' in request.session:
        return redirect("/Home")
    if request.method == "GET":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            #if user.is_superuser:
             #   return HttpResponse("Super")
            #else:
            # adm = HaitiAdm3Stats.objects.all()
            # communes = {}
            # for ad in adm:
            #     communes[ad.id]=ad.commune
            # communes = communes.values()
            # print communes
                    # for u in User.objects.all():
                    #     for group in u.groups.all():
                    #         for g in communes:
                    #             if g==group:
                    #                 request.session['commune']=group
                    #                 break
                    #     if request.session.has_key('commune'):
                # request.session['userid']  = user.id
                # return redirect('/Home')
            #elif user.is_superuser:
            request.session['userid']  = user.id
            #     return redirect('/Home')
            # else:
            #     return redirect('/')

            #return HttpResponse(request.user)
        return redirect('/Home')
    return render_to_response('login.html',{'form': form}, context_instance=RequestContext(request))

def logout(request):
    del request.session['userid']
    return redirect("/")