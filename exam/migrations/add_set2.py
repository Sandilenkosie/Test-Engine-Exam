from django.db import migrations

def add_set2(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')

    # Create an exam instance
    exam = Exam.objects.create(title='ADM-201-Set2 Exam')

    # Define questions and answers
    questions_data = [
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
        ('CREATE THREE SALES PROCESSES.', False),
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
        {
        'text': 'Cloud Kicks wants users to only be able to choose opportunity stage Closed Won if the Lead Source has been selected. How should the administrator accomplish this goal?',
        'answers': [
            ('Make Lead Source a dependent picklist to the Opportunity Stage field.', False),
            ('Configure a validation rule requiring Lead Source when the stage is set to Closed Won.', True),
            ('Change the Opportunity Stage field to read-only on the page layout.', False),
            ('Modify the Opportunity Stage as a dependent picklist to the Lead Source field.', False)
            ]
        },
        {
        'text': 'Ursa Major Solar wants to automatically notify a manager about any cases awaiting a response from an agent for more than 2 hours after case creation. Which feature should an administrator use to fulfill this requirement?',
        'answers': [
            ('Assignment rule', False),
            ('Case escalation rule', True),
            ('Omni-channel supervisor', False),
            ('Formula field', False)
            ]
        },
        {
        'text': 'Sales users at Universal Containers are reporting that it is taking a long time to edit opportunity records. Normally, the only field they are editing is the Stage field. Which two options should the administrator recommend helping simplify the process? (Choose 2 answers)',
        'answers': [
            ('Add a path for stage to the Opportunity record page.', True),
            ('Use a Kanban list view for Opportunity.', True),
            ('Configure an auto-launched flow for opportunity editing.', False),
            ('Create a simplified Opportunity page layout.', False)
            ]
        },
        {
        'text': 'A sales rep has a list of 300 accounts with contacts that they want to load at one time. Which tool should the administrator utilize to import the records to Salesforce?',
        'answers': [
            ('Dataloader.io', False),
            ('Data loader', False),
            ('Manual import', False),
            ('Data import wizard', True)
            ]
        },
        {
        'text': 'An administrator created a record trigger flow to update contacts. How should the administrator reference the values of the active record the flow is running on?',
        'answers': [
            ('Use the {!contact.id} global variable.', False),
            ('Use the {!account.id} record variable.', False),
            ('Use the $record global variable.', True),
            ('Use the Get Records element to find the ID.', False)
            ]
        },
        {
        'text': 'An administrator gets a rush request from Human Resources to remove a user’s access to Salesforce immediately. The user is part of a hierarchy field called Direct Manager. What should the administrator do to fulfill the request?',
        'answers': [
            ('Freeze the user to prevent them from logging in while removing them from being referenced in the Direct Manager field.', True),
            ('Deactivate the user and delete any records where they are referenced in the Direct Manager field.', False),
            ('Change the user’s profile to read-only while removing them from being referenced in the Direct Manager field.', False),
            ('Delete the user and leave all records where they are referenced in the Direct Manager field without changes.', False)
            ]
        },
        {
        'text': 'Aw computing (AWC) occasionally works with independent contractors, who the company stores as contacts in Salesforce. Contractors often change agencies, and AWC wants to maintain the historical accuracy of the record. What should AWC use to track contacts?',
        'answers': [
            ('Use a partner community to track the contacts.', False),
            ('Create a new contact record for each agency.', False),
            ('Create a junction object to track many-to-many relationships.', False),
            ('Enable contacts to multiple accounts.', True)
        ]
    },
    {
        'text': 'Which two actions should an administrator perform with case escalation rules? (Choose 2 answers)',
        'answers': [
            ('Re-open the case.', False),
            ('Send email notifications.', True),
            ('Change the case priority.', False),
            ('Re-assign the case.', True)
        ]
    },
    {
        'text': 'The sales director at Cloud Kicks wants to be able to predict upcoming revenue in the next several fiscal quarters so they can set goals and benchmark how reps are performing. Which two features should the administrator configure? (Choose 2 answers)',
        'answers': [
            ('Sales quotes', True),
            ('Opportunity list view', False),
            ('Forecasting', True),
            ('Opportunity stages', False)
        ]
    },
    # blue bro___
    
    {
        'text': 'Universal Containers requires a different Lightning page to be displayed when accounts are viewed in the Sales Console and in the Service Console. How should an administrator meet this requirement?',
        'answers': [
            ('Update page layout assignments.', True),
            ('Define multiple record types.', False),
            ('Assign Lightning pages as app default.', False),
            ('Create different user profiles.', False)
        ]
    },
    {
        'text': 'Sales reps at Northern Trail Outfitters have asked for a way to change the probability field value of their opportunities. What should an administrator suggest to meet this request?',
        'answers': [
            ('Define a new stage picklist value.', False),
            ('Create a custom field on Opportunity.', False),
            ('Configure forecasting support.', False),
            ('Make the field editable on page layouts.', True)
        ]
    },
    {
        'text': 'Ursa Major Solar has its business hours set from 9:00 am to 5:00 pm for the reps that are on Pacific Time. The reps on Eastern Time need business hours set to start 3 hours earlier to cover for support. How should an administrator solve this issue?',
        'answers': [
            ('Set temporary business hours for each time zone.', False),
            ('Adjust the current business hours to accommodate the Eastern Time Zone.', False),
            ('Create one set of business hours per time zone.', True),
            ('Allow the reps to set business hours manually.', False)
        ]
    },
    {
        'text': 'An administrator at Cloud Kicks is building a flow that needs to search for records that meet certain conditions and store values from those records in variables for use later in the flow. What flow element should the administrator add?',
        'answers': [
            ('Assignment', False),
            ('Get Records', True),
            ('Create Records', False),
            ('Update Records', False)
        ]
    },
    {
        'text': 'An administrator at Cloud Kicks has a flow in production that is supposed to create new records. However, no new records are being created. What could the issue be?',
        'answers': [
            ('The flow is read-only.', False),
            ('The flow is inactive.', True),
            ('The flow URL is deactivated.', False),
            ('The flow trigger is missing.', False)
        ]
    },
    {
        'text': 'The sales manager at Cloud Kicks wants to set up a business process where opportunity discounts of over 30% need to be approved by the VP of Sales. Any discounts above 10% need to be approved by the user’s manager. The administrator has been tasked with creating an approval process. Which are two considerations the administrator needs to review before setting up this approval process? (Choose 2 answers)',
        'answers': [
            ('Create a custom discount field on the Opportunity to capture the discount amount.', True),
            ('Populate the Manager standard field on the sales users’ user detail page.', True),
            ('Configure two separate approval processes.', False),
            ('Allow the submitter to choose the approver manually.', False)
        ]
    },
    {
        'text': 'What are three characteristics of a master-detail relationship? (Choose 3 answers)',
        'answers': [
            ('The master object can be a standard or custom object.', True),
            ('Permissions for the detail record are set independently of the master.', False),
            ('Each object can have up to five master-detail relationships.', False),
            ('Roll-up summaries are supported in master-detail relationships.', True),
            ('The owner field on the detail records is the owner of the master record.', True)
        ]
    },
    {
        'text': 'An administrator at Universal Containers has been asked to prevent users from accessing Salesforce from outside of their network. What are two considerations for this configuration? (Choose 2 answers)',
        'answers': [
            ('IP address restrictions are set on the profile or globally for the org.', True),
            ('Users can change their password to avoid login IP restrictions.', False),
            ('Enforce login IP ranges on every request must be selected to enforce IP restrictions.', True),
            ('Single sign-on will allow users to log in from anywhere.', False)
        ]
    },
    {
        'text': 'The administrator at Cloud Kicks has created an approval process for time off requests. Which two automated actions are available to be added as part of the approval process? (Choose 2 answers)',
        'answers': [
            ('Field update', True),
            ('Chatter post', True),
            ('Auto-launched flow', False),
            ('Email alert', True)
        ]
    },
    {
        'text': 'Which two capabilities are considerations when marking a field as required in object manager? (Choose 2 answers)',
        'answers': [
            ('The field is not required to save records via the API on that object.', False),
            ('The field is universally required to save a record on that object.', True),
            ('The field is added to every page layout on that object.', True),
            ('The field is optional when saving records via web-to-lead and web-to-case.', False)
        ]
    },
    {
        'text': 'Universal Containers requires that when an opportunity is Closed Won, all other open opportunities on the same account must be marked as Closed Lost. Which automation solution should an administrator use to implement this request?',
        'answers': [
            ('Quick action', False),
            ('Workflow rule', False),
            ('Flow builder', True),
            ('Outbound message', False)
        ]
    },
    {
        'text': 'Cloud Kicks wants a report to categorize accounts into small, medium, and large based on the dollar value found in the contract value field. What feature should an administrator use to meet this request?',
        'answers': [
            ('Detail column', False),
            ('Bucket column', True),
            ('Group rows', False),
            ('Filter logic', False)
        ]
    },
    {
        'text': 'Cloud Kicks (CK) is partnering with a used shoe store and second-hand bicycle emporium. CK has an automated business process it wants to run once a week to count the number of open cases related to an account. How should the administrator recommend automating this business process?',
        'answers': [
            ('Create a workflow rule with an outbound message.', False),
            ('Set up a scheduled process in Process Builder.', False),
            ('Configure a scheduled flow in Flow Builder.', True),
            ('Use a process to update the account when it is edited.', False)
        ]
    },
    {
        'text': 'An administrator has assigned a permission set group with the Two-Factor Authentication for User Interface Logins permission and the Two-Factor Authentication for API Logins permission to a group of users. Which two prompts will happen when one of the users attempts to log in to Data Loader? (Choose 2 answers)',
        'answers': [
            ('Users need to download and install an authenticator app on their mobile device.', True),
            ('Users need to enter a verification code from email or SMS, whichever has higher priority.', False),
            ('Users need to connect an authenticator app to their Salesforce account.', True),
            ('Users need to get a security token from a trusted network using reset my security token.', False)
        ]
    },
    {
        'text': 'Cloud Kicks needs to be able to show different picklist values for sales and marketing users. Which two options will meet this requirement? (Choose 2 answers)',
        'answers': [
            ('One page layout, two record types, one picklist', True),
            ('Two page layouts, one record type, two picklists', True),
            ('Two permission sets, one record type, one picklist', False),
            ('One record type, two profiles, one picklist', False)
        ]
    },
    {
        'text': 'At Universal Containers, users would like to be able to share Salesforce records with other members of their team, while collaborating around general topics as well. Which are two considerations for enabling this functionality? (Choose 2 answers)',
        'answers': [
            ('Collaboration groups are created automatically for every department.', False),
            ('Object layouts should be configured to include the groups related list.', False),
            ('The Add Record action must be configured in the group publisher.', True),
            ('An administrator needs to create a group to enable record sharing.', True)
        ]
    },
    {
        'text': 'Executives at Cloud Kicks have reported that their dashboards are showing inaccurate data. The administrator has discovered that users have been changing the source reports. Which two actions should the administrator take to preserve the integrity of the source reports? (Choose 2 answers)',
        'answers': [
            ('Create a new report folder with viewer access.', False),
            ('Move the dashboard to the user’s private folder.', False),
            ('Move the dashboard reports to the view-only folder.', True),
            ('Change the dashboard to be a dynamic dashboard.', True)
        ]
    },
    {
        'text': 'Cloud Kicks has decided to delete a custom field. What will happen to the data in the field when it is deleted?',
        'answers': [
            ('The data in the field is stored for 20 days.', False),
            ('The data is permanently deleted.', True),
            ('The data associated with the field is required.', False),
            ('The data is restorable from the recycle bin.', False)
        ]
    },
    {
        'text': 'AW Computing has six sales teams in a region. These teams always consist of the same account manager, engineer, and assistant. What should the administrator configure to make it easier for teams to collaborate with the same customer?',
        'answers': [
            ('Enable and configure standard opportunity teams with splits.', False),
            ('Enable account teams and show the users how to set up a default account team.', True),
            ('Create a queue for each team and assign account ownership to the queue.', False),
            ('Propose the users manually share all their accounts with their teammates.', False)
        ]
    },
    {
        'text': 'A user at Cloud Kicks is having issues logging in to Salesforce. The user asks the administrator to reset their password. Which two options should the administrator consider when resetting the user’s password? (Choose 2 answers)',
        'answers': [
            ('Resetting the password will change the user’s password policy.', False),
            ('Single sign-on users can reset their own passwords using the forgot password link.', False),
            ('Resetting a locked-out user’s password automatically unlocks the user’s account.', True),
            ('After resetting a password, the user may be required to activate their device to successfully login to Salesforce.', True)
        ]
    },
    {
        'text': 'When users log in to Salesforce via the user interface, which two settings does the system check for authentication? (Choose 2 answers)',
        'answers': [
            ('The user’s two-factor authentication for API logins permission.', False),
            ('The role IP address restrictions.', False),
            ('The user’s profile login hours restrictions.', True),
            ('The user’s two-factor authentication for user interface logins permission.', True)
        ]
    },
    {
        'text': 'Which two solutions could an administrator find on the AppExchange to enhance their organization? (Choose 2 answers)',
        'answers': [
            ('Communities', True),
            ('Consultants', False),
            ('Components', True),
            ('Customers', False)
        ]
    },
    {
        'text': 'Northern Trail Outfitters has requested that when the referral date field is updated on the custom object referral source, the parent object referral also needs to be updated. Which automation solution should an administrator use to meet this request?',
        'answers': [
            ('Lightning web component', False),
            ('Approval process', False),
            ('Workflow field update', False),
            ('Process builder', True)
        ]
    },
    {
        'text': 'Sales and customer care at Ursa Major Solar need to see different fields on the case related list from the account record. Sales users want to see case created date and status, while customer care would like to see owner, status, and contact. What should the administrator use to achieve this?',
        'answers': [
            ('Related lookup filters', False),
            ('Compact layout editor', False),
            ('Page layout editor', True),
            ('Search layout editor', False)
        ]
    },
    {
        'text': 'The support manager at Cloud Kicks wants to respond to customers as quickly as possible. They have requested that the response include the top five troubleshooting tips that could help solve the customer’s issue. What should the administrator suggest to meet these requirements?',
        'answers': [
            ('Auto-response rules', True),
            ('Email alerts', False),
            ('Knowledge articles', False),
            ('Assignment rules', False)
        ]
    },
    {
        'text': 'Northern Trail Outfitters is using one profile for all of its marketing users, providing read-only access to the campaign object. A few marketing users now require comprehensive edit access on campaigns. How should an administrator fulfill this request?',
        'answers': [
            ('Permission sets', False),
            ('Organization-wide defaults', False),
            ('Marketing user checkbox', False),
            ('Field-level security', True)
        ]
    },
    {
        'text': 'The administrator for Cloud Kicks has created a screen flow to help service reps ask the same set of questions when customers call in with issues. This screen should be visible from cases. How should the screen flow be distributed?',
        'answers': [
            ('Page layout', False),
            ('Component filter', False),
            ('Lightning page', True),
            ('Home page', False)
        ]
    },
    {
        'text': 'Northern Trail Outfitters has a custom quick action on account that creates a new case. How should an administrator make the quick action available on the Salesforce mobile app?',
        'answers': [
            ('Create a custom Lightning app with the action.', False),
            ('Modify compact case page layout to include the action.', False),
            ('Include the action in the Salesforce mobile navigation menu.', False),
            ('Add the Salesforce mobile and Lightning Experience action to the page layout.', True)
        ]
    },
    {
        'text': 'The administrator at Dreamhouse Realty added an email quick action to the case page layout and is unable to see the action on the case feed. Which feature must be enabled to ensure the quick action will be displayed as expected?',
        'answers': [
            ('Email notifications', False),
            ('Email-to-case', True),
            ('Email alerts', False),
            ('Email templates', False)
        ]
    },
    {
        'text': 'An administrator has reviewed an upcoming critical update. How should the administrator proceed with activation of the critical update?',
        'answers': [
            ('Activate the critical update in a sandbox.', True),
            ('Allow the critical update to auto-activate.', False),
            ('Activate the critical update in production.', False),
            ('Allow the critical update to auto-activate in a sandbox.', False)
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
    }
    ]

    for question_data in questions_data:
        question = Question.objects.create(exam=exam, text=question_data['text'], multiple_correct=any(answer[1] for answer in question_data['answers']))
        for answer_text, is_correct in question_data['answers']:
            Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

class Migration(migrations.Migration):

    dependencies = [
        # Add your app's dependencies here
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_set2),
    ]

