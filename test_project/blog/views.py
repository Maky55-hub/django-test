from django.shortcuts import render

posts = [
	{
		'author' : 'Max Mustermann',
		'date_posted' : '04.06.2020',
		'title' : 'First Post',
		'content' : 'This is my first post'
	},
	{
		'author' : 'Andy Labello',
		'date_posted' : '05.06.2020',
		'title' : 'First Post',
		'content' : 'This is my second post'
	}
]

def Home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def About(request):
    return render(request, 'blog/about.html')
