request.session.get('access', None):
return HttpResponseRedirect(request.session['loginURL'])
if request.method == "POST":
username = request.POST.get('username', '') #logic only for member login
password = request.POST.get('password', '')
try:
if labUser.objects.filter(username=username, password=str(password), isDisable=0).exists():
user = labUser.objects.get(username__startswith=username, password__startswith=str(password), isDisable=0)
msg = 'Logged in'
# setActivityLog(user.labId_i
[9/8, 10:33 PM] Telore Sagar: return render_to_response('loginTemplates/labLogin.jinja', {'loginPageBanner': loginPageBannerImg,'loginBannerURL':loginBannerURL} ,context_instance=RequestContext(request))