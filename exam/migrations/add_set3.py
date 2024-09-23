from django.db import migrations

def add_set3(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')

    # Create an exam instance
    exam = Exam.objects.create(title='ADM-201-Set3 Exam')

    # Define questions and answers
    questions_data = [
  {
    'text': 'Northern Trail Outfitters wants to know the average stage duration for all closed opportunities. How should an administrator support this request?',
    'answers': [
        ('Use Process Builder to capture the daily average on each opportunity.', False),
        ('Add formula fields to track stages on each opportunity.', False),
        ('Run the opportunity stage duration report.', True),
        ('Refresh weekly reporting snapshots for closed opportunities.', False)
    ]
},
{
    'text': 'Ursa Major Solar has a path on the case. The company wants to require its users to follow the status values as they are on the path. Agents should be prohibited from preventing the case back to a previous status. Which feature should an administrator use to fulfill this request?',
    'answers': [
        ('Validation rules', True),
        ('Global value picklists', False),
        ('Predefined field values', False),
        ('Dependent picklists', False)
    ]
},
{
    'text': 'Sales reps miss key fields when filling out an opportunity record through the process. Reps need to move forward without being able to enter previous stage. Which three options should the administrator use to address this need? (Choose 3 answers)',
    'answers': [
        ('Enable guided selling.', False),
        ('Use validation rules.', True),
        ('Configure opportunity path.', True),
        ('Use flow to mark fields required.', False),
        ('Mark fields required on the page layout.', True)
    ]
},
{
    'text': 'Cloud Kicks (CK) has a new administrator who is asked to put together a memo detailing Salesforce uses to budget for upcoming license purchases. Where should the administrator go to find out what type of licenses CK has purchased and how many are available?',
    'answers': [
        ('Search for license types in setup.', False),
        ('User licenses related list in company information.', True),
        ('User management settings in setup.', False),
        ('Usage-based entitlement related list in company information.', False)
    ]
},
{
    'text': 'The marketing team at Ursa Major Solar wants to send a personalized email whenever a lead fills out the web-to-lead form on their website. They want to send different messages based on the lead industry field value. What should an administrator configure to meet this requirement?',
    'answers': [
        ('Use validation rules to trigger workflow to email the lead.', False),
        ('Configure an auto-response rule to email the lead.', True),
        ('Add a public group and process builder to email the lead.', False),
        ('Create an assignment rule to email the lead.', False)
    ]
},
{
    'text': 'A team of support users at Cloud Kicks is helping inside sales reps make follow-up calls to prospects that filled out an interest form online. The team currently does not have access to the lead object. How should an administrator provide proper access?',
    'answers': [
        ('Create a new profile', False),
        ('Configure permission sets', True),
        ('Assign a new role', False),
        ('Set up manual sharing', False)
    ]
},
{
    'text': 'Which item is available in a Lightning app where visibility is limited to the Salesforce mobile app?',
    'answers': [
        ('Today', False),
        ('Favorites', False),
        ('Utility bar', True),
        ('Home page', False)
    ]
},
{
    'text': 'Ursa Major Solar uses two different page layouts for account records. One page layout reflects the fields related to customer accounts and another page layout includes fields for partner accounts. The administrator has assigned the customer account page layout to sales and support users and the partner account layout to the partner management team. What should the administrator configure to meet this requirement?',
    'answers': [
        ('Use a public group and a criteria-based sharing rule to share customer accounts with the partner team.', False),
        ('Add members of the partner management team to the default account team for the customer accounts.', False),
        ('Grant create, read, edit, and delete access to customer accounts on the partner team profile.', False),
        ('Create one record type for customer accounts and one record type for partner accounts.', True)
    ]
},
{
    'text': 'Users at Cloud Kicks want to see information more useful for their role on the case page. How should an administrator make the pages more dynamic and easier to use?',
    'answers': [
        ('Add component visibility filters to the components.', True),
        ('Remove fields from the record details component.', False),
        ('Delete the extra components from the page.', False),
        ('Include more tab components with filters.', False)
    ]
},
{
    'text': 'Universal Containers (UC) customers have provided feedback that their support cases are not being responded to quickly enough. UC wants to send all unassigned cases that have been open for more than 2 hours to an urgent case queue and alert the support manager. Which feature should an administrator configure to meet this requirement?',
    'answers': [
        ('Case scheduled reports', False),
        ('Case dashboard refreshes', False),
        ('Case escalation rules', True),
        ('Case assignment rules', False)
    ]
},
{
    'text': 'Cloud Kicks has created a screen flow for their sales team to use when they add new leads. The screen flow collects name, email, and shoe preference. Which two things should the administrator do to display the screen flow? (Choose 2 answers)',
    'answers': [
        ('Create a tab and add the screen flow to the page.', True),
        ('Use a flow element and add the screen flow to the record page.', True),
        ('Add the flow in the utility bar of the console.', False),
        ('Install an app from the AppExchange.', False)
    ]
},
{
    'text': 'Universal Containers has two sales teams, Sales Team A and Sales Team B. Each team has its own role in the role hierarchy. Both roles are subordinates of the same manager role. How should the administrator share records owned by Sales Team A with Sales Team B?',
    'answers': [
        ('Hierarchical sharing', False),
        ('Use manual sharing', False),
        ('Criteria-based sharing', True),
        ('Owner-based sharing', False)
    ]
},
{
    'text': 'An administrator at Cloud Kicks needs to export a file of closed won opportunities from the last 90 days. The file should include the opportunity name, ID, close date, and amount. How should the administrator export this file?',
    'answers': [
        ('Data export wizard', False),
        ('Data import wizard', False),
        ('Data export service', False),
        ('Data loader', True)
    ]
},
{
    'text': 'Northern Trail Outfitters wants emails received from customers to generate cases automatically. How should the administrator ensure that the emails are sent to the correct queue?',
    'answers': [
        ('Utilize a flow to identify the correct queue and assign the case.', False),
        ('Use a custom email service to set the owner of the case upon creation.', False),
        ('Create escalation rules to send cases to the correct queue.', False),
        ('Configure email-to-case so emails are delivered to the correct queue.', True)
    ]
},
{
    'text': 'Sales reps at Cloud Kicks want to be notified when they have a high likelihood of winning an opportunity over $1,000,000. Which feature meets this requirement?',
    'answers': [
        ('Key deals', False),
        ('Big deal alerts', True),
        ('Activity timeline', False),
        ('Performance chart', False)
    ]
},
{
    'text': 'Universal Containers wants to increase the security of their org by requiring stricter user passwords. Which two of the following should an administrator configure? (Choose 2 answers)',
    'answers': [
        ('Password different from username', False),
        ('Prevent common words', False),
        ('Minimum password length', True),
        ('Password complexity requirement', True)
    ]
},
{
    'text': 'Dreamhouse Realty regularly processes customer requests for warranty work and would like to offer customers a self-serve option to generate cases. Which two solutions should an administrator use to meet this request? (Choose 2 answers)',
    'answers': [
        ('Web-to-case', True),
        ('Case escalation', False),
        ('Case queues', False),
        ('Email-to-case', True)
    ]
},
{
    'text': 'An administrator is on a tight deadline to create dashboards for the sales and marketing teams at AW Computing. What should the administrator do to meet the deadline without increasing the budget?',
    'answers': [
        ('Train someone on the sales and marketing teams to build dashboards.', False),
        ('Check the AppExchange for prebuilt solutions that can be easily customized.', True),
        ('Hire a consultant to build the custom dashboards.', False),
        ('Build the dashboards manually to meet the deadline.', False)
    ]
},
{
    'text': 'Dreamhouse Realty wants to offer a form on its Experience Cloud site where inspectors will submit findings from a property inspection. Which feature should an administrator place on the page to fulfill this requirement?',
    'answers': [
        ('Related list', False),
        ('Autolaunched flow', False),
        ('Record detail', False),
        ('Screen flow', True)
    ]
},
{
    'text': 'The administrator at Ursa Major Solar needs to make sure the unassigned cases from VIP customers get transferred to the appropriate service representative within 5 hours. VIP customers have access to support 24 hours a day. How should this be configured?',
    'answers': [
        ('Assignment rules', False),
        ('Business hours', False),
        ('Case queues', False),
        ('Escalation rules', True)
    ]
},
{
    'text': 'An administrator at Ursa Major Solar needs to send information to an external accounting system whenever an opportunity closes. What workflow action should the administrator use to accomplish this?',
    'answers': [
        ('Assign task', False),
        ('Outbound message', True),
        ('Create record', False),
        ('Custom notification', False)
    ]
},
{
    'text': 'Northern Trail Outfitters has the Case object set to private. The support manager raised a concern that the reps have a broader view of data than expected and can see all cases on their group’s dashboards. What could be causing reps to have inappropriate access to data on dashboards?',
    'answers': [
        ('Dashboard filters', False),
        ('Dashboard subscriptions', False),
        ('Dynamic dashboards', True),
        ('Public dashboards', False)
    ]
},
{
    'text': 'An administrator wants to trigger a follow-up task for the opportunity owner when they close an opportunity as won and another task after 60 days to check in with the customer. Which two automation tools should the administrator use? (Choose 2 answers)',
    'answers': [
        ('Process builder', True),
        ('Workflow rule', True),
        ('Field update', False),
        ('Outbound message', False)
    ]
},

{
    'text': 'An administrator creates a custom text area field on the Account object and adds it to the service team’s page layout. The service team manager loves the addition of this field and wants it to appear in the highlights panel so that the service reps can quickly find it when on the Account page. How should the administrator accomplish this?',
    'answers': [
        ('Create a new page layout and a new section titled highlights panel.', False),
        ('In the Account object manager, create a custom compact layout.', True),
        ('From the page layout editor, drag the field to the highlights panel.', False),
        ('Make the field required and move it to the top of the page.', False)
    ]
},
{
    'text': 'A team of support users at Cloud Kicks is helping inside sales reps make follow-up calls to prospects that filled out an interest form online. The team currently does not access to the lead object. How should an administrator provide proper access?',
    'answers': [
        ('Create a new profile', False),
        ('Configure permission sets', True),
        ('Assign a new role', False),
        ('Set up Manual Sharing', False)
    ]
},
{
    'text': 'An administrator supporting a global team of Salesforce users has been asked to configure company settings. Choose 2 options.',
    'answers': [
        ('Currency Locale', True),
        ('Default Language', True),
        ('Password Policy', False),
        ('Login Hours', False)
    ]
},
{
    'text': 'Ursa Major Solar wants to know which of its marketing efforts are helping the team win Opportunities. What should an administrator configure to provide these insights?',
    'answers': [
        ('Campaign Hierarchy', False),
        ('Campaign Influence', True),
        ('Map Custom Lead Fields', False),
        ('List Email Activities', False)
    ]
},
{
    'text': 'Ursa Major Solar uses two different page layouts for Account records. One page layout reflects the fields related to customer accounts and another page layout includes fields for partner accounts. The administrator has assigned the customer account page layout to sales and support users and the partner account layout to the partner management team. What should the administrator configure to meet this requirement?',
    'answers': [
        ('Use a public group and a criteria-based sharing rule to share customer accounts with the partner team', False),
        ('Add members of the partner management team to the default Account team for the customer accounts', False),
        ('Grant create, read, edit, and delete access to customer accounts on the partner team profile', False),
        ('Create one record type for customer accounts and one record type for partner accounts', True)
    ]
},
{
    'text': 'Users at Cloud Kicks want to see information more useful for their role on the Case page. How should an administrator make the pages more dynamic and easier to use?',
    'answers': [
        ('Add Component visibility filters to the Components', True),
        ('Remove fields from the record details component', False),
        ('Delete the extra component from the page', False),
        ('Include more tab components with filters', False)
    ]
},
{
    'text': 'Universal Containers (UC) customers have provided feedback that their support cases are not being responded to quickly enough. UC wants to send all unassigned Cases that have been open for more than 2 hours to an urgent Case queue and alert the support manager. Which feature should an administrator configure to meet this requirement?',
    'answers': [
        ('Case Scheduled Reports', False),
        ('Case Dashboard Refreshes', False),
        ('Case Escalation Rules', True),
        ('Case Assignment Rules', False)
    ]
},
{
    'text': 'Cloud Kicks has created a screen flow for their sales team to use when they add new leads. The screen flow collects name, email, and shoe preference. Which two things should the administrator do to display the screen flow? Choose 2 answers.',
    'answers': [
        ('Create a tab and add the screen flow to the page', True),
        ('Use a flow element and add the screen flow to the record page', True),
        ('Add the flow in the utility bar of the console', False),
        ('Install an app from the AppExchange', False)
    ]
},
{
    'text': 'Universal Containers has two sales teams, Sales team A and Sales team B. Each team has their own role in the role hierarchy. Both roles are subordinates of the same Manager role. How should the administrator share records owned by Sales team A with Sales team B?',
    'answers': [
        ('Hierarchical sharing', False),
        ('Use Manual sharing', False),
        ('Criteria based sharing', True),
        ('Owner based sharing', False)
    ]
},
{
    'text': 'An administrator at Cloud Kicks needs to export a file of closed won opportunities from the last 90 days. The file should include the Opportunity Name, ID, Close Date, and Amount. How should the administrator export this file?',
    'answers': [
        ('Data Export Wizard', True),
        ('Data Import Wizard', False),
        ('Data Loader', True),
        ('Data Export Wizard', False)
    ]
},
{
    'text': 'Northern Trail Outfitters wants emails received from customers to generate cases automatically. How should the administrator ensure that the emails are sent to the correct queue?',
    'answers': [
        ('Utilize a flow to identify the correct queue and assign the case', False),
        ('Use a custom email service to set the owner of the case upon creation', False),
        ('Create an Escalation Rule to send cases to the correct queue', False),
        ('Configure Email-to-Case so emails are delivered to the correct queue', True)
    ]
},
{
    'text': 'Sales reps at Cloud Kicks want to be notified when they have a high likelihood of winning an opportunity over $1,000,000. Which feature meets this requirement?',
    'answers': [
        ('Key Deals', False),
        ('Big Deal Alerts', True),
        ('Activity Timeline', False),
        ('Performance Chart', False)
    ]
},
    {
        'text': 'Universal Container wants to increase the security of their org by requiring stricter user passwords. Which two of the following should an administrator configure? Choose 2 answers.',
        'answers': [
            ('Password different than username', True),
            ('Prevent common words', True),
            ('Minimum password length', True),
            ('Password complexity requirement', True)
        ]
    },
    {
        'text': 'Northern Trail Outfitters wants to know the average stage duration for all closed Opportunities. How should an administrator support this request?',
        'answers': [
            ('Use process builder to capture the daily average on each opportunity.', False),
            ('Add Formula Fields to track Stages on each Opportunity.', False),
            ('Run the Opportunity Stage Duration report.', True),
            ('Refresh weekly reporting snapshots for Closed Opportunities.', False)
        ]
    },
    {
        'text': 'Ursa Major Solar has a path on Case. The Company wants to require its users to follow the status values as they are on the path. Agents should be prohibited from preventing the case back to a previous status. Which Feature Should an administrator use to fulfill this request?',
        'answers': [
            ('Validation rules.', True),
            ('Global Value Picklists', False),
            ('Predefined field Values.', False),
            ('Dependent Picklists.', False)
        ]
    },
    {
        'text': 'The marketing team at Ursa Major Solar wants to send a personalized email whenever a lead fills out the web-to-lead form on their website. They want to send a different message based on the Lead Industry Field Value. What should an administrator configure to meet this requirement?',
        'answers': [
            ('Use Validation rule to trigger workflow to email to Lead.', False),
            ('Configure an auto response rule to email the lead.', True),
            ('Add a public group and process builder to email the lead.', False),
            ('Create an assignment rule to email the lead.', False)
        ]
    },
    {
        'text': 'Cloud Kicks has a Customer success agent going on leave and needs to change ownership on multiple cases. Which two users are able to fulfill this request? Choose 2 answers.',
        'answers': [
            ('A user with Read Permission on account.', False),
            ('A user with manager role above the agent.', False),
            ('A user with the System Administrator profile.', True),
            ('A user with the Manage Cases Permission.', True)
        ]
    },
    {
        'text': 'The marketing director at Northern Trail Outfitters has requested that the budget field is populated in order for the Lead Status field to be marked as qualified. What tool should the administrator use to fulfill this request?',
        'answers': [
            ('Lead Conversion.', False),
            ('Require Field.', False),
            ('Workflow Rule', False),
            ('Validation Rule', True)
        ]
    },
    {
        'text': 'The administrator at Cloud Kicks created a new field for tracking returns on their new cloud shoe. A user has submitted a case to the administrator indicating that the new field is unavailable. Which two steps should an administrator do to troubleshoot this issue? Choose 2 answers.',
        'answers': [
            ('Ensure that the page layout for the user\'s profile has been updated.', True),
            ('Run the setup audit trail for the organization.', False),
            ('Update the organization wide default for the object.', False),
            ('Review the field level security of the field for the user profile.', True)
        ]
    },
    {
        'text': 'The administrator at Ursa Major Solar has created a new record type for customer warranty cases. Which two assignments should the administrator use to display the new record type to users? Choose 2 answers.',
        'answers': [
            ('Profile Assignment', True),
            ('Role Assignment.', False),
            ('App Manager Assignment.', False),
            ('Page layout Assignment.', True)
        ]
    },
    {
        'text': 'A new Sales Rep at Ursa Major has a qualified lead that is ready for conversion. When using the Lead Conversion process, which two records can be created? Choose 2 answers.',
        'answers': [
            ('Account', True),
            ('Campaign', False),
            ('Case', False),
            ('Contact', True)
        ]
    },
    {
        'text': 'Universal Containers (UC) has a queue that is used for managing tasks that need to be worked by the UC customer support team. The same team will now be working some of UC\'s Cases. Which two options should the administrator use to help the support team? Choose 2 answers.',
        'answers': [
            ('Configure a flow to assign the cases to the queue.', True),
            ('Use assignment rules to set the queue as the owner of the case.', True),
            ('Add Cases to the existing queue as available object.', False),
            ('Create a new queue and add Cases as an available object.', False)
        ]
    },
    {
        'text': 'The administrator at AW Computing wants to send off client welcome tasks and a welcome email to the primary contact automatically when an Opportunity is Closed Won. What automation tool best accomplishes this?',
        'answers': [
            ('Validation Rule', False),
            ('Outbound Message', False),
            ('Approval Process', False),
            ('Process Builder', True)
        ]
    },
    {
        'text': 'Cloud Kicks users are seeing error messages when they use one of their screen flows. The error messages are confusing but could be resolved if the users entered more information on the account before starting the flow. How should the administrator address this issue?',
        'answers': [
            ('Remove validation rules so that the users are able to process without complete records.', False),
            ('Create a permission set to allow users to bypass the error.', False),
            ('Use a fault connector and display a screen with text explaining what went wrong and how to correct it.', True),
            ('Uncheck the end user Flow Errors box in setup.', False)
        ]
    },
    {
        'text': 'Cloud Kicks has a custom object named Shoe. The administrator has been asked to ensure that when a relationship is created between Account and Shoe to prevent orphaned Shoe records. What should the administrator do to complete this requirement?',
        'answers': [
            ('Create an indirect lookup', False),
            ('Create an encrypted lookup', False),
            ('Create a hierarchical lookup', False),
            ('Create a master-detail lookup.', True)
        ]
    },
    {
        'text': 'AW Computing needs to capture a loss reason in a rich text field when an opportunity is Closed Lost. How should an administrator configure this requirement?',
        'answers': [
            ('Select the requirement checkbox next to the loss reason field on the page layout.', False),
            ('Create a validation rule to display an error if stage is Closed Lost and Loss Reason is blank.', True),
            ('Check the required checkbox on the Loss Reason field in Object Manager.', False),
            ('Configure a workflow rule to display an error if Loss Reason is blank.', False)
        ]
    },
    {
        'text': 'Users at Cloud Kicks want to be able to create a task that will repeat every two weeks. What should an administrator do to meet the requirement?',
        'answers': [
            ('Enable Creation of Recurring Tasks.', True),
            ('Flow to create recurring tasks.', False),
            ('Workflow rule to create recurring tasks.', False),
            ('Turn on Recurring Activities.', False)
        ]
    },
    {
        'text': 'Cloud Kicks want its reports to show a Fiscal Year that starts on February 1 and has 12 months. How should the Administrator address this requirement?',
        'answers': [
            ('Set the Fiscal Year to Custom and the starting month as February.', False),
            ('Set the Fiscal Year to Custom and the duration to 4 quarters.', False),
            ('Set the Fiscal Year to Standard and the starting month as February.', True),
            ('Set the Fiscal Year to Standard and the duration to 12 months.', False)
        ]
    },
    {
        'text': 'Cloud Kicks has asked the administrator to test a new screen flow that creates contacts. What are two key components of testing the flow? Choose 2 answers.',
        'answers': [
            ('Set Up a flow interview to test the flow.', False),
            ('Run the flow using it to create contacts.', True),
            ('Use Debug to test the flow in Flow Builder.', False),
            ('Test the flow in a sandbox.', True)
        ]
    },
    {
        'text': 'An administrator at Universal Containers is reviewing current security settings in the company\'s Salesforce org. What should the administrator do to prevent unauthorized access to Salesforce?',
        'answers': [
            ('Disable TLS requirements for sessions.', False),
            ('Enable multi-factor authentication.', True),
            ('Customize organization-wide default.', False),
            ('Enable caching and autocomplete on login page.', False)
        ]
    },
    {
        'text': 'An administrator needs to store the ID of a record type for later use in a flow. Which kind of variable should the administrator use?',
        'answers': [
            ('Boolean variable', False),
            ('Text variable', False),
            ('ID variable', False),
            ('Record variable', True)
        ]
    },
    {
        'text': 'Universal Containers (UC) would like to count the number of open cases associated with each account and update the account with this value every Friday evening. UC has several hundred open cases at any given time. What should the administrator use to complete this request?',
        'answers': [
            ('Use a record trigger flow.', False),
            ('Use a scheduled process builder.', False),
            ('Use a Roll-Up summary.', False),
            ('Use a scheduled flow.', True)
        ]
    },
    {
        'text': 'The business development team at Cloud Kicks thinks the account creation process has too many fields to fill out and the page feels cluttered. They have requested the administrator to simplify the process. Which automation tool should an administrator use?',
        'answers': [
            ('Approval process', False),
            ('Workflow rule', False),
            ('Flow builder', True),
            ('Validation rule', False)
        ]
    },
    {
        'text': 'What should an administrator use as an identifier when importing and updating records from a separate financial system?',
        'answers': [
            ('Auto-Number field', False),
            ('External ID', True),
            ('Rich text field', False),
            ('Record ID', False)
        ]
    },
    {
        'text': 'DreamHouse Reality has an approval process. A manager attempts to approve the record but receives an error. What should an administrator review to troubleshoot this request?',
        'answers': [
            ('Add a delegated approver for the next approver in the process.', False),
            ('Update the field level security to view on fields that are updated in the process.', False),
            ('Check if the user in the next approver is inactive or missing', True),
            ('Review the page layout to ensure the fields updated in the process are visible.', False)
        ]
    },
    {
        'text': 'Cloud Kicks wants to try out an app from the AppExchange to ensure that the app meets its needs. Which two options should the administrator suggest?',
        'answers': [
            ('Test Drive in a production org.', False),
            ('Download into a Trailhead Playground.', True),
            ('Install in a sandbox.', True),
            ('Check edition compatibility.', False)
        ]
    },
    {
        'text': 'Which three aspects of standard fields should an administrator customize? Choose 3 answers.',
        'answers': [
            ('Picklist Values', True),
            ('Help Text', True),
            ('Field history tracking', True),
            ('Decimal Places', False),
            ('Field name', False)
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
        migrations.RunPython(add_set3),
    ]   