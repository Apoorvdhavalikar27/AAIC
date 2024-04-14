from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal, User

def home(request):
    """Render the homepage with a form to start the game."""

    return render(request, 'game_app/home.html')

def game(request):
    """Render the game interface."""
    # Initialize user and animals
    user = User()
    animals = [
        Animal(name='Animal', x_coordinate=100, y_coordinate=100, color='Red'),
        Animal(name='Animal', x_coordinate=200, y_coordinate=200, color='skyblue'),
        Animal(name='Animal', x_coordinate=300, y_coordinate=50, color='pink'),
        Animal(name='Animal', x_coordinate=400, y_coordinate=300, color='skyblue'),
        Animal(name='Animal', x_coordinate=500, y_coordinate=100, color='pink'),
        Animal(name='Animal', x_coordinate=150, y_coordinate=200, color='skyblue'),
        Animal(name='Animal', x_coordinate=10, y_coordinate=50, color='skyblue'),
        Animal(name='Animal', x_coordinate=300, y_coordinate=300, color='pink'),
        Animal(name='Animal', x_coordinate=50, y_coordinate=300, color='pink'),
        Animal(name='Animal', x_coordinate=259, y_coordinate=300, color='pink'),

        # Add more animals as needed
    ]


    # Create the context dictionary with the variables you want to pass to the template
    context = {
        'user': user,  # Pass the user object
        'animals': animals,  # Pass the list of animals
    }

    # context = {'user': user, 'animals': animals}
    return render(request, 'game_app/game_app.html', context)

def end_game(request, score):
    """Render the end game screen with the final score."""
    context = {'score': score}
    return render(request, 'game_app/end_game.html', context)


