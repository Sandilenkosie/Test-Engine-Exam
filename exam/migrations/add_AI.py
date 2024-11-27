from django.db import migrations, transaction

def add_AI(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')
    Group = apps.get_model('exam', 'Group')

    with transaction.atomic():
        # Create or get the Group for the exam
        group, created = Group.objects.get_or_create(
            name='AI-Associate Exams',
            defaults={'description': 'Group for AI-Associate related exams'}
        )

        # Create an exam instance and associate it with the group
        exam = Exam.objects.create(title='#AI-Associate Exam')

        # Add the exam to the group
        group.exams.add(exam)

        # Define the questions and answers data
        questions_data = [
            {
                'text': 'What is a benefit of a diverse, balanced, and large dataset?',
                'answers': [
                    ('Training time', False),
                    ('Data privacy', False),
                    ('Model accuracy', True)
                ]
            },
            {
                'text': 'What are the three commonly used examples of AI in CRM?',
                'answers': [
                    ('Predictive scoring, reporting, Image classification', False),
                    ('Predictive scoring, forecasting, recommendations', True),
                    ('Einstein Bots, face recognition, recommendations', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to optimize its business operations by incorporating AI into its CRM. What should the company do first to prepare its data for use with AI?',
                'answers': [
                    ('Remove biased data.', False),
                    ('Determine data availability.', True),
                    ('Determine data outcomes.', False)
                ]
            },
            {
                'text': 'A healthcare company implements an algorithm to analyze patient data and assist in medical diagnosis. Which primary role does data Quality play in this AI application?',
                'answers': [
                    ('Enhanced accuracy and reliability of medical predictions and diagnoses', True),
                    ('Ensured compatibility of AI algorithms with the system\'s Infrastructure', False),
                    ('Reduced need for healthcare expertise in interpreting AI outputs', False)
                ]
            },
            {
                'text': 'What are some of the ethical challenges associated with AI development?',
                'answers': [
                    ('Potential for human bias in machine learning algorithms and the lack of transparency in AI decision-making processes', True),
                    ('Implicit transparency of AI systems, which makes it easy for users to understand and trust their decisions', False),
                    ('Inherent neutrality of AI systems, which eliminates any potential for human bias in decision making', False)
                ]
            },
            {
                'text': 'Cloud Kicks discovered multiple variations of state and country values in contact records. Which data quality dimension is affected by this issue?',
                'answers': [
                    ('Usage', False),
                    ('Accuracy', False),
                    ('Consistency', True)
                ]
            },
            {
                'text': 'How is natural language processing (NLP) used in the context of AI capabilities?',
                'answers': [
                    ('To cleanse and prepare data for AI implementations', False),
                    ('To interpret and understand programming language', False),
                    ('To understand and generate human language', True)
                ]
            },
            {
                'text': 'What is an example of Salesforce\'s Trusted AI Principle of Inclusivity in practice?',
                'answers': [
                    ('Testing models with diverse datasets', True),
                    ('Striving for model explainability', False),
                    ('Working with human rights experts', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to create a custom service analytics application to analyze cases in Salesforce. The application should rely on accurate data to ensure efficient case resolution. Which data quality dimension is essential for this custom application?',
                'answers': [
                    ('Consistency', True),
                    ('Duplication', False),
                    ('Age', False)
                ]
            },
            {
                'text': 'What should organizations do to ensure data quality for their AI initiatives?',
                'answers': [
                    ('Collect and curate high-quality data from reliable sources.', True),
                    ('Rely on AI algorithms to automatically handle data quality issues.', False),
                    ('Prioritize model fine-tuning over data quality improvements.', False)
                ]
            },
            {
                'text': 'Which Einstein capability uses emails to create content for Knowledge articles?',
                'answers': [
                    ('Generate', True),
                    ('Discover', False),
                    ('Predict', False)
                ]
            },
            {
                'text': 'Which type of bias results from data being labeled according to stereotypes?',
                'answers': [
                    ('Association', False),
                    ('Societal', True),
                    ('Interaction', False)
                ]
            },
            {
                'text': 'Salesforce defines bias as using a person\'s Immutable traits to classify them or market to them. Which potentially sensitive attribute is an example of an immutable trait?',
                'answers': [
                    ('Financial status', True),
                    ('Nickname', False),
                    ('Email address', False)
                ]
            },
            {
                'text': 'Cloud Kicks relies on data analysis to optimize its product recommendation; however, CK encounters a recurring issue of incomplete customer records, with missing contact information and incomplete purchase histories. How will this incomplete data quality impact the company\'s operations?',
                'answers': [
                    ('The accuracy of product recommendations is hindered.', True),
                    ('The diversity of product recommendations is improved.', False),
                    ('The response time for product recommendations is stalled.', False)
                ]
            },
            {
                'text': 'What are some key benefits of AI in improving customer experiences in CRM?',
                'answers': [
                    ('Improves CRM security protocols, safeguarding sensitive customer data from potential breaches and threats.', False),
                    ('Streamlines case management by categorizing and tracking customer support cases, identifying topics, and summarizing case resolutions.', True),
                    ('Fully automates the customer service experience, ensuring seamless automated interactions with customers.', False)
                ]
            },
            {
                'text': 'How does an organization benefit from using AI to personalize the shopping experience of online customers?',
                'answers': [
                    ('Customers are more likely to share personal information with a site that personalizes their experience.', False),
                    ('Customers are more likely to be satisfied with their shopping experience.', True),
                    ('Customers are more likely to visit competitor sites that personalize their experience.', False)
                ]
            },
            {
                'text': 'Cloud Kicks is testing a new AI model. Which approach aligns with Salesforce\'s Trusted AI Principle of Inclusivity?',
                'answers': [
                    ('Test only with data from a specific region or demographic to limit the risk of data leaks.', False),
                    ('Rely on a development team with uniform backgrounds to assess the potential societal implications of the model.', False),
                    ('Test with diverse and representative datasets appropriate for how the model will be used.', True)
                ]
            },
            {
                'text': 'Cloud Kicks wants to develop a solution to predict customers\' product interests based on historical data. The company found that employees from one region use a text field to capture the product category, while employees from all other locations use a picklist. Which data quality dimension is affected in this scenario?',
                'answers': [
                    ('Completeness', False),
                    ('Accuracy', False),
                    ('Consistency', True)
                ]
            },
            {
                'text': 'Cloud Kicks wants to implement AI features on its Salesforce platform but has concerns about potential ethical and privacy challenges. What should they consider doing to minimize potential AI bias?',
                'answers': [
                    ('Integrate AI models that auto-correct biased data.', False),
                    ('Implement Salesforce\'s Trusted AI Principles.', True),
                    ('Use demographic data to identify minority groups.', False)
                ]
            },
            {
                'text': 'Which features of Einstein enhance sales efficiency and effectiveness?',
                'answers': [
                    ('Opportunity List View, Lead List View, Account List view', False),
                    ('Opportunity Scoring, Opportunity List View, Opportunity Dashboard', False),
                    ('Opportunity Scoring, Lead Scoring, Account Insights', True)
                ]
            },
            {
                'text': 'Cloud Kicks implements a new product recommendation feature for its shoppers that recommends shoes of a given color to display to customers based on the color of the products from their purchase history. Which type of bias is most likely to be encountered in this scenario?',
                'answers': [
                    ('Confirmation', True),
                    ('Survivorship', False),
                    ('Societal', False)
                ]
            },
            {
                'text': 'What is the main focus of the Accountability principle in Salesforce\'s Trusted AI Principles?',
                'answers': [
                    ('Safeguarding fundamental human rights and protecting sensitive data', False),
                    ('Taking responsibility for one\'s actions toward customers, partners, and society', True),
                    ('Ensuring transparency in AI-driven recommendations and predictions', False)
                ]
            },
            {
                'text': 'What is a sensitive variable that can lead to bias?',
                'answers': [
                    ('Education level', False),
                    ('Country', False),
                    ('Gender', True)
                ]
            },
            {
                'text': 'A marketing manager wants to use AI to better engage their customers. Which functionality provides the best solution?',
                'answers': [
                    ('Journey Optimization', False),
                    ('Bring Your Own Model', False),
                    ('Einstein Engagement', True)
                ]
            },
            {
                'text': 'A Salesforce administrator creates a new field to capture an order\'s destination country. Which field type should they use to ensure data quality?',
                'answers': [
                    ('Text', False),
                    ('Picklist', True),
                    ('Number', False)
                ]
            },
            {
                'text': 'A customer using Einstein Prediction Builder is confused about why a certain prediction was made. Following Salesforce\'s Trusted AI Principle of Transparency, which customer information should be accessible on the Salesforce Platform?',
                'answers': [
                    ('An explanation of how Prediction Builder works and a link to Salesforce\'s Trusted AI Principles', False),
                    ('An explanation of the prediction\'s rationale and a model card that describes how the model was created', True),
                    ('A marketing article of the product that clearly outlines the product\'s capabilities and features', False)
                ]
            },
            {
                'text': 'How does the "right of least privilege" reduce the risk of handling sensitive personal data?',
                'answers': [
                    ('By limiting how many people have access to data', True),
                    ('By reducing how many attributes are collected', False),
                    ('By applying data retention policies', False)
                ]
            },
            {
                'text': 'What is the best method to safeguard customer data privacy?',
                'answers': [
                    ('Automatically anonymize all customer data.', False),
                    ('Track customer data consent preferences.', True),
                    ('Archive customer data on a recurring schedule.', False)
                ]
            },
            {
                'text': 'What is the key difference between generative and predictive AI?',
                'answers': [
                    ('Generative AI creates new content based on existing data and predictive AI analyzes existing data.', True),
                    ('Generative AI finds content similar to existing data and predictive AI analyzes existing data.', False),
                    ('Generative AI analyzes existing data and predictive AI creates new content based on existing data.', False)
                ]
            },
            {
                'text': 'What is a key benefit of effective interaction between humans and AI systems?',
                'answers': [
                    ('Leads to more informed and balanced decision making', True),
                    ('Alerts humans to the presence of biased data', False),
                    ('Reduces the need for human involvement', False)
                ]
            },
            {
                'text': 'What is a key characteristic of machine learning in the context of AI capabilities?',
                'answers': [
                    ('Uses algorithms to learn from data and make decisions', True),
                    ('Relies on preprogrammed rules to make decisions', False),
                    ('Can perfectly mimic human intelligence and decision-making', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to ensure that multiple records for the same customer are removed in Salesforce. Which feature should be used to accomplish this?',
                'answers': [
                    ('Duplicate management', True),
                    ('Trigger deletion of old records', False),
                    ('Standardized field names', False)
                ]
            },
            {
                'text': 'An administrator at Cloud Kicks wants to ensure that a field is set up on the customer record so their preferred name can be captured. Which Salesforce field type should the administrator use to accomplish this?',
                'answers': [
                    ('Multi-Select Picklist', False),
                    ('Text', True),
                    ('Rich Text Area', False)
                ]
            },
            {
                'text': 'What is a possible outcome of poor data quality?',
                'answers': [
                    ('AI models maintain accuracy but have slower response times.', False),
                    ('Biases in data can be inadvertently learned and amplified by AI systems.', True),
                    ('AI predictions become more focused and less robust.', False)
                ]
            },
            {
                'text': 'To avoid introducing unintended bias to an AI model, which type of data should be omitted?',
                'answers': [
                    ('Transactional', False),
                    ('Engagement', False),
                    ('Demographic', True)
                ]
            },
            {
                'text': 'What is an implication of user consent in regard to AI data privacy?',
                'answers': [
                    ('AI ensures complete data privacy by automatically obtaining user consent.', False),
                    ('AI infringes on privacy when user consent is not obtained.', True),
                    ('AI operates Independently of user privacy and consent.', False)
                ]
            },
            {
                'text': 'How does data quality impact the trustworthiness of AI-driven decisions?',
                'answers': [
                    ('The use of both low-quality and high-quality data can improve the accuracy and reliability of AI-driven decisions.', False),
                    ('High-quality data improves the reliability and credibility of AI-driven decisions, fostering trust among users.', True),
                    ('Low-quality data reduces the risk of overfitting the model, improving the trustworthiness of the predictions.', False)
                ]
            },
            {
                'text': 'Cloud Kicks learns of complaints from customers who are receiving too many sales calls and emails. Which data quality dimension should be assessed to reduce these communication inefficiencies?',
                'answers': [
                    ('Duplication', True),
                    ('Usage', False),
                    ('Consent', False)
                ]
            },
            {
                'text': 'A developer is tasked with selecting a suitable dataset for training an AI model in Salesforce to accurately predict current customer behavior. What is a crucial factor that the developer should consider during selection?',
                'answers': [
                    ('Number of variables in the dataset', False),
                    ('Size of the dataset', True),
                    ('Age of the dataset', False)
                ]
            },
            {
                'text': 'What is machine learning?',
                'answers': [
                    ('AI that can grow its intelligence', False),
                    ('AI that creates new content', False),
                    ('A data model used in Salesforce', True)
                ]
            },
            {
                'text': 'A service leader wants to use AI to help customers resolve their issues quicker in a guided self-serve application. Which Einstein functionality provides the best solution?',
                'answers': [
                    ('Case Classification', False),
                    ('Bots', True),
                    ('Recommendation', False)
                ]
            },
            {
                'text': 'Why is it critical to consider privacy concerns when dealing with AI and CRM data?',
                'answers': [
                    ('Ensures compliance with laws and regulations', True),
                    ('Confirms the data is accessible to all users', False),
                    ('Increases the volume of data collected', False)
                ]
            },
            {
                'text': 'Which action should be taken to develop and implement trusted generated AI with Salesforce’s safety guideline in mind?',
                'answers': [
                    ('Develop right-sized models to reduce our carbon footprint.', False),
                    ('Create guardrails that mitigate toxicity and protect PII.', True),
                    ('Be transparent when AI has created and automatically delivered content.', False)
                ]
            },
            {
                'text': 'What is a potential source of bias in training data for AI models?',
                'answers': [
                    ('The data is collected in area time from sources systems.', False),
                    ('The data is skewed toward a particular demographic or source.', True),
                    ('The data is collected from a diverse range of sources and demographics.', False)
                ]
            },
            {
                'text': 'In the context of Salesforce’s Trusted AI Principles, what does the principle of Empowerment primarily aim to achieve?',
                'answers': [
                    ('Empower users of all skill levels to build AI applications with clicks, not code.', True),
                    ('Empower users to contribute to the growing body of knowledge of leading AI research.', False),
                    ('Empower users to solve challenging technical problems using neural networks.', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to use Einstein Prediction Builder to determine a customer’s likelihood of buying specific products; however, data quality is a concern. How can data quality be assessed?',
                'answers': [
                    ('Build a Data Management Strategy.', False),
                    ('Build reports to explore the data quality.', False),
                    ('Leverage data quality apps from AppExchange.', True)
                ]
            },
            {
                'text': 'What should be done to prevent bias from entering an AI system when training it?',
                'answers': [
                    ('Use alternative assumptions.', False),
                    ('Import diverse training data.', True),
                    ('Include Proxy variables.', False)
                ]
            },
            {
                'text': 'What is a key consideration regarding data quality in AI implementation?',
                'answers': [
                    ('Techniques for customizing AI features in Salesforce.', False),
                    ('Data’s role in training and fine-tuning Salesforce AI models.', True),
                    ('Integration process of AI models with Salesforce workflows.', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to use AI to enhance its sales processes and customer support. Which capability should they use?',
                'answers': [
                    ('Dashboard of Current Leads and Cases.', False),
                    ('Sales Path and Automation Case Escalations.', False),
                    ('Einstein Lead Scoring and Case Classification.', True)
                ]
            },
            {
                'text': 'Which statement exemplifies Salesforce’s honesty guideline when training AI models?',
                'answers': [
                    ('Minimize the AI models carbon footprint and environmental impact during training.', False),
                    ('Ensure appropriate consent and transparency when using AI-generated responses.', True),
                    ('Control bias, toxicity, and harmful content with embedded guardrails and guidance.', False)
                ]
            },
            {
                'text': 'What is a benefit of data quality and transparency as it pertains to bias in generated AI?',
                'answers': [
                    ('Chances of bias are mitigated', True),
                    ('Chances of bias are aggravated', False),
                    ('Chances of bias are removed', False)
                ]
            },
            {
                'text': 'A business analyst (BA) wants to improve business by enhancing their sales processes and customer support. Which AI application should the BA use to meet their needs?',
                'answers': [
                    ('Sales data cleansing and customer support data governance', False),
                    ('Machine learning models and chatbot predictions', False),
                    ('Lead scoring, opportunity forecasting, and case classification', True)
                ]
            },
            {
                'text': 'Cloud Kicks uses Einstein to generate predictions but is not seeing accurate results. What is a potential reason for this?',
                'answers': [
                    ('Poor data quality', True),
                    ('The wrong product', False),
                    ('Too much data', False)
                ]
            },
            {
                'text': 'A data quality expert at Cloud Kicks wants to ensure that each new contact contains at least an email address or phone number. Which feature should they use to accomplish this?',
                'answers': [
                    ('Autofill', False),
                    ('Duplicate matching rule', False),
                    ('Validation rule', True)
                ]
            },
            {
                'text': 'Cloud Kicks wants to develop a solution to predict customers’ interest based on historical data. The company found that employee regions use a text field to capture the product category, while employees from other locations use a picklist. Which dimension of data quality is affected in this scenario?',
                'answers': [
                    ('Accuracy', False),
                    ('Consistency', True),
                    ('Completeness', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to use an AI model to predict the demand for shoes using historical data on sales and regional characteristics. What is an essential data quality dimension to achieve this goal?',
                'answers': [
                    ('Reliability', True),
                    ('Volume', False),
                    ('Age', False)
                ]
            },
            {
                'text': 'A sales manager wants to improve their processes using AI in Salesforce. Which application of AI would be most beneficial?',
                'answers': [
                    ('Lead scoring and opportunity forecasting', True),
                    ('Sales dashboards and reporting', False),
                    ('Data modeling and management', False)
                ]
            },
            {
                'text': 'How does AI with CRM help sales representatives better understand previous customer interactions?',
                'answers': [
                    ('Creates, localizes, and translates product descriptions', False),
                    ('Triggers personalized service replies', False),
                    ('Provides call summaries', True)
                ]
            },
            {
                'text': 'What is the most likely impact that high-quality data will have on customer relationships?',
                'answers': [
                    ('Increased brand loyalty', False),
                    ('Higher customer acquisition costs', False),
                    ('Improved customer trust and satisfaction', True)
                ]
            },
            {
                'text': 'What is the role of Salesforce Trusted AI principles in the context of CRM systems?',
                'answers': [
                    ('Guiding ethical and responsible use of AI', True),
                    ('Providing a framework for AI data model accuracy', False),
                    ('Outlining the technical specifications for AI integration', False)
                ]
            },
            {
                'text': 'What role does data quality play in the ethical use of AI applications?',
                'answers': [
                    ('High-quality data is essential for ensuring unbiased and fair AI decisions, promoting ethical use, and preventing discrimination.', True),
                    ('High-quality data ensures the process of demographic attributes required for personalized campaigns.', False),
                    ('Low-quality data reduces the risk of unintended bias as the data is not overfitted to demographic groups.', False)
                ]
            },
            {
                'text': 'What can bias in AI algorithms in CRM lead to?',
                'answers': [
                    ('Personalization and target marketing changes', False),
                    ('Advertising cost increases', False),
                    ('Ethical challenges in CRM systems', True)
                ]
            },
            {
                'text': 'What is an example of ethical debt?',
                'answers': [
                    ('Violating a data privacy law and failing to pay fines', False),
                    ('Launching an AI feature after discovering a harmful bias', True),
                    ('Delaying an AI product launch to retrain an AI data model', False)
                ]
            },
            {
                'text': 'A consultant conducts a series of Consequence Scanning workshops to support testing diverse datasets. Which Salesforce Trusted AI Principle is being practiced?',
                'answers': [
                    ('Transparency', False),
                    ('Inclusivity', True),
                    ('Accountability', False)
                ]
            },
            {
                'text': 'A financial institution plans a campaign for preapproved credit cards. How should they implement Salesforce’s Trusted AI Principle of Transparency?',
                'answers': [
                    ('Communicate how risk factors such as credit score can impact customer eligibility.', False),
                    ('Flag sensitive variables and their proxies to prevent discriminatory lending practices.', True),
                    ('Incorporate customer feedback into the model’s continuous training.', False)
                ]
            },
            {
                'text': 'Cloud Kicks wants to decrease the workload for its customer care agents by implementing a chatbot on its website that partially deflects incoming cases by answering frequently asked questions. Which field of AI is most suitable for this scenario?',
                'answers': [
                    ('Natural language processing', True),
                    ('Computer vision', False),
                    ('Predictive analytics', False)
                ]
            },
            {
                'text': 'What are the key components of the data quality standard?',
                'answers': [
                    ('Naming, formatting, monitoring', False),
                    ('Accuracy, completeness, consistency', True),
                    ('Reviewing, updating, archiving', False)
                ]
            },
            {
                'text': 'Which best describes the difference between predictive AI and generative AI?',
                'answers': [
                    ('Predictive AI analyzes existing data to make predictions or recommendations, while generative AI creates new and original content.', True),
                    ('Predictive AI and generative AI have the same capabilities but differ in the type of input they receive: predictive AI receives raw data whereas generative AI receives natural language.', False),
                    ('Predictive AI uses machine learning to classify or predict output from input data whereas generative AI does not use machine learning to generate output.', False)
                ]
            },
            {
                'text': 'Which type of bias imposes a system’s values on others?',
                'answers': [
                    ('Societal', True),
                    ('Automation', False),
                    ('Association', False)
                ]
            },
            {
                'text': 'What is the role of data quality in achieving AI business objectives?',
                'answers': [
                    ('Data quality is unnecessary because AI can work with all data types.', False),
                    ('Data quality is required to create accurate AI data insights.', True),
                    ('Data quality is important for maintaining AI data storage limits.', False)
                ]
            },
            {
                'text': 'What is a potential outcome of using poor-quality data in AI applications?',
                'answers': [
                    ('AI model training becomes slower and less efficient.', False),
                    ('AI models may produce biased or erroneous results.', True),
                    ('AI models become more interpretable.', False)
                ]
            },
            {
                'text': 'The Cloud technical team is assessing the effectiveness of their AI development processes. Which established Salesforce Ethical Maturity Model should the team use to guide the development of trusted AI solutions?',
                'answers': [
                    ('Ethical AI Prediction Maturity Model', False),
                    ('Ethical AI Process Maturity Model', True),
                    ('Ethical AI Practice Maturity Model', False)
                ]
            },
            {
                'text': 'Which data does Salesforce automatically exclude from Marketing Cloud Einstein engagement model training to mitigate bias and ethical concerns?',
                'answers': [
                    ('Geographic', False),
                    ('Demographic', True),
                    ('Cryptographic', False)
                ]
            },
            {
                'text': 'How does a data quality assessment impact business outcomes for companies using AI?',
                'answers': [
                    ('Improves the speed of AI recommendations', False),
                    ('Accelerates the delivery of new AI solutions', False),
                    ('Provides a benchmark for AI predictions', True)
                ]
            },
            {
                'text': 'What is a key challenge of human-AI collaboration in decision-making?',
                'answers': [
                    ('Leads to more informed and balanced decision-making', False),
                    ('Creates a reliance on AI, potentially leading to less critical thinking and oversight', True),
                    ('Reduces the need for human involvement in decision-making processes', False)
                ]
            },
            {
                'text': 'A system admin recognizes the need to put a data management strategy in place. What is a key component of a data management strategy?',
                'answers': [
                    ('Naming Convention', False),
                    ('Data Backup', True),
                    ('Color Coding', False)
                ]
            },
        ]

        # Loop through the questions and create corresponding Question and Answer records
        for question_data in questions_data:
            # Determine if multiple answers are correct
            multiple_correct = sum(1 for answer in question_data['answers'] if answer[1]) > 1
            question = Question.objects.create(
                exam=exam,
                text=question_data['text'],
                multiple_correct=multiple_correct
            )
            # Create Answer objects for each question
            for answer_text, is_correct in question_data['answers']:
                Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_AI, atomic=False),
    ]
