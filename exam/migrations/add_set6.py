from django.db import migrations

def add_set6(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')

    # Create an exam instance
    exam = Exam.objects.create(title='ADM-201-Set 6 Exam')

    # Define questions and answers
    questions_data = [
        {
            'text': 'Universal Containers triggered a process scheduled action to send a Chatter post to the department VP if a job posting remains open and is not Interviewing. On the 10th, an applicant interviewed, and the job posting status was updated to Interviewing. What will happen to the Chatter post?',
            'answers': [
                ('The pending Chatter post will be cancelled.', False),
                ('The pending Chatter post will be sent in 30 days.', True),
                ('The pending Chatter post will be paused.', False),
                ('The pending Chatter post will be sent on the 10th of the month.', False),
            ]
        },
        {
            'text': 'The standard Lead Rating field has picklist values of Hot, Warm, and Cold. A list of new leads was imported without errors even though several records had the value of Unrated in the Rating field. How were these records added without error?',
            'answers': [
                ('The Add to All Record Types checkbox was selected.', False),
                ('A global picklist value set was used to populate the picklist.', True),
                ('The Restricted picklist checkbox was unchecked.', False),
                ('Field-level security was set to Visible for all profiles.', False),
            ]
        },
        {
            'text': 'Dreamhouse Realty Sales Manager wants sales users to quickly view and edit Opportunities expected to close in 90 days. What should the administrator do?',
            'answers': [
                ('Create a custom report and schedule the sales users to receive it each day as a reminder to update their opportunities.', False),
                ('Make a new Sales dashboard and add a component that shows all opportunities that meet the criteria.', False),
                ('Enable Sales Console and show users how to open a tab for each opportunity in the pipeline that meets the requirements.', False),
                ('Create a list view on the Opportunity object and recommend users switch to Kanban to edit by drag and drop.', True),
            ]
        },
        {
            'text': 'AW Computing defined a new policy for cases. Cases with the reason Installation must be acknowledged via email and assigned to agents. Cases still in the New status after 4 hours must be escalated. Which case management tools are required?',
            'answers': [
                ('Auto-response rules, Queues, Macros', True),
                ('Auto-response rules, Macros, Entitlements', False),
                ('Auto-response rules, Queues, Escalation Rules', False),
                ('Auto-response rules, Entitlements, Escalation Rules', False),
            ]
        },
        {
            'text': 'Northern Trail Outfitters created users for ten new employees. They are unable to access the Account object. Why?',
            'answers': [
                ('Users\' profile requires a sharing rule for Accounts.', False),
                ('Users\' profile requires permission to the Account object.', True),
                ('Organization-wide defaults are set to private.', False),
                ('Users\' roles are low on the role hierarchy.', False),
            ]
        },
        {
            'text': 'Cloud Kicks generates leads for three product categories: shoes, apparel, accessories. Each category has its own lead sources. How should Salesforce be configured to meet this requirement?',
            'answers': [
                ('Create business processes and record types for each product category.', True),
                ('Create a dependency between the Product Category field and Lead Source field.', False),
                ('Create a page layout for each category and filter the Lead Source field based on category.', False),
                ('Create a single business process, then create record types for each product category.', False),
            ]
        },
        {
            'text': 'Cloud Kicks (CK) is testing an AppExchange package in a sandbox. What should be considered?',
            'answers': [
                ('The package will be removed any time the sandbox is refreshed.', False),
                ('Install for Admins Only will be the only option available.', True),
                ('The installation link has to be modified to test.salesforce.com.', False),
                ('Any metadata changes to the package have to be replicated in production.', True),
            ]
        },
        {
            'text': 'Universal Containers wants a custom Lead Product Category field to be mapped to the Opportunity field on lead conversion. What action should be taken?',
            'answers': [
                ('Create a workflow to update Opportunity fields based on the lead.', False),
                ('Create a custom field on the Opportunity and map the two fields.', True),
                ('Configure the product categories picklist field on the product.', False),
                ('Map the lead custom field to the product\'s product category field.', False),
            ]
        },
        {
            'text': 'Cloud Kicks added a lookup field to the Event object for the primary contact. They want contact fields to be referenced in Event reports. What should be done?',
            'answers': [
                ('Create a new report type with Event as the primary object and Contact as a related object.', False),
                ('Edit the Event report type and add fields related via lookup.', True),
                ('Configure formula fields on Event to populate contact information.', False),
                ('Use a dashboard with filters to show Event and contact data as requested.', False),
            ]
        },
        {
            'text': 'AW Computing user having login trouble. What should the administrator check?',
            'answers': [
                ('Check the attempted logins by running the setup audit trail.', False),
                ('Pull the password history to ensure the password policy was followed.', False),
                ('Reset the security token for the profile.', True),
                ('Review the login history for the user.', False),
            ]
        },
        {
            'text': 'Ursa Major Solar\'s sales team wants to automate an outbound message. What should the administrator use?',
            'answers': [
                ('Task Assignment', False),
                ('Case Auto-Response Rule', False),
                ('Recorded-triggered flow', True),
                ('Process Builder', False),
            ]
        },
        {
            'text': 'Cloud Kicks sends a 30-day warranty expiration reminder via a flow. The customer renews the warranty. What happens to the email element?',
            'answers': [
                ('The email is not sent because the customer\'s email address was missing.', False),
                ('The email is locked in the job queue until it meets the criteria.', False),
                ('The email is sent with the 30-day reminder criteria.', False),
                ('The email is not sent because the record no longer meets the criteria.', True),
            ]
        },
        {
            'text': 'Northern Trail Outfitters wants to track ROI for contacts on Opportunities. VP of Sales requested reporting capabilities. What should be configured?',
            'answers': [
                ('Add the Campaign Member related list to the Opportunity page layout.', False),
                ('Add the Opportunity Contact Role related list to the Opportunity page layout.', True),
                ('Customize Campaign Member Role.', False),
                ('Customize Campaign Role.', False),
                ('Customize Opportunity Contact Role.', True),
            ]
        },
        {
            'text': 'A user at Northern Trail Outfitters is locked out of Salesforce. What actions can the administrator take?',
            'answers': [
                ('Us the unlock button on the user\'s record detail page.', True),
                ('Log in as the user to unlock and reset the password.', False),
                ('Reset password on the user\'s record detail page.', True),
                ('Reset the password policies to allow the user to login.', False),
            ]
        },
        {
            'text': 'Cloud Kicks is working on a rebrand and wants to customize branding for the Salesforce mobile app. Which areas can be customized?',
            'answers': [
                ('Popups header color', False),
                ('Record background color', False),
                ('Header background color', True),
                ('Loading page logo', True),
            ]
        },
        {
            'text': 'Which two objects are customizable in the Stage Setup Flow?',
            'answers': [
                ('Campaign Members', False),
                ('Leads', True),
                ('Campaigns', False),
                ('Opportunities', True),
            ]
        },
        {
            'text': 'Support reps at Cloud Kicks (CK) report that the Closed option is missing in the Case Status picklist. Why is this happening?',
            'answers': [
                ('The record type for the Case does not have Closed as a picklist value.', True),
                ('The user profiles have permission set to restrict picklist values.', False),
                ('The administrator has restricted access to that record type.', False),
                ('The organization-wide default is set to private.', False),
            ]
        },
    {
        'text': 'Northern Trail Outfitters uses a custom object Invoice to collect customer payment information from an external billing system. The Billing System field needs to be filled in on every Invoice record. How should an administrator ensure this requirement?',
        'answers': [
            ('Define an approval process for the field.', False),
            ('Make the field universally required.', False),
            ('Create a Process Builder to set the field.', True),
            ('Require the field on the record type.', False),
        ]
    },
    {
        'text': 'Once an opportunity reaches the negotiation stage at Cloud Kicks, the Amount field becomes required for sales users. Sales managers need to be able to move opportunities into this stage without knowing the amount. How should the administrator require this field during the negotiation stage for sales users but allow their managers to make changes?',
        'answers': [
            ('Make the field required for all users.', True),
            ('Configure a validation rule to meet the criteria.', False),
            ('Create a formula field to fill in the field for managers.', False),
            ('Assign the Administrator profile to the managers.', False),
        ]
    },
    {
        'text': 'The administrator at Cloud Kicks updated the custom object Event to include a lookup field to the primary contact for the event. When running an event report, they want to reference fields from the associated contact record. What should the administrator do to pull contact fields into the custom report?',
        'answers': [
            ('Configure formula fields on Event to populate contact information.', False),
            ('Use a dashboard with filters to show Event and contact data as requested.', False),
            ('Edit the custom Event report type and add fields related via lookup.', True),
            ('Create a new report type with Event as the primary object and Contact as a related object.', False),
        ]
    },
    {
        'text': 'The administrator at Cloud Kicks created a new field for tracking returns on their new cloud shoe. A user has submitted a case to the administrator indicating that the new field is unavailable. Which two steps should an administrator do to troubleshoot this issue? Choose 2 answers.',
        'answers': [
            ('Review the field-level security of the field for the user profile.', True),
            ('Update the organization-wide defaults for the object.', False),
            ('Run the setup audit trail for the organization.', False),
            ('Ensure that the page layout for the user\'s profile has been updated.', True),
        ]
    },
    {
        'text': 'Management at Universal Containers would like to share dashboard components with their team in Chatter but currently do not have access to this capability. How should the administrator make this functionality available to management?',
        'answers': [
            ('Select Download Chart on the component.', False),
            ('Set View Dashboard As to the dashboard viewer.', False),
            ('Enable reporting snapshots.', False),
            ('Enable dashboard feed tracking.', True),
        ]
    },
    {
        'text': 'What data loss considerations should an administrator keep in mind when changing a custom field type from Text to Picklist? Choose 2 answers.',
        'answers': [
            ('Assignment and escalation rules may be affected.', True),
            ('There will be no data loss with use of a global value set.', True),
            ('Any list view based on the custom field is deleted.', False),
            ('Auto updates will be made to Visualforce references to prevent data loss.', False),
        ]
    },
    {
        'text': 'Cloud Kicks generates leads for its different product categories (shoes, apparel, and accessories) through many different sources. While some lead sources are used for all three categories, other lead sources are specific to a single category. The VP of marketing requests that only the proper lead sources be displayed based on the product category chosen. How should the administrator configure Salesforce to meet this requirement?',
        'answers': [
            ('Create business processes and record types for each of the three product categories.', True),
            ('Create a single lead process, then create record types for each product category.', False),
            ('Create a page layout for each category and filter the Lead Source field based on category.', False),
            ('Create a dependency between the Product Category field and Lead Source field.', False),
        ]
    },
    {
        'text': 'The CTO of AW Computing has defined a new policy for cases to improve customer satisfaction. All cases submitted with a Case Reason of Installation must be acknowledged immediately via email and assigned to the appropriate agents. Any cases that are still in the New status after 4 hours must be escalated to support management. What case management tools need to be utilized for this requirement?',
        'answers': [
            ('Auto-response rules, Support Processes, Entitlements', False),
            ('Auto-response rules, Entitlements, Queues', True),
            ('Auto-response rules, Support Processes, Escalation Rules', False),
            ('Auto-response rules, Queues, formulas', False),
        ]
    },
    {
        'text': 'Northern Trail Outfitters uses web-to-case to convert support requests submitted through its website into cases. The support team want to automatically send an email containing password reset instructions to the customers when the case subject contains the words forgot and password. What two options should the administrator configure to meet this requirement? Choose 2 answers.',
        'answers': [
            ('Password reset template', False),
            ('Email-to-case', False),
            ('Auto-response rule', True),
            ('Email template', True),
        ]
    },
    {
        'text': 'The administrator at Cloud Kicks writes an assignment rule to send all cases created via email or the web to the Automated Cases Queue. Any manually created cases should be owned by the agent creating them; however, the manually created cases now show the administrator as the owner. What will the administrator find when troubleshooting this issue?',
        'answers': [
            ('The Owner field is missing on the webform and email template.', False),
            ('Another assignment rule is giving ownership to the administrator.', False),
            ('An escalation rule is changing the case owner on case creation.', False),
            ('The Assignment Rule checkbox is selected by default.', True),
        ]
    },
    {
        'text': 'Northern Trail Outfitters wants to update data with information from their data warehouse. What should an administrator do to accomplish this?',
        'answers': [
            ('Use the data loader to match records between the systems.', False),
            ('Use an external object to match records between the systems.', True),
            ('Use a unique ID field to match records between the systems.', False),
            ('Use an external ID field to match records between the systems.', False),
        ]
    },
    {
        'text': 'The standard Lead Rating field has picklist values of Hot, Warm, and Cold. A list of new leads was imported without errors even though several records had the value of Unrated in the Rating field. How were these records added without error?',
        'answers': [
            ('The Add to All Record Types checkbox was selected.', False),
            ('A global picklist value set was used to populate the picklist.', True),
            ('The Restricted picklist checkbox was unchecked.', False),
            ('Field-level security was set to Visible for all profiles.', False),
        ]
    },
    {
        'text': 'An administrator at AW Computing has been asked to help the Support team with report folders. They want a folder called Support Reports and two folders underneath called Helpdesk and R&D. The Support organization uses public groups for Support Agents, R&D, and Managers. Support agents should be able to run Helpdesk reports, but should not be able to view R&D reports. Support managers should be able to view and edit all reports. Which two ways should these folders be shared? Choose 2 answers',
        'answers': [
            ('Share the Support Reports folder with Support Agents with View Access.', False),
            ('Share the Support Reports folder with Support Managers with Edit Access.', True),
            ('Share the R&D folder with Support Managers with Edit Access.', False),
            ('Share the Helpdesk folder with Support Agents with View Access.', True),
    ]
    },
    {
        'text': 'Ursa Major Solar uses Opportunity to track sales of solar energy products. The company has two separate sales teams that focus on different energy markets. The Services team also wants to use Opportunity to track installation. All three teams will need to use different fields and stages. How should the administrator configure this requirement?',
        'answers': [
            ('Create one sales process. Create one record type and three page layouts.', False),
            ('Create three sales processes. Create three record types and three page layouts.', True),
            ('Create three sales processes. Create three record types and one page layout.', False),
            ('Create one sales process. Create three record types and three page layouts.', False),
    ]
    },
    {
        'text': 'Customer service accesses articles with the Knowledge Lightning component on the Service Cloud Console. Billing department users would like similar functionality on the case record without using the console. How should the administrator configure this request?',
        'answers': [
            ('Add the Knowledge related list to the page layout.', False),
            ('Add the Knowledge component list to the page layout.', False),
            ('Add the knowledge related list to the record page.', False),
            ('Add the knowledge component to the page layout.', True),
    ]
    }
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
        migrations.RunPython(add_set6),
    ]
