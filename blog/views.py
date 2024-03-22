from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from.models import Post,Comment
from django.db.models import Q 
from . forms import PostForm,PostCreateForm,CategoryForm
# from django.http import HttpResponseRedirect
# Create your views here.

def HomeView(request):
    
    return render(request,'blog/index.html')
def searchView(request):
    if request.method == 'POST':
        search_query = request.POST.get('search','')
        search_input = Post.objects.filter(Q(title__icontains = search_query) | Q(content__icontains = search_query) | Q(category__name__icontains = search_query))
        print(search_input,"+++++++++++++++")
        return render(request,'blog/search.html',{'search_data':search_input,'query':search_query})
    return render(request,'blog/search.html')
def PostCreate(request):
    if request.method=='POST':
        form = PostCreateForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('postList')
    else:
        form = PostCreateForm()
    return render(request,'blog/post_create.html',{'form':form})

def PostListView(request):
    queryset = Post.objects.all().order_by('-created_date')
    return render(request,'blog/post_list.html',{'PostList':queryset})

def PostDetails(request,id):
    
    post_data = Post.objects.get(id=id)

    comments = Comment.objects.filter(post=post_data, parent=None)
    replies = Comment.objects.filter(post=post_data).exclude(parent=None)

   
    context = {
        'post':post_data,
        'comments': comments,
        'replies': replies,
    }

    return render(request, "blog/post_detail.html", context)
def PostDelete(request,id):
    
    post_data = Post.objects.get(id=id)
    if request.method=='POST':
        post_data.delete()
        return redirect('postList')
  
    return render(request, "blog/delete.html")


def PostEdit(request,id):
    post_data = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=post_data)
    if form.is_valid():
        form.save()
        return redirect('PostDetails', id= post_data.id)
    return render(request,'blog/post_edit.html',{'form':form})


def CategoryCreate(request):
    if request.method == 'POST':
        form_data = CategoryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('CategoryCreate')
    else:
        form_data = CategoryForm()
    return render(request,'blog/post_categories.html',{'form_data':form_data})



def  AddComment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        postid=request.POST['postid']
        parentid=request.POST['parentid']

        post = Post.objects.get(id=postid)
        if parentid:
            parent = Comment.objects.get(id=parentid)
            newcom = Comment(text=comment, user=request.user,post=post,parent=parent)
            newcom.save()
        else:
            newcom = Comment(text=comment, user=request.user,post=post)
            newcom.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



