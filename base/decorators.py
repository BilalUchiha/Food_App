from django.shortcuts import redirect


from django.shortcuts import redirect

def allow_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='customer').exists():
            # User is in the 'customer' group, redirect to the main page
            return redirect('/customer_page')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

