from django.shortcuts import render

def inputdata(request):
    return render(
        request,
        'program/inputdata.html'
    )

def result(request):
    lis=[]
    lis.append(request.GET['a'])
    lis.append(request.GET['b'])

    sum = 0
    mul = 1

    all = []
    for l in lis:
        sum += int(l)
        mul *= int(l)

    all.append(sum)
    all.append(mul)

    ans = all

    return render(request,'program/result.html',{'ans':ans,'lis':lis})
