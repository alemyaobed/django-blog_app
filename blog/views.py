from django.shortcuts import render

posts = [
    {
        'author': 'Kay',
        'title': 'Some amazing content',
        'content': 'Some amazing title you just left up there',
        'created_at': '16th April, 2024 @15:05'
    },
    {
        'author': 'Sabs',
        'title': 'Some amazing content',
        'content': 'Some amazing title you just left up there',
        'created_at': '16th April, 2024 @15:06'
    }
]


def home(request):
    # Return this following response when the home is called.
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # Return this following response when the about is called.
    context = {
        'posts': posts,
    }
    return render(request, 'blog/about.html', context)
