from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exam, Answer, Question, ExamResult, ExamResultOption


@login_required
def index(request):
    user = request.user
    taken_exams = ExamResult.objects.filter(user=user).values_list('exam', flat=True)
    # Get all exams except the ones the user has already taken
    exams = Exam.objects.exclude(id__in=taken_exams)
    
    show_success_alert = request.session.pop('show_success_alert', False)

    context = {
        'exams': exams,
        'show_success_alert': show_success_alert
    }
    return render(request, "index.html", context)


@login_required
def take_exam(request, exam_id):
    # Fetch exam or show 404 error if not found
    exam = get_object_or_404(Exam, id=exam_id)
    
    # Shuffle and fetch questions
    questions = Question.get_shuffled_questions(exam)

    # Fetch answers for questions
    for question in questions:
        question.answers = Answer.get_shuffled_answers(question)

    if request.method == "POST":
        score = 0
        total_questions = len(questions)
        correct_answers = []
        wrong_answers = []

        for question in questions:
            if question.multiple_correct:
                # Retrieve selected and correct answer IDs
                selected_answer_ids = [int(id) for id in request.POST.getlist(f'answers_{question.id}')]
                correct_answer_ids = [int(id) for id in question.answer_set.filter(is_correct=True).values_list('id', flat=True)]

                # Check correctness
                is_correct = set(selected_answer_ids) == set(correct_answer_ids)
                if is_correct:
                    score += 1

                correct_answers.append({
                    'question': question.text,
                    'selected_answers': list(Answer.objects.filter(id__in=selected_answer_ids).values_list('text', flat=True)),
                    'is_correct': is_correct
                })

                if not is_correct:
                    wrong_answers.append({
                        'question': question.text,
                        'selected_answers': list(Answer.objects.filter(id__in=selected_answer_ids).values_list('text', flat=True)),
                        'correct_answers': list(question.answer_set.filter(is_correct=True).values_list('text', flat=True)),
                        'is_correct': False
                    })

            else:
                # Handle single-select answers
                selected_answer_id = request.POST.get(f'answer_{question.id}')
                if selected_answer_id:
                    try:
                        selected_answer = Answer.objects.get(id=selected_answer_id)
                        is_correct = selected_answer.is_correct
                    except Answer.DoesNotExist:
                        selected_answer = None
                        is_correct = False

                    if is_correct:
                        score += 1

                    correct_answers.append({
                        'question': question.text,
                        'selected_answer': selected_answer.text if is_correct else None,
                        'is_correct': is_correct
                    })
                    
                    if not is_correct:
                        wrong_answers.append({
                            'question': question.text,
                            'selected_answer': selected_answer.text,
                            'correct_answer': question.answer_set.filter(is_correct=True).first().text,
                            'is_correct': False
                        })
                else:
                    wrong_answers.append({
                        'question': question.text,
                        'selected_answer': 'No answer selected',
                        'correct_answer': question.answer_set.filter(is_correct=True).first().text,
                        'is_correct': False
                    })

        percentage_score = (score / total_questions) * 100 if total_questions > 0 else 0

        # Save result to the database
        exam_result = ExamResult.objects.create(
            user=request.user,
            exam=exam,
            score=score,
            total_questions=total_questions,
            percentage_score=percentage_score,
            correct_answers=correct_answers,
            wrong_answers=wrong_answers
        )

        # Save selected options in ExamResultOption
        for question in questions:
            if question.multiple_correct:
                selected_answer_ids = request.POST.getlist(f'answers_{question.id}')
                for answer_id in selected_answer_ids:
                    ExamResultOption.objects.create(
                        exam_result=exam_result,
                        answer_id=answer_id,
                        is_selected=True
                    )
            else:
                selected_answer_id = request.POST.get(f'answer_{question.id}')
                if selected_answer_id:
                    ExamResultOption.objects.create(
                        exam_result=exam_result,
                        answer_id=selected_answer_id,
                        is_selected=True
                    )
                    
        return redirect('exam_result', exam_result_id=exam_result.id)

    context = {
        'exam': exam,
        'questions': questions,
    }
    
    return render(request, 'exam/take_exam.html', context)


@login_required
def exam_result(request, exam_result_id):
    exam_result = ExamResult.objects.get(id=exam_result_id)
    if not exam_result:
        return redirect('take_exam', exam_result.exam_result_id)  # Redirect if no result is found

    # Prepare a list of questions with their associated options
    questions = []
    for question in Question.objects.filter(exam=exam_result.exam):
        options = Answer.objects.filter(question=question)
        exam_result_options = ExamResultOption.objects.filter(exam_result=exam_result, answer__in=options)

        options_with_selection = []
        for option in options:
            is_selected = ExamResultOption.objects.filter(
                exam_result=exam_result, 
                answer=option,
                is_selected=True
            ).exists()

            options_with_selection.append({
                'text': option.text,
                'is_correct': option.is_correct,
                'is_selected': is_selected
            })

        questions.append({
            'text': question.text,
            'options': options_with_selection
        })

    context = {
        'exam_result': exam_result,
        'questions': questions
    }

    return render(request, 'exam/result.html', context)


@login_required
def box(request):
    user = request.user
    # Get all exams the user has taken along with their result IDs
    taken_exams = Exam.objects.filter(examresult__user=user).distinct()
    
    # Create a list of dictionaries with exam details and the latest result
    exam_results = []
    for exam in taken_exams:
        latest_result = exam.examresult_set.filter(user=user).order_by('-created_at').first()
        if latest_result:
            exam_results.append({
                'exam': exam,
                'exam_result_id': latest_result.id,
                'taken_date': latest_result.created_at
            })
    
    context = {'exam_results': exam_results}
    return render(request, "exam/box.html", context)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            remember_me = request.POST.get('remember-me')
            
            if remember_me:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Browser session
            
            login(request, user)
            # Redirect to the admin dashboard if the user is an admin
            if user.is_superuser:
                return redirect('admin:index')
            request.session['show_success_alert'] = True
            return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('login') 



