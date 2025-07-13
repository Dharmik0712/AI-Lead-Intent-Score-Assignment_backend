# import pandas as pd
# import random
# from faker import Faker
# import numpy as np

# fake = Faker()
# Faker.seed(42)
# random.seed(42)
# np.random.seed(42)

# tier_1 = ['Mumbai', 'Delhi', 'Bangalore']
# tier_2 = ['Pune', 'Ahmedabad', 'Chandigarh']
# tier_3 = ['Indore', 'Rajkot', 'Nagpur']
# cities = tier_1 + tier_2 + tier_3

# age_groups = {
#     "18-25": (18, 25),
#     "26-35": (26, 35),
#     "36-50": (36, 50),
#     "51+": (51, 60)
# }

# def generate_lead():
#     city = random.choice(cities)
#     age_group_label, (age_min, age_max) = random.choice(list(age_groups.items()))
#     age = random.randint(age_min, age_max)
#     family_background = random.choices(
#         ["Single", "Married", "Married with Kids"],
#         weights=[0.3, 0.4, 0.3]
#     )[0]
#     income = random.randint(100_000, 1_000_000)
#     credit_score = random.randint(300, 850)
#     num_site_visits = random.randint(0, 15)
#     avg_time_on_page = round(random.uniform(5, 150), 2)
#     form_filled = random.choices([0, 1], weights=[0.3, 0.7])[0]
#     whatsapp_reply_count = random.randint(0, 5)
#     clicked_ad = random.choices([0, 1], weights=[0.5, 0.5])[0]
#     bounced = random.choices([0, 1], weights=[0.1, 0.9])[0]
#     referral_source = random.choice(["Paid Ad", "SEO", "Referral", "Email", "Organic"])
#     ip_geolocation_verified = random.choice([0, 1])
#     device_type = random.choice(["Mobile", "Desktop", "Tablet"])
#     campaign_id = random.choice(["CAMP001", "CAMP002", "CAMP003"])
#     crm_segment_tag = random.choice(["A", "B", "C"])
#     linkedin_profile_exists = random.choice([0, 1])
#     news_sentiment_about_company = round(random.uniform(-1, 1), 2)
#     company_size = random.choice(["<50", "50-200", "200-1000", "1000+"])
#     industry_type = random.choice(["Tech", "Real Estate", "Finance", "Education", "Healthcare"])

#     # Logic-based intent score generation
#     base_score = 0
#     base_score += form_filled * 20
#     base_score += clicked_ad * 15
#     base_score += whatsapp_reply_count * 3
#     base_score += (income / 1000000) * 10
#     base_score += ((credit_score - 300) / 550) * 10
#     base_score += 10 if family_background == "Married with Kids" else 0
#     base_score += 5 if linkedin_profile_exists else 0
#     base_score -= bounced * 15
#     base_score = max(0, min(100, round(base_score, 2)))

#     return {
#         "lead_id": fake.uuid4(),
#         "name": fake.name(),
#         "email": fake.email(),
#         "phone_number": fake.phone_number().replace(' ', '').replace('.', ''),
#         "age": age,
#         "age_group": age_group_label,
#         "city": city,
#         "city_tier": (
#             1 if city in tier_1 else
#             2 if city in tier_2 else 3
#         ),
#         "family_background": family_background,
#         "occupation": random.choice(["Salaried", "Self-Employed", "Student", "Freelancer", "Unemployed"]),
#         "income": income,
#         "credit_score": credit_score,
#         "education_level": random.choice(["Undergrad", "Graduate", "Postgrad", "PhD"]),
#         "num_site_visits": num_site_visits,
#         "avg_time_on_page": avg_time_on_page,
#         "form_filled": form_filled,
#         "whatsapp_reply_count": whatsapp_reply_count,
#         "clicked_ad": clicked_ad,
#         "bounced": bounced,
#         "referral_source": referral_source,
#         "ip_geolocation_verified": ip_geolocation_verified,
#         "device_type": device_type,
#         "campaign_id": campaign_id,
#         "crm_segment_tag": crm_segment_tag,
#         "linkedin_profile_exists": linkedin_profile_exists,
#         "news_sentiment_about_company": news_sentiment_about_company,
#         "company_size": company_size,
#         "industry_type": industry_type,
#         "lead_created_at": fake.date_time_between(start_date='-30d', end_date='now'),
#         "intent_score": base_score
#     }

