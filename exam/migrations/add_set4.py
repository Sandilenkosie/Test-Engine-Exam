from django.db import migrations,transaction

def add_set4(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')
    Group = apps.get_model('exam', 'Group')

    with transaction.atomic():
        group, created = Group.objects.get_or_create(
            name='ADM-Exams',
            defaults={'description': 'Group for ADM related exams'}
        )

        # Create an exam instance and associate it with the group
        exam = Exam.objects.create(title='#ADM-4 Exam')

        # If you want to add the exam to the group (assuming a many-to-many relation):
        group.exams.add(exam)

        # Define questions and answers
        questions_data = [
        {
            'text': 'DreamHouse Realty agents are double-booking open house event nights. The event manager wants the event submission process to help agents fill in event details and request dates. How should an administrator accomplish this request?',
            'answers': [
                ('Create a campaign for agents to request event dates.', True),
                ('Create a workflow rule to update the Event Date Field.', False),
                ('Create an approval process on the Campaign object.', False),
                ('Create a sharing rule so that other agents can view events.', False)
            ]
        },
        {
            'text': 'Cloud Kicks intends to protect data with backups by using the data export service. Which two considerations should the administrator remember when scheduling the export?',
            'answers': [
                ('Data Backups are limited to weekly or monthly intervals.', True),
                ('Metadata backups must be run via a separate process.', False),
                ('Data export service should be run from a sandbox.', False),
                ('Metadata Backups are limited to sandbox refresh intervals.', True)
            ]
        },
        {
            'text': 'Cloud Kicks needs to change the owner of a case when it has been open for more than 7 days. How should the administrator complete this requirement?',
            'answers': [
                ('Escalation Rule', True),
                ('Auto-Response Rules', False),
                ('Validation Rule', False),
                ('Assignment Rule', False)
            ]
        },
        {
            'text': 'The administrator has been asked to automate a simple field update on the account. When a support agent changes the status of the account to ‘Audited’, they would like the system to automatically update the Audited date field on the account with today’s date. Which tool should the administrator use to complete this automation?',
            'answers': [
                ('Flow Builder', True),
                ('Formula Field', False),
                ('Approval process', False),
                ('Validation Rule', False)
            ]
        },
        {
            'text': 'AW Computing wants to prevent users from updating the Account Annual Revenue field to be a negative value or an amount more than $100 billion. How should an administrator accomplish this request?',
            'answers': [
                ('Create a validation rule that displays an error if Account revenue is below 0 or greater than 100 billion.', True),
                ('Build a scheduled report displaying Accounts with revenue that is negative or greater than 100 billion.', False),
                ('Make the Account Revenue field required on the page layout.', False),
                ('Enable the Account Revenue limits in setup, with 0 as minimum and 100 billion as maximum.', False)
            ]
        },
        {
            'text': 'DreamHouse Realty (DHR) wants a templated process with a mortgage calculator that generates leads for loans. DHR needs to complete the project within 30 days and has maxed out its budget for the year. Which AppExchange item should help the administrator to meet the request?',
            'answers': [
                ('Flow Solutions', True),
                ('Lightning Data', False),
                ('Lightning Community', False),
                ('Bolt Solutions', False)
            ]
        },
        {
            'text': 'The Call Centre manager at Ursa Major Solar wants to provide agents with a case dashboard that can be drilled down by case origin, status, and owner. What should an administrator add to the dashboard to fulfill the request?',
            'answers': [
                ('Dashboard Filter', True),
                ('Bucket column', False),
                ('Dashboard component', False),
                ('Combination Chart', False)
            ]
        },
        {
            'text': 'Universal Container wants to prevent its service team from accessing deal records. While service users are unable to access deal list views, they are able to find the deal records via a search. What options should the administrator adjust to fully restrict access?',
            'answers': [
                ('Record setting and search index', False),
                ('Permissions and tab visibility', False),
                ('App permissions and search terms', False),
                ('Page layouts and field-level security', True)
            ]
        },
        {
            'text': 'Ursa Major Solar is noticing a decrease in deals with a cross-sell opportunity type and wants to share all cross-sell opportunities with a team of subject matter experts in their organization. The company has different roles, and the organization-wide default opportunity is set to private. How should the administrator accomplish this?',
            'answers': [
                ('Add the subject matter experts to a public group and give them access to records with a criteria-based sharing rule.', True),
                ('Change the organization-wide default for opportunity from private to public Read/Write to open up access for subject matter experts.', False),
                ('Enable territory management, assign the subject matter experts to the same territory, and give them access to the records with manual sharing.', False),
                ('Create a new role for the subject matter experts and give them access to the records with the owner-based sharing rule.', False)
            ]
        },
        {
            'text': 'Cloud Kicks has a screen flow with two questions on the same screen, but only one is necessary at a time. The administrator has been asked to show only the question that is needed. How should an administrator complete this?',
            'answers': [
                ('Use conditional visibility to hide the unnecessary question.', True),
                ('Use a decision element and a new screen to show the proper question.', False),
                ('Use a new version of the flow for each scenario.', False),
                ('Use branching in the flow screen to show the proper scenario.', False)
            ]
        },
        {
            'text': 'AW Computing would like to improve its Case Lightning record page by including: • A filtered component to display a message in bold font when a case is saved as a critical record type. • A quick way to update the account status from the case layout. Which two components should an administrator use to satisfy these requests?',
            'answers': [
                ('Related Record', True),
                ('Rich text', True),
                ('Related List', False),
                ('Record details', False)
            ]
        },
        {
            'text': 'An administrator at DreamHouse Realty wants an easier way to assign cases based on the agent’s capacity and skill set. Which feature should the administrator enable to meet this requirement?',
            'answers': [
                ('Omni-Channel', True),
                ('Escalation rules', False),
                ('Territory management', False),
                ('Knowledge management', False)
            ]
        },
        {
            'text': 'The Administrator at Universal Container wants to add branding to Salesforce. Which two considerations should the administrator keep in mind?',
            'answers': [
                ('Only one theme can be active at a time, and a theme applies to the entire org.', True),
                ('Themes apply to Salesforce Classic and to the Salesforce mobile app.', False),
                ('Up to 150 custom themes can be created, modified, or cloned from the built-in themes.', True),
                ('Chatter external users see the built-in Lightning theme only.', True)
            ]
        },
        {
            'text': 'An administrator supporting a global team of Salesforce users has been asked to configure the company settings. Which two options should the administrator configure?',
            'answers': [
                ('Default Language', True),
                ('Currency Locale', True),
                ('Login Hours', False),
                ('Password Policy', False)
            ]
        },
        {
            'text': 'Users at Cloud Kicks are reporting different options when uploading a custom picklist on the Opportunity object based on the kind of opportunity. Where should an administrator update the option in the picklist?',
            'answers': [
                ('Record Type', True),
                ('Fields and relationships', False),
                ('Picklist value sets', False),
                ('Related lookup filters', False)
            ]
        },
        {
            'text': 'An administrator has been asked to update a flow that was created as part of a recent update. When the administrator opens the flow for editing, the Flow toolbox offers only four elements: Assignment, Decision, Get Records, and Loop. What would cause this?',
            'answers': [
                ('The flow is a before save flow.', True),
                ('The flow is a screen flow.', False),
                ('The version of the flow is inactive.', False),
                ('The version of the flow is activated.', False)
            ]
        },
        {
        'text': 'THE ADMINISTRATOR AT CLOUD KICKS HAS A CUSTOM PICKLIST FIELD ON LEAD, WHICH IS MISSING ON THE CONTACT WHEN LEADS ARE CONVERTED. WHICH TWO ITEMS SHOULD THE ADMINISTRATOR DO TO MAKE SURE THESE VALUES ARE POPULATED? CHOOSE 2 ANSWERS',
        'answers': [
            ('CREATE A CUSTOM PICKLIST FIELD ON CONTACT.', True),
            ('UPDATE THE PICKLIST VALUE WITH A VALIDATION RULE.', False),
            ('MAP THE PICKLIST FIELD ON THE LEAD TO THE CONTACT.', True),
            ('SET THE PICKLIST FIELD TO BE REQUIRED ON THE LEAD OBJECT.', False)
        ]
    },
    {
        'text': 'UNIVERSAL CONTAINERS IS TRYING TO IMPROVE THE USER EXPERIENCE WHEN SEARCHING FOR THE RIGHT STATUS ON A CASE. THE COMPANY CURRENTLY HAS ONE SUPPORT PROCESS THAT IS USED FOR ALL RECORD TYPES ON CASES. THE SUPPORT PROCESS HAS 10 STATUS VALUES. SERVICE REPS SAY THEY NEVER NEED MORE THAN FIVE DEPENDING ON WHAT KIND OF CASE THEY ARE WORKING ON. HOW SHOULD THE ADMINISTRATOR IMPROVE ON THE CURRENT IMPLEMENTATION?',
        'answers': [
            ('REDUCE THE NUMBER OF CASE STATUS VALUES TO FIVE.', False),
            ('CREATE A SCREEN FLOW THAT SHOWS ONLY THE CORRECT VALUES FOR STATUS AND SURFACE THE FLOW IN THE UTILITY BAR OF THE CONSOLE.', False),
            ('REVIEW WHICH STATUS CHOICES ARE NEEDED FOR EACH RECORD TYPE AND CREATE SUPPORT PROCESSES FOR EACH THAT IS NECESSARY.', True),
            ('EDIT THE STATUS CHOICES DIRECTLY ON THE RECORD TYPE.', False)
        ]
    },
    {
        'text': 'AN ADMINISTRATOR WANTS TO CREATE A FORM IN SALESFORCE FOR USERS TO FILL OUT WHEN THEY LOSE A CLIENT. WHICH AUTOMATION TOOL SUPPORTS CREATING A WIZARD TO ACCOMPLISH THIS GOAL?',
        'answers': [
            ('PROCESS BUILDER', False),
            ('APPROVAL PROCESS', False),
            ('OUTBOUND MESSAGE', False),
            ('FLOW BUILDER', True)
        ]
    },
    {
        'text': 'THE CLIENT SERVICES AND CUSTOMER SUPPORT TEAMS SHARE THE SAME PROFILE BUT HAVE DIFFERENT PERMISSION SETS. THE CUSTOM OBJECT RETENTION RELATED LIST NEEDS TO BE RESTRICTED TO THE CLIENT SERVICES TEAM ON THE LIGHTNING RECORD PAGE LAYOUT. WHAT SHOULD THE ADMINISTRATOR USE TO FULFILL THIS REQUEST?',
        'answers': [
            ('SHARING SETTINGS', False),
            ('PAGE LAYOUT ASSIGNMENT', False),
            ('COMPONENT VISIBILITY', True),
            ('RECORD TYPE ASSIGNMENT', False)
        ]
    },
    {
        'text': 'THE VP OF SALES AT UNIVERSAL CONTAINERS WANTS TO PREVENT MEMBERS OF THE SALES TEAM FROM CHANGING AN OPPORTUNITY TO A DATE IN THE PAST. WHAT SHOULD AN ADMINISTRATOR CONFIGURE TO MEET THIS REQUIREMENT?',
        'answers': [
            ('ASSIGNMENT RULE', False),
            ('VALIDATION RULE', True),
            ('FIELD-LEVEL SECURITY', False),
            ('APPROVAL PROCESS', False)
        ]
    },
    {
        'text': 'NORTHERN TRAIL OUTFITTERS WANTS TO TRACK ROI FOR CONTACTS THAT ARE KEY STAKEHOLDERS FOR OPPORTUNITIES. THE VP OF SALES REQUESTED THAT THIS INFORMATION BE ACCESSIBLE ON THE OPPORTUNITY AND AVAILABLE FOR REPORTING. WHICH TWO OPTIONS SHOULD THE ADMINISTRATOR CONFIGURE TO MEET THESE REQUIREMENTS? CHOOSE 2 ANSWERS',
        'answers': [
            ('CUSTOMIZE CAMPAIGN MEMBER ROLE.', False),
            ('ADD THE CAMPAIGN MEMBER RELATED LIST TO THE OPPORTUNITY PAGE LAYOUT.', False),
            ('CUSTOMIZE CAMPAIGN ROLE.', False),
            ('CUSTOMIZE OPPORTUNITY CONTACT ROLE.', True),
            ('ADD THE OPPORTUNITY CONTACT ROLE RELATED LIST TO THE OPPORTUNITY PAGE LAYOUT.', True)
        ]
    },
    {
        'text': 'THE ADMINISTRATOR AT CLOUD KICKS NEEDS TO AUTOMATICALLY ROUTE SUPPORT CASES, REGARDLESS OF HOW THEY ARE CREATED, TO A QUEUE BASED ON CASE PRIORITY. WHAT TOOL SHOULD THE ADMINISTRATOR USE?',
        'answers': [
            ('EMAIL-TO-CASE', False),
            ('ASSIGNMENT RULES', True),
            ('AUTO-RESPONSE RULES', False),
            ('WEB-TO-CASE', False)
        ]
    },
    {
        'text': 'DREAM HOUSE REALTY NEEDS TO USE CONSISTENT PICKLIST VALUE ON A CATEGORY FIELD ON ACCOUNTS AND CASES, WITH VALUE RESPECTIVE TO RECORD TYPES. WHICH TWO FEATURES SHOULD THE ADMINISTRATOR USE TO FULFILL THIS REQUIREMENT? CHOOSE 2 ANSWERS',
        'answers': [
            ('DEPENDENT PICKLIST', False),
            ('GLOBAL PICKLIST', True),
            ('MULTI-SELECT PICKLIST', False),
            ('CUSTOM PICKLIST', True)
        ]
    },
    {
        'text': 'WHEN A SALES REP CLICKS A BUTTON ON AN OPPORTUNITY, A SIMPLE DISCOUNT CALCULATOR SCREEN SHOULD BE LAUNCHED. WHICH AUTOMATION TOOL SHOULD AN ADMINISTRATOR USE TO BUILD THIS DISCOUNT CALCULATOR SCREEN?',
        'answers': [
            ('FLOW BUILDER', True),
            ('WORKFLOW RULE', False),
            ('PLATFORM EVENT', False),
            ('PROCESS BUILDER', False)
        ]
    },
    {
        'text': 'NORTHERN TRAIL OUTFITTERS WANTS TO INITIATE EXPENSE REPORTS FROM SALESFORCE TO THE EXTERNAL HR SYSTEM. THIS PROCESS NEEDS TO BE REVIEWED BY MANAGERS AND DIRECTORS. WHICH TWO TOOLS SHOULD AN ADMINISTRATOR CONFIGURE? CHOOSE 2 ANSWERS',
        'answers': [
            ('QUICK ACTION', False),
            ('OUTBOUND MESSAGE', True),
            ('APPROVAL PROCESS', True),
            ('EMAIL ALERT ACTION', False)
        ]
    },
    {
        'text': 'CLOUD KICKS IS WORKING ON A BETTER WAY TO TRACK ITS PRODUCT SHIPMENTS UTILIZING SALESFORCE. WHICH FIELD TYPE SHOULD AN ADMINISTRATOR USE TO CAPTURE COORDINATES?',
        'answers': [
            ('GEOLOCATION', True),
            ('GEOFENCE', False),
            ('CUSTOM ADDRESS', False),
            ('EXTERNAL LOOKUP', False)
        ]
    },
    {
        'text': 'WHAT ARE TWO CONSIDERATIONS AN ADMINISTRATOR SHOULD KEEP IN MIND WHEN WORKING WITH SALESFORCE OBJECTS? CHOOSE 2 ANSWERS',
        'answers': [
            ('CUSTOM AND STANDARD OBJECTS HAVE STANDARD FIELDS.', True),
            ('STANDARD OBJECTS ARE INCLUDED WITH SALESFORCE.', True),
            ('A NEW STANDARD OBJECT CAN BE CREATED.', False),
            ('ONLY STANDARD OBJECTS SUPPORT MASTER-DETAIL RELATIONSHIPS.', False)
        ]
    },
    {
        'text': 'USERS HAVE NOTICED THAT WHEN THEY CLICK ON A REPORT IN A DASHBOARD TO VIEW THE REPORT DETAILS, THE VALUES IN THE REPORT ARE DIFFERENT FROM THE VALUES DISPLAYED ON THE DASHBOARD. WHAT ARE THE TWO REASONS THIS IS LIKELY TO OCCUR? CHOOSE 2 ANSWERS',
        'answers': [
            ('THE REPORT NEEDS TO BE REFRESHED.', False),
            ('THE DASHBOARD NEEDS TO BE REFRESHED.', True),
            ('THE CURRENT USER DOES NOT HAVE ACCESS TO THE REPORT FOLDER.', False),
            ('THE RUNNING DASHBOARD USER AND VIEWER HAVE DIFFERENT PERMISSIONS.', True)
        ]
    },
    {
        'text': 'THE MARKETING TEAM WANTS A NEW PICKLIST VALUE ADDED TO THE CAMPAIGN MEMBER STATUS FIELD FOR THE UPSELL PROMOTIONAL CAMPAIGN. WHICH TWO SOLUTIONS SHOULD THE ADMINISTRATOR USE TO MODIFY THE PICKLIST FIELD VALUES? CHOOSE 2 ANSWERS',
        'answers': [
            ('ADD THE CAMPAIGN MEMBER STATUSES RELATED LIST TO THE PAGE LAYOUT.', True),
            ('EDIT THE PICKLIST VALUES FOR THE CAMPAIGN STATUS IN OBJECT MANAGER.', True),
            ('MASS MODIFY THE CAMPAIGN MEMBER STATUSES RELATED LIST.', False),
            ('MODIFY THE PICKLIST VALUE ON THE CAMPAIGN MEMBER STATUSES RELATED LIST.', False)
        ]
    },
    {
        'text': 'URSA SOLAR MAJOR IS EVALUATING SALESFORCE FOR ITS SERVICE TEAM AND WOULD LIKE TO KNOW WHAT OBJECTS WERE AVAILABLE OUT OF THE BOX. WHICH THREE OF THE STANDARD OBJECTS ARE AVAILABLE TO AN ADMINISTRATOR CONSIDERING A SUPPORT USE CASE? CHOOSE 3 ANSWERS',
        'answers': [
            ('CONTRACT', True),
            ('CASE', True),
            ('TICKET', False),
            ('REQUEST', False),
            ('ACCOUNT', True)
        ]
    },
    {
        'text': 'THE ADMINISTRATOR AT CLOUD KICKS HAS BEEN ASKED TO REPLACE TWO OLD WORKFLOW RULES THAT ARE DOING SIMPLE FIELD UPDATED WHEN A LEAD IS CREATED TO IMPROVE PROCESSING TIME. WHAT TOOL SHOULD THE ADMINISTRATOR USE TO REPLACE THE WORKFLOW RULES?',
        'answers': [
            ('QUICK ACTION FLOW', False),
            ('BEFORE SAVE FLOW', True),
            ('SCHEDULED FLOW', False),
            ('SCREEN FLOW', False)
        ]
    },
    {
        'text': 'URSA MAJOR SOLAR USES OPPORTUNITY TO TRACK SALES OF SOLAR ENERGY PRODUCTS. THE COMPANY HAS TWO SEPARATE SALES TEAMS THAT FOCUS ON DIFFERENT ENERGY MARKETS. THE SERVICES TEAM ALSO WANTS TO USE OPPORTUNITY TO TRACK INSTALLATION. ALL THREE TEAMS WILL NEED TO USE DIFFERENT FIELDS AND STAGES. HOW SHOULD THE ADMINISTRATOR CONFIGURE THIS REQUIREMENT?',
        'answers': [
            ('CREATE THREE SALES PROCESSES.', True),
            ('CREATE THREE PAGE LAYOUTS.', True),
            ('CREATE ONE PAGE LAYOUT.', False),
            ('CREATE ONE SALES PROCESS.', False)
        ]
    },
            {
                'text': 'THE SERVICE MANAGER AT URSA MAJOR SOLAR WANTS TO LET CUSTOMERS KNOW THAT THEY HAVE RECEIVED THEIR CASES VIA EMAIL AND THEIR WEBSITES. MEDIUM-PRIORITY AND HIGH-PRIORITY CASES SHOULD RECEIVE DIFFERENT EMAIL NOTIFICATIONS THAN LOW-PRIORITY CASES. THE ADMINISTRATOR HAS CREATED THREE EMAIL TEMPLATES FOR THIS PURPOSE. HOW SHOULD AN ADMINISTRATOR CONFIGURE THIS REQUIREMENT?',
                'answers': [
                    ('INCLUDE THREE ASSIGNMENT RULES THAT FIRE WHEN CASES ARE CREATED. ADD A FILTER FOR CASE PRIORITY. SELECT THE APPROPRIATE EMAIL TEMPLATE FOR EACH RULE.', False),
                    ('ADD THREE AUTO-RESPONSE RULES. CONFIGURE ONE RULE ENTRY CRITERIA FOR EACH RULE AND SET A FILTER FOR CASE PRIORITY. SELECT THE APPROPRIATE EMAIL TEMPLATE FOR EACH RULE ENTRY.', False),
                    ('CONFIGURE ONE WORKFLOW RULE THAT FIRES WHEN CASES ARE CREATED. ADD A FILTER FOR CASE PRIORITY. SELECT THE APPROPRIATE EMAIL TEMPLATE FOR THE RULE.', False),
                    ('CREATE ONE AUTO-RESPONSE RULE. CONFIGURE THREE RULE ENTRY CRITERIA AND SET A FILTER FOR CASE PRIORITY. SELECT THE APPROPRIATE EMAIL TEMPLATE FOR EACH RULE ENTRY.', True)
                ]
            },
            {
                'text': 'THE VP OF SALES AT DREAMHOUSE REALTY HAS REQUESTED A DASHBOARD TO VISUALIZE ENTERPRISE SALES ACROSS THE DIFFERENT TEAMS. THE KEY PLACE OF DATA IS THE TOTAL OF ALL SALES FOR THE YEAR AND THE PROGRESS TO THE ENTERPRISE SALES GOAL. WHAT DASHBOARD COMPONENT WILL EFFECTIVELY SHOW THIS NUMBER AND THE PROXIMITY TO THE TOTAL GOAL AS A SINGLE VALUE?',
                'answers': [
                    ('TABLE', False),
                    ('STACKED BAR', False),
                    ('DONUT', False),
                    ('GAUGE', True)
                ]
            },
            {
                'text': 'A SALES REP HAS LEFT THE COMPANY AND AN ADMINISTRATOR HAS BEEN ASKED TO RE-ASSIGN ALL THEIR ACCOUNTS AND OPPORTUNITIES TO A NEW SALES REP AND KEEP THE TEAMS AS IS. WHICH TOOL SHOULD AN ADMINISTRATOR USE TO ACCOMPLISH THIS?',
                'answers': [
                    ('DATA LOADER', False),
                    ('MASS TRANSFER TOOL', True),
                    ('DATA IMPORT WIZARD', False),
                    ('DATALOADER.IO', False)
                ]
            },
            {
                'text': 'Northern trail outfitters has two different sales processes: one for business opportunities with four stages and one for partner opportunities with eight stages. Both processes will vary in page layouts and picklist value options What should an administrator configure to meet these requirements?',
                'answers': [
                    ('Validation rules that ensure that users are entering accurate sales stage information.', False),
                    ('Different page layouts that control the picklist values for the opportunity types.', False),
                    ('Public groups to limit record types and sales processes for opportunities.', False),
                    ('Separate record types and sales processes for the different types of opportunities.', True)
                ]
            },
            {
                'text': 'Cloud kicks want to allow customers to create their own cases while visiting its public home page. What should the administrator recommend?',
                'answers': [
                    ('Sms response', False),
                    ('Web-to-case', True),
                    ('Email-to-case', False),
                    ('Omni-channel', False)
                ]
            },
            {
                'text': 'Northern trail outfitters want to calculate how much revenue has been generated for each of its marketing campaigns.How should an administrator deliver this information?',
                'answers': [
                    ('Design a standard campaign report and add the value won opportunities in campaign  field.', True),
                    ('Perform periodic data job to update campaign records.', False),
                    ('Create a roll-up summary field on opportunity to campaign.', False),
                    ('Add a total value field on campaign and use a workflow rule to update the value when an opportunity won.', False)
                ]
            },
            {
            'text': 'An administrator installed a managed package that contains a permission set group. The permission set group that was installed includes delete access on several objects, and the administrator needs to prevent users in the permission set group from being able to delete records. What should the administrator do to control delete access?',
            'answers': [
                ('Use a muting permission set with a permission set group to mute selected permissions.', True),
                ('Create a new permission set that has delete access deselected for the objects.', False),
                ('Create a new role that prevents delete permissions from rolling up to the users.', False),
                ('Edit the profile for the users to remove delete access from the objects.', False)
                ]
            },
            {
            'text': 'An administrator at Universal Containers needs a simple way to trigger an alert to the Director of Sales when opportunities reach an amount of $500,000. What should the administrator configure to meet this requirement?',
            'answers': [
                ('Set up big deal alerts for the amount.', True),
                ('Enable opportunity update reminders.', False),
                ('Opportunity warning in Kanban view.', False),
                ('Key deals component on the home page.', False)
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
        migrations.RunPython(add_set4, atomic=False),
    ]