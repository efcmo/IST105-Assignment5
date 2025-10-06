from django.shortcuts import render
from .forms import PuzzleForm
import random

def puzzle_view(request):
    result = None
    secret_number = 42  # fixed secret number
    attempts = []

    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

            # 🧮 Number Puzzle
            number_type = "even" if number % 2 == 0 else "odd"
            cube = number ** 3

            # 💬 Text Puzzle
            binary_text = ' '.join(format(ord(char), '08b') for char in text)
            vowels = "aeiouAEIOU"
            vowel_count = sum(1 for ch in text if ch in vowels)

            # 🪙 Treasure Hunt simulation
            guesses = [random.randint(20, 60), random.randint(20, 60), secret_number]
            feedback = []
            for i, guess in enumerate(guesses, start=1):
                if guess < secret_number:
                    feedback.append(f"Attempt {i}: {guess} (Too low!)")
                elif guess > secret_number:
                    feedback.append(f"Attempt {i}: {guess} (Too high!)")
                else:
                    feedback.append(f"Attempt {i}: {guess} (Correct!)")
                    break

            result = {
                'number': number,
                'number_type': number_type,
                'cube': cube,
                'text': text,
                'binary_text': binary_text,
                'vowel_count': vowel_count,
                'feedback': feedback,
                'attempts': len(feedback),
            }
    else:
        form = PuzzleForm()

    return render(request, 'puzzle/puzzle_form.html', {'form': form, 'result': result})
