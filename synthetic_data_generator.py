import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Sample size
n_samples = 100

# Define possible responses for each question
role_options = ['IT Implementer', 'Educator (Faculty)', 'Administrator', 'Student']
institution_options = ['Public University', 'Private University', 'IT Company', 'Technical Institute']
experience_options = ['Less than 1 year', '1-3 years', '3-5 years', 'More than 5 years']
familiarity_options = ['Very familiar', 'Somewhat familiar', 'Not familiar']
readiness_options = ['Very ready', 'Somewhat ready', 'Not ready', 'Unsure']
scale_options = [1, 2, 3, 4, 5]
benefit_options = ['Increased efficiency', 'Improved student engagement', 'Personalized learning experiences', 'Automation of administrative tasks', 'Other']
concern_options = ['Data privacy and security', 'Job displacement', 'Ethical issues (e.g., bias, transparency)', 'Lack of human interaction in learning', 'High implementation costs', 'Other']
regulatory_options = ['Yes', 'No', 'Not sure']
ethical_priorities_options = ['Data privacy and protection', 'Transparency in AI algorithms', 'Avoiding algorithmic bias', 'Academic integrity', 'Ensuring equitable access to AI tools', 'Safeguarding human roles in education']
confidence_options = ['Very confident', 'Somewhat confident', 'Not confident', 'Unsure']
strategy_options = ['Ethical AI implementation', 'Faculty and student training', 'Reducing administrative costs', 'Enhancing learning experiences', 'Developing new AI-driven academic services', 'Other']

# Generate synthetic data
data = {
    'Role': [random.choice(role_options) for _ in range(n_samples)],
    'Institution Type': [random.choice(institution_options) for _ in range(n_samples)],
    'Years of Experience': [random.choice(experience_options) for _ in range(n_samples)],
    'Familiarity with AI': [random.choice(familiarity_options) for _ in range(n_samples)],
    'IT Readiness': [
        'Not ready' if role in ['Educator (Faculty)', 'Student'] else 'Somewhat ready'
        for role in data['Role']
    ],
    'Personalized Learning': [random.choice(scale_options) for _ in range(n_samples)],
    'Administrative Efficiency': [random.choice(scale_options) for _ in range(n_samples)],
    'Student Engagement': [random.choice(scale_options) for _ in range(n_samples)],
    'Educational Content Creation': [random.choice(scale_options) for _ in range(n_samples)],
    'Timely Feedback': [random.choice(scale_options) for _ in range(n_samples)],
    'Automation of Tasks': [random.choice(scale_options) for _ in range(n_samples)],
    'Significant Benefit of AI': [
        random.choice(['Increased efficiency', 'Automation of administrative tasks']) if role in ['IT Implementer', 'Educator (Faculty)']
        else 'Improved student engagement' for role in data['Role']
    ],
    'Data Privacy Concern': [random.choice(scale_options) for _ in range(n_samples)],
    'Job Displacement Concern': [random.choice(scale_options) for _ in range(n_samples)],
    'Bias in Content Concern': [random.choice(scale_options) for _ in range(n_samples)],
    'Over-reliance on AI Concern': [random.choice(scale_options) for _ in range(n_samples)],
    'Implementation Costs Concern': [random.choice(scale_options) for _ in range(n_samples)],
    'Biggest Concern': [
        random.choice(['Data privacy and security', 'Bias in AI-generated content']) for _ in range(n_samples)
    ],
    'Need for Regulatory Oversight': [random.choice(regulatory_options) for _ in range(n_samples)],
    'Top Ethical Priorities': [random.sample(ethical_priorities_options, 3) for _ in range(n_samples)],
    'Confidence in Preparedness': [random.choice(confidence_options) for _ in range(n_samples)],
    'Academic Administration Transformation': [random.choice(scale_options) for _ in range(n_samples)],
    'Training on AI Tools': [random.choice(scale_options) for _ in range(n_samples)],
    'AI-driven Academic Services': [random.choice(scale_options) for _ in range(n_samples)],
    'Promoting Inclusivity': [random.choice(scale_options) for _ in range(n_samples)],
    'Reducing Operational Costs': [random.choice(scale_options) for _ in range(n_samples)],
    'Primary Focus of AI Strategy': [random.choice(strategy_options) for _ in range(n_samples)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('synthetic_survey_data.csv', index=False)
print("Synthetic survey data generated and saved to 'synthetic_survey_data.csv'")
