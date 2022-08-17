from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import SentenceListComment, WordList
from .models import SentenceList
from .forms import RSentencesWriteForm, SentencesCommentForm
from board.models import Board
from board.forms import PBoardWriteForm
from django.core.paginator import Paginator


# Create your views here.

def rwordpage(request):
    if request.method == 'GET':
        if request.GET.get('button3')=="3":
            rwordlist = WordList.objects.order_by('?')[:3]
        elif request.GET.get('button4')=="4":
            rwordlist = WordList.objects.order_by('?')[:4]
        elif request.GET.get('button5')=="5":
            rwordlist = WordList.objects.order_by('?')[:5]
        else:
            rwordlist = ''
        form = RSentencesWriteForm()
        context = {
            'forms': form,
            'rwordlist' : rwordlist,
        }
        return render(request, 'rwordpage.html', context)

    elif request.method == 'POST':
        if request.GET.get('button3')=="3":
            rwordlist = WordList.objects.order_by('?')[:3]
        elif request.GET.get('button4')=="4":
            rwordlist = WordList.objects.order_by('?')[:4]
        elif request.GET.get('button5')=="5":
            rwordlist = WordList.objects.order_by('?')[:5]
        else:
            rwordlist = 'click button'

        form = RSentencesWriteForm(request.POST)

        if form.is_valid():
            s = SentenceList()
            s.sentence = form.cleaned_data['sentence']
            s.contents = form.cleaned_data['contents']
            # s.writer = request.user "SentenceList.writer" must be a "User" instance.
            s.save()
            return redirect('/rboard')
        else:
            context = {
                'forms': form,
                'rwordlist' : rwordlist,
            }
            return render(request, 'rwordpage.html', context)

    
def rwordboard(request):
    rword_setences = SentenceList.objects.filter().order_by('-id')

    paginator = Paginator(rword_setences, 10)
    pagenum = request.GET.get('page')
    rword_setences = paginator.get_page(pagenum)

    context = {
        'rword_setences' : rword_setences,
    }
    return render(request, 'rwordboard.html', context)

#문장 게시판 상세보기
def rword_detail(request, pk):
    sentence = get_object_or_404(SentenceList, id=pk)
    comments = SentenceListComment.objects.filter(Sentence=sentence.id).order_by('created_at')
    write_form = PBoardWriteForm()
    comment_form = SentencesCommentForm()

    context = {
        'sentence': sentence,
        'forms': write_form,
        #'like_num' : like_num,
        'comment_form' : comment_form,
        'comments' : comments
    }
    return render(request, 'rwordboard_detail.html', context)

#댓글 생성
def sen_comments_create(request, pk):
    if request.method == "POST":
        if request.user.is_authenticated:
            sentence = get_object_or_404(SentenceList, pk=pk)
            commentform = SentencesCommentForm(request.POST)
            if commentform.is_valid():
                comment = commentform.save(commit=False)
                comment.Sentence = sentence
                comment.user = request.user
                comment.save()
            return redirect('/' + 'rboard/detail/' + str(pk))
        return redirect('/'+'accounts/login')

#댓글 삭제
def sen_comments_delete(request, Sentence_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(SentenceList, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('/' + 'rword/detail/' + str(Sentence_pk))