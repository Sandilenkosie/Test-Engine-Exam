from django.db import migrations, transaction

def add_crt4(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')
    Group = apps.get_model('exam', 'Group')

    with transaction.atomic():
        group, created = Group.objects.get_or_create(
            name='CRM-Exams',
            defaults={'description': 'Group for CRM related exams'}
        )

        exam = Exam.objects.create(title='#CRM-4 Exam')

        group.exams.add(exam)


        questions_data = [
            {
                'text': 'Cloud Kicks wants to start tracking how many shoe subscriptions have been sold for each shoe catalog. A master-detail relationship exists between the Subscription__c and the Shoe__c objects. Which type of field should an app builder create?',
                'answers': [
                    ('Roll-up summary field', True),
                    ('Lookup field', False),
                    ('Master-detail relationship field', False),
                    ('Number field', False)
                ]
            },
            {
                'text': 'On the Account Lightning record page, users need to see ten fields and the ability to sort and wrap text on their Related Lists. What Related List type would the app builder select for the Related List Lightning component?',
                'answers': [
                    ('Enhanced List', True),
                    ('Basic List', False),
                    ('ListView', False),
                    ('List Class', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to make sure that users without the Marketing role are unable to update the Contact Retail Opt In picklist field to Yes. What validation rule would an app builder use to prevent other users from making this update?',
                'answers': [
                    ('AND( $UserRole.Name != \'Marketing\', ISCHANGED(Retail_Opt_In__c), ISPICKVAL(Retail_Opt_In__c,"Yes") )', True),
                    ('AND( $UserRole.Name != \'Marketing\', Retail_Opt_In__c = "Yes" )', False),
                    ('AND( $UserRole.Name = \'Marketing\', ISPICKVAL(Retail_Opt_In__c,"Yes") )', False),
                    ('AND( $UserRole.Name = \'Marketing\', Retail_Opt_In__c= "Yes" )', False)
                ]
            },
            {
                'text': 'An App Builder at UVC would like to prevent users from creating new records on an Account related list by overriding standard buttons. Which two should the App Builder consider before overriding standard buttons?',
                'answers': [
                    ('Standard buttons can be changed on lookup dialogs, list views, and search result layouts', False),
                    ('Standard buttons can be overridden with a Visualforce page', True),
                    ('Standard buttons that are not available for overrides can still be hidden on page layouts', True),
                    ('Standard buttons can be overridden, relocated on the detail page, and relabeled', False)
                ]
            },
            {
                'text': 'Universal Containers is piloting new features in an existing sandbox and wants to prevent outbound email sends during testing. What should the app builder do to meet the requirement?',
                'answers': [
                    ('Email deliverability set to system email only.', False),
                    ('Email configured for SMTP authentication.', False),
                    ('Email relay to the configured host enabled.', False),
                    ('Email deliverability set to no access.', True)
                ]
            },
            {
                'text': 'Cloud Kicks (CK) wants to begin socializing and collaborating within Salesforce around customer accounts to discuss various topics. CK would like all company employees to see these conversations. Which two features of Chatter would meet CK\'s business needs?',
                'answers': [
                    ('Set up new private Chatter groups.', False),
                    ('Set up new public Chatter groups.', True),
                    ('Use post action on the Account object.', True),
                    ('Use Chatter actions to create tasks to complete.', False)
                ]
            },
            {
                'text': 'At Universal containers, all US Sales reps should be able to view the US Team dashboard, however, only the US sales directors should be able to see the data in the component and view its source report. How can an app builder ensure the proper access is granted?',
                'answers': [
                    ('Make the US Sales Director the running user and share the dashboard folder with the role US Sales Rep', False),
                    ('Make the dashboard dynamic and give US Sales Reps the view my teams dashboard permission', False),
                    ('Share the dashboard folder with roles and subordinates of the US Sales Director and share the report folder with the role of US Sales Director', True),
                    ('Share the dashboard with the public group US Sales Reps and share the dashboard source reports folder with the US Sales Director profile', False)
                ]
            },
            {
                'text': 'DreamHouse Realty (DR) has many properties for sale and wants to identify the highest value of all Offer__c records on each Property__c record. What solution should the app builder use to meet DreamHouse Realty\'s needs?',
                'answers': [
                    ('Master-Detail Child Object', True),
                    ('Text Area (Long)', False),
                    ('Multi-select Picklist', False),
                    ('Lookup Object', False)
                ]
            },
            {
                'text': 'Ursa Major Solar (UMS) is looking to hire some new employees. UMS wants to allow the same applicant to apply for multiple open positions using a single application. What should an app builder recommend to meet these requirements?',
                'answers': [
                    ('Create a master-detail relationship on Open_Position__c to Application__c', False),
                    ('Create a master-detail relationship held on Applicant__c to Application__c', False),
                    ('Create a master-detail relationship field on Application__c to Open_Position__c', False),
                    ('Create a master-detail relationship field on Applicant__c to Application__c', True)
                ]
            },
            {
                'text': 'Universal Containers conduct evaluations of their sales reps using a custom object consisting of numerical scores and executive comments. The company wants to ensure that only the sales reps, and their manager\'s executive can view the rep\'s evaluation record but the reps should not be able to view the executive comment field on their review. How can these requirements be met?',
                'answers': [
                    ('Use a private sharing model granting record access using hierarchy; manage field access with record types and field-level security', False),
                    ('Use a private sharing model granting record access using custom setting; manage field access with page layouts and field level security', False),
                    ('Use a private sharing model granting record access using hierarchy; manage field access with field-level security', True),
                    ('Use a private sharing model granting record access using custom setting; manage field access with record types and page layouts', False)
                ]
            },
            {
                'text': 'To increase adoption, Universal Containers is proposing changes to its Salesforce data model to allow easier visibility for sales reps into key metrics. The proposal has three custom objects related to the Account object, one with a master-detail, and two that are not. Each of these objects has 15 fields they would like to summarize on the Account object. What are two considerations for this proposal?',
                'answers': [
                    ('Roll-up summaries allow MAX, MIN, SUM, COUNT, and AVG.', False),
                    ('An object can have 20 object references.', False),
                    ('An object can have 25 roll-up summaries.', True),
                    ('Roll-up summaries are limited to master-detail relationships.', True)
                ]
            },
            {
                'text': 'Universal Containers wants users to have access to the pricing guidelines document when viewing a Contract related to an Account. What feature should an app builder use to create easy access to the document?',
                'answers': [
                    ('Quick Action on the Contracts object', False),
                    ('Quick Action on the Account object', False),
                    ('A custom detail page link on the Account object', False),
                    ('A custom detail page link on the Contract object', True)
                ]
            },
            {
                'text': 'A recently refreshed partial sandbox at Cloud Kicks has no data in the custom object Shipping. Checking in production, there are two million rows of data in the object. What could be the reason the data is missing?',
                'answers': [
                    ('The sandbox was refreshed too early.', False),
                    ('The selected objects in the sandbox template.', True),
                    ('The Partial sandbox is at capacity.', False),
                    ('The sandbox is still populating data.', False)
                ]
            },
            {
                'text': 'Cloud Kicks received a new requirement to calculate summaries from child objects of a standard object. The team would prefer to solve this declaratively. What are two considerations an app builder should evaluate?',
                'answers': [
                    ('An app builder is unable to change a lookup to a master-detail relationship.', False),
                    ('An object can have up to two master-detail relationships.', True),
                    ('A trigger on save or update can kick off calculations.', False),
                    ('A value is required in all records of the lookup field prior to converting to a master-detail relationship.', True)
                ]
            },
            {
                'text': 'Northern Trail Outfitters wants the field sales team to only see the accounts that they own. Separate North American and European marketing teams should only see accounts in their respective regions. The inside sales team needs to see all accounts in Salesforce. How can this be accomplished?',
                'answers': [
                    ('Set the Organization-Wide Default to Public for accounts. Create criteria-based sharing rules for each marketing team, and create an Inside Sales Team permission set with the "View All" setting for accounts.', False),
                    ('Set the Organization-Wide Default to Public for accounts. Create profiles for each marketing team, and create an Inside Sales Team role that is at the top of the Role Hierarchy.', False),
                    ('Set the Organization-Wide Default to Private for accounts. Create criteria-based sharing rules for each marketing team, and create an Inside Sales Team profile with the "View All" setting for accounts.', True),
                    ('Set the Organization-Wide Default to Private for accounts. Create permission sets for each marketing team, and create an Inside Sales Team profile with the "View All" setting for accounts.', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to display the number of opportunities that are Closed Won with a Close Date within the last year on the Account detail page. Which tool should an app builder use to implement this?',
                'answers': [
                    ('Process Builder', False),
                    ('Activity Timeline', False),
                    ('Roll-Up Summary Field', True),
                    ('Workflow Rule', False)
                ]
            },
            {
                'text': (
                    "The DreamHouse Realty (DR) service manager has asked for some improvements "
                    "in case management to enforce process compliance so that cases are unable to be "
                    "reverted to an earlier case status, and to ensure that certain fields are "
                    "required when specific case criteria are met. What solution should an app builder "
                    "implement to meet these requirements?"
                ),
                'answers': [
                    ('Workflow Rules', False),
                    ('Process Builder', False),
                    ('Validation Rules', True),
                    ('Activities Component', False)
                ]
            },
            {
                'text': (
                    "Universal Containers has several new fields they've requested for the Opportunity "
                    "Product object. What should an app builder be able to configure using a formula field?"
                ),
                'answers': [
                    ('A hyperlink to the parent Account of the parent Opportunity.', False),
                    ('A Rich Text area field that uses HTML to bold certain characters.', False),
                    ('A combination of the Opportunity\'s Text and a Description fields.', True),
                    ('A mix of functions and concatenation of 10 Account fields and 10 Opportunity fields.', False)
                ]
            },
            {
                'text': (
                    "Which two solutions prevent a formula field from being referenced by a Roll-Up Summary "
                    "Field?"
                ),
                'answers': [
                    ('A cross-object workflow updating a field referenced by the formula field', False),
                    ('A cross-object field reference in the formula field', True),
                    ('The CASE () function in the formula field', False),
                    ('The NOW () function in the formula field', True)
                ]
            },
            {
                'text': (
                    "An app builder is preparing to deploy a new app from the sandbox to production using "
                    "change sets. What two considerations should an app builder keep in mind during this process?"
                ),
                'answers': [
                    ('Salesforce Connect automatically establishes a link between environments.', False),
                    ('Change sets do not include all components and may have to perform some changes manually.', True),
                    ('Users should be logged out of production when receiving inbound change sets.', False),
                    ('Transactions will revert if the deployment errors.', True)
                ]
            },
            {
                'text': (
                    "At Ursa Major Solar there is a requirement for a new field called Planet Details on the "
                    "Planet object where users can write detailed descriptions that can include pictures and links. "
                    "What field type should the app builder utilize to fulfill this requirement?"
                ),
                'answers': [
                    ('Long Text Area', False),
                    ('Rich Text Area', True),
                    ('Multi-Select Picklist', False),
                    ('URL', False)
                ]
            },
            {
                'text': (
                    "Sales reps at Universal Containers use Salesforce on their mobile devices. They want a way "
                    "to add new contacts quickly and then follow up later to complete the additional information "
                    "necessary. What mobile solution should an App Builder recommend?"
                ),
                'answers': [
                    ('Customize the mobile menu to move Contacts to the top.', False),
                    ('Build a global action to create Contacts.', True),
                    ('Add a compact layout to Contacts.', False),
                    ('Use Path and set pre-defined values.', False)
                ]
            },
            {
                'text': (
                    "The developer at Universal Containers wants to test code in a sandbox environment. In order "
                    "to ensure the code works properly, the sandbox needs to have at least half a gigabyte of data. "
                    "The sandbox will need to be refreshed after each three-day sprint. What type of sandbox should "
                    "the App Builder provision to the developer?"
                ),
                'answers': [
                    ('Developer', False),
                    ('Full Copy', False),
                    ('Developer Pro', True),
                    ('Partial Data', False)
                ]
            },
            {
                'text': (
                    "An app builder wants to create a custom object and 10 fields. What should they use to create "
                    "the object, fields, and relationships quickly from one place?"
                ),
                'answers': [
                    ('Schema Builder', True),
                    ('Developer Console', False),
                    ('Manage Field Permissions', False),
                    ('Lightning Object Creator', False)
                ]
            },
            {
                'text': (
                    "Universal Containers wants to display the real-time stock price for each Account on the "
                    "Account record page. How should an app builder implement this request?"
                ),
                'answers': [
                    ('Create a Lightning Web Component.', False),
                    ('Install a solution from the AppExchange.', True),
                    ('Build a Flow that uses API calls.', False),
                    ('Use a scheduled Apex job.', False)
                ]
            },
            {
                'text': "An app Builder creates an Account validation rule on the Industry field that "
                        "will throw an error if the length of the field is longer than 6 characters. "
                        "Another App Builder creates a workflow rule with a field update that sets "
                        "the Industry field to Technology whenever the Billing City field is set to "
                        "San Francisco. What will happen the next time a salesperson saves an "
                        "Account with a Billing City of San Francisco?",
                'answers': [
                    ('The record will save and the Industry field will change to Technology', False),
                    ('The record will not save and the validation rule\'s error message will be displayed', True),
                    ('The record will not save and no error message will be displayed', False),
                    ('The record will save but the Industry field will not change to Technology', False)
                ]
            },
            {
                'text': "UC has a requirement that an opportunity should have a field showing the value "
                        "of its associated account\'s billing state. This value should not change after "
                        "the opportunity has been created. Is there a recommended solution to configure "
                        "this automated behavior?",
                'answers': [
                    ('Formula field', False),
                    ('Apex', False),
                    ('Workflow', True),
                    ('Roll-up summary field', False)
                ]
            },
            {
                'text': "A user is unable to use inline editing on a list view. A quick check verifies "
                        "the user should be able to perform inline editing as they have been assigned the "
                        "appropriate permissions. Which two conditions should the app builder review?",
                'answers': [
                    ('If the list view restricts sharing for the user', False),
                    ('If the list view selected is the recently viewed list view', True),
                    ('If the list view contains a chart created by the user', False),
                    ('If the list view contains more than one record type', True)
                ]
            },
            {
                'text': "Universal Containers uses a custom picklist called Account_Region__c on the "
                        "Account object. The vice president of sales has asked that the value of this "
                        "field is visible on Opportunities. How should an app builder create this solution?",
                'answers': [
                    ('Lookup field', False),
                    ('Field-level security', False),
                    ('Field history tracking', False),
                    ('Cross-object formula field', True)
                ]
            },
            {
                'text': "Universal Containers manages leads in a Lead qualification queue where sales "
                        "reps can accept ownership of the Lead. Campaign members are required to have a "
                        "sales owner. What validation rule should an app builder configure?",
                'answers': [
                    ('AND( ISBLANK(Lead.Owner.Id) )', False),
                    ('NOT(ISNEW() && ISBLANK(Lead.Owner:Queue.Id))', False),
                    ('AND(ISNEW(), ISBLANK(Lead.Owner:User.Id))', False),
                    ('NOT(ISBLANK(Lead.Owner:Queue.Id))', True)
                ]
            },
            {
                'text': "An app builder at Northern Trail Outfitters created a sandbox template for "
                        "Accounts, Projects, and Project Milestones to reconfigure some flows for the "
                        "project management app. Which type of testing environment should the app builder create?",
                'answers': [
                    ('Developer', False),
                    ('Partial Copy', True),
                    ('Developer Pro', False),
                    ('Scratch Org', False)
                ]
            },
            {
                'text': "Cloud Kicks wants to set up a new opportunity approval process and execute "
                        "various action items based on the initial submission. Which three action types "
                        "should an app builder use in the approval process?",
                'answers': [
                    ('Email Alert', True),
                    ('Outbound Message', True),
                    ('Task', True),
                    ('Invocable Flow', False),
                    ('Invocable Process Builder', False)
                ]
            },
            {
                'text': "Service agents at Ursa Major Solar want a more condensed case view. Service "
                        "agents also want to be able to modify the associated contact and account records "
                        "from the case page layout on the Lightning record page. Which two components "
                        "should an app builder use to meet these requirements?",
                'answers': [
                    ('Path', False),
                    ('Rich text', False),
                    ('Related record', True),
                    ('Tabs', True)
                ]
            },
            {
                'text': "A Cloud Kicks employee submitted an opportunity for approval by their manager. "
                        "What would happen if the employee attempts to edit the description field after "
                        "submission?",
                'answers': [
                    ('User will be presented with a \'Record Lock\' notification', True),
                    ('User will be able to edit the description field only', False),
                    ('User will see the record is now owned by their manager', False),
                    ('User will be able to edit the name, but unable to edit the description', False)
                ]
            },
            {
                'text': "A sales rep at AW Computing is unable to find what they are looking for while "
                        "scrolling through their Chatter feed. How can a filter be utilized to show only "
                        "posts from their key account and opportunity records?",
                'answers': [
                    ('Create a Chatter group', False),
                    ('Create Chatter bookmarks', False),
                    ('Create a Chatter stream', True),
                    ('Create a Chatter notification', False)
                ]
            },

            {
                'text': 'Sales reps want the ability to see who can view their account records and how the people have access. Which button should the app builder add to the Account page layout to enable this?',
                'answers': [
                    ('Sharing Hierarchy', False),
                    ('New Task', False),
                    ('Sharing', True),
                    ('Fait', False)
                ]
            },
            # Question 179
            {
                'text': 'The app builder at Ursa Major Solar has just created a master-detail relationship between a parent object Galaxy__c and child object Star__c. What would be the effect of creating this type of relationship if users want to report on Galaxy__c with Star__c?',
                'answers': [
                    ('A Star__c report type with Galaxy__c as a field will be automatically created.', False),
                    ('A new custom report type will need to be created for Star__c with lookup fields from Galaxy__c.', False),
                    ('A Galaxy__c with Star__c report type will be automatically created.', True),
                    ('A new custom report type will need to be created for Galaxy__c with Star__c.', False)
                ]
            },
            {
                'text': 'Shipments at Cloud Kicks (CK) are created and updated by the warehouse staff in a shipping application. The Information needs to be pushed into Salesforce on a regular basis. CK\'s app builder creates a custom object called Delivery_c to track the information. How can the app builder prevent creating duplicate delivery records and update the correct existing records when migrating data from the shipping application?',
                'answers': [
                    ('Use the Import Wizard and match on the tracking number.', False),
                    ('Create a unique External ID field and use Dataloader.', True),  # Correct Answer
                    ('Use the Import Wizard and match on the Salesforce ID.', False),
                    ('Create a duplicate match rule and use Dataloader.', False),
                ]
            },
            {
                'text': 'An App Builder is loading the data into Salesforce. To link the new records back to the legacy system, a field will be used to track the legacy ID on the account object. For future data loads, this ID will be used when upserting records. Which field attribute should be selected? Choose 2 answers.',
                'answers': [
                    ('Unique', True),  # Correct Answer
                    ('Required', False),
                    ('External ID', True),  # Correct Answer
                    ('Text (encrypted)', False),
                ]
            },
            {
                'text': 'Universal Containers has a Lightning record page that supports both the mobile app and desktop. An app builder has downloaded a custom Lightning component from AppExchange, but users are unable to view the component on mobile devices. What can be the issue?',
                'answers': [
                    ('The record page needs to be activated.', False),
                    ('The component has been developed for Desktop Pages.', True),  # Correct Answer
                    ('The component needs to be activated.', False),
                    ('The record page template is unable to support mobile devices.', False),
                ]
            },
            {
                'text': 'The appraisal team at DreamHouse Realty wants to leverage the Salesforce mobile app. What are three things an app builder should do to optimize the mobile experience? Choose 3 answers.',
                'answers': [
                    ('Use Global Actions to make it easy to perform vital functionality on mobile.', True),  # Correct Answer
                    ('Avoid using default field values so that the user is required to fill in all fields on the screen.', False),
                    ('Minimize the amount of formula fields and lookup fields to reduce page load time.', True),  # Correct Answer
                    ('Create individual customized layouts for different phone operating systems.', False),
                    ('Put the most important fields in the compact layout so they are easy to find.', True),  # Correct Answer
                ]
            },
            {
                'text': 'Where can an app builder edit an existing app to add components to the utility bar?',
                'answers': [
                    ('App Menu', False),
                    ('Lightning App Builder', False),
                    ('App Manager', True),  # Correct Answer
                    ('Lightning Record Page', False),
                ]
            },
            {
                'text': 'Cloud Kicks has five years of sales data and would like to track when customers made their first purchase. How should an app builder use a roll-up summary to meet the requirements?',
                'answers': [
                    ('Create a new roll-up summary field called First Order Date, using Type MIN on the Opportunity Close Date with a filter where IsWon = TRUE.', True),  # Correct Answer
                    ('Create a new date field called First Order Date, create a new Workflow to set the date, and roll up the value with a filter where IsWon = TRUE.', False),
                    ('Create a new roll-up summary field called First Order Date, using Type SUM on Opportunity Close Date.', False),
                    ('Create a new date field called First Order Date, then create a roll-up summary to update the field using Type MIN.', False),
                ]
            },
            {
                'text': 'Universal Containers assigns system access via permission sets and permission set groups to ensure each user has proper access. One department with varying levels of support staff has five consistent permission sets they require in order to complete their duties. Some higher-level staff have additional permission sets that are only required for them. How should an app builder recommend assigning permission sets to users?',
                'answers': [
                    ('Utilize the manage assignments button to assign a permission set group and additional individual permission sets to each user.', True),  # Correct Answer
                    ('Utilize the manage assignments button to assign each user with the same set of permission set groups and permission sets.', False),
                    ('Utilize the Data Import Wizard to mass update the desired users with their full list of permission sets and permission set groups.', False),
                    ('Utilize the Data Loader to mass update the desired users with their full list of permission sets and permission set groups.', False),
                ]
            },
            {
                'text': 'Cloud Kicks is redefining its entire business process to convert the Manager Notes field from a long text area field. The goal is to encourage managers to be more concise in their comments and stay at 255 characters or less. There is preexisting information in the Manager Notes field that often is well beyond the character limit. What would happen to any existing information if the app builder tries to convert a preexisting long text area field to text area?',
                'answers': [
                    ('Preexisting information will truncate to the first 255 characters.', True),  # Correct Answer
                    ('Preexisting information will remain even if it was over 255 characters.', False),
                    ('Preexisting information will cause an error message to pop up.', False),
                    ('Preexisting information in the field will be completely lost.', False),
                ]
            },
            {
                'text': 'An app builder has created a new report type but users are unable to select it from the Report Type list when making a new report for records they own. What could be causing this issue?',
                'answers': [
                    ('Access to the necessary object is unavailable.', False),
                    ('The report type is in a status of Deployed.', False),
                    ('Access to Create and Customize Reports is disabled.', False),
                    ('The report type is in a status of In Development.', True)
                ]
            },
            {
                'text': 'The marketing team at UVC has a list of 400 leads it wants to upload to Salesforce. The team needs to avoid creating duplicate records. Which two actions should be taken to meet this requirement? Choose 2 answers.',
                'answers': [
                    ('Utilize a Lead Matching Rule and corresponding Duplicate Rule to block newly created duplicate leads.', True),
                    ('Upload the lead list using the import wizard and select a Matching type to prevent duplicate lead creation.', True),
                    ('Use Data Loader\'s update function to import lead and match to existing records based on e-mail address.', False),
                    ('Enable Duplicate Matching in the Data Management section in Setup and activate the Lead-to-Lead scenario.', False)
                ]
            },
            {
                'text': 'An App Builder at UVC would like to prevent users from creating new records on an Account related list by overriding standard buttons. Which two should the App Builder consider before overriding standard buttons?',
                'answers': [
                    ('Standard buttons can be changed on lookup dialogs, list views, and search result layouts.', False),
                    ('Standard buttons can be overridden with a Visualforce page.', True),
                    ('Standard buttons that are not available for overrides can still be hidden on page layouts.', True),
                    ('Standard buttons can be overridden, relocated on the detail page, and relabeled.', False)
                ]
            },
            {
                'text': 'DreamHouse Realty asks for improvements in case management. They want to enforce process compliance so that cases are unable to be reverted to an earlier status. Which solution should an app builder implement?',
                'answers': [
                    ('Configure validation rules with help text.', True),
                    ('Create dependent picklist fields and set them as required.', False),
                    ('Use an approval process to check field criteria are met.', False),
                    ('Make the fields required on the page layout.', False)
                ]
            },
            # Question 192
            {
                'text': 'Where should the app builder go to build roll-up summaries for open and won Opportunities for each Account?',
                'answers': [
                    ('Lightning App Builder', False),
                    ('Account Object', True),
                    ('Lightning Object Creator', False),
                    ('Opportunity Object', False)
                ]
            },
            # Question 193
            {
                'text': 'How should an app builder connect Testimonial__c records with Contact and Account so that Testimonial__c is deleted if Account is deleted, but remains if Contact is deleted?',
                'answers': [
                    ('Make both fields required and create lookup relationships.', False),
                    ('Master-detail to Account, lookup to Contact.', True),
                    ('Use junction object with master-detail relationships.', False),
                    ('Lookup to Account, master-detail to Contact.', False)
                ]
            },
            # Question 194
            {
                'text': 'What functionality should be used to prevent naming conflicts when setting up managed packages?',
                'answers': [
                    ('Description', False),
                    ('Allow sharing', False),
                    ('Help setting', False),
                    ('Namespace', True)
                ]
            },
            # Question 195
            {
                'text': 'Universal Containers wants to capture coordinates to deliver containers to remote locations. What type of field should the app builder use?',
                'answers': [
                    ('Number', False),
                    ('Geo  ocation', True),
                    ('Text', False),
                    ('External Lookup', False)
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
        migrations.RunPython(add_crt4, atomic=False),
    ]