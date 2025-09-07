from django.shortcuts import render ,redirect

def index(request):
    if 'visit_counter' not in request.session:
        request.session['visit_counter'] =0

    if 'counter' not in request.session:
        request.session  ['counter'] =0  

    request.session['visit_counter'] += 1

    context= {
        'visit_counter' : request.session['visit_counter'],
        'counter' : request.session['counter']

    }
    return render(request , 'myapp/index.html' ,context)


def destroy_session(request):
    request.session.flush()
    return redirect('/')

def increment2(request):
    request.session['visit_counter'] += 1
    request.session['counter'] += 2
    return redirect('/')

def increment_value(request):
    if request.method == "POST":
        increment_value = int(request.POST.get('increment_value'))
        if 'visit_counter' not in request.session:
            request.session['visit_counter'] =0

        if 'counter' not in request.session:
            request.session  ['counter'] =0  
        else:    
            request.session['counter'] += increment_value
            request.session['visit_counter'] += increment_value -1

    return redirect('/')