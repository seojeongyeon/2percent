from django.shortcuts import render
from .models import Comment
from .models import Mission, MissionComment
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
    missions = Mission.objects.order_by('-pub_date')
    return render(request, 'mission.html', {'missions':missions})

def mission_create(request):
    if request.method == 'POST' :
        mission = Mission()
        mission.title = request.POST['title']
        mission.pub_date = timezone.datetime.now()
        mission.writer = 'anonymous'
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

def mission_delete(request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    mission.delete()
    return redirect('mission')

def mission_comment_create(request, mission_id):
    comment = MissionComment()
    mission = get_object_or_404(Mission, pk=mission_id)
    comment.mission = mission
    comment.writer = 'anonymous'
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

def commenting(request, photoshop_id):
    new_comment = Comment()
    new_comment.photoshop = get_object_or_404(Blog, pk = photoshop_id)
    new_comment.author = request.user
    new_comment.body = request.POST.get('body')
    new_comment.save()

    return redirect('/photoshop/' + str(photoshop_id))

def comment_update(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    document = get_object_or_404(Photoshop, pk=comment.photoshop.id)

    if request.user != comment.author:
        messages.warning(request, "권한 없음")
        return redirect(photoshop)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(photoshop)
    else:
        form = CommentForm(instance=comment)
    return render(request,'photodetail/comment/comment_update.html',{'form':form})


def comment_delete(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    photoshop = get_object_or_404(Photoshop, pk=comment.photoshop.id)

    if request.user != comment.author and request.user != photoshop.author:
        messages.warning(request, '권한 없음')
        return redirect(photodetail)

    else:
        delete_photoshop_comment.delete()
        return redirect(photodetail)