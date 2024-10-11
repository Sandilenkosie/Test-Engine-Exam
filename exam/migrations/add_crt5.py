from django.db import migrations

def add_crt5(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')

    # Create an exam instance
    exam = Exam.objects.create(title='CRM-5 Exam')

    # Define questions and answers
    questions_data = [
   {
            'text': 'Cloud Kicks (CK) is finding sales reps are inconsistent in data entry when deals are won. CK requires that custom shoes are shipped within two weeks after the close date. A custom field called Scheduled Ship Date on the opportunity records the ship date. How should the app builder ensure this field is properly filled out before setting the opportunity to closed won?',
            'answers': [
                ('OR(ISPICKVAL(StageName, "Closed Won") && (Scheduled_Ship_Date__c - CloseDate) > 14, ISBLANK(Scheduled_Ship_Date__c))', True),
                ('OR(ISPICKVAL(StageName, "Closed Won") && (Scheduled_Ship_Date__c - CloseDate) < 14, ISBLANK(Scheduled_Ship_Date__c))', False),
                ('ISPICKVAL(StageName, "Closed Won") && (Scheduled_Ship_Date__c - CloseDate) > 14', False),
                ('ISPICKVAL(StageName, "Closed Won") && (CloseDate - Scheduled_Ship_Date__c) > 14', False),
            ]
        },
        {
            'text': 'The Director of Marketing at Northern Trail Outfitters wants the app builder to create a formula field that tracks how many days have elapsed since a contact was sent a marketing communication. Which function should be used to return a date for calculating the difference?',
            'answers': [
                ('DATETIMEVALUE()', False),
                ('TODAY()', True),
                ('DATEVALUE()', False),
                ('NOW()', False),
            ]
        },
        {
            'text': 'An app builder at Ursa Major Solar has been working on a new custom app in a sandbox that has been upgraded to the next major Salesforce version. What should the app builder consider when planning the deployment?',
            'answers': [
                ('It will fail if there is a feature only available in the next version.', True),
                ('The change set components will be upgraded to the next version in production.', False),
                ('The change set will be automatically deployed when production is upgraded.', False),
                ('The deployment is not possible due to different versions.', False),
            ]
        },
        {
            'text': 'Universal Containers utilizes opportunities and a custom object called Detailed.Sales__c. The company would like to roll sales metrics up to an opportunity for only Detailed.Sales__c records that have their picklist status set to Active. What is the recommended method for the app builder to achieve this request?',
            'answers': [
                ('Utilize the AppExchange to download a third-party application that can roll-up the sales dollars with the appropriate filter.', False),
                ('Create a master-detail relationship between the parent and child object with a roll-up summary field that filters on the status held.', True),
                ('Create a lookup relationship between the parent and child object with a roll-up summary field that filters on the status field.', False),
                ('Utilize Apex code to roll up the desired amounts.', False),
            ]
        },
        {
            'text': 'Universal Containers wants to improve the process to create Opportunity records related to an Account. What should an app builder configure to meet the requirement?',
            'answers': [
                ('Process Builder triggered from Opportunity update', False),
                ('Quick Action on the Account object', True),
                ('Quick Action on the Opportunity object', False),
                ('Process Builder triggered from Account update', False),
            ]
        },
        {
            'text': 'Cloud Kicks (CK) keeps track of its shoe inventory in Salesforce. When an order\'s status is changed to Activated, the inventory for the ordered shoe is reduced. At that point, a SOAP web service on the CK website must be called. What should an app builder use to communicate to the CK web service?',
            'answers': [
                ('After-Save Record-Triggered flow', True),
                ('Before-Save Record-Triggered flow', False),
                ('Process Builder', False),
                ('Workflow rule', False),
            ]
        },
        {
            'text': 'DreamHouse Realty has a mentorship program that pairs experienced Realtors with new Realtors. What type of relationship would an app builder set up to meet this specification?',
            'answers': [
                ('Indirect lookup', False),
                ('Many-to-many', False),
                ('Master-detail', False),
                ('Lookup', True),
            ]
        },
        {
            'text': 'Due to the complexity of the Universal Containers sandbox release schedule, it is advised that change sets are used as often as possible to migrate from one environment to another. Which three common items can an app builder move when using a change set? Choose 3 answers',
            'answers': [
                ('Web-to-lead', False),
                ('Standard fields', False),
                ('Custom object', True),
                ('Apex class', True),
                ('Custom field', True),
            ]
        },
        {
            'text': 'An app builder wants to add the option to \'Send New Email\' from Leads, Contacts and Accounts for users on mobile. What is the benefit of using global actions to accomplish this?',
            'answers': [
                ('Global actions can be accessed anywhere actions are pages, feed and Chatter groups.', True),
                ('Salesforce Lightning Component Library houses existing global actions prebuilt for use.', False),
                ('The global action\'s layout automatically clones the default page layout.', False),
                ('Global actions are record-specific and are available when searching that particular record.', False),
            ]
        },
        {
            'text': "Cloud Kicks (CK) captures all shipping information in a custom object called Shipments__c. "
                    "CK's app builder is tasked with creating an approval process to ensure department members "
                    "can approve all overnight shipments. Where should the app builder route the approval request?",
            'answers': [
                ('Hierarchy field', False),
                ('Role', False),
                ('Public group', True),
                ('Queue', False)
            ]
        },

                {
            'text': 'Universal Containers (UC) has large data volumes and is nearing data storage limits. The planned solution is to archive historical data to reduce data storage in Salesforce; however, UC would still like to use reports, queries, and lookups on the archived information. Which two options could meet this requirement?',
            'answers': [
                ('Big objects', True),
                ('Custom objects', False),
                ('Related objects', False),
                ('External objects', True)
            ]
        },
        {
            'text': 'The app builder at Northern Trail Outfitters created a report type for opportunities with or without shipments. The operations team wants to see the account rating Information on the report. What should the app builder do to fulfill this request?',
            'answers': [
                ('Change the primary object of the custom type to the Account object.', False),
                ('Add the Account Rating field to the opportunity record page.', False),
                ('Use add fields related via lookup with the view set to opportunities.', True),
                ('Change the account/opportunity relationship to a master/detail relationship.', False)
            ]
        },
        {
            'text': 'Which two places can an app builder go to see a list of available Custom Lightning components in their org?',
            'answers': [
                ('Visualforce components in Setup', False),
                ('Lightning component Generator', False),
                ('Lightning App Builder', True),
                ('Lightning components in Setup', True)
            ]
        },
        {
            'text': 'Universal Containers generates leads from three different sources: web, trade shows, and partners. Some of the information collected is applicable to all sources, there is also information that is unique to each type of lead. What should an app builder configure to meet these requirements?',
            'answers': [
                ('Create three lead record types each with its own page layout containing the relevant fields', True),
                ('Create a partner community and a record type for web and trade show leads', False),
                ('Create three sections on the lead layout and instruct users to collapse the non-relevant fields', False),
                ('Create custom page layouts for each type of lead only containing the relevant fields', False)
            ]
        },
        {
            'text': 'Sales Managers want to be automatically notified any time there is a change to an Opportunity Close Date and want these changes to be tracked on the Opportunity. Which two configurations should an app builder recommend?',
            'answers': [
                ('Create an Opportunity outbound message.', False),
                ('Use Process Builder on Opportunities and a Chatter post action.', True),
                ('Activate Historical Trending for Opportunities.', False),
                ('Enable Feed Tracking on Opportunities.', True)
            ]
        },
        {
            'text': 'SERVICE AGENTS ARE REQUIRED TO CONFIRM A USER IDENTITY BEFORE PROVIDING SUPPORT INFORMATION OVER THE PHONE. WHAT FEATURE CAN AN APP BUILDER USE TO HELP AGENTS MEET THIS REQUIREMENT?',
            'answers': [
                ('Include Surveys as a Case related list', False),
                ('Case Validation Rules', False),
                ('Add Path to the top of the Case layout', False),
                ('Guided Action Flows on the record page', True)
            ]
        },
        {
            'text': 'The VP of sales at AW Computing would like a Roll-Up Summary field on the Account object to aggregate the amount of opportunities related to an Account. The app builder is unable to implement this change. Why is the app builder unable to fulfill the request?',
            'answers': [
                ('Currency fields are unable to be referenced in Roll-Up Summary fields.', False),
                ('The organization has Advanced Currency Management enabled', True),
                ('Roll-Up Summary fields are unavailable on the Account object.', False),
                ('The default currency is not an active currency in the organization.', False)
            ]
        },
        {
            'text': 'What option is available to an App Builder when defining an object-specific Create Record custom action? Choose 2 answers',
            'answers': [
                ('Specifying the fields and layout of the action.', True),
                ('Allowing the end user to choose the record type', False),
                ('Redirecting the end user to the detail page of the target object', False),
                ('Pre-Defining field values on the target object.', True)
            ]
        },
        {
            'text': 'A new field has been added to the Applicant object that is part of an unmanaged package. A recruiter ran the Position with or without Applicants report and noticed that the new field was missing as an option to add as a column. How should an app builder troubleshoot this issue?',
            'answers': [
                ('Adjust the field level security to include in the report type.', False),
                ('Check Allow Reports for the position and applicant objects.', False),
                ('Add the field to the custom report type field layout.', True),
                ('Update the profile with the Manage Public Reports permission.', False)
            ]
        },
        {
            'text': 'AW Computing uses a private sharing model for opportunities. Whenever an opportunity with a type of Service Agreement is created, all users in the Service Manager role should be able to view the opportunity. Which tool should AW Computing use to accomplish this?',
            'answers': [
                ('Owner-based sharing rules', False),
                ('Criteria-based sharing rules', True),
                ('Apex sharing rules', False),
                ('Manual sharing', False)
            ]
        },
                {
            'text': 'Universal Containers wants to display the real-time stock price for each account on the account record page. How should an app builder implement this request?',
            'answers': [
                ('Add a dynamic report to the page layout', False),
                ('Create a Lightning Web Component', True),
                ('Install a solution from the AppExchange', False),
                ('Build a visual flow that uses API calls', False)
            ]
        },
                {
            'text': 'After utilizing the Lightning Object Creator to create a new object, its fields, and to insert all of the data, an app builder now needs to set up the Lightning Record Page. Which component should the app builder have on their Lightning Record Page to see all of the fields from the page layout?',
            'answers': [
                ('Highlights Panel', False),
                ('Recommendations', False),
                ('Record Detail', True),
                ('Path', False)
            ]
        },
        {
            'text': 'Cloud Kicks is implementing an approval process for opportunities that requires managers to approve all opportunities above $50,000 before they can be marked as Closed Won. Which two delivery methods can a manager utilize to respond to approval requests in the Salesforce mobile app?',
            'answers': [
                ('Home Screen', False),
                ('In-App Notification', True),
                ('Record Detail', True),
                ('Navigation Menu', False)
            ]
        },
        {
            'text': 'An app builder has deployed a change set from a sandbox to production. There is a long delay in the deployment. What can be causing the delay?',
            'answers': [
                ('Profiles are included in the change set.', False),
                ('A field type change is included in the change set.', True),
                ('Dependent fields are included in the change set.', False),
                ('Roles are included in the change set.', False)
            ]
        },
        {
            'text': 'Ursa Major Solar is ramping up the sales team to meet increased demand. As part of the short ramp up for these new reps, the manager wants to provide a help guide to enable reps to easily get help where needed during the different sales processes. Which solution should an app builder recommend?',
            'answers': [
                ('Flow', False),
                ('Journey Builder', False),
                ('Chatter Publisher', False),
                ('Path', True)
            ]
        },
        {
            'text': 'DreamHouse Realty is building a custom Lightning app to track its expanding solar water collection business. The Lightning app currently contains a custom Lightning record page with standard components. From which two resources should an app builder get custom components to bring into the new Lightning app?',
            'answers': [
                ('AppExchange', True),
                ('Apex Code', True),
                ('Import Wizard', False),
                ('Visualforce', False)
            ]
        },
        {
            'text': 'Universal Containers wants to understand return on investment for the latest advertising buy. They currently use a private security model for all objects. What should an app builder recommend?',
            'answers': [
                ('Utilize Account Hierarchies and Roll-Up Summary fields', False),
                ('Run an opportunities pipeline report', True),
                ('Change to a public security model', False),
                ('Configure Campaign Hierarchies and Campaign statistics', False)
            ]
        },
        {
            'text': 'At Universal Containers, the Account object has a Master-Detail relationship with an Invoice custom object. The App Builder would like to change to a lookup field, but is not able to do so. What could be causing this?',
            'answers': [
                ('The invoice must have at least one Master-Detail field for reporting.', False),
                ('The Account record includes Invoice roll-up summary fields.', True),
                ('The Invoice records have existing values in the Account.', False),
                ('The Account is included in the workflow on the Invoice object.', False)
            ]
        },
        {
            'text': 'Universal Containers is migrating its sales operations from a legacy system. Opportunities need to be imported with the proper country currency. Which two steps should an app builder configure to meet these requirements?',
            'answers': [
                ('Include the currency ISO code in all currency fields in the import file.', True),
                ('Use Data Loader to import the records.', True),
                ('Include the currency ISO Code Column in the import file.', False),
                ('Use Import Wizard to import the records.', False)
            ]
        },
        {
            'text': 'DreamHouse Realty wants to display a weather map component on a Lightning record page when a house is scheduled for a showing. How should the app builder meet the requirement?',
            'answers': [
                ('Component visibility', True),
                ('Field-level security', False),
                ('Field-level field', False),
                ('Sharing rules', False)
            ]
        },
                {
            'text': 'Universal Containers (UC) want to delete data in several fields for 5000 lead records. UC exports the selected record IDs and fields that need to have data deleted in a CSV file. Which two steps should an app builder suggest to meet these requirements? Choose 2 answers',
            'answers': [
                ('Select the correct record type', False),
                ('Use import Wizard to update leads using the CSV file', False),
                ('Select insert null values in settings.', True),
                ('Use Data Loader to update leads using the CSV file', True)
            ]
        },
                {
            'text': 'At Universal Containers, the VP of Service has requested a visual indicator flag on each case, based on the case priority. High-priority cases should be flagged red, medium-priority should be flagged yellow, and low-priority cases should be flagged green. Which formula would accomplish this requirement? Choose 2 answers',
            'answers': [
                ('CASE(Priority, "Low", "img/samples/flag_green.gif", "Medium", "img/samples/flag_yellow.gif", "High", "img/samples/flag_red.gif", "/s.gif")', True),
                ('IMAGE(IF(ISPICKVAL(Priority, "Low"), "img/samples/flag_green.gif", IF(ISPICKVAL(Priority, "Medium"), "img/samples/flag_yellow.gif", IF(ISPICKVAL(Priority, "High"), "img/samples/flag_red.gif"))), "Priority Flag")', False),
                ('IF (ISPICKVAL(Priority, "Low"), "img/samples/flag_green.gif", IF(ISPICKVAL(Priority, "Medium"), "img/samples/flag_yellow.gif", IF(ISPICKVAL(Priority,"High"), "img/samples/flag_red.gif", "/s.gif"))) ', False),
                ('IMAGE (CASE(Priority, "Low", "img/samples/flag_green.gif", "Medium", "img/samples/flag_yellow.gif", "High", "img/samples/flag_red.gif", "Priority Flag")', True),
            ]
        },
        {
            'text': 'Universal Containers has a custom object that holds over 100 fields. The app builder wants to break up the fields into separate tabs on the lightning page. Which Lightning component is most appropriate to fulfill this requirement?',
            'answers': [
                ('Highlights panel', False),
                ('Record detail', False),
                ('Field section', False),
                ('Accordion', True),
            ]
        },
        {
            'text': 'An app builder wants to create a report to compare the number of support cases in each status (New, In-progress, or Closed) and by priority (Critical, High, Medium, or Low). What solution should be used for the report?',
            'answers': [
                ('Grouping', True),
                ('Bucket Columns', False),
                ('Custom Report Type', False),
                ('Filters', False),
            ]
        },
        {
            'text': 'After a deal is closed, Cloud Kicks (CK) wants to assign a user as a customer service manager (CSM) in addition to the account owner and would like a new field to easily track and report which CSM is assigned to the Account. Which solution should an app builder use for this request?',
            'answers': [
                ('Multi-select picklist', False),
                ('Picklist field', False),
                ('Lookup field', True),
                ('Text field', False),
            ]
        },
        {
            'text': 'Universal Containers wants to streamline its data capture process by linking fields together. They wish to do this so that the available value on dependent fields are driven by value selected on controlling fields. Which consideration supports the stated requirements? Choose 3 answers',
            'answers': [
                ('The import wizard only allows value to be imported into a dependent picklist if they match the appropriate controlling field', True),
                ('Custom picklist field can be either controlling or dependent field', True),
                ('Multi select picklist can be dependent picklist but not controlling fields', False),
                ('Standard and custom picklist fields can be dependent fields', False),
                ('Checkbox fields can be controlling fields but not dependent fields', True),
            ]
        },
        {
            'text': 'Universal Containers created a "New Task" custom action on the Opportunity object. The action was added to all page layouts in the Mobile & Lightning Actions section. Which Lightning component should the app builder add to the layout to display the action?',
            'answers': [
                ('Related record', False),
                ('Related lists', False),
                ('Highlights panel', True),
                ('Activities', False),
            ]
        },
        {
            'text': 'Ursa Major Solar wants to provide sales console users with an Incredible experience, with the most-used components easily accessible at all times. What solution can enable reps to see and access these components from anywhere within the app without leaving the pages where the team is working?',
            'answers': [
                ('Favorites', False),
                ('Home page', False),
                ('Global actions', False),
                ('Utility bar', True),
            ]
        },
        {
            'text': 'Universal Containers has created two custom objects called Seminars and Attendees. Organization-wide defaults for these objects have been set to Private. Universal Containers wants to set up a new Junction object between these custom objects. A select group of users should be able to edit records in the Junction object. Which two steps should an app builder take to configure the proper security?',
            'answers': [
                ('Set Sharing Settings to Read Only on both Master-Detail relationship fields.', True),
                ('Create owner-based sharing rules that give Read access to the master objects.', False),
                ('Set lookup filters on both Junction object relationship field.', False),
                ('Create an owner-based sharing rule that gives Read action to the junction object.', True),
            ]
        },
         {
            'text': 'Accounts at Universal Containers are currently readable by all users but editable only by their owners. Management wants to designate some Accounts as VIP Accounts. Only Account owners should have read access to these VIP accounts. Which two actions should an app builder take to meet the requirements? Choose 2 answers',
            'answers': [
                ('Implement a sharing rule.', True),
                ('Configure a permission set.', False),
                ('Set up an Account Team.', False),
                ('Change organization-wide defaults.', True),
            ]
        },
        {
            'text': 'Cloud Kicks (CK) increased its Salesforce development efforts so that it now has multiple custom development efforts happening in parallel. CK\'s developers and admins perform the customizations and have complained that working in one sandbox has led to many problems. They requested a solution in which they can work in at least 20 different sandboxes at once, that all start with the same base configuration and data. What should an app builder use to solve the problem?',
            'answers': [
                ('Sandbox refreshes', False),
                ('Full copy sandboxes', False),
                ('Partial copy sandboxes', True),
                ('Sandbox during', False),
            ]
        },
        {
            'text': 'An app builder wants to create a new field using Schema Builder. Who will get access to the new field by default?',
            'answers': [
                ('Standard profiles', False),
                ('No profiles', False),
                ('Internal profiles', False),
                ('All profiles', True),
            ]
        },
        {
            'text': 'Universal Containers uses the Asset object to track products that are installed at customer locations. A new object, Asset Inventory, has been created to capture details about the asset. Which approach should the app builder take to show Asset Inventory as a related list on Asset?',
            'answers': [
                ('Create a roll-up on Asset. Add the Asset Inventory related list to the Asset page layout.', False),
                ('Create a junction object to relate Asset Inventory and Asset. Add the Asset Inventory related list to the Asset page layout.', False),
                ('Create a lookup relationship on Asset Inventory to Asset. Add the Asset Inventory related list to the Asset page layout.', True),
                ('Create a master-detail relationship on Asset-to-Asset Inventory. Add the Asset Inventory related list to the Asset page layout.', False),
            ]
        },
        {
            'text': 'Universal Containers expects impacts to operations due to increased demand. The executive team will reach out to current customers and wants to see the number of open cases for the account and parent account. What should an app builder use to display the number of open cases on the account page?',
            'answers': [
                ('Flow', False),
                ('Approval Process', False),
                ('Roll-up summary', True),
                ('Custom object', False),
            ]
        },
        {
            'text': 'DreamHouseRealty (DR) is expanding into subsidized housing by partnering with local government entities. DR uses Sales Cloud and has enabled field history tracking on the Opportunity object. Due to increased information requirements, the App Dev team is changing Text Area (Long) fields to Rich Text fields to allow for up to 1,000 characters and better descriptions. Which two considerations should be made by the team? Choose 2 answers',
            'answers': [
                ('Rich text field values of all lengths are displayed fully in reports.', False),
                ('Data loss may occur when changing custom field types.', True),
                ('Field History Tracking records value changes of 255 characters or less.', True),
                ('Audit Trail is available through REST API extracts.', False),
            ]
        },
        {
            'text': 'An app builder needs to deploy a new account detail page layout from sandbox to production. Which three components should an app builder include in the Change Set to ensure it deploys successfully and visually as expected? Choose 3 answers',
            'answers': [
                ('Detail page layout', True),
                ('Custom fields', True),
                ('Custom actions', True),
                ('Lightning App Builder', False),
                ('System administrator profile', False),
            ]
        },
        {
            'text': 'Cloud Kicks (CK) wants to set up a custom child object to track gift cards issued to a customer. A key requirement is to track the total number of gift cards opened and gift cards issued on an Account. CK wants to permanently ensure the gift cards are unable to be moved across any other Account once it is created. On the gift card object, what type of field should be created to support this requirement?',
            'answers': [
                ('Master-detail relationship', True),
                ('Roll-up summary', False),
                ('Formula', False),
                ('Lookup relationship', False),
            ]
        },
        {
            'text': 'Cloud Kicks has leads owned by users and queues. The sales manager wants the status to change to working when a user takes ownership. What does an app builder need to have in the criteria to ensure the process runs without error?',
            'answers': [
                ('BEGINS([Lead].OwnerId, ,,005")', False),
                ('[Lead].Owner:User.Role Is Null = False', False),
                ('[Lead].Owner:Queue.OwnerId Is Null = True', False),
                ('NOT(ISBLANK([Lead].OwnerId))', True),
            ]
        },
                {
            'text': 'The marketing director is concerned that too many car parts were given away for free last year. Which functionality should be used to ensure all free parts receive the marketing director\'s sign-off?',
            'answers': [
                ('Stack post', False),
                ('Chatter approval', False),
                ('Automated email message', False),
                ('Approval process', True)
            ]
        },
        {
            'text': 'Sales manager at Universal Containers would like to standardize what information sales reps are gathering. Sales reps want recommendations, sales strategies, and to know what key fields need to be completed at each step of the sales process on the opportunity record. What feature should an app builder use to provide this functionality?',
            'answers': [
                ('Workflow', False),
                ('Path', True),
                ('Chatter feed', False),
                ('Global Action', False)
            ]
        },
        {
            'text': 'Cloud Kicks wants to efficiently increase the company\'s adoption of Salesforce while simultaneously moving away from their reliance on spreadsheets. An app builder is given a spreadsheet that everyone is sharing and needs to add it to Salesforce. The object with fields needs to be created and the data inserted simultaneously. Which tool should be used?',
            'answers': [
                ('Import Wizard', False),
                ('Lightning Object Creator', True),
                ('Data Loader', False),
                ('Schema Builder', False)
            ]
        },
        {
            'text': 'Ursa Major Solar (UMS) uses Cases to track customer complaints, an Issue__c object to represent known problems with its solar panels, and a Case_Issue__c junction object to relate known problems to customer complaints. Periodically, UMS conducts audits which require the auditing users to view Case _Issue__c records. Which access levels must be configured to allow UMS users to access Case_Issue__c records?',
            'answers': [
                ('Read-Only access on Case and Issue__c', True),
                ('Read-Only access on Issue__c', False),
                ('Read-Only access on Case only', False),
                ('No access is required', False)
            ]
        },
        {
            'text': 'Cloud Kicks is redefining its entire business process to convert the Manager Notes field from a long text area to a text area. The goal is to encourage managers to be more concise in their comments and stay at 255 characters or less. There is preexisting information in the Manager Notes field that often exceeds the character limit. What will happen to any existing information if the app builder tries to convert the long text area field to a text area?',
            'answers': [
                ('Preexisting information will truncate to the first 255 characters.', True),
                ('Preexisting information will be lost.', False),
                ('Preexisting information will remain even if over 255 characters.', False),
                ('Preexisting information will cause an error.', False)
            ]
        },
                {
            'text': 'Universal Containers uses a private sharing model on Accounts. User A and user B both own Accounts of their own and have both been sent a new account record in an email owned by user C to take a look at. User A is able to open and view the record but user B receives an insufficient privileges error. User A and user B have the same role in the role hierarchy as user. What are the three reasons user A has access but user B is unable to access the record? (Choose 3 answers)',
            'answers': [
                ('User A is on the same account team as user C.', True),
                ('User A and user B have different profiles.', False),
                ('User C has manually shared the record with user A.', True),
                ('User A was granted an additional permission set.', False),
                ('User A is in a public group that has access via a sharing rule.', True)
            ]
        },
        {
            'text': 'Universal Containers wants some enhancements on its Opportunity page layout to improve efficiency and collaboration. Which two solutions should an app builder suggest to help meet these requirements? (Choose 2 answers)',
            'answers': [
                ('Mark stage dependent fields as required on the Opportunity page layout.', True),
                ('Use two Tabs components to separate record information from activities.', False),
                ('Add a Path component with fields and instructions aligning to stages on the Opportunity.', True),
                ('Set up an approval process requiring manager consent at each stage of the Opportunity.', False)
            ]
        },
        {
            'text': 'Universal Containers needs the 18-digit record ID from Opportunity records when exporting data to Excel in order to ensure each record is treated uniquely. What formula should an app builder use to create this new field?',
            'answers': [
                ('ISNUMBER(Id)', False),
                ('CASESAFEID(Id)', True),
                ('TEXT(Id)', False),
                ('VALUE(Id)', False)
            ]
        },
        {
            'text': 'The VP of Sales wants a Chatter post to the All-Sales private group when an opportunity goes to the closed won stage. What two tools should the app builder use to automate this process? (Choose 2 answers)',
            'answers': [
                ('Flow', False),
                ('Process Builder', True),
                ('Big Deal Alert', False),
                ('Workflow', True)
            ]
        },
        {
            'text': 'How should an app builder configure access to a contact\'s Twitter profile for Salesforce mobile app users?',
            'answers': [
                ('Add a formula field to the Contact page layout.', False),
                ('Add an AppExchange Lightning Component to the mobile app.', False),
                ('Add the Twitter component to mobile view Lightning pages.', True),
                ('Add a Twitter Quick Action to the mobile navigation.', False)
            ]
        },
        {
            'text': 'A new app builder on the Cloud Kicks team is getting familiar with relationships in the data model. What functionality would present the app builder a comprehensive view of all relationships in one place?',
            'answers': [
                ('Schema Builder', True),
                ('Lightning Object Creator', False),
                ('Object Manager', False),
                ('Lightning Record Page', False)
            ]
        },
        {
            'text': 'Universal Containers is expecting impacts to operations due to increased demand. The executive team will be reaching out to current customers and want to see the number of open cases for the account and parent account. Which two tools could an app builder combine to display the number of open cases on the account page? (Choose 2 answers)',
            'answers': [
                ('Flow', True),
                ('Workflow', False),
                ('Approval Process', False),
                ('Process Builder', True)
            ]
        },
        {
            'text': 'Cloud Kicks has a shipment date on each shipment that is sent out. Dispatchers need more details on the day and time the shipment was sent out. The app builder needs to change the current field type that is used from Date to Date/Time. What should the app builder be aware of when it comes to data already in the system?',
            'answers': [
                ('The change will be instant', False),
                ('Historical data will be updated to 12:00 timestamp.', True),
                ('The field name will change.', False),
                ('Data loss will be experienced.', False)
            ]
        },
        {
            'text': 'Which three Salesforce functionalities are ignored when processing field updates in workflow rules and approval processes? (Choose 3 answers)',
            'answers': [
                ('Multiple currencies', False),
                ('Field-Level Security', True),
                ('Validation Rules', True),
                ('Record type picklist value assignments', False),
                ('Decimal places and character limits', True)
            ]
        },
                {
            'text': 'Universal Containers uses Contracts for agreements with customers. A sales manager is required to provide approval for contracts and director approval for any contract over $10,000. What should an app builder do?',
            'answers': [
                ('Create an approval process with criteria for contracts over $10,000 and set the approver as the director.', True),
                ('Create an approval process and set the approver as manager.', False),
                ('Create a validation rule that prevents updates while under review.', True),
                ('Create a separate approval step for each sales manager.', False),
            ]
        },
        {
            'text': 'Universal Containers wants sales reps to get permission from their managers before deleting Opportunities. What can be used to meet these requirements?',
            'answers': [
                ('Process Builder with Submit for Approval action.', False),
                ('Approval Process with a triggered Flow process.', False),
                ('Approval Process with Time-Dependent Workflow action.', False),
                ('Two-step Approval Process.', True),
            ]
        },
        {
            'text': 'The Service Manager provided the app builder with color code requirements for case age on open cases. How should an app builder implement this requirement?',
            'answers': [
                ('Formula Field', True),
                ('Quick Action', False),
                ('Custom Button', False),
                ('Lightning Web Component', False),
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
        migrations.RunPython(add_crt5),
    ]

