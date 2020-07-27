from django.shortcuts import render
from .models import Comment

# Create your views here.
def home(request):
    return render(request, 'home.html')

def photoshop(request):
    return render(request, 'photoshop.html')

def photodetail(request):
    return render(request, 'photodetail.html')

def contest(request):
    return render(request, 'contest.html')

def mission(request):
    return render(request, 'mission.html')

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