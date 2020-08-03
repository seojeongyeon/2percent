from django.shortcuts import render
<<<<<<< HEAD
from .models import Mission, MissionComment,Photoshop,Comment,Contest
from .forms import PhotoshopForm, ContestForm
=======
from django.contrib.auth import get_user_model
from .models import Mission, MissionComment,Photoshop,Comment
from .forms import PhotoshopForm
>>>>>>> 08158e19491ff21394a970d456a23434f50de829
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

User = get_user_model()

# Create your views here.
def home(request):
    return render(request, 'home.html')

def photoshop(request):
    photoshops = Photoshop.objects
    return render(request, 'photoshop.html',{'photoshops':photoshops})

def photowrite(request):
    if request.method =='POST':
        form = PhotoshopForm(request.POST,request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.writer = request.user
            content.save()
            return redirect('home')
    else:
        form = PhotoshopForm()
        return render(request, 'photowrite.html', {'form':form})

def photodetail(request, pk):
    photodetail = get_object_or_404(Photoshop, pk=pk)
    comments = photodetail.comments.all()
    return render(request, 'photodetail.html', {'photodetail': photodetail,'comments':comments})

def photoscrap(request, pk):
    photodetail = get_object_or_404(Photoshop, pk=pk)
    comments = photodetail.comments.all()
    request.user.pscraps.add(photodetail)
    return render(request, 'photodetail.html', {'photodetail': photodetail,'comments':comments})

def photoscrap_del(request, pk):
    photodetail = get_object_or_404(Photoshop, pk=pk)
    comments = photodetail.comments.all()
    request.user.pscraps.remove(photodetail)
    return render(request, 'photodetail.html', {'photodetail': photodetail,'comments':comments})

def contest(request):
    contests = Contest.objects
    return render(request, 'contest.html',{'contests':contests})

def contestwrite(request):
    if request.method == 'POST':
        form = ContestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contest')
    else:
        form = ContestForm()
        return render(request, 'contestwrite.html', {'form':form})

def contest_like(request,contest_id):
    contest = get_object_or_404(Contest, pk = contest_id)
    contest.like.add(request.user)
    contest.save()
    return redirect('contest', contest.id)
    


def mission(request):
    if request.method == 'POST':
        word = request.POST['search']
        missions = Mission.objects.filter(Q(title__icontains=word) | Q(writer__icontains=word) | Q(body__icontains=word))
        return render(request, 'mission.html', {'missions':missions})
    else :
        missions = Mission.objects.order_by('-pub_date')
        return render(request, 'mission.html', {'missions':missions})

def mission_create(request):
    if request.method == 'POST' :
        mission = Mission()
        mission.title = request.POST['title']
        mission.pub_date = timezone.datetime.now()
        mission.writer = request.user
        mission.body = request.POST['body']
        mission.image = request.FILES['image']
        mission.point = request.POST['point']
        mission.end_date = request.POST['end_date']
        mission.save()
        return redirect('mission_detail', mission.id)
    else :
        return render(request, 'mission_create.html')

def mission_detail(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    comments = mission.missioncomment_set.all()
    return render(request, 'mission_detail.html', {
        'mission': mission,
        'comments' : comments,
        })

def mission_scrap(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    comments = mission.missioncomment_set.all()
    request.user.mscraps.add(mission)
    return render(request, 'mission_detail.html', {
        'mission': mission,
        'comments' : comments,
        })

def mission_scrap_del(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    comments = mission.missioncomment_set.all()
    request.user.mscraps.remove(mission)
    return render(request, 'mission_detail.html', {
        'mission': mission,
        'comments' : comments,
        })

def mission_delete(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    mission.delete()
    return redirect('mission')

def mission_comment_like(request, comment_id):
    comment = get_object_or_404(MissionComment, pk=comment_id)
    if request.user in comment.likers.all():
        comment.likers.set(comment.likers.exclude(username=request.user))
    else : 
        comment.likers.add(request.user)
    comment.save()
    return redirect('mission_detail', comment.mission.id)

def mission_comment_create(request, mission_id):
    comment = MissionComment()
    mission = get_object_or_404(Mission, pk=mission_id)
    comment.mission = mission
    comment.writer = request.user
    comment.pub_date = timezone.datetime.now()
    comment.body = request.POST['body']
    comment.image = request.FILES['image']
    comment.save()
    return redirect('mission_detail', mission_id)


def mission_comment_delete(request, comment_id):
    comment = get_object_or_404(MissionComment, pk=comment_id)
    mission_id = comment.mission.id
    comment.delete()
    return redirect('mission_detail', mission_id)

def commenting(request, pk):
    new_comment = Comment()
    new_comment.photoshop = get_object_or_404(Photoshop, pk = pk)
    new_comment.author = request.user
    new_comment.body = request.POST.get('body')
    new_comment.save()
    return redirect('photodetail', pk)

def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk= pk)
    comment.like.add(request.user)
    comment.save()
    return redirect('photodetail', comment.photoshop.id)

def comment_delete(request, comment_id):
    comment_delete = get_object_or_404(Comment, pk = comment_id)
    id = comment_delete.photoshop.id
    comment_delete.delete()
    return redirect('photodetail', id)
    

def photo_search(request):
    photos = Photoshop.objects.all()
    query = request.GET['query']
    if query:
        photo = Photoshop.objects.filter(title__icontains=query)

    return render(request, 'photo_search.html', {'photos':photos,'photo':photo})
