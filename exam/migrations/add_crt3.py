from django.db import migrations

def add_crt3(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')

    # Create an exam instance
    exam = Exam.objects.create(title='CRM-3 Exam')

    # Define questions and answers
    questions_data = [
        {
            'text': 'DreamHouse Realty wants to make sure an Opportunity has a field Expected_Close_Date_c populated before it is allowed to enter the qualified stage. How should an app builder solve this request?',
            'answers': [
                ('Record Type', False),
                ('Validation Rule', True),
                ('Activity History', False),
                ('Page Layout', False)
            ]
        },
        {
            'text': 'Universal Containers wants to match Opportunity data from Salesforce to the records in a financial database. What is required to configure an indirect lookup relationship in Salesforce between the Salesforce Opportunity records and those in a financial database?',
            'answers': [
                ('Salesforce Record ID', False),
                ('TEXT(Id)', False),
                ('External ID', True),
                ('CASESAFE(Id)', False)
            ]
        },
        {
            'text': 'Ursa Major Solar has a lookup relationship between a custom Galaxy__c object and a custom Star__c object. An app builder wants to create a roll-up summary field that counts the total number of Star__c records related to each Galaxy__c record. How would the current configuration impact the ability to achieve the desired result?',
            'answers': [
                ('The roll-up summary can be achieved by creating a formula field on the Galaxy__c object.', False),
                ('The lookup relationship will need to be converted to a master-detail relationship before a roll-up summary field can be created.', True),
                ('The roll-up summary can be achieved by creating a formula field on the Star__c object.', False),
                ('A roll-up summary field will need to be created on the Galaxy__c object with a field filter that selects all related Star__c records.', False)
            ]
        },
        {
            'text': 'Universal Containers wants to track installation information once a container has been purchased on a custom object. Sales reps should have visibility of all the installations associated with their opportunities. What kind of relationship should this new object have to the Opportunity?',
            'answers': [
                ('Lookup', True),
                ('Hierarchical', False),
                ('Master-Detail', False),
                ('Many to Many', False)
            ]
        },
                {
            'text': 'An app builder is creating a Lightning record page and has added Mobile & Lightning Actions to the page layout. What two components could be included on the layout to display the actions?',
            'answers': [
                ('Highlights panel', True),
                ('Chatter', False),
                ('Activities', False),
                ('Path', True)
            ]
        },
        {
            'text': 'Universal Containers uses a custom picklist field Account Region on the account record. They want this region to be reflected on all related contact records and stay in sync if the value of this field changes on the Account. How should an app builder meet this requirement?',
            'answers': [
                ('Create a picklist field called "Account Region" on Contact object > Create a workflow rule to update this picklist field if the Account Region field on the Account is changed.', False),
                ('Create a formula field on the Contact object > Set the value of the formula to ISPICKVAL(Account.Account_Region__c).', False),
                ('Create a formula field on the Contact object > Set the value of the formula to TEXT(Account.Account_Region__c).', True),
                ('Create a text field called "Account Region" on Contact object > Create a workflow rule to update this picklist field if the Account Region field on the Account is changed.', False)
            ]
        },
        {
            'text': 'Which two features can be used to allow users to access Flows?',
            'answers': [
                ('Quick Action', True),
                ('Approval Process', False),
                ('Flow Launcher', True),
                ('Apex', False)
            ]
        },
        {
            'text': 'The CFO of Cloud Kicks needs a way for new vendors to accept terms on agreements for any new major retail store lease before the opportunity can be closed. Which feature should be used to handle this requirement?',
            'answers': [
                ('Email Alert', False),
                ('Dynamic Action', False),
                ('Approval Process', True),
                ('Validation Rule', False)
            ]
        },
        {
            'text': 'Universal Containers (UC) tracks Account locations in Zip Code, a custom text field with a validation rule to enforce proper formatting of the US ZIP+4 code for UC\'s orders. What formula should the app builder create on Order to display only the first five digits of Zip Code from the parent Account?',
            'answers': [
                ('BEGINS(Account.Zip_Code_r, 5)', False),
                ('TEXT(Account.Zip_Code_c, 5)', False),
                ('LEFT(Account.Zip_Code_c, 5)', True),
                ('LPAD(Account.Zip_Code__r, 5)', False)
            ]
        },
        {
            'text': 'The VP of Sales at Universal Containers has asked the app builder to let sales reps create opportunity records directly from the account, with a number of fields pre-populated. Which feature should the app builder use to allow users to create the opportunity?',
            'answers': [
                ('A quick action', True),
                ('A default action', False),
                ('A custom button', False),
                ('A custom link', False)
            ]
        },
        {
            'text': 'A customer service representative at a call center wants to be able to collect information from customers using a series of question prompts. What should an app builder use to accomplish this?',
            'answers': [
                ('Approval Process', False),
                ('Flow', True),
                ('Validation Rule', False),
                ('Path', False)
            ]
        },
        {
            'text': 'Universal Containers (UC) requires that all users specify a contract is sent on each Opportunity prior to marking it as "Closed Won". UC wants to be able to report on how many Opportunities have sent Contracts compared to how many have a missing contract when the Opportunities closed. Which field type should an app builder configure to fulfill this requirement?',
            'answers': [
                ('Text', False),
                ('Text Area', False),
                ('Picklist', False),
                ('Checkbox', True)
            ]
        },
        {
            'text': 'Universal Containers created a custom object called Component to capture details about products sold. What approach should an app builder take to show Component as a related list on Product?',
            'answers': [
                ('Create a master-detail relationship on Product to Component. Add the Component related list to the Product page layout.', True),
                ('Create a junction object to relate Component and Product. Add the Component related list to the Product page layout.', False),
                ('Create a roll-up on Product. Add the Component related list to the Product page layout.', False),
                ('Create a lookup relationship on Component to Product. Add the Component related list to the Product page layout.', False)
            ]
        },
                {
            'text': 'An app builder is creating a Lightning record page and has added Mobile & Lightning Actions to the page layout. What two components could be included on the layout to display the actions? Choose 2 answers.',
            'answers': [
                ('Highlights panel', True),
                ('Chatter', False),
                ('Activities', False),
                ('Path', True)
            ]
        },
        # Question 71
        {
            'text': 'Universal Containers uses a custom picklist field Account Region on the account record. They want this region to be reflected on all related contact records and stay in sync if the value of this field changes on the Account. How should an app builder meet this requirement?',
            'answers': [
                ('Create a picklist field called "Account Region" on Contact object > Create a workflow rule to update this picklist field if the Account Region field on the Account is changed.', False),
                ('Create a formula field on the Contact object > Set the value of the formula to ISPICKVAL(Account.Account_Region__c).', False),
                ('Create a formula field on the Contact object > Set the value of the formula to TEXT(Account.Account_Region__c).', True),
                ('Create a text field called "Account Region" on Contact object > Create a workflow rule to update this picklist field if the Account Region field on the Account is changed.', False)
            ]
        },
        # Question 72
        {
            'text': 'Which two features can be used to allow users to access Flows? Choose 2 answers.',
            'answers': [
                ('Quick Action', True),
                ('Approval Process', False),
                ('Flow Launcher', True),
                ('Apex', False)
            ]
        },
        # Question 73
        {
            'text': 'The CFO of Cloud Kicks needs a way for new vendors to accept terms on agreements for any new major retail store lease before the opportunity can be closed. Which feature should be used to handle this requirement?',
            'answers': [
                ('Email Alert', False),
                ('Dynamic Action', False),
                ('Approval Process', True),
                ('Validation Rule', False)
            ]
        },
        # Question 74
        {
            'text': 'Universal Containers (UC) tracks Account locations in Zip Code, a custom text field with a validation rule to enforce proper formatting of the US ZIP+4 code for UC\'s orders. What formula should the app builder create on Order to display only the first five digits of Zip Code from the parent Account?',
            'answers': [
                ('BEGINS(Account.Zip_Code_r, 5)', False),
                ('TEXT(Account.Zip_Code_c, 5)', False),
                ('LEFT(Account.Zip_Code_c, 5)', True),
                ('LPAD(Account.Zip_Code__r, 5)', False)
            ]
        },
        # Question 75
        {
            'text': 'The VP of Sales at Universal Containers has asked the app builder to let sales reps create opportunity records directly from the account, with a number of fields pre-populated. Which feature should the app builder use to allow users to create the opportunity?',
            'answers': [
                ('A quick action', True),
                ('A default action', False),
                ('A custom button', False),
                ('A custom link', False)
            ]
        },
        # Question 76
        {
            'text': 'A customer service representative at a call center wants to be able to collect information from customers using a series of question prompts. What should an app builder use to accomplish this?',
            'answers': [
                ('Approval Process', False),
                ('Flow', True),
                ('Validation Rule', False),
                ('Path', False)
            ]
        },
        # Question 77
        {
            'text': 'Universal Containers (UC) requires that all users specify a contract is sent on each Opportunity prior to marking it as "Closed Won". UC wants to be able to report on how many Opportunities have sent Contracts compared to how many have a missing contract when the Opportunities closed. Which field type should an app builder configure to fulfill this requirement?',
            'answers': [
                ('Text', False),
                ('Text Area', False),
                ('Picklist', False),
                ('Checkbox', True)
            ]
        },
        {
            'text': 'Universal Containers created a custom object called Component to capture details about products sold. What approach should an app builder take to show Component as a related list on Product?',
            'answers': [
                ('Create a master-detail relationship on Product to Component. Add the Component related list to the Product page layout.', False),
                ('Create a junction object to relate Component and Product. Add the Component related list to the Product page layout.', False),
                ('Create a roll-up on Product. Add the Component related list to the Product page layout.', False),
                ('Create a lookup relationship on Component to Product. Add the Component related list to the Product page layout.', True)
            ]
        },
        {
            'text': 'An app builder at Universal Containers has been asked to add the Chatter feed to a custom object record page. Which approach should the app builder use?',
            'answers': [
                ('Add the standard Chatter feed component.', True),
                ('Add the standard related list component.', False),
                ('Add a custom Chatter feed component.', False),
                ('Add the Chatter feed component from the AppExchange.', False)
            ]
        },
        {
            'text': 'Universal Containers require different fields to be filled out at each stage of the Opportunity sales process. What configuration steps can an app builder use to meet this requirement?',
            'answers': [
                ('Set page layout required fields based on the current stage.', False),
                ('Create a Process Builder to prompt the User for field information.', False),
                ('Define record types and page layouts for each stage.', False),
                ('Add the Path component to the Lightning record page.', True)
            ]
        },
                {
            'text': 'An app builder wants to update a field on the parent record when a child record connected via lookup is deleted. What automation should the app builder use?',
            'answers': [
                ('Screen flow', False),
                ('Process Builder', False),
                ('Apex code', True),
                ('Workflow rule', False)
            ]
        },
        {
            'text': 'Universal Containers (UC) delivers purchased containers to remote construction sites. Customers supply UC with crossroads or location markers. Which field type should the app builder use to capture this information?',
            'answers': [
                ('Number', False),
                ('Geolocation', True),
                ('Reference', False),
                ('External Lookup', False)
            ]
        },
        {
            'text': 'DreamHouse Realty (DR) has a policy that requires the phone number on Contact to be deleted when the DoNotCall checkbox is checked. What automation tool should the app builder recommend?',
            'answers': [
                ('Quick action', False),
                ('Approval process', False),
                ('Validation rule', False),
                ('Workflow rule', True)
            ]
        },
        {
            'text': 'Universal Containers has a new custom object for Invoices that includes an Invoice Number field. After the migration, Salesforce will be the system of record and each new Invoice created in Salesforce must have a unique Invoice Number. How should the app builder configure the Invoice Number field?',
            'answers': [
                ('Create a Text field for the original Invoice Number and an AutoNumber field for the Salesforce Invoice Number.', False),
                ('Create a Text field and mark it as a unique external ID field.', True),
                ('Create a Text field, then change it to AutoNumber after the migration.', False),
                ('Create an AutoNumber field and migrate the Invoices', False)
            ]
        },
        {
            'text': 'At Ursa Major Solar, only users with the Outer Planets profile need to see the Jupiter field on the Solar System object. How should the app builder satisfy this requirement?',
            'answers': [
                ('Classic encryption', False),
                ('Filtered view', False),
                ('Field-level security', True),
                ('Sharing rules', False)
            ]
        },
        {
            'text': 'Which opportunity standard field is available to be configured directly?',
            'answers': [
                ('Forecast category', False),
                ('Stage', True),
                ('Lead source', True),
                ('Type', True)
            ]
        },
        {
            'text': 'Which three options are available when activating a Lightning page from the Lightning App Builder?',
            'answers': [
                ('Assign the page to a combination of apps and profiles.', True),
                ('Assign the page to a combination of apps and permission sets.', False),
                ('Make the page the org default.', True),
                ('Make the page the default homepage for specific roles.', False),
                ('Make the page the default homepage for specific apps.', True)
            ]
        },
        {
            'text': 'Universal Containers\' app builder has been tasked with replacing workflow rules and Apex triggers with Process Builders where possible. What are two important considerations an app builder should know before the project is started?',
            'answers': [
                ('Avoid generating infinite loops.', True),
                ('Apex has a different SOQL query limit than Flow.', False),
                ('Create a process for each workflow rule.', False),
                ('Combine actions when possible.', True)
            ]
        },
        {
            'text': 'After Universal Containers converted qualified leads, sales reps need to be able to report on converted leads. How should an app builder support this requirement?',
            'answers': [
                ('Enable preserve lead status in the lead conversion settings', False),
                ('Assign the representative view and edit converted leads permission', False),
                ('Ensure the representative has read access to the original lead records', False),
                ('Create a custom report type with converted leads as the primary object', True)
            ]
        },
        {
            'text': 'An app builder has downloaded a component from the AppExchange successfully; however, they are unable to add it to the Lightning home page. Which two reasons can be preventing the app builder from being able to add the custom component?',
            'answers': [
                ('My Domain must be deployed to add custom components to the page with the App Builder.', True),
                ('A custom tab must be created to add custom components to the page with the App Builder.', False),
                ('The component requires a developer permission to add it to the page with the App Builder.', False),
                ('The component is tagged for record pages instead of home pages and is not showing up in the App Builder.', True)
            ]
        },
                {
            'text': "Sales reps at Universal Containers create multiple quotes per opportunity. "
                    "What automation tool should an app builder recommend to delete rejected quotes?",
            'answers': [
                ('Approval process', False),
                ('Validation rule', False),
                ('Workflow rule', False),
                ('Flow', True)
            ]
        },
        {
            'text': "Ursa Major Solar wants to create a relationship between the standard Contact object and a "
                    "custom Solar Project object. Contacts potentially be related to multiple Solar Project objects, "
                    "and a Solar Project can have multiple Contacts associated with it. "
                    "How should an app builder configure the data model?",
            'answers': [
                ('One Master-detail relationship on Contact and one Master-detail relationship on Solar Project', False),
                ('Two Lookup relationships on a new custom object', False),
                ('One Lookup relationship on Contact and one Lookup relationship on Solar Project', True),
                ('Two Master-detail relationships on a new custom object', False)
            ]
        },
        {
            'text': "DreamHouse Realty is rethinking its sandbox utilization strategy after acquiring Cloud Kicks. "
                    "What type of sandbox should each team member use?",
            'answers': [
                ('Full sandbox', False),
                ('Developer sandbox', True),
                ('Developer pro sandbox', False),
                ('Partial sandbox', False)
            ]
        },
        {
            'text': "An app builder just added a lookup field to Account from the existing custom object, Box. "
                    "Which report type is automatically created?",
            'answers': [
                ('Boxes with or without Accounts', False),
                ('Accounts with or without Boxes', False),
                ('Boxes with Accounts', False),
                ('Accounts with Boxes', True)
            ]
        },
        {
            'text': "Northern Trail Outfitters has two custom objects that are part of a master-detail relationship. "
                    "What determines the ownership and sharing access of the detail record?",
            'answers': [
                ('The default owner is set in the parent object\'s settings.', False),
                ('The Owner field on the Detail record.', False),
                ('The Owner field on the Master record.', True),
                ('The owner is set independently on the detail object\'s settings.', False)
            ]
        },
        {
            'text': "An app builder at Cloud Kicks has been working on changes to a custom Shoe Sales app in "
                    "a sandbox and is ready to deploy their changes to production with a change set. "
                    "What should the app builder take into consideration when deploying the change set to production?",
            'answers': [
                ('The deployed permission set will only contain changes related to the change set.', True),
                ('Change to field-level security in the permission set will not be applied.', False),
                ('The deployed permission set will merge with the existing permission set.', False),
                ('The existing permission set will be completely overwritten.', False)
            ]
        },
        {
            'text': "Universal Containers asked the app builder to ensure when an account type changes to 'Past-Customer' "
                    "the contacts directly related to that account get an updated status of 'ReMarket'. "
                    "Which automation should the app builder use to accomplish this task?",
            'answers': [
                ('Screen flow', False),
                ('Lightning component', False),
                ('Validation rule', False),
                ('Record triggered flow', True)
            ]
        },
        {
            'text': "Universal Containers implemented an application process that uses custom objects Internships and Applications. "
                    "The organization-wide default for Internships has been set to private and is the master in the master-detail "
                    "relationship with Applications. How should an app builder configure the proper access?",
            'answers': [
                ('Set the organization-wide default on the Applications object to Read/Write.', False),
                ('Add a sharing rule that grants the users Read/Write access to the Internship records.', False),
                ('Create a queue for the web applications and assign access to the users who will be editing the records.', False),
                ('Create a sharing rule that grants the users Read/Write access to the Application records.', True)
            ]
        },
        {
            'text': "An app builder needs to create new automation on an object. What best practice should the app builder follow "
                    "when building out automation?",
            'answers': [
                ('One Workflow rule per object.', False),
                ('One Flow per object.', False),
                ('One invocable process per object.', False),
                ('One record change process per object.', True)
            ]
        },
                {
            'text': 'The sales Operations team at AWS Computing deletes accounts for a variety of reasons. The sales ops director is worried that the Sales team may delete accounts that sales reps are actively selling into. How should the app builder keep accounts with open opportunities from being deleted?',
            'answers': [
                ('Create an Apex Trigger on the Account object', False),
                ('Create a validation rule on the Account object', True),
                ('Remove the delete button on the account layout', False),
                ('Remove the Delete permission from the Sales Rep profile', False)
            ]
        },
        {
            'text': 'Universal Containers would like to collaborate with its customers within Salesforce, and has decided to enable the "Allow Customer Invitations" Chatter setting. What permission is granted to Customers when invited to Chatter Group?',
            'answers': [
                ('The ability to invite members to groups of which they are a member', False),
                ('The ability to @mention accounts of which they are a contact.', False),
                ('The ability to request access to public groups', False),
                ('The ability to interact with members of their groups', True)
            ]
        },
        {
            'text': 'A business user wants a quick way to edit a record\'s status and enter a custom due date field from the record\'s feed in Salesforce Mobile App. What should be used to accomplish this?',
            'answers': [
                ('Custom action', True),
                ('Custom button', False),
                ('Custom quick access link', False),
                ('Custom URL formula Field', False)
            ]
        },
        {
            'text': 'Ursa Major Solar\'s sales team has been struggling to enter data on mobile since rollout; the team dislikes scrolling through all of the fields to input only the necessary data. How could the app builder solve this with minimal impact to desktop users?',
            'answers': [
                ('Filter components by device using Form Factor.', True),
                ('Reorder the fields to make sense for the reps when in the field.', False),
                ('Update the training documentation with better screenshots.', False),
                ('Deselect the phone radio button on the Lightning record page assignment.', False)
            ]
        },
        {
            'text': 'Universal Containers is setting up Salesforce for the first time. Management wants the sales and marketing teams to have different navigation names in the Salesforce1 mobile app. Which option is available to an app builder to satisfy the requirement?',
            'answers': [
                ('Create sales and marketing profiles to ensure read access to different objects', False),
                ('Create roles for sales and marketing and assign a custom homepage layout for each role.', False),
                ('Create mobile navigation menus for both the sales and marketing profiles.', True),
                ('Create public groups for sales and marketing and create mobile navigation menus for each group.', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters (NTO) has created the custom objects Trail and Park in Salesforce to track trails and parks respectively. NTO wants to track the total number of trails a park has on the park record without writing any code. Which two actions should an app builder take to accomplish this requirement?',
            'answers': [
                ('Use a formula field on the Park record to show the total number of trails.', False),
                ('Use a roll-up summary field on the Park record to show the total number of Trails.', True),
                ('Use a master-detail relationship between the Park and Trail objects.', True),
                ('Use a lookup relationship between the Park and Trail objects.', False)
            ]
        },
        {
            'text': 'DreamHouse Realty wants to track how many lifts are being installed into customer garages. The To Be Installed custom checkbox field on the custom Lift object should be checked and an external system should be notified via an outbound message the next day when a lift is sold. What automation tool should be used to complete this task?',
            'answers': [
                ('Approval process', False),
                ('Workflow', False),
                ('Flow', False),
                ('Process Builder', True)
            ]
        },
        {
            'text': 'Cloud Kicks (CK) tracks the support level of its customers on the account record page. CK wants to show a text notification on a case record page when the related account is a platinum-level customer. How could an app builder meet this requirement?',
            'answers': [
                ('Add a rich text area to the Case Lightning page > Set the component visibility of the rich text area to show when the account support level is platinum.', False),
                ('Create a text-only Visualforce page > Drag the Visualforce component into the Case page layout > Set its visibility to show when the account support level is platinum.', True),
                ('Create a text-only Visualforce page > Clone the case page layout > Drag the Visualforce component into the page, and assign the layout to platinum cases.', False),
                ('Clone the Case Lightning page > Add a rich text area to the new page, and assign this page to platinum accounts.', False)
            ]
        },
        {
            'text': 'An app builder wants to use Process Builder to automate some of the work being done by the sales team. What are three capabilities of Process Builder that can improve productivity?',
            'answers': [
                ('Send an email alert.', True),
                ('Update a related record.', True),
                ('Send an outbound message.', True),
                ('Delete records.', False)
            ]
        },
                {
            'text': 'An app builder needs a custom solution and is considering using community. Ease of updates is the primary consideration. What should the app builder consider?',
            'answers': [
                ('A managed package from AppExchange', True),
                ('An unmanaged package from AppExchange', False),
                ('An open-source unmanaged package', False),
                ('An open-source custom development', False),
            ],
        },
        {
            'text': 'An app builder notices several Accounts converted from Leads are missing information they expected to be caught via Account validation rules. What could be the source of this issue?',
            'answers': [
                ('The lead settings are unchecked to require validation for converted leads.', True),
                ('Account validation rules fail to validate on records converted from a lead.', False),
                ('The lead settings are allowing users to intentionally bypass validation rules.', False),
                ('Lead validation rules fail to validate on records when they are being converted.', False),
            ],
        },
        {
            'text': 'Universal Containers (UC) utilizes two custom picklist fields called sales_Organization__c and Pricing_Tier__c. Which validation rule should an app builder use to ensure pricing_Tier__c is required for customers with a Sales_Organization__c value of Canada?',
            'answers': [
                ('Use a validation rule that checks Sales_Organization__c.', True),
                ('Use a validation rule that checks Pricing_Tier__c.', False),
                ('Make both fields required.', False),
                ('Create a flow to enforce the requirement.', False),
            ],
        },
        {
            'text': 'Cloud Kicks wants to display 10 key fields at once in a separate section at the top of opportunity records on the desktop. Which component should an app builder add to the record page to enable this functionality?',
            'answers': [
                ('Path', False),
                ('Highlights Panel', True),
                ('Custom Lightning Web Component', False),
                ('Accordion', False),
            ],
        },
        {
            'text': 'What is one limitation of using schema builder when creating a field?',
            'answers': [
                ('Cannot create formula fields.', False),
                ('Cannot see existing relationships between objects.', False),
                ('Cannot add fields to page layouts.', True),
                ('Cannot create lookup relationships.', False),
            ],
        },
        {
            'text': 'Cloud Kicks recently implemented the application lifecycle management process to its release management strategy. Which category handles bug fixes and simple changes?',
            'answers': [
                ('Patch', True),
                ('Minor', False),
                ('Major', False),
                ('Rollback', False),
            ],
        },
        {
            'text': 'Universal Containers has a private sharing model for Accounts and Opportunities and uses Territory Management to grant access to records. Why can sales rep B see the Account related to the Opportunity?',
            'answers': [
                ('Sales rep B has implicit access to the Account.', True),
                ('Sales rep B was added to the Account team.', False),
                ('Sharing set is granting access to the Account.', False),
                ('Account was also manually shared.', False),
            ],
        },
        {
            'text': 'An app builder wants to limit the number of fields users are required to fill out when creating a new Opportunity. How could this be accomplished?',
            'answers': [
                ('Make the Opportunity type a required field on the initial Opportunity page layout and use automation to fill in the type field to a record type.', True),
                ('Use different page layouts for Opportunity types based on the user profile.', False),
                ('Once the required fields are populated, use a sharing rule to share the new fields with the user.', False),
                ('Hide additional sections on the page layout and show the users how to manually expand them when they want to fill in the fields in the hidden sections.', False),
            ],
        },
        {
            'text': 'An app builder has created a custom Lightning App and wants to make it available to the internal users at Universal Containers. Which two steps are necessary to accomplish this task?',
            'answers': [
                ('Create a subdomain using My Domain.', True),
                ('Build a Custom Tab for the app.', True),
                ('Add the app to a Visualforce page.', False),
                ('Upload the app to Static Resources.', False),
            ],
        },
        {
            'text': 'Containers have the Account object\'s Organization-Wide Default set to Private. What feature should be used to enable marketing to see sales-owned accounts?',
            'answers': [
                ('Public Group', False),
                ('Flow', False),
                ('Workflow', False),
                ('Sharing Rules', True),
            ],
        },
        {
            'text': 'Universal Containers deployed an app in a large change set from a Developer Sandbox to a Developer Pro Sandbox used for testing. After testing, changes had to be made to several components in the change set. How should an app builder move the new changes to the Developer Pro Sandbox?',
            'answers': [
                ('Refresh the text sandbox and re_display the change set.', False),
                ('Clone the change set and re_display', False),
                ('Rename the change set, add the changes and re_display', False),
                ('Update the change set and re_display', True),
            ],
        },
        {
            'text': 'Universal Containers (UC) has created a picklist field called Status on three separate custom objects. UC has a requirement to share the list of values for this field across each object. Which feature would an app builder use?',
            'answers': [
                ('Field Update', False),
                ('Global Picklist', True),
                ('Custom Setting', False),
                ('Custom Metadata', False),
            ],
        },
                {
            'text': 'What option is available to an App Builder when defining an object-specific Create Record custom action? Choose 2 answers',
            'answers': [
                ('Pre-Defining field values on the target object.', True),
                ('Redirecting the end user to the detail page of the target object', False),
                ('Specifying the fields and layout of the action.', True),
                ('Allowing the end user to choose the record type', False)
            ]
        },
        {
            'text': 'A business user at Universal Containers wants to update an Account directly from an Opportunity record. What should the app builder create to allow the business user to make these edits?',
            'answers': [
                ('An update record action with a related record component.', True),
                ('An update record action with a details component', False),
                ('Formula fields displaying the Account fields.', False),
                ('Opportunity fields updated by a process.', False)
            ]
        },
        {
            'text': 'DreamHouse Realty (DR) employees started using company-owned airplanes for work travel after Ursa Major Solar was acquired. DR executives want to automate the submission travel request forms to enforce the Internal policy. How should an app builder automate travel requests based on these criteria?',
            'answers': [
                ('Process Builder', False),
                ('Workflow rule', False),
                ('Approval process', True),
                ('Apex', False)
            ]
        },
        {
            'text': 'What are two reasons to create an unmanaged package? Choose 2 answers',
            'answers': [
                ('Distributing open-source projects on the AppExchange.', True),
                ('Publishing an application for sale on the AppExchange', False),
                ('Deploying from a Developer Edition environment', True),
                ('Distributing upgradeable components to another Salesforce org', False)
            ]
        },
        {
            'text': 'The case handling process at Universal Containers includes multiple steps including approvals, notifications, and fields updates. To manage and evaluate all of these changes in a single save operation, an app builder wants to use Process Builder and the Advanced option to let the process evaluate a record multiple times has been selected. Which two options should the app builder avoid to prevent recursion? Choose 2 answers',
            'answers': [
                ('IF statements', False),
                ('Setting a criteria node to No criteria-just execute the procedure', True),
                ('Invocable processes', True),
                ('The ISCHANGED function', False)
            ]
        },
        {
            'text': 'Universal Containers has a custom picklist called Support Level on the Account object. They would like to show the real-time value of Support Level on all case records. How should an app builder implement this requirement?',
            'answers': [
                ('Create a formula field on the Case object using the TEXT function.', True),
                ('Create a formula field on the Account object using the ISPICKVAL function.', False),
                ('Create a Process Builder and use a field update on the Case object.', False),
                ('Create a roll-up summary field using Support Level on the Account object.', False)
            ]
        },
        {
            'text': 'Nickname__c is a custom text field on a contact record that is utilized to override the contact\'s name appearing on an email template. This field is not required and is not always filled in. Which formula should an app builder use to select the contact\'s preferred name for email communications?',
            'answers': [
                ('IF(NOT(ISBLANK(Nickname__c)), Nickname__c, FirstName)', False),
                ('IF(TEXT(Nickname__c), Nickname__c, FirstName)', False),
                ('IF (ISNULL(Nickname__c), Nickname__c, FirstName)', False),
                ('IF(NOT(BLANKVALUE(Nickname__c)), Nickname__c, FirstName)', True)
            ]
        },
        {
            'text': 'A new field is being created on a custom object. However, the app builder does not want the field to show up on pre-existing custom report types. What should the app builder do on the custom field setup to fulfill this requirement?',
            'answers': [
                ('Remove the new field from all page layouts.', False),
                ('Remove visibility to all report profiles.', False),
                ('Grant read-only access to all report profiles.', False),
                ('Deselect auto add to custom report type.', True)
            ]
        },
        {
            'text': 'An app builder created multiple custom fields, page layouts, and reports in the sandbox and added them to a change set that was deployed to production, the reports were NOT deployed. What should the app builder do?',
            'answers': [
                ('Move the reports to the Unfiled Public Reports folder and add them to a new change set.', False),
                ('Move the reports from the Unfiled Public Reports folder and add them to a new change set.', True),
                ('Recreate the reports in production. Reports are not supported in change sets.', False),
                ('Add the reports to an unmanaged package and install the unmanaged package into production.', False)
            ]
        },
                {
            'text': 'Universal Containers has deployed custom tabs to Production via changes sets, without including the profile settings or permission sets. What is the settings for the visibility of custom tabs?',
            'answers': [
                ('Custom tabs are default off for all users.', True),
                ('Custom tabs are default on for all users.', False),
                ('Custom tabs are hidden for all users.', False),
                ('Custom tabs are NOT deployed.', False)
            ]
        },
        {
            'text': 'At Ursa Major Solar, there is a single Lightning record page for the Celestial Bodies custom object; however, there is a Lightning component the app builder wants to restrict to mobile app users. Which feature on the Lightning app builder should be utilized?',
            'answers': [
                ('Chatter feed', False),
                ('Highlights panel', False),
                ('Component visibility filter', True),
                ('Related list quick links', False)
            ]
        },
        {
            'text': 'An app builder at DreamHouse Realty created a custom object which has fields containing data from two different objects via related lookups. What is needed to create "with" or "without" reports on the new custom object?',
            'answers': [
                ('Row-Level Formula', False),
                ('Report Bucket Field', False),
                ('Report Filters', False),
                ('Custom Report Type', True)
            ]
        },
        {
            'text': 'At Universal Containers, each admin and developer use a separate developer pro sandbox. Configuration and code are then migrated to a partial data sandbox for combination and initial testing. Once approved the configuration and code are then migrated to a full sandbox for final load and regression testing before going to production. When should the full sandbox be refreshed?',
            'answers': [
                ('After user acceptance testing is complete.', False),
                ('After each push from the partial data sandbox.', False),
                ('After each major release to production.', True),
                ('After a new user is added to production.', False)
            ]
        },
        {
            'text': 'An app builder wants to create a formula field on an Account to include data from related Contacts but is unable to find the relationship in the formula editor. What is a limitation of formulas that could be causing the issue?',
            'answers': [
                ('Unable to reference the child records.', True),
                ('A master-detail relationship should be created.', False),
                ('Formula field limit reached on the Account object.', False),
                ('More than 5,000 characters in the formula.', False)
            ]
        },
        {
            'text': 'An app builder has created a change set and deployed a report from their development sandbox for User Acceptance Testing. When the app builder runs the report, no data is returned. What can be a reason for this?',
            'answers': [
                ('Reports have to be deployed with Salesforce DX.', False),
                ('Reports have to be manually re-created in each environment.', False),
                ('Data is deployed when added to a change set.', False),
                ('Data is unable to be deployed with change sets.', True)
            ]
        },
        {
            'text': 'UVC\'s CFO has asked that all deals with more than a 40% discount get automatically sent to the VP of Finance. He will review these deals without the sales rep needing to take action. Which two ways can this be accomplished without building code? Choose two answers.',
            'answers': [
                ('Launch a new approval process that has automatic submission enabled as an initial submission action', True),
                ('Create a new process with a submit for approval action to automatically submit deals for approval', False),
                ('Create a new approval process that has automatic submission enabled in the entry criteria', True),
                ('Launch a flow that uses the submit for approval action to submit deals for approval', False)
            ]
        },
        {
            'text': 'An app builder installs an unmanaged package in a full copy sandbox that is an exact match for production, and now they are ready to install it in production. When the app builder attempts to install the package in production, it fails. Why did the package fail to install?',
            'answers': [
                ('Incorrect license types', False),
                ('Package features not compatible', False),
                ('Object limits exceeded', False),
                ('Apex unit test failures', True)
            ]
        },
        {
            'text': 'Universal Containers wants to give sales managers the ability to quickly provide sign off on an Opportunity via the Opportunity record page when a sales rep has discounted a deal by 20% to 30%. Which two features should be used for this requirement? Choose 2 answers.',
            'answers': [
                ('Validation Rule', False),
                ('Dynamic Actions', True),
                ('Schema Builder', False),
                ('Approval Process', True)
            ]
        },
        {
            'text': 'Universal Containers allows all employees to submit reviews for leadership using a custom object called Review. These Reviews should only be visible to the HR department and the employee who submitted the record. Which three steps should an app builder take to properly control access to Reviews? Choose 3 answers.',
            'answers': [
                ('Disable Grant Access Using Hierarchies.', False),
                ('Add a Master-Detail (User) field on the Review object.', True),
                ('Create a criteria-based Sharing Rule for the HR Department.', True),
                ('Remove Review Read permission from non-HR Department user Profiles.', True),
                ('Set organization-wide default to Private.', False)
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
        migrations.RunPython(add_crt3),
    ]   