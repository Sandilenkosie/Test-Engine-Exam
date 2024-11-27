from django.db import migrations, transaction

def add_crt1(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')
    Group = apps.get_model('exam', 'Group')


    with transaction.atomic():
        group, created = Group.objects.get_or_create(
            name='CRM-Exams',
            defaults={'description': 'Group for CRM related exams'}
        )

        # Create an exam instance and associate it with the group
        exam = Exam.objects.create(title='#CRM-1 Exam')

        # If you want to add the exam to the group (assuming a many-to-many relation):
        group.exams.add(exam)

        # Define questions and answers
        questions_data = [
               
                {
                    'text': 'Cloud Kicks (CK) tracks the support level of its customers on the account record page. CK wants to show a text notification on a case record page when the related account is a platinum-level customer. How could an app builder meet this requirement?',
                    'answers': [
                        ('Add a rich text area to the Case Lightning page > Set the component visibility of the rich text area to show when the account support level is platinum.', False),
                        ('Create a text-only Visualforce page > Drag the Visualforce component into the Case page layout > Set its visibility to show when the account support level is platinum.', True),
                        ('Create a text-only Visualforce page > Clone the case page layout > Drag the Visualforce component into the page, and assign the layout to platinum cases.', False),
                        ('Clone the Case Lightning page > Add a rich text area to the new page, and assign this page to platinum accounts.', False)
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
        migrations.RunPython(add_crt1, atomic=False),
    ]
