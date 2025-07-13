from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List
from model_utils import predict
from reranker import apply_reranker
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory lead store
lead_store = []

class LeadRequest(BaseModel):
    name: str
    email: EmailStr
    phone_number: str = Field(..., min_length=10, max_length=20)
    age: int
    age_group: str
    city: str
    city_tier: int
    family_background: str
    occupation: str
    income: int = Field(..., ge=0)
    credit_score: int = Field(..., ge=300, le=850)
    education_level: str
    num_site_visits: int
    avg_time_on_page: float
    form_filled: int
    whatsapp_reply_count: int
    clicked_ad: int
    bounced: int
    referral_source: str
    ip_geolocation_verified: int
    device_type: str
    campaign_id: str
    crm_segment_tag: str
    linkedin_profile_exists: int
    news_sentiment_about_company: float
    company_size: str
    industry_type: str
    comment: str
    consent: bool  # ✅ required for backend validation

@app.post("/score")
def score_lead(lead: LeadRequest):
    if not lead.consent:
        raise HTTPException(status_code=400, detail="Consent is required to process data.")
    
    lead_data = lead.dict()
    comment = lead_data.pop("comment")
    consent = lead_data.pop("consent")

    initial_score = predict(lead_data)
    reranked_score = apply_reranker(initial_score, comment)

    result = {
        "name": lead.name,
        "email": lead.email,
        "initial_score": initial_score,
        "reranked_score": reranked_score,
        "comment": comment
    }

    lead_store.append(result)
    return result

@app.get("/leads")
def get_leads() -> List[dict]:
    return lead_store
