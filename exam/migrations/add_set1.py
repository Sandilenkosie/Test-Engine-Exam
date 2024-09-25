from django.db import migrations

def add_set1(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')

    # Create an exam instance
    exam = Exam.objects.create(title='ADM-201-Set1 Exam')

    # Define questions and answers
    questions_data = [
    # Divide here for set 1
    {
        'text': 'Which tool should an administrator use to review recent configuration changes made in their org?',
        'answers': [
            ('Critical Updates', False),
            ('Debug logs', False),
            ('Setup Audit Trail', True),
            ('Field History Tracking', False)
        ]
    },
    
]

    for question_data in questions_data:
        # Automatically set multiple_correct if more than one answer is correct
        multiple_correct = sum(1 for answer in question_data['answers'] if answer[1]) > 1
        question = Question.objects.create(
            exam=exam, 
            text=question_data['text'], 
            multiple_correct=multiple_correct
        )
        for answer_text, is_correct in question_data['answers']:
            Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

class Migration(migrations.Migration):

    dependencies = [
        # Add your app's dependencies here
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_set1),
    ]   