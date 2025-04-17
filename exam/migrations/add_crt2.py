from django.db import migrations, transaction

def add_crt2(apps, schema_editor):
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
        exam = Exam.objects.create(title='#CRM-2 Exam')

        # If you want to add the exam to the group (assuming a many-to-many relation):
        group.exams.add(exam)

        # Define questions and answers
        questions_data = [
      {
            'text': 'Universal Containers (UC) has several large customers that sell their products through dealers. UC identifies and works with a single individual at each customer and at each dealer. Separate bills are sent to each customer and each dealer. These details need to be stored in a format that clearly displays the business entities and their appropriate representatives. How should an app builder implement these requirements?',
            'answers': [
                ('Create a single parent record, add each rep as a contact to the parent account and add each dealer as a child record.', False),
                ('Create both customer and dealer as accounts, create account teams on each account and associate the dealer records with the parent account.', False),
                ('Create a single account record, add each rep as a contact and create a custom dealer object.', False),
                ('Create both customer and dealer as accounts, add each rep as a contact on the corresponding account and create an account hierarchy.', True),
            ]
        },
        {
            'text': 'The Director of customer service wants to receive a notification when a case stays in the "new" status for more than four business hours. Which two automation processes should be used to accomplish this?',
            'answers': [
                ('Escalation rules', True),
                ('Flow Builder', False),
                ('Process Builder', True),
                ('Scheduled Apex', False)
            ]
        },
        {
            'text': 'Universal Containers (UC) has a custom Invoice object and a custom Invoice Line Item object. The Invoice Line Item object has a lookup relationship to the Invoice. UC would like to convert the lookup relationship to a master-detail relationship but is unable to do so. Which two reasons could be preventing this relationship conversion?',
            'answers': [
                ('Custom objects are unable to be on the detail side of a master-detail relationship.', False),
                ('There are already two master-detail relationships on the Invoice Line Item.', True),
                ('Invoice Line-Item records exist without having the Invoice lookup field populated.', True),
                ('There is a roll-up summary field on the Invoice object.', False)
            ]
        },
        {
            'text': 'The app builder at AW Computing has been asked to track the number of times a case has been reopened. Which solution should the app builder utilize to help with this request?',
            'answers': [
                ('Scheduled Triggered flow', True),
                ('Screen flow', False),
                ('Process Builder', False),
                ('Apex Trigger', False)
            ]
        },
        {
            'text': 'Universal Containers would like to automatically assign a specific permission set to new users. How can this requirement be met? Choose 2 Answers',
            'answers': [
                ('Create an approval process on the User object to assign a permission set', False),
                ('Create a flow on the user object to assign a permission set.', True),
                ('Create a lightning process on the user object to launch a flow.', True),
                ('Create a workflow rule on the User object to assign a permission set.', False)
            ]
        },
        {
            'text': 'Cloud Kicks has three types of customer support processes: Platinum, Diamond, and Bronze. The app builder created separate record types for each process on the Case object. The customer support team should be unable to create new cases with the Bronze record type. How should this requirement be met?',
            'answers': [
                ('Update the organization-wide defaults to private for Case.', False),
                ('Update the support team profile to remove the Bronze record type.', True),
                ('Create permission set group for Case that includes Platinum and Diamond record types.', False),
                ('Make the record type hidden to support users; update sharing roles to private.', False)
            ]
        },
        {
            'text': 'Universal Containers sales reps can modify fields on an opportunity until it is closed. The sales operations team has access to modify the Post-Close Follow-up Date and Post-Close Follow-up Comments fields after the opportunity is closed. After the opportunity is closed, the rest of the fields are read-only. How should these requirements be met?',
            'answers': [
                ('Use record types with field sets and restrict editing fields using field-level security.', False),
                ('Use field-level security on page layouts to restrict editing fields.', False),
                ('Use field-level security on page layouts with record types to restrict editing fields.', True),
                ('Use field-level security to mark fields as read-only on the Sales profile.', False)
            ]
        },
        {
            'text': 'Universal Containers uses a private sharing model for opportunities. This model cannot be changed due to a regional structure. A new sales operations team has been created. This team needs to perform analysis on Opportunity data, and all should have read and write access to all Opportunities. What are two recommended solutions for the app builder to give the users appropriate access?',
            'answers': [
                ('Create a criteria-based sharing rule to all opportunities with the sales operations public group.', True),
                ('Add a manual share for all opportunities with each user on the sales operations team.', False),
                ('Add a permission set with "View All" and "Modify All" opportunity permissions enabled.', True),
                ('Create a criteria-based sharing rule to share all opportunities with the sales operations private group.', False)
            ]
        },
        {
            'text': 'A new custom object is being created with a private sharing setting. The business wants to share individual records with specific people or group of people on a case-by-case basis. What options does the business user have to manually share individual records?',
            'answers': [
                ('Public Groups', True),
                ('Permission Sets', False),
                ('Roles', True),
                ('Profiles', False),
                ('Users', True)
            ]
        },
        {
            'text': 'An app builder would like to streamline the user experience by reflecting summarized calculations of specific fields on various objects. Which field types could be used in roll-up ummary fields to accomplish this? Choose 3 answers',
            'answers': [
                ('Currency', True),
                ('Percent', True),
                ('Date', True),
                ('Checkbox', False),
                ('Time', False)
            ]
        },
        {
            'text': 'What are the limitations of Schema Builder when creating a custom object?',
            'answers': [
                ('Save should be clicked each time a new object, field, or relationship is created.', True),
                ('Fields and relationships can be created but not added to the page layout.', True),
                ('Relationships can be made to custom objects but not standard objects.', False),
                ('Custom fields excluding formula field types can be added.', False)
            ]
        },
        {
            'text': 'Universal Containers wants to create a report to show job applications with or without resumes. What should an app builder be aware of when creating the custom report type?',
            'answers': [
                ('An app builder cannot create custom report types for objects they do not have permissions for.', False),
                ('Once the report type has been deployed it is unable to be deleted.', False),
                ('A primary object selection is locked once the custom report type has been saved.', True),
                ('When a custom or external object is deleted, the report type remains.', False)
            ]
        },
        {
            'text': 'When an opportunity close date is delayed by more than 60 days, the manager and VP sales must approve the change. How can this be met?',
            'answers': [
                ('Build an approval process requiring unanimous approval from manager and VP of sales.', True),
                ('Create a workflow rule for close dates delayed less than 60 days.', False),
                ('Use a lightning process builder flow to submit the record for approval.', True),
                ('Build a validation rule to prevent saving the opportunity.', False)
            ]
        },
        {
            'text': 'UMS leadership wants four custom location fields to be concatenated into a single formula field on two lines. Which formula fulfills this requirement?',
            'answers': [
                ('Correct formula option', True),
                ('Incorrect formula option', False),
                ('Incorrect formula option', False),
                ('Incorrect formula option', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters wants to initiate a daily backup of its Salesforce org. Which tool should be recommended for this task?',
            'answers': [
                ('Report export', False),
                ('Refresh full copy sandbox', False),
                ('AppExchange package', False),
                ('Data Export Service', True)
            ]
        },
        {
            'text': 'What are two capabilities of Schema Builder?',
            'answers': [
                ('Editing custom settings', True),
                ('Creating a new record type', False),
                ('Showing selected objects on a page', True),
                ('Viewing page layouts in a new window', False)
            ]
        },
        {
            'text': 'When a sales rep submits an account for approval, Universal Containers wants additional questions answered in a popup window. What should be used?',
            'answers': [
                ('Process Builder and Flow', False),
                ('Lightning component and Process Builder', False),
                ('Custom picklist field and Process Builder', False),
                ('Custom button and Flow', True)
            ]
        },
        {
            'text': 'An app builder wants to deploy a new version of an auto-launched flow to production in an active state. What should be considered?',
            'answers': [
                ('Verify there is an Apex test that provides test coverage for the Flow.', True),
                ('Grant user access to the Flow.', False),
                ('Manually activate the Flow after deployment.', False),
                ('Include the Process Builder calling the Flow in the deployment.', False)
            ]
        },
        {
            'text': 'The sales team receives a list of approximately 800 leads each morning from marketing. Which tool should be used to import these leads while preventing duplicates?',
            'answers': [
                ('Dataloader.io', False),
                ('Data Import Wizard', True),
                ('Data Loader', False),
                ('Manual entry', False)
            ]
        },
        {
            'text': 'The Recruiting team at AW Computing captures job acceptance and hire date on the Job Application custom object. Once the candidate accepts, the hire date should not be changed. Which validation formula should be used?',
            'answers': [
                ('NOT(ISBLANK(Job_Accepted__c)) && ISCHANGED(Hire_Date__c)', True),
                ('ISBLANK(Job_Accepted__c) || NOT(ISCHANGED(Hire_Date__c))', False),
                ('NOT(ISBLANK(Job_Accepted__c)) || ISCHANGED(Hire_Date__c)', False),
                ('ISBLANK(Job_Accepted__c) && NOT(ISCHANGED(Hire_Date__c))', False)
            ]
        },
          {
            'text': 'Cloud Kicks wants to summarize the number of open Cases related to an Account, as well as the number of closed Cases to indicate customer support utilization. Which two automation solutions would meet these business requirements? (Choose 2)',
            'answers': [
                ('AppExchange', True),
                ('Validation Rule', False),
                ('Approval Process', False),
                ('Apex', True)
            ]
        },
        {
            'text': 'Cloud Kicks has a sales rep who is stating that their Contact is unavailable for other users to see within Salesforce. In which three ways can an app builder troubleshoot this issue? (Choose 3)',
            'answers': [
                ('Create an Account Sharing Rule', False),
                ('Confirm Organization-Wide Sharing Settings', True),
                ('Review the Contact record and ensure it is linked to an Account', True),
                ('Verify users have access to the Contact object', True),
                ('Create a new Contact and try again', False)
            ]
        },
        {
            'text': 'DreamHouse Realty acquired Cloud Kicks, which is still on Salesforce Classic. Where should the app builder find prebuilt resources to help with the migration and adoption?',
            'answers': [
                ('Import Wizard', False),
                ('Lightning Object Creator', False),
                ('AppExchange', True),
                ('Flow Builder', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters wants to change a master-detail relationship on Account to a lookup relationship with a custom object Park. What could be causing this?',
            'answers': [
                ('The Account is included in a flow process', False),
                ('The Park object needs one Master-Detail field', False),
                ('The Account includes roll-up summary fields', True),
                ('Park records have existing formulas on the Account', False)
            ]
        },
        {
            'text': 'Universal Containers is adding drone delivery to service offerings. The developer has written and tested code prior to deployment. What can the app builder do to ensure a smooth deployment?',
            'answers': [
                ('Remove Apex classes from the change set', False),
                ('Validate the inbound change set', False),
                ('Use a metadata package set', False),
                ('Validate the outbound change set', True)
            ]
        },
        {
            'text': 'An app builder wants to show Groups as the last navigation menu item in the mobile app but is unable to select Groups. What could cause this?',
            'answers': [
                ('Groups is available in the recent section of the navigation menu', False),
                ('Groups is included in the Smart Search items', False),
                ('Groups is unavailable in the selected list for the navigation menu', False),
                ('Groups is available in the Chatter section of the navigation menu', True)
            ]
        },
        {
            'text': 'Cloud Kicks asked the app builder to insert a list of 25,000 records using deduplication for the Race_Track__c custom object. Which tool should be used?',
            'answers': [
                ('Import Wizard', True),
                ('Lightning Object Creator', False),
                ('Data Loader', False),
                ('Schema Builder', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters wants to broadcast an email to 7,000 contacts using Salesforce but realizes there is a daily email limit. What action should the app builder take?',
            'answers': [
                ('Request Salesforce to increase the daily limit', False),
                ('Develop Apex code and Lightning components', False),
                ('Research AppExchange products to send mass emails', True),
                ('Export Contacts and use an email client', False)
            ]
        },
        {
            'text': 'An app builder wants to display an overdue date that is two months after a task\'s due date. Which approach should the app builder take?',
            'answers': [
                ('Use process builder and set overdue date equal to Due Date + (365/12)*2', False),
                ('Create a formula field using Due Date + 60', False),
                ('Use process builder and set overdue Date equal to Due Date + 60', False),
                ('Create a formula field using the ADDMONTHS() function', True)
            ]
        },
        {
            'text': 'An app builder received a request to extend record access beyond the organization-wide defaults configured. Which two features satisfy this requirement? (Choose 2)',
            'answers': [
                ('Sharing Rules', True),
                ('Public Groups', True),
                ('Permission Set Groups', False),
                ('Manual Sharing Rules', False)
            ]
        },
                {
            'text': 'Universal Containers has 20 different workflows on the opportunity object. To ensure that updates are processing properly for all field updates, UC has the re-evaluate workflow rules after field change checkbox checked. Recently, after adding a new workflow, users have reported receiving errors about workflow limits. What should an app builder look at to address this?',
            'answers': [
                ('Talk to a developer about apex code issues', False),
                ('Number of workflows per object limits', False),
                ('Workflows that cause each other to fire back and forth recursively', True),
                ('Workflows on other objects that are being re-triggered', False)
            ]
        },
        {
            'text': 'Ursa Major Solar wants to convert the relationship between Galaxy and Star from a lookup relationship to a master-detail relationship so each Galaxy record can be equipped with a rollup summary count of Star records. Which two considerations should be made?',
            'answers': [
                ('The Star records are all required to have an existing value in their Galaxy field.', True),
                ('The Galaxy object has fewer than two existing master-detail relationships.', True),
                ('The Galaxy object is required to contain existing roll-up summary fields.', False),
                ('The Star object has fewer than two existing master-detail relationships.', False)
            ]
        },
        {
            'text': 'Cloud Kicks is implementing an approval process for opportunities that requires managers to approve all opportunities above $50,000 before they can be marked as Closed Won. Which two delivery methods can a manager utilize to respond to approval requests in the Salesforce mobile app?',
            'answers': [
                ('In-App Notification', True),
                ('Record Detail', True),
                ('Navigation Menu', False),
                ('Home Screen', False)
            ]
        },
        {
            'text': 'A production org includes custom objects containing confidential information. A sandbox is needed that includes data records, excludes all of the confidential objects, and can be refreshed weekly. What steps should an App Builder take to meet these requirements?',
            'answers': [
                ('Create a Full Sandbox and use a sandbox template', False),
                ('Create a Developer Pro Sandbox and schedule Data Loader to download selected object data weekly.', False),
                ('Create a Partial Copy Sandbox and use a sandbox template.', True),
                ('Create a Developer Sandbox and schedule Data Loader to download selected object data weekly.', False)
            ]
        },
        {
            'text': 'When a deal is closed-won, it has to be approved by the owner\'s manager prior to being added to the leaderboard for a quarterly sales competition. An opportunity is won on the last day of the quarter and the manager is on vacation. What is recommended to ensure all of the appropriate deals are reviewed and the leaderboard is up to date?',
            'answers': [
                ('Forward the approval request to the manager\'s assistant.', False),
                ('Set up a delegated approver for the manager.', True),
                ('Have the manager log on and reassign the approval request.', False),
                ('Use Process Builder to assign a delegated approver.', False)
            ]
        },
        {
            'text': 'What should an app builder consider when choosing a template for a new Lightning record page?',
            'answers': [
                ('The template is unable to be changed after the initial save.', False),
                ('To view the record page, users need "View All Data" permissions for the object.', False),
                ('A Page structure will automatically adapt to the device being used to view the record page.', True),
                ('Select a new template for each type of device users use to view the record page.', False)
            ]
        },
        {
            'text': 'Managers at Universal Containers want a quick way to create additional accounts to form a hierarchy from a parent account record. They want to auto-populate five fields based on the parent to make it easier for users to create the child accounts quickly.',
            'answers': [
                ('Custom Global Quick Action', False),
                ('Custom Global Quick Account', False),
                ('Custom action on Account', True),
                ('Custom link on Account', False)
            ]
        },
        {
            'text': 'Cloud Kicks works on an annual subscription model. When a sales rep marks an opportunity as closed won, a new opportunity should automatically be created for the renewal. The contracts team works outside of Salesforce but also needs to be notified about closed deals in order to initiate the contract process with the customer. Which automation solution would meet these requirements?',
            'answers': [
                ('Approval Process', False),
                ('Outbound Message', False),
                ('Validation Rule', False),
                ('Record-triggered flow', True)
            ]
        },
        {
            'text': 'The CFO of Cloud Kicks needs to sign off on any major show retail deal that has a discount of more than 30% before the deal can be closed. What feature would be used to handle this requirement?',
            'answers': [
                ('Approval Process', True),
                ('Email Alert', False),
                ('Field Update', False),
                ('Workflow Rule', False)
            ]
        },
        {
            'text': 'Universal Containers (UC) has a time-sensitive need for a custom component to be built in 4 weeks; UC developers require additional enablement to complete the work and are backlogged by several months. Which option should an app builder suggest to meet this requirement?',
            'answers': [
                ('Use an AppExchange solution.', True),
                ('Build a screen flow page.', False),
                ('Build a Lightning record page.', False),
                ('Use a Bolt solution', False)
            ]
        },
                {
            'text': 'An app builder wants to create a custom Sync button on Account that will call a Lightning Web Component that connects with an external system. This action should only be available if the custom Status field is set to Ready to Sync. What should an app builder use to add this functionality to an Account record page?',
            'answers': [
                ('Formula field', False),
                ('Dynamic action', True),
                ('AppExchange product', False),
                ('Custom link', False)
            ]
        },
        {
            'text': 'Which three standard component types are available in the Lightning App Builder? Choose 3 answers.',
            'answers': [
                ('Plain text', False),
                ('Rich text', True),
                ('Filter list', False),
                ('Report details', True),
                ('Recent items', True)
            ]
        },
        {
            'text': 'Cloud Kicks has created a custom object called Interests which is joined to Accounts by way of a junction object called Account Interest. What is the impact to users attempting to view an Account and the associated Account Interest records if they are without read access to the Interest object?',
            'answers': [
                ('Users will be able to view the Account Interest records and will have read-only access to the Interest records.', False),
                ('Users will be unable to view Account records that have a related Account Interest record.', False),
                ('Users will be unable to view the Account Interest records or the Interest records.', True),
                ('Users will be able to view the Account Interest record, but unable to view the field or any information relating back to the Interest record.', False)
            ]
        },
        {
            'text': 'An app builder installed a custom Lightning component from AppExchange and has deployed My Domain. What should be done next in order to configure the component for use in a record page?',
            'answers': [
                ('Edit a record page using Lightning App Builder > Drag the component onto the page.', True),
                ('Edit a record page using the Page Layout editor > Drag the component onto the page.', False),
                ('Edit a record page using the Page Layout editor > Drag the Visualforce component onto the page.', False),
                ('Edit a record page using App Manager > Drag the component onto the page.', False)
            ]
        },
        {
            'text': 'Managers at Universal Containers want a quick way to create additional accounts to form a hierarchy from a Parent Account record. They want to auto-populate five fields based on the parent to make it easier for users to create the child accounts quickly. What should the app builder recommend?',
            'answers': [
                ('Add Path on Account hierarchy', False),
                ('Add a custom link on Account', False),
                ('Customize a Global Quick Action', False),
                ('Create a custom action', True)
            ]
        },
        {
            'text': 'Cloud Kicks (CK) switched to Lightning Experience and started using Chatter across its global workforce to support its fast-paced sales cycle. CK loves Chatter but struggles with gathering feedback from core team members, including understanding who is available to respond. Which two ways could CK use Chatter to solve this problem? Choose 2 answers.',
            'answers': [
                ('Streams', False),
                ('Polls', True),
                ('Out of Office', True),
                ('Topics', False)
            ]
        },
        {
            'text': 'Universal Containers has a single Contact Lightning record page. A component takes up a lot of room on the page and is NOT needed by users with a Marketing profile. What should the app builder use to solve this Issue?',
            'answers': [
                ('Detail page layouts', False),
                ('Component visibility filter', True),
                ('Field-level security', False),
                ('AppExchange', False)
            ]
        },
        {
            'text': 'Cloud Kicks (CK) wants to quickly insert a list of over 60,000 net new Accounts. The template based on CK\'s data model was used to populate the list. Which tool should be used?',
            'answers': [
                ('Data Loader', True),
                ('Lightning Object Creator', False),
                ('Import Wizard', False),
                ('Schema Builder', False)
            ]
        },
        {
            'text': 'Universal Containers wants to ensure that they are accepting clean data from their users and verify that important fields are entered. What should an app builder recommend to meet this requirement?',
            'answers': [
                ('Update the important fields to be required on the page layout', False),
                ('Make a formula field to check the format of the important fields', False),
                ('Create a workflow rule to check the fields are formatted correctly', False),
                ('Configure a validation to require a field for a specific record type', True)
            ]
        },
        {
            'text': 'Universal Containers (UC) wants to test code against a subset of production data that is under 5 GB. Additionally, UC wants to refresh this sandbox every weekend. Which type of sandbox should be used to accomplish this?',
            'answers': [
                ('Developer Sandbox', False),
                ('Partial Copy Sandbox', True),
                ('Full Sandbox', False),
                ('Scratch Org', False)
            ]
        },
                {
            'text': 'An App Builder has been asked to integrate Salesforce with an external web service. The web service must be notified every time an Opportunity is Won. Which two can satisfy this requirement?',
            'answers': [
                ('Use a workflow rule and an outbound message', True),
                ('Use a flow and an outbound message', False),
                ('Use a process and Apex Code', True),
                ('Use a process and an outbound message', False)
            ]
        },
        {
            'text': 'Universal Containers (UC) maintains information for over 2 million assets in an external system. UC needs to access these assets in real-time data in Salesforce and is nearing the data storage limits. What feature could an app builder recommend UC use?',
            'answers': [
                ('Data Loader', False),
                ('Salesforce Connect', True),
                ('Salesforce to Salesforce', False),
                ('Data Export Wizard', False)
            ]
        },
        {
            'text': 'An app builder at Cloud Kicks created a custom object and related fields in the schema builder. What next steps should the app builder take to ensure users can access the new object and fields?',
            'answers': [
                ('Create a permission set for access to the object and fields', False),
                ('Allow reporting for the object and fields', False),
                ('Assign data types to the fields on the object', False),
                ('Add the fields to the page layout on the object', True)
            ]
        },
        {
            'text': 'Ursa Major Solar (UMS) uses a public sharing model for accounts. UMS would like to move to a more restrictive sharing model but wants the Sales team to continue to have access to all account records with the sales record type. Which two actions should an app builder complete to implement this change?',
            'answers': [
                ('Update the Sales profile', False),
                ('Update the organization-wide defaults', True),
                ('Create a criteria-based sharing rule', True),
                ('Create an owner-based sharing rule', False)
            ]
        },
        {
            'text': 'Ursa Major Solar\'s service department gets requests for several types of services, such as installation, repair, and maintenance. Service managers need to be able to tell when maintenance was last done on an asset to help determine if they are meeting contract agreements, but the last maintenance date can be difficult to determine when there are many work orders related to the asset. They think it would be helpful to have a field auto-populated on the Asset record when a maintenance work order gets closed. What tool should an app builder recommend to help meet this requirement?',
            'answers': [
                ('Visualforce', False),
                ('Roll-up Summary', False),
                ('Apex Trigger', False),
                ('Flow', True)
            ]
        },
        {
            'text': 'Universal Containers uses a custom object called Projects. When managers assign projects they set a custom field on the project called Estimated Hours. Once set, users should be able to decrease but not increase the value. How can an app builder meet this requirement?',
            'answers': [
                ('Create a formula default value for the custom field', False),
                ('Create a formula field that uses the PREVGROUPVAL function', False),
                ('Create a validation rule that uses the ISCHANGED function', False),
                ('Create a validation rule that uses the PRIOR VALUE function', True)
            ]
        },
        {
            'text': 'Universal Containers has Public Read/Write as the Account organization-wide default (OWD) setting. Visitors to the customer community site report that they can see all of the company\'s account records. How should an app builder configure Account sharing so that community users only see their own Account?',
            'answers': [
                ('Create an account record type for external accounts', False),
                ('Define an owner-based sharing rule for external accounts', False),
                ('Define a permission set for external accounts', False),
                ('Set the account external OWD to private', True)
            ]
        },
        {
            'text': 'Universal Containers has a customer base where many customers have the same or similar company names. Which functionality should be configured to improve an end user’s search experience?',
            'answers': [
                ('Update the account search layout\'s view filter settings', False),
                ('Update the account search layout\'s search results columns displayed', True),
                ('Update the account search filter fields', True),
                ('Update the account search layout\'s accounts tab columns displayed', False)
            ]
        },
        {
            'text': 'The Universal Containers data manager has been complaining about the lack of data integrity on Contact records. Sales reps have not been filling out the Region field. The data manager wants the Region field filled out only for Contacts that are associated to Accounts that have been marked as \'High Priority\' on the Customer Status field. What can the app builder do to fulfill this requirement?',
            'answers': [
                ('Make the Region field required on Contact', False),
                ('Create a validation rule on Contact', True),
                ('Create 4 validation rules on Account', False),
                ('Make the Customer Status field required on Account', False)
            ]
        },
        {
            'text': 'An app builder has modified a Lightning record page for a case and has added an email button item to the page layout; however, users are unable to see the new item on the layout. What are two potential reasons why users are unable to view the item on the Case Lightning record page?',
            'answers': [
                ('The page layout includes the case feed component', False),
                ('The email button contains JavaScript', True),
                ('The case page layout also contains custom buttons.', False),
                ('The page layout excludes the case feed component.', True)
            ]
        },
        {
            'text': 'AW Computing has a custom object for service plans. A service plan needs to be associated to one and only one contact. The support manager noticed if the wrong contact is associated, the reps are unable to change the contact. The app builder already confirmed the user has correct access to the field and there are no validations associated with the service plans. What could be causing the issue?',
            'answers': [
                ('The Read Only radio button is selected.', False),
                ('The Allow reparenting checkbox is unchecked.', True),
                ('The Read/Write radio button is selected.', False),
                ('The Allow reparenting checkbox is checked.', False)
            ]
        },
        {
            'text': 'Cloud Kicks wants to know the total value of all won Opportunities for Accounts and display it on the record. What type of summary should the app builder use in the roll-up summary field?',
            'answers': [
                ('Count', False),
                ('Q Max', False),
                ('Sum', True),
                ('Min', False)
            ]
        },
        {
            'text': 'The app builder needs to change the data types of new custom fields. The app builder is not able to delete and recreate any of the fields, nor modify any apex code. Which data type change will require the app builder to perform additional steps in order to retain existing functionalities?',
            'answers': [
                ('Changing the data type of a field used in an apex class from number to text.', True),
                ('Changing the data type of a field used in a report from a text to an encrypted field.', False),
                ('Changing the data type of a field used as an external id from number to text.', False),
                ('Changing the data type of a field used in lead conversion from number to text.', False)
            ]
        },
        {
            'text': 'A Service Coordinator (SC) for Ursa Major Solar (UMS) does a final review of work orders owned by a technician for a specific region before the records are submitted for an invoice. Before closing out the work order, the SC needs to modify data or remove attachments that were added by mistake. The SC also needs access to any other related records owned by the technician. What solution would provide the required access, given a private data model?',
            'answers': [
                ('Give the SC a permission set with the Modify All Data system permission.', False),
                ('Put the SC in the role hierarchy above the technicians whose work orders they review.', True),
                ('Create a workflow rule that updates records owned by technicians in that region with the SC.', False),
                ('Change work order access on the SC\'s profile to "Modify All."', False)
            ]
        },
        {
            'text': 'An app builder needs to change the data type of some custom fields. Which two limitations should the app builder be aware of when changing the data type of a custom field? Choose 2 answers.',
            'answers': [
                ('It is not possible to change the data type of a formula field to any data type.', False),
                ('It is not possible to change the data type of a field referenced by Apex code.', True),
                ('It is not possible to change the data type of a field used as an External ID from number to text.', False),
                ('It is not possible to change the data type of a Text Area (Long) field to Text.', True)
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
        migrations.RunPython(add_crt2, atomic=False),
    ]
