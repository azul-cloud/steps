from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from stepsofatraveler.blog.models import Blog, Category, PhotoAlbum
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    posts = Blog.objects.filter(active=True)[:3]
    return render(request, 'content/home.html', {'posts':posts, 'page':'home'})

def about(request):
    return render(request, 'content/about.html', {'page':'about'})

def contact(request):
    return render(request, 'content/contact.html', {'page':'contact'})

def overview(request):
    return render(request, 'content/overview.html', {'page':'overview'})

def photoalbum(request):
    albums = PhotoAlbum.objects.all()
    return render(request, 'content/photoalbum.html', {'albums':albums, 'page':'photoalbum'})

@staff_member_required
def stats(request):
    blogs = Blog.objects.all().order_by('-views')
    return render(request, 'content/stats.html', {'blogs':blogs})

def archive(request):
    try:
        #get list of categories to fill ddl
        categories = Category.objects.all().order_by('title')

        search = ''
        pop_posts = Blog.objects.all().order_by('-views')[0:5]
        posts = Blog.objects.all()
        text = ''

        #get list of posts before making paginator
        if 'search' in request.GET:
            if request.GET['search']:
                search = request.GET['search']
                posts = Blog.objects.filter(Q(body__icontains = search) | Q(title__icontains = search), active=True)
                text = 'Your search query was not listed in any title or body of a post.'

        paginator = Paginator(posts, 10) # Show 10 posts per page

        # Make sure page request is an int. If not, deliver first page.
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        # If page request (9999) is out of range, deliver last page of results.
        try:
            posts = paginator.page(page)
        except (EmptyPage, InvalidPage):
            posts = paginator.page(paginator.num_pages)

    except Blog.DoesNotExist:
        raise Http404

    return render(request, 'content/archive.html',
        {'posts':posts, 'pop_posts':pop_posts, 'page':'archive', 'search':search,
        'text':text, 'categories':categories})

def post(request, postid):
    try:
        post = Blog.objects.get(id=postid)

        #get posts to display on the sidebar
        previous_posts = Blog.objects.filter(id__lt=postid)

        maxBlog = Blog.objects.all().order_by('-id')[0]
        maxId = maxBlog.id
        minBlog = Blog.objects.all().order_by('id')[0]
        minId = minBlog.id

        #set defaults for the next/prev post
        nextPost = post
        prevPost = post

        #if id isn't min/max then pass in the prev/next post
        if post.id != maxId:
            nextPost = Blog.objects.get(id=int(postid) + 1)
        if post.id != minId:
            prevPost = Blog.objects.get(id=int(postid) - 1)

        #add to view total field
        if post.views:
            views = post.views
            post.views = views + 1
        else:
            post.views = 1
        post.save()

        return render(request, 'content/post.html',
            {'p':post, 'nextPost':nextPost, 'prevPost':prevPost, 'max':maxId,
            'min':minId, 'previous_posts':previous_posts})

    except Blog.DoesNotExist:
        raise Http404

def category(request, categoryName=''):
    try:
        #get all categories to pass into sidebar
        categories = Category.objects.all().order_by('title')

        #get queried category for main content
        if categoryName:
            categoryObject = Category.objects.get(title=categoryName)
            categoryId = categoryObject.id
            posts = Blog.objects.filter(category=categoryId, active=True)
        else:
            posts = {}

    except Category.DoesNotExist:
        return render(request, 'content/category.html', {'categories':categories})

    return render(request, 'content/category.html', {'posts':posts, 'category':categoryName, 'categories':categories})