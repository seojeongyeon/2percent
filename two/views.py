from .models import Mission
from .forms import PhotoshopForm
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def photoshop(request):
    return render(request, 'photoshop.html')

def photowrite(request):
    if request.method =='POST':
        form = PhotoshopForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoshopForm()
        return render(request, 'photowrite.html', {'form':form})

def photodetail(request):
    return render(request, 'photodetail.html')

def contest(request):
    return render(request, 'contest.html')

def mission(request):
    missions = Mission.objects.all()
    return render(request, 'mission.html', {'missions':missions})

def mission_create(request):
    if request.method == 'POST' :
        new_mission = Mission()
        new_mission.title = request.POST['title']
        new_mission.pub_date = timezone.datetime.now()
        new_mission.writer = request.user
        new_mission.body = request.POST['body']
        new_mission.image = request.FILES
        new_mission.point = request.POST['point']
        new_mission.end_date = request.POST['end_date']
        new_mission.save()
        return redirect('mission_detail', new_mission.id)
    else :
        return render(request, 'mission_create.html')


def mission_detail(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    comments = mission.missioncomment_set.all()
    return render(request, 'mission_detail.html', {
        'mission': mission,
        'comments' : comments,
        })

def mission_delete(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    mission.delete()
    redirect('mission')