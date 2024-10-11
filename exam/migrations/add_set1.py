from django.db import migrations,transaction

def add_set1(apps, schema_editor):
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
        exam = Exam.objects.create(title='#ADM-1 Exam')

        # If you want to add the exam to the group (assuming a many-to-many relation):
        group.exams.add(exam)

        # Define questions and answers
        questions_data = [
        # Divide here for set 1
        {
            'text': 'Which tool should an administrator use to review recent configuration changes made in their org?',
            'answers': [
                ('Critical Updates', False),
                ('Debug logs', False),
                ('Setup Audit Trail', True),
                ('Field History Tracking', False)
            ]
        },
        {
            'text': 'DreamHouse Reality just announced its new home concierge offering. This product is unlike anything the company has offered in the past and follows a different business model. What should the administrator configure to meet this requirement?',
            'answers': [
                ('Create a quick action.', False),
                ('Create a new approval process.', False),
                ('Create a new sales process.', True),
                ('Create a new Opportunity product.', False)
            ]
        },
        {
            'text': 'The administrator at Ursa Major Solar has been asked to change the Work Item and Project custom object relationship from a master-detail to a Lookup. Which scenario could prevent the administrator from fulfilling this requirement?',
            'answers': [
                ('A junction object is required to support the lookup.', False),
                ('The lookup field in all the records contains a value.', False),
                ('The Look-Up field is required for Saving Records.', False),
                ('Roll-Up summary field exists on the master object.', True)
            ]
        },
        {
            'text': 'Users at DreamHouse Reality are only allowed to see opportunities they own. Leadership wants an enterprise-wide dashboard of all open opportunities in the pipeline so that users can see how the company is performing at any point in time. How should an administrator create the dashboard without changing any sharing settings?',
            'answers': [
                ('Update the dashboard to folder settings to manager for the sales reps role.', False),
                ('Add a filter to the dashboard to filter the opportunities by owner role.', False),
                ('Build individual dashboards for profiles that need to see the enterprise results.', True),
                ('Create a dashboard with the running User set as someone who can see all Opportunities.', False)
            ]
        },
        {
            'text': 'An administrator at DreamHouse Reality needs to create customized pages for the Salesforce mobile app. Which two types of pages could an administrator build and customize using the Lightning App Builder? Choose 2 Answers.',
            'answers': [
                ('User Page', False),
                ('Dashboard page', False),
                ('App page', True),
                ('Record Page', True)
            ]
        },
        {
            'text': 'An administrator at Cloud Kicks wants to deactivate a user who has left the company. What are two reasons that would prevent a user from being deactivated? Choose 2 answers.',
            'answers': [
                ('The user is part of a territory hierarchy.', False),
                ('The User is in a Custom hierarchy field.', True),
                ('The User is assigned in workflow email alert.', True),
                ('The User is the highest role in the role hierarchy.', False)
            ]
        },
        {
            'text': 'An administrator has been asked to change the data type of an auto number to a text field. What should the administrator be aware of before changing the field?',
            'answers': [
                ('Existing field values will retain unchanged.', True),
                ('Existing field values will be Converted.', False),
                ('Existing field values will be deleted.', False),
                ('Existing auto number field to Text is prevented.', False)
            ]
        },
        {
            'text': 'Sales users at Cloud Kicks are requesting that the data in the Industry field on the Account object displays on the Opportunity page layout. Which type of field should an administrator create to accomplish this?',
            'answers': [
                ('Custom Account Field', False),
                ('Standard Account Field.', False),
                ('Cross Object Formula Field', True),
                ('Master detail relationship Field', False)
            ]
        },
        {
            'text': 'Cloud Kicks wants to track shoe designs by products. Shoe designs should be unable to be deleted, and there can be multiple designs for one product across various stages. Which two steps should the administrator configure to meet this requirement? Choose 2 answers.',
            'answers': [
                ('Create a Custom Object for shoe design.', True),
                ('Configure a Custom Lookup Field for shoe design on the product object.', False),
                ('Add a custom master detail field for shoe design on the Product Object.', True),
                ('Use the Standard Object for designs.', False)
            ]
        },
        {
            'text': 'The VP of Sales at Cloud Kicks is receiving an error message that prevents them from saving an Opportunity. The administrator attempted the same edit without receiving an error. How can the administrator validate the error the user is receiving?',
            'answers': [
                ('Edit the page layout.', False),
                ('View the setup audit trail.', False),
                ('Log in as the user', True),
                ('Review the sharing model', False)
            ]
        },
        {
            'text': 'Clod Kicks has the organization wide defaults for Opportunity set to private. Which two features should the administrator use to open up access to Opportunity records for sales users working on collaborative deals? Choose 2 answers.',
            'answers': [
                ('Sharing set', False),
                ('Role hierarchy', True),
                ('Profiles', False),
                ('Sharing rules', True)
            ]
        },
        {
            'text': 'The administrator at Aw Computing wants Account Details, related list and chatter feeds to each appear on separate tabs when reviewing an account. Which type of page should the administrator create?',
            'answers': [
                ('Lightning app page.', False),
                ('Lightning page Tab.', True),
                ('Lightning record page.', False),
                ('Lightning page Component.', False)
            ]
        },
        {
            'text': 'When a Cloud Kicks Opportunity closes, the company would like to automatically create a renewal opportunity. Which two automation tools should an administrator use to accomplish this request? Choose 2 answers.',
            'answers': [
                ('Approval Process', False),
                ('Flow Builder', True),
                ('Workflow Rule', False),
                ('Process Builder', True)
            ]
        },
        {
            'text': 'Cloud Kicks want to give credit to Opportunity team members based on the level of effort contributed by each person toward each deal. What feature should the administrator use to meet this requirement?',
            'answers': [
                ('Stages', False),
                ('Splits', True),
                ('Queues', False),
                ('List Views', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters has a new flow that automatically sets the field values when a new account is created. That the flow is launched by a process, But the flow is not working properly. What should administrator do to identify the problem?',
            'answers': [
                ('Use the native debug feature in the flow builder.', True),
                ('Review debug logs with the login level.', False),
                ('View the setup audit Trail and review for errors.', False),
                ('Setup Email logs and review the send error log.', False)
            ]
        },
        {
            'text': 'The sales manager at Cloud Kicks approves time off for their employees. They asked the administrator to ensure these requests are seen and responded to by a backup manager while the sales manager is out on vacation. What should administrator use to fulfill the requirement?',
            'answers': [
                ('Delegated approver', True),
                ('Two step Approval process', False),
                ('Approval history related list', False),
                ('Delegated Administrator', False)
            ]
        },
        {
            'text': 'Ursa Major Solar offers amazing experiences for all of its employees. The Employee engagement committee wants to post updates while restricting other employees from posting. What should the administrator create to meet this request?',
            'answers': [
                ('Chatter Stream.', False),
                ('Chatter Broadcast Group', True),
                ('Chatter Recommendations.', False),
                ('Chatter Unlisted Group', False)
            ]
        },
        {
            'text': 'A sales rep at Ursa Major Solar has launched a series of networking events. They are hosting one event per month and want to be able to report on campaign ROI by month and series. How should the administrator set up the Campaign to simplify reporting?',
            'answers': [
                ('Add different record types for the monthly event types.', False),
                ('Create individual Campaigns that all have the same name.', False),
                ('Configure campaign Member Statuses to record which event members attended.', True),
                ('Use Campaign Hierarchy where the monthly events roll up to a parent Campaign.', False)
            ]
        },
        {
            'text': 'Cloud Kicks has a custom object called Shipments. The Company wants to see all the shipment items from an Account page. When an Account is deleted, the shipments should remain. What type of relationship should the administrator make between Shipments and Account?',
            'answers': [
                ('Shipments should have a lookup to Account.', True),
                ('Accounts should have a lookup to Shipments.', False),
                ('Shipments should have a master-detail to Accounts.', False),
                ('Accounts should have a master-detail to Shipments.', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters uses a custom object Invoice to collect customer payment information from an external billing system. The Billing System field needs to be filled on every Invoice record. How should an administrator ensure this requirement?',
            'answers': [
                ('Make the field universally required.', True),
                ('Create a Process Builder to set the field.', False),
                ('Define an approval process for the child.', False),
                ('Require the field on the record type.', False)
            ]
        },
        {
            'text': 'Cloud Kicks has a team of product owners that need a space to share feedback and ideas with just the product team. How should the administrator leverage Salesforce to help the team collaborate?',
            'answers': [
                ('Use Quick Actions to log communication.', False),
                ('Configure a Chatter Public Group.', False),
                ('Create a Chatter Private Group.', True),
                ('Add Activity History to document tasks.', False)
            ]
        },
        {
            'text': 'An analytics user at Cloud Kicks needs Read, Create, and Edit access for objects and should be restricted from deleting any records. What should the administrator do to meet this requirement?',
            'answers': [
                ('Assign the standard System Administrator profile to the analytical user.', False),
                ('Give the user View all access and assign them to the highest role in the role hierarchy.', False),
                ('Create and assign a custom profile with delete access removed for each object.', True),
                ('Create and assign a permission set that includes Read, Create, and Edit access.', True)
            ]
        },
        {
            'text': 'Universal Containers has enabled Data Protection and Privacy for its org. Which page layouts will have the Individual field available for tracking data privacy information?',
            'answers': [
                ('Case and Opportunity', False),
                ('Account and User', True),
                ('Contact, Lead, and Person Account', False),
                ('Individual, User, and Account', False)
            ]
        },
        {
            'text': 'The administrator for Cloud Kicks needs to give access to a new custom object with custom fields to more than one user. Which two options should an administrator use to meet this requirement? Choose 2 answers.',
            'answers': [
                ('Add to manual sharing list', True),
                ('Assign permission set group to Users', False),
                ('Create a Permission Set', True),
                ('Edit organization-wide defaults', False)
            ]
        },
        {
            'text': 'Cloud Kicks wants to update a screen flow so that if the checkbox field High Value Customer is set to true, the first screen is skipped and the user is directed to the second screen. How should the administrator configure the decision element?',
            'answers': [
                ('Use the equals operator and {!$GlobalConstant.True} as the value.', True),
                ('Use the equals operator and “High Value Customer” as the value.', False),
                ('Use the contains operator and {!$GlobalConstant.False} as the value.', False),
                ('Use the contains operator and “High Value Customer” as the value.', False)
            ]
        },
        {
            'text': 'The administrator at Ursa Major Solar imported records into an object by mistake. Which two tools should be used to undo this import? Choose 2 answers.',
            'answers': [
                ('Weekly Data Export', False),
                ('Mass Delete Records', True),
                ('Data Loader', True),
                ('Data Import Wizard', False)
            ]
        },
        {
            'text': 'Ursa Major Solar wants to assist users with a guided expense report process to simplify submissions, routing, and authorizations. Which two tools should an administrator use to build this solution? Choose 2 answers.',
            'answers': [
                ('Validation Rule', False),
                ('Flow Builder', True),
                ('Approval Process', True),
                ('Quick Action', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters has asked an administrator to ensure that when a contact with a title of CEO is created, the contact’s account record gets updated with the CEO’s name. Which feature should an administrator use to implement this request?',
            'answers': [
                ('Quick Action', False),
                ('Workflow Rule', False),
                ('Process Builder', True),
                ('Validation Rule', False)
            ]
        },
        {
            'text': 'New leads need be routed to the correct Sales person based on the lead address. What should an administrator use?',
            'answers': [
                ('Configure validation rule', False),
                ('Use lead assignment rule', True),
                ('Create a formula field', False),
                ('Assign with an escalation rule', False)
            ]
        },
        {
            'text': 'Users at Universal Containers would like to visually see the sales stages on an Opportunity page. The administrator is configuring path for Opportunities. Which is an important consideration for path configuration?',
            'answers': [
                ('Kanban views for Path must be configured manually.', False),
                ('The Owner field can be edited in the key fields Panel.', False),
                ('Celebrations are unable to be added to a path.', False),
                ('Path can include guidance and key fields for each stage.', True)
            ]
        },
        {
            'text': 'Which tool should an administrator use to identify and fix potential session vulnerabilities?',
            'answers': [
                ('Field History Tracking', False),
                ('Setup Audit Trail', False),
                ('Security Health Check', True),
                ('Organization-Wide Defaults', False)
            ]
        },
        {
            'text': 'Which three items are available in the mobile navigation menu? Choose 3 answers.',
            'answers': [
                ('Lightning App Pages', False),
                ('Lightning Home Page', False),
                ('Chatter', True),
                ('Utility Bar', True),
                ('Dashboards', True)
            ]
        },
        {
            'text': 'Support agents at Cloud Kicks are spending too much time finding resources to solve cases. The agents need a more efficient way to find documentation and similar cases from the Case page layout. How should an administrator meet this requirement?',
            'answers': [
                ('Create a custom object to capture popular case resolutions.', False),
                ('Use an interview flow to capture Case details.', False),
                ('Direct users to Global Search to look for similar cases.', True),
                ('Configure Knowledge with articles and data categories.', False)
            ]
        },
        {
            'text': 'Dream House Realty needs to use consistent picklist values in the category field on accounts and cases, with values respective to record types. Choose 2 options.',
            'answers': [
                ('Multi-select picklist', False),
                ('Dependent picklist', False),
                ('Global picklist', True),
                ('Custom picklist', True)
            ]
        },
        {
            'text': 'Universal Containers (UC) customers have provided feedback that their support cases are not being responded to quickly enough. UC wants to send all unassigned Cases that have been open for more than two hours to an urgent Case queue and alert the support manager. Which feature should an administrator configure to meet this requirement?',
            'answers': [
                ('Case Escalation Rules', True),
                ('Case Dashboard Refreshes', False),
                ('Case Scheduled Report', False),
                ('Case Assignment Rules', False)
            ]
        },
        {
            'text': 'An administrator at Universal Container needs an automated way to delete records based on field values. What automated solution should the administrator use?',
            'answers': [
                ('Workflow', False),
                ('Process Builder', False),
                ('Flow Builder', True),
                ('Automation Studio', False)
            ]
        },
        {
            'text': 'The Human resources department at Northern Trail outfitters wants employees to provide feedback about the manager using a custom object in Salesforce. It is important that managers are unable to see the feedback records from their staff. How should an administrator configure the custom object to meet this requirement?',
            'answers': [
                ('Uncheck grant access using Hierarchies.', False),
                ('Define a criteria-based sharing rule.', True),
                ('Set the default external access to private.', False),
                ('Configure an owner-based sharing rule.', False)
            ]
        },
        {
            'text': 'The administrator at Cloud Kicks has been asked to change the company’s Shoe style field to prevent users from selecting more than one style on a record. Which two steps should an administrator do to accomplish this? Choose 2 answers',
            'answers': [
                ('Reactivate the appropriate Shoe Style values after the field type changes.', False),
                ('Select the “Choose only one value” checkbox on the picklist field.', True),
                ('Back-up the Shoe Style values in existing records.', False),
                ('Change the field type from a multi-select picklist field to a picklist field.', True)
            ]
        },
        {
            'text': 'Universal Containers administrator has been asked to create a many-to-many relationship between two existing custom objects. Which two steps should the administrator take when enabling the many-to-many relationship? Choose 2 answers',
            'answers': [
                ('Create a junction with a custom object.', True),
                ('Create two master detail relationships on the new object.', True),
                ('Create two lookup relationships on the new object.', False),
                ('Create URL fields on a custom object.', False)
            ]
        },
        {
            'text': 'A user at Universal Containers left the company. The administrator needs to create a new user for their replacement, but they have assigned all available user licenses. What should the administrator do to free up user licenses for the new users?',
            'answers': [
                ('Deactivate the former employee’s user record.', False),
                ('Delete the former employee’s user record.', False),
                ('Freeze the former employee’s user record.', False),
                ('Change the former user’s record to the new user.', True)
            ]
        },
        {
            'text': 'The events manager at Dream House Realty has a hot lead from a successful open house that needs to become a contact with an associated opportunity. How should this be accomplished from the campaign keeping the associated campaign member history?',
            'answers': [
                ('Delete the lead and create a new contact and opportunity.', False),
                ('Clone the lead and convert the cloned record to a contact.', False),
                ('Convert the lead from the campaign member detail page.', True),
                ('Add a contact from a campaign member detail page.', False)
            ]
        },
        {
            'text': 'Cloud Kicks has the organization-wide sharing default set to private on the shoe object. The sales manager should be able to view a report containing shoe records for all of the sales reps on their team. Which 3 items should the administrator configure to provide appropriate access to the report? Choose 3 answers',
            'answers': [
                ('Custom report type.', False),
                ('Folder access', True),
                ('Report subscription', False),
                ('Field level security', True),
                ('Role hierarchy', True)
            ]
        },
        {
            'text': 'The sales team at Ursa Major Solar has asked the administrator to automate an outbound message. What should the administrator utilize to satisfy the request?',
            'answers': [
                ('Process builder', False),
                ('Task assignment', False),
                ('Workflow rule', True),
                ('Flow builder', False)
            ]
        },
        {
            'text': 'Sales managers would like to know what could be implemented to surface important values based on the stage of the opportunity. Which tool should an administrator use to meet the requirement?',
            'answers': [
                ('Dynamic forms', False),
                ('Path key fields', True),
                ('Opportunity processes', False),
                ('Workflow rules', False)
            ]
        },
        {
            'text': 'Cloud Kicks needs to ensure appropriate shipping details are used in orders. Reps should have a streamlined solution to update the shipping address on selected orders associated with an account when the shipping address is changed on the account. How should the administrator deliver this requirement?',
            'answers': [
                ('An autolaunched flow on the order page that updates all open orders’ shipping addresses whenever the account shipping address changes.', False),
                ('An autolaunched flow on the account page that updates all open orders’ shipping addresses whenever the account shipping address changes.', True),
                ('A screen flow on the order page that lets the reps choose the updated account shipping address in all open associated orders.', False),
                ('A screen flow on the account page that lets the reps choose the updated account shipping address in all open associated orders.', False)
            ]
        },
        {
            'text': 'The administrator at Universal Containers has a screen flow that helps users create new leads. When the lead source is “Search Engine”, the administrator needs to require the user to choose a specific search engine from a picklist. If the lead source is not “Search Engine”, this picklist should be hidden. How should the administrator complete this requirement?',
            'answers': [
                ('Assign a decision element to direct the user to a second screen to hold specific search engine only when a lead source is “Search Engine”.', True),
                ('Use an assignment element, one for when lead source is “Search Engine” and one for everything else.', False),
                ('Create a picklist for specific search engine, and set conditional visibility so that it is only shown when lead source is “Search Engine”.', False),
                ('Configure a picklist for specific search engine, and use a validation rule to conditionally show only when lead source is “Search Engine”.', False)
            ]
        },
        {
            'text': 'The administrator at Cloud Kicks is trying to debug a screen flow that creates contacts. One of the variables in the flow is missing on the debug screen. What could cause this issue?',
            'answers': [
                ('The available for input checkbox was unchecked.', False),
                ('The flow is an inactive version.', False),
                ('The field type is unsupported by debugging.', True),
                ('The available for output checkbox was unchecked.', False)
            ]
        },
        {
            'text': 'Cloud Kicks executives have noticed the opportunity Expected Revenue Field displays incorrect values. How should the administrator correct this?',
            'answers': [
                ('Update the expected revenue associated with the stage.', False),
                ('Adjust the forecast category associated with the stage.', False),
                ('Modify the closed won value associated with the stage.', False),
                ('Change the probability associated with the stage.', True)
            ]
        },
        {
            'text': 'The administrator at Cloud Kicks has been told that users are unable to add repeating tasks in Salesforce. Which two solutions should the administrator use to ensure users are able to do this? Choose 2 Answers',
            'answers': [
                ('Enable creation of Recurring Tasks in Activity Settings', True),
                ('Disable shares Activities.', False),
                ('Add create Recurring series of Tasks field on Page Layouts', True),
                ('Turn on Task Notifications service.', False)
            ]
        },
        {
            'text': 'An administrator at Northern Trail Outfitters is unable to add a new user in Salesforce. What could cause this issue?',
            'answers': [
                ('The Username is not a corporate email address.', False),
                ('The username is less than 80 characters.', False),
                ('The Username is a fake email address.', False),
                ('The Username is already in use.', True)
            ]
        },
        {
            'text': 'The DreamHouse Realty team has a master-detail relationship set up with open house as the parent object and visitors as the child object. What type of field should the administrator add to the open house object to track the number of visitors?',
            'answers': [
                ('Roll-up Summary.', True),
                ('Multi-select Picklist', False),
                ('Cross-object formula', False),
                ('Indirect lookup', False)
            ]
        },
        {
            'text': 'The administrator at Cloud Kicks deleted a custom field but realized there is a business unit that still uses the field. What should an administrator take into consideration when undeleting the field?',
            'answers': [
                ('The field needs to be re-added to reports.', False),
                ('The field history will remain deleted.', False),
                ('The field needs to be restored from the recycle bin.', True),
                ('The field needs to be re-added to page Layouts.', False)
            ]
        },
        {
            'text': 'An administrator needs to create a one-to-many relationship between two objects with limited access to child records. What type of field should the administrator use?',
            'answers': [
                ('Roll-up summary', False),
                ('Master-detail field', True),
                ('Cross Object formula', False),
                ('Lookup field', True)
            ]
        },
        {
            'text': 'Northern Trail Outfitters wants to use contract hierarchy in its org to display contact association. What should the administrator take into consideration regarding the contact hierarchy?',
            'answers': [
                ('Contacts displayed in the contact hierarchy are limited to record-level access by User.', True),
                ('Contact Hierarchy is limited to only active contacts.', False),
                ('Contact Hierarchy is visible on Account Detail Pages only.', False),
                ('Contacts in the hierarchy are limited to only user’s contacts.', False)
            ]
        },
        {
            'text': 'The administrator at Ursa Major Solar has created a custom report type and built a report for the sales operation team. However, none of the users are able to access the report. Which two options could cause this issue?',
            'answers': [
                ('The custom report type is in development.', False),
                ('The user’s profile is missing view access.', True),
                ('The org has reached its limit of custom report types.', False),
                ('The report is saved in a private folder.', True)
            ]
        },
        {
            'text': 'Sales reps at Ursa Solar are having difficulty managing deals. The leadership team has asked the administrator to help sales reps prioritize and close more deals. What should the administrator use to help sales reps prioritize and close more deals?',
            'answers': [
                ('Einstein Opportunity Scoring', True),
                ('Einstein Lead Scoring', False),
                ('Einstein Search Personalization', False),
                ('Einstein Activity Capture', False)
            ]
        },
        {
            'text': 'The administrator for AW Computing is working with a user who is having trouble logging in to Salesforce. What should the administrator do to identify why the user is unable to log in?',
            'answers': [
                ('Review the Login history.', True),
                ('Review the Security token.', False),
                ('Review the password history.', False),
                ('Review the Password policies.', False)
            ]
        },
        {
            'text': 'Once an opportunity reaches the negotiation stage at Cloud Kicks, the Amount field becomes required for sales users. Sales managers need to be able to move opportunities into this stage without knowing the amount. How should the administrator require this field during the negotiation stage for sales users but allow their managers to make changes?',
            'answers': [
                ('Configure a validation rule to meet the criteria.', True),
                ('Make the field required for all users.', False),
                ('Create a formula field to fill in the field for managers.', False),
                ('Assign the administrator profile to the managers.', False)
            ]
        },
        {
            'text': 'Northern Trail Outfitters has hired interns to enter Leads into Salesforce and has requested a way to identify these new records from existing Leads. What approach should an administrator take to meet this requirement?',
            'answers': [
                ('Define a record type and assign it to the interns.', True),
                ('Set up a Web-to-Lead form the interns use.', False),
                ('Create a separate Lead Lightning App.', False),
                ('Update the active Lead Assignment Rules.', False)
            ]
        },
        {
            'text': 'The Cloud Kicks sales manager wants to boost productivity by providing insights at the start of each day. Which three sales-specific standard Lightning components should the administrator add to the homepage to meet this requirement?',
            'answers': [
                ('Activities', True),
                ('Path', False),
                ('Assistant', False),
                ('Key Deals', True),
                ('Performance chart.', True)
            ]
        },
        {
            'text': 'What are three settings an administrator should configure to make it easy for approvers to respond to approval requests?',
            'answers': [
                ('Enable the organization’s Email approval response setting.', True),
                ('Add the Items to approve component to the approvers home page.', True),
                ('Update the organization’s Chatter setting to allow approvals.', True),
                ('Specify initial submission actions within the approval process.', False),
                ('Create a flow to automatically approve all records.', False)
            ]
        },
        {
            'text': 'New Leads need to be routed to the correct salesperson based on the lead address. How should the administrator configure this requirement?',
            'answers': [
                ('Use lead assignment rules.', True),
                ('Create a formula field.', False),
                ('Assign with an escalation rule.', False),
                ('Configure a validation rule.', False)
            ]
        },
        {
            'text': 'An administrator at DreamHouse Realty wants an easier way to assign an agent capacity and skill set. Which feature should the administrator enable to meet this requirement?',
            'answers': [
                ('Omni-Channel', True),
                ('Knowledge Management.', False),
                ('Escalation Rules', False),
                ('Territory Management.', False)
            ]
        },
        {
            'text': 'Universal Container has a contact Lightning record page with a component that shows LinkedIn data. The sales team would like to only show this component to sales users when they are on their mobile phones. Which two options should the administrator use to achieve this?',
            'answers': [
                ('Filter the component visibility with Form Factor = phone', True),
                ('Filter the component visibility with User > Profile > name = sales User.', True),
                ('Filter the component visibility with view = Mobile/Tablet.', False),
                ('Filter the component visibility with User > Role > Name = Sales User.', False)
            ]
        },
        {
            'text': 'At Cloud Kicks, sales reps use discounts on the opportunity record to help win sales on products. When an opportunity is won, they then have to manually apply the discount to the related opportunity products. The sales manager has asked if there is a way to automate this time-consuming task. What should the administrator use to deliver this requirement?',
            'answers': [
                ('Flow Builder', True),
                ('Approval Process', False),
                ('Prebuilt Macro.', False),
                ('Formula field', False)
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
        migrations.RunPython(add_set1, atomic=False),
    ]