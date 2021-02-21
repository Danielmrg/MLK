from django.shortcuts import redirect,Http404

class IsAuthenticated(object):
    def __init__(self,func,*args,**kwargs):
        self.func = func
    def __call__(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return self.func(request,*args,**kwargs)
        # if kwargs['redirect_to']:
        #     return redirect(kwargs['redirect_to'])
        return redirect('home:home')
    

class IsAllowRole(object):
    def __init__(self,func,*args,**kwargs):
        self.func = func
    def __call__(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.get_role_title() is not None:
                return self.func(request,*args,**kwargs)
            return redirect("home:home")
        return redirect("home:home")