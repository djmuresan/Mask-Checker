from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'mask/home.html')

def status (request):

    score = 0
    status = 'terrible'
    picture = ''
    questions = 10
    score += int(request.GET.get('q1a'))
    score += int(request.GET.get('q2a'))
    score += int(request.GET.get('q3a'))
    score += int(request.GET.get('q4a'))
    score += int(request.GET.get('q5a'))
    score += int(request.GET.get('q6a'))
    score += int(request.GET.get('q7a'))
    score += int(request.GET.get('q8a'))
    score += int(request.GET.get('q9a'))
    score += int(request.GET.get('q10a'))
    if score < (questions * 5):
        status = (f"Please use another, You seriously need to buy a new mask. This one you have will not protect you because it is not snug on your face, properly covering your nose and mouth. It is also made from large-pores materials, so viruses can still sneak in when you breath. Please get a new mask... or double your current mask with a surgical mask. You do want to stay healthy, right? score: {score}")
        picture = "https://st3.depositphotos.com/3356953/14145/v/600/depositphotos_141459568-stock-illustration-emoticon-smiley-with-thumb-down.jpg"

    elif score < (questions * 10):
        status = (f"You can do better, Your mask will probably protect you, but not others. The vent on your mask will let out viruses and not protect other people surrounding you. One way you get away with wearing this mask is by doubling your wear with a surgical mask. Otherwise, please get a safer mask. score: {score}")
        picture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQatf22EQo5pgvboeJWExzD2jAN64ctFO9_UQ&usqp=CAU"

    elif score < (questions * 15):
        status = (f"Decent, Your mask will protect you and other people around you. It is snug on your face, and reusable so you get a good point for being environmentally friendly. However, IF you don't wash/clean/disinfect your mask properly, you may get infected with leftover virus. So be sure to disinfect your mask for proper reuse in the future.  score: {score}")
        picture = "https://toppng.com/uploads/preview/ok-emoji-ok-11562897400j6tlsbtsse.png"

    else:
        status = (f"Good quality, Your mask will protect you and other people around you. It is snug on your face, covering both your nose and mouth. It is also a one-time use mask, so your risk of not 'cleaning' it for reuse is none. Keep up the good work!, score: {score}" )
        picture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsVdEj4B_CX5g9cy_QEdsm2XUL93AeXawjRQ&usqp=CAU"

    return render(request, 'mask/status.html', {'score':status, 'image': picture})