# # Generate and save 10,000 rows
# data = [generate_lead() for _ in range(10_000)]
# df = pd.DataFrame(data)
# df.to_csv("data/leads.csv", index=False)

# print("✅ leads.csv generated with 10,000 rows and upgraded fields.")

import pandas as pd
import random
from faker import Faker
import numpy as np

fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

tier_1 = ['Mumbai', 'Delhi', 'Bangalore']
tier_2 = ['Pune', 'Ahmedabad', 'Chandigarh']
tier_3 = ['Indore', 'Rajkot', 'Nagpur']
cities = tier_1 + tier_2 + tier_3

def generate_lead():
    city = random.choice(cities)
    age = random.randint(21, 60)
    credit_score = random.randint(300, 850)
    avg_time = round(random.uniform(5, 150), 2)
    whatsapp_replies = random.randint(0, 5)
    bounced = random.choice([0, 1])
    clicked_ad = random.choice([0, 1])
    form_filled = random.choice([0, 1])
    linkedin_profile = random.choice([0, 1])
    referral_source = random.choice(["Paid Ad", "SEO", "Referral", "Email", "Organic"])

    lead = {
        "lead_id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "age": age,
        "age_group": (
            "18-25" if age <= 25 else
            "26-35" if age <= 35 else
            "36-50" if age <= 50 else "51+"
        ),
        "city": city,
        "city_tier": (
            1 if city in tier_1 else
            2 if city in tier_2 else 3
        ),
        "family_background": random.choice(["Single", "Married", "Married with Kids"]),
        "occupation": random.choice(["Salaried", "Self-Employed", "Student", "Freelancer", "Unemployed"]),
        "income": random.randint(100000, 1000000),
        "credit_score": credit_score,
        "education_level": random.choice(["Undergrad", "Graduate", "Postgrad", "PhD"]),
        "num_site_visits": random.randint(1, 15),
        "avg_time_on_page": avg_time,
        "form_filled": form_filled,
        "whatsapp_reply_count": whatsapp_replies,
        "clicked_ad": clicked_ad,
        "bounced": bounced,
        "referral_source": referral_source,
        "ip_geolocation_verified": random.choice([0, 1]),
        "device_type": random.choice(["Mobile", "Desktop", "Tablet"]),
        "campaign_id": random.choice(["CAMP001", "CAMP002", "CAMP003"]),
        "crm_segment_tag": random.choice(["A", "B", "C"]),
        "linkedin_profile_exists": linkedin_profile,
        "news_sentiment_about_company": round(random.uniform(-1, 1), 2),
        "company_size": random.choice(["<50", "50-200", "200-1000", "1000+"]),
        "industry_type": random.choice(["Tech", "Real Estate", "Finance", "Education", "Healthcare"]),
        "lead_created_at": fake.date_time_between(start_date='-30d', end_date='now'),
    }

    # 👉 Rule-based intent scoring
    score = 0
    score += 15 if clicked_ad else 0
    score += 10 if form_filled else 0
    score += 5 * whatsapp_replies
    score += 10 if linkedin_profile else 0
    score += 10 if credit_score > 700 else 0
    score += 10 if avg_time > 60 else 0
    score += 10 if referral_source in ["Email", "Referral"] else 0
    score -= 10 if bounced else 0
    score = min(score, 100)

    lead["intent_score"] = round(score, 2)

    return lead

# 🔁 Generate 10,000 leads
data = [generate_lead() for _ in range(10000)]
df = pd.DataFrame(data)
df.to_csv("data/leads.csv", index=False)

print("✅ leads.csv generated with realistic intent scores.")
