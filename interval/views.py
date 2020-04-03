from django.shortcuts import render
from .logic import *
import logging
from django.contrib.auth.decorators import login_required
from .models import Question as DatabaseQuestion
from .models import Test
from django.shortcuts import *


# Create your views here.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('test')


def learn(request):
    logger.info(request)
    return render(request, 'learn.html')


@login_required
def choose_practice(request):
    return render(request, 'choose_practice.html')


input_to_methods = {
    'perfect': generate_data_for_question_perfect_with_simple_wrong_answers,
    'consonant': generate_data_for_question_consonant_simple_with_only_diatonic_c_options_wrong_answers,
    'consonant-advanced':  generate_data_for_question_consonant_normal_with_any_start_and_any_wrong_answers,
    'dissonant': generate_data_for_question_dissonant_with_simple_start,
    'dissonant-advanced': generate_data_for_question_dissonant_with_any_wrong_answers,
    'augdim': generate_data_for_aug_and_dim_with_simple_start,
    'augdim-advanced': generate_data_for_aug_and_dim_with_any_start,
    'interval': generate_data_for_question_with_expanded_answers_and_choices,
    'interval-advanced': generate_data_for_question_all_intervals_with_simple_choices,
}

xp = {  
    'perfect': 250,
    'consonant': 260,
    'consonant-advanced': 270,
    'dissonant': 300,
    'dissonant-advanced': 320,
    'augdim': 400,
    'augdim-advanced': 450,
    'interval': 500,
    'interval-advanced': 600,
}


def practice(request, question):
    if request.GET.get('chosen_answer', ''):
        try:
            test = Test.objects.get(user=request.user, status=True, test_type=question) #select active test
        except Test.DoesNotExist:
            return redirect(reverse('choose_practice'))
        current_question = DatabaseQuestion.objects.get(question_index=test.question_index, test=test)
        current_question.user_answer = request.GET.get('chosen_answer')
        current_question.save()
        if current_question.user_answer == current_question.right_answer:         
            profile = test.user.profile
            profile.xp = profile.xp + current_question.xp_gain
            
            profile.save()
        if current_question.is_last_question():
            test.status = False
            test.save()
            return redirect(reverse('score'))
        next_question = DatabaseQuestion.objects.get(question_index=test.question_index+1, test=test)
        test.question_index = next_question.question_index 
        test.save()
        return render(request, 'practice.html', {'question': next_question, 'question_index': next_question.question_index, 'type': question})
    if Test.objects.filter(status=True, user=request.user, test_type=question).count() > 0:
        test = Test.objects.get(status=True, user=request.user, test_type=question)
        current_question = DatabaseQuestion.objects.get(question_index=test.question_index, test=test)
        return render(request, 'practice.html', {'question': current_question, 'question_index': current_question.question_index, 'type': question})
    else:
        test = Test(user=request.user, test_type=question)
        test.save()
        first_question = generate_question_return_first(question, test)
        return render(request, 'practice.html', {'question': first_question, 'question_index': 1, 'type': question})


def generate_question_return_first(question, test):
    first_question = None
    for i in range(8):
        data = input_to_methods[question]()
        db_question = DatabaseQuestion(test=test, question_index=i, interval_type=data.my_interval,
                                       answer_array=','.join(data.all_answers), start_note=data.start_note,
                                       right_answer=data.right_answer, xp_gain=xp[question])
        db_question.save()
        if i == 0:
            first_question = db_question
    return first_question


def score(request):
    return render(request, 'score.html')
