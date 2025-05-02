from django.db import migrations, transaction

def add_dp1(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')
    Group = apps.get_model('exam', 'Group')

    with transaction.atomic():
        group, created = Group.objects.get_or_create(
            name='DP1-Exams',
            defaults={'description': 'Group for CRM related exams'}
        )

        exam = Exam.objects.create(title='#DP-1 Exam')
        group.exams.add(exam)

        questions_data = [
            {
                'text': 'Why would a developer use Test.startTest() and Test.stopTest()?',
                'answers': [
                    ('To avoid Apex code coverage requirements for the code between lines.', False),
                    ('To start and stop anonymous block execution when executing anonymous Apex code.', False),
                    ('To indicate test code so that it does not impact Apex line count governor limits.', False),
                    ('To create additional set of governor limits during the execution of single test class.', True),
                ]
            },
            {
                'text': 'What must the controller of a visualforce page utilize to override the standard Opportunity view button?',
                'answers': [
                    ('The StandardSetController to support related list in pagination.', False),
                    ('The Opportunity StandardController for pre-built functionality.', True),
                    ('The callback constructor to reference the standard controller.', False),
                    ('A constructor that initializes a private Opportunity variable.', False),
                ]
            },
{
                'text': [('A developer uses a before insert trigger on the Lead object to fetch Territory__c object, where'
                        'the Territory__c.PostalCode__c matches the Lead.PostalCode. The code fails when the'
                        'developer uses Apex data loader to insert 100000 lead records. The developer executes the below'
                        'code:'),
                        ('01 For (Lead l: Trigger.new)'),
                        ('02     If(l.postalCode != null){'),
                        ('03         List<Territoty__c> terrList = [SELECT Id FROM Territory__c WHERE'),
                                    ('PostalCode__c = :l.PostalCode];'),
                        ('04      If(terrList.size() >0){'),
                        ('05          l.Territory__c = terrList[0].Id;'),
                                ('}'),
                           ('}'),
                        ('}'),
                        ('Which line of code is causing the code block to fail?'),],
                        
                'answers': [
                    ("03: A SOQL query is located inside of the for loop code.", True),
                    ("01: Trigger.new is not valid in a before insert trigger.", False),
                    ("02: A NullPointerException is thrown if PostalCode is null.", False),
                    ("05: The Lead in a before insert trigger cannot be updated.", False),
                ]
            },
            {
                'text': 'What would a developer do to update a picklist field on related opportunity records when a modification to the associated Account record is detected?',
                'answers': [
                    ('Create a process with Process Builder', True),
                    ('Create a workflow rule with a field update', False),
                    ('Create a Lightning component.', False),
                    ('Create a Visualforce page.', False),
                ]
            },
            {
                'text': 'Which requirement needs to be implemented by using standard workflow instead of Process Builder? (Choose 2)',
                'answers': [
                    ('Create activities at multiple intervals.', False),
                    ('Send an outbound message without Apex code.', True),
                    ('Copy an account address to its Contact.', False),
                    ('Submit a contract for approval.', True),
                ]
            },
            {
                'text': 'An org has different Apex classes that provide Account related functionality. After a new validation'
                        'rule is added to the Account object, many of the test methods failWhat can be done to resolve the failure and reduce the number of code changes needed for future validation rules?',
                'answers': [
                    ('Create a method that creates valid Account records, and call this method from within test method.', True),
                    ('Create a method that loads valid Account records from a Static Resource, and call this method within test method.', False),
                    ('Create a method that performs a callout for a valid Account record, and call this method from within test method.', False),
                    ('Create a method that queries for valid Account records, and call this method from within test methods.', False),
                ]
            },
            {
                'text': 'Which component is available to deploy using Metadata API? (Choose 2)',
                'answers': [
                    ('Case Layout', True),
                    ('Account Layout', True),
                    ('Case Feed Layout', False),
                    ('Console Layout', False),
                ]
            },
            {
                'text': 'In the code below, what type does Boolean inherit from?\nBoolean b = true;',
                'answers': [
                    ('Enum', False),
                    ('Object', True),
                    ('String', False),
                    ('Class', False),
                ]
            },
            {
                'text': 'What is the preferred way to reference web content – such as images, stylesheets, JavaScript, and other libraries – that is used in Visualforce pages?',
                'answers': [
                    ('By accessing the content from chatter files', False),
                    ('By uploading the content in the Documents tab.', False),
                    ('By accessing the content from a third party CDN', False),
                    ('By uploading the content as a Static Resource.', True),
                ]
            },
            {
                'text': 'A company has a custom object named Warehouse. Each Warehouse record has a distinct record'
                        'owner, and is related to a parent Account in Salesforce.Which kind of relationship would a developer use to relate the Account to Warehouse?',
                'answers': [
                    ('One-to-Many', False),
                    ('Lookup', True),
                    ('Master-Detail', False),
                    ('Parent-Child', False),
                ]
            },
            {
                'text': 'A developer creates a workflow rule declaratively that updates a field on an object. An Apex trigger'+
                        'exists for the object.What happens when a user updates a record with an Apex trigger and workflow rule on the object?',
                'answers': [
                    ('No changes are made to data.', False),
                    ('Both the Apex Trigger and Workflow Rule are fired only once.', True),
                    ('The Workflow Rule is fired more than once.', False),
                    ('The Apex Trigger is fired more than once.', False),
                ]
            },
            {
                'text': 'What is true of a partial sandbox that is not true of a full sandbox? (Choose 2)',
                'answers': [
                    ('More frequent refreshes.', True),
                    ('Only includes necessary metadata.', False),
                    ('Use of change sets.', False),
                    ('Limited to 5 GB of data.', True),
                ]
            },
            {
                'text': 'In which order does Salesforce executes events upon saving a record?',
                'answers': [
                    ('Before triggers; Validation rules; After triggers; Assignment rules; Workflow rules; Commit', False),
                    ('Validation rules; Before triggers; After triggers; Workflow rules; Assignment rules; Commit', False),
                    ('Before triggers; Validation rules; After triggers; Workflow rules; Assignment rules; Commit', True),
                    ('Validation rules; Before triggers; After triggers; Assignment rules; Workflow rules; Commit', False),
                ]
            },
            {
                'text': 'When loading data into an organization, wWhat can a developer do to match records to update existing records when loading data? (Choose 2)',
                'answers': [
                    ('Match an external id text field to a column in the imported file.', True),
                    ('Match the Id field to a column in the imported file.', True),
                    ('Match the Name field to a column in the imported file.', False),
                    ('Match an auto generated number field to a column in the imported file.', False),
                ]
            },
            {
                'text': 'In an organization that has enabled multiple currencies, a developer needs to aggregate the sum of'
                        'the Estimated_Value__c currency field from the CampaignMember object using a roll-up summary'
                        'field called Total_Estimated_Value__c on Campaign. How is the currency of the Total_Estimated_Value__c roll-up summary field determined?',
                'answers': [
                    ('The values in CampaignMember.Estimated_Value__c are converted into the currency of the Campaign record, and the sum is displayed using currency on the Campaign record.', True),
                    # You can add a few more distractors here if needed
                ]
            },
        ]

        for question_data in questions_data:
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
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_dp1, atomic=False),
    ]
