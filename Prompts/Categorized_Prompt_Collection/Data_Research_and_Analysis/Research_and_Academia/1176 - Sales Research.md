---
name: sales-research
description: This skill provides methodology and best practices for researching sales prospects.
---

# Sales Research

## Overview

This skill provides methodology and best practices for researching sales prospects. It covers company research, contact profiling, and signal detection to surface actionable intelligence.

## Usage

The company-researcher and contact-researcher sub-agents reference this skill when:
- Researching new prospects
- Finding company information
- Profiling individual contacts
- Detecting buying signals

## Research Methodology

### Company Research Checklist

1. **Basic Profile**
   - Company name, industry, size (employees, revenue)
   - Headquarters and key locations
   - Founded date, growth stage

2. **Recent Developments**
   - Funding announcements (last 12 months)
   - M&A activity
   - Leadership changes
   - Product launches

3. **Tech Stack**
   - Known technologies (BuiltWith, StackShare)
   - Job postings mentioning tools
   - Integration partnerships

4. **Signals**
   - Job postings (scaling = opportunity)
   - Glassdoor reviews (pain points)
   - News mentions (context)
   - Social media activity

### Contact Research Checklist

1. **Professional Background**
   - Current role and tenure
   - Previous companies and roles
   - Education

2. **Influence Indicators**
   - Reporting structure
   - Decision-making authority
   - Budget ownership

3. **Engagement Hooks**
   - Recent LinkedIn posts
   - Published articles
   - Speaking engagements
   - Mutual connections

## Resources

- `resources/signal-indicators.md` - Taxonomy of buying signals
- `resources/research-checklist.md` - Complete research checklist

## Scripts

- `scripts/company-enricher.py` - Aggregate company data from multiple sources
- `scripts/linkedin-parser.py` - Structure LinkedIn profile data
FILE:company-enricher.py
#!/usr/bin/env python3
"""
company-enricher.py - Aggregate company data from multiple sources

Inputs:
  - company_name: string
  - domain: string (optional)

Outputs:
  - profile:
      name: string
      industry: string
      size: string
      funding: string
      tech_stack: [string]
      recent_news: [news items]

Dependencies:
  - requests, beautifulsoup4
"""

# Requirements: requests, beautifulsoup4

import json
from typing import Any
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class NewsItem:
    title: str
    date: str
    source: str
    url: str
    summary: str


@dataclass
class CompanyProfile:
    name: str
    domain: str
    industry: str
    size: str
    location: str
    founded: str
    funding: str
    tech_stack: list[str]
    recent_news: list[dict]
    competitors: list[str]
    description: str


def search_company_info(company_name: str, domain: str = None) -> dict:
    """
    Search for basic company information.
    In production, this would call APIs like Clearbit, Crunchbase, etc.
    """
    # TODO: Implement actual API calls
    # Placeholder return structure
    return {
        "name": company_name,
        "domain": domain or f"{company_name.lower().replace(' ', '')}.com",
        "industry": "Technology",  # Would come from API
        "size": "Unknown",
        "location": "Unknown",
        "founded": "Unknown",
        "description": f"Information about {company_name}"
    }


def search_funding_info(company_name: str) -> dict:
    """
    Search for funding information.
    In production, would call Crunchbase, PitchBook, etc.
    """
    # TODO: Implement actual API calls
    return {
        "total_funding": "Unknown",
        "last_round": "Unknown",
        "last_round_date": "Unknown",
        "investors": []
    }


def search_tech_stack(domain: str) -> list[str]:
    """
    Detect technology stack.
    In production, would call BuiltWith, Wappalyzer, etc.
    """
    # TODO: Implement actual API calls
    return []


def search_recent_news(company_name: str, days: int = 90) -> list[dict]:
    """
    Search for recent news about the company.
    In production, would call news APIs.
    """
    # TODO: Implement actual API calls
    return []


def main(
    company_name: str,
    domain: str = None
) -> dict[str, Any]:
    """
    Aggregate company data from multiple sources.

    Args:
        company_name: Company name to research
        domain: Company domain (optional, will be inferred)

    Returns:
        dict with company profile including industry, size, funding, tech stack, news
    """
    # Get basic company info
    basic_info = search_company_info(company_name, domain)

    # Get funding information
    funding_info = search_funding_info(company_name)

    # Detect tech stack
    company_domain = basic_info.get("domain", domain)
    tech_stack = search_tech_stack(company_domain) if company_domain else []

    # Get recent news
    news = search_recent_news(company_name)

    # Compile profile
    profile = CompanyProfile(
        name=basic_info["name"],
        domain=basic_info["domain"],
        industry=basic_info["industry"],
        size=basic_info["size"],
        location=basic_info["location"],
        founded=basic_info["founded"],
        funding=funding_info.get("total_funding", "Unknown"),
        tech_stack=tech_stack,
        recent_news=news,
        competitors=[],  # Would be enriched from industry analysis
        description=basic_info["description"]
    )

    return {
        "profile": asdict(profile),
        "funding_details": funding_info,
        "enriched_at": datetime.now().isoformat(),
        "sources_checked": ["company_info", "funding", "tech_stack", "news"]
    }


if __name__ == "__main__":
    import sys

    # Example usage
    result = main(
        company_name="DataFlow Systems",
        domain="dataflow.io"
    )
    print(json.dumps(result, indent=2))
FILE:linkedin-parser.py
#!/usr/bin/env python3
"""
linkedin-parser.py - Structure LinkedIn profile data

Inputs:
  - profile_url: string
  - or name + company: strings

Outputs:
  - contact:
      name: string
      title: string
      tenure: string
      previous_roles: [role objects]
      mutual_connections: [string]
      recent_activity: [post summaries]

Dependencies:
  - requests
"""

# Requirements: requests

import json
from typing import Any
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class PreviousRole:
    title: str
    company: str
    duration: str
    description: str


@dataclass
class RecentPost:
    date: str
    content_preview: str
    engagement: int
    topic: str


@dataclass
class ContactProfile:
    name: str
    title: str
    company: str
    location: str
    tenure: str
    previous_roles: list[dict]
    education: list[str]
    mutual_connections: list[str]
    recent_activity: list[dict]
    profile_url: str
    headline: str


def search_linkedin_profile(name: str = None, company: str = None, profile_url: str = None) -> dict:
    """
    Search for LinkedIn profile information.
    In production, would use LinkedIn API or Sales Navigator.
    """
    # TODO: Implement actual LinkedIn API integration
    # Note: LinkedIn's API has strict terms of service

    return {
        "found": False,
        "name": name or "Unknown",
        "title": "Unknown",
        "company": company or "Unknown",
        "location": "Unknown",
        "headline": "",
        "tenure": "Unknown",
        "profile_url": profile_url or ""
    }


def get_career_history(profile_data: dict) -> list[dict]:
    """
    Extract career history from profile.
    """
    # TODO: Implement career extraction
    return []


def get_mutual_connections(profile_data: dict, user_network: list = None) -> list[str]:
    """
    Find mutual connections.
    """
    # TODO: Implement mutual connection detection
    return []


def get_recent_activity(profile_data: dict, days: int = 30) -> list[dict]:
    """
    Get recent posts and activity.
    """
    # TODO: Implement activity extraction
    return []


def main(
    name: str = None,
    company: str = None,
    profile_url: str = None
) -> dict[str, Any]:
    """
    Structure LinkedIn profile data for sales prep.

    Args:
        name: Person's name
        company: Company they work at
        profile_url: Direct LinkedIn profile URL

    Returns:
        dict with structured contact profile
    """
    if not profile_url and not (name and company):
        return {"error": "Provide either profile_url or name + company"}

    # Search for profile
    profile_data = search_linkedin_profile(
        name=name,
        company=company,
        profile_url=profile_url
    )

    if not profile_data.get("found"):
        return {
            "found": False,
            "name": name or "Unknown",
            "company": company or "Unknown",
            "message": "Profile not found or limited access",
            "suggestions": [
                "Try searching directly on LinkedIn",
                "Check for alternative spellings",
                "Verify the person still works at this company"
            ]
        }

    # Get career history
    previous_roles = get_career_history(profile_data)

    # Find mutual connections
    mutual_connections = get_mutual_connections(profile_data)

    # Get recent activity
    recent_activity = get_recent_activity(profile_data)

    # Compile contact profile
    contact = ContactProfile(
        name=profile_data["name"],
        title=profile_data["title"],
        company=profile_data["company"],
        location=profile_data["location"],
        tenure=profile_data["tenure"],
        previous_roles=previous_roles,
        education=[],  # Would be extracted from profile
        mutual_connections=mutual_connections,
        recent_activity=recent_activity,
        profile_url=profile_data["profile_url"],
        headline=profile_data["headline"]
    )

    return {
        "found": True,
        "contact": asdict(contact),
        "research_date": datetime.now().isoformat(),
        "data_completeness": calculate_completeness(contact)
    }


def calculate_completeness(contact: ContactProfile) -> dict:
    """Calculate how complete the profile data is."""
    fields = {
        "basic_info": bool(contact.name and contact.title and contact.company),
        "career_history": len(contact.previous_roles) > 0,
        "mutual_connections": len(contact.mutual_connections) > 0,
        "recent_activity": len(contact.recent_activity) > 0,
        "education": len(contact.education) > 0
    }

    complete_count = sum(fields.values())
    return {
        "fields": fields,
        "score": f"{complete_count}/{len(fields)}",
        "percentage": int((complete_count / len(fields)) * 100)
    }


if __name__ == "__main__":
    import sys

    # Example usage
    result = main(
        name="Sarah Chen",
        company="DataFlow Systems"
    )
    print(json.dumps(result, indent=2))
FILE:priority-scorer.py
#!/usr/bin/env python3
"""
priority-scorer.py - Calculate and rank prospect priorities

Inputs:
  - prospects: [prospect objects with signals]
  - weights: {deal_size, timing, warmth, signals}

Outputs:
  - ranked: [prospects with scores and reasoning]

Dependencies:
  - (none - pure Python)
"""

import json
from typing import Any
from dataclasses import dataclass


# Default scoring weights
DEFAULT_WEIGHTS = {
    "deal_size": 0.25,
    "timing": 0.30,
    "warmth": 0.20,
    "signals": 0.25
}

# Signal score mapping
SIGNAL_SCORES = {
    # High-intent signals
    "recent_funding": 10,
    "leadership_change": 8,
    "job_postings_relevant": 9,
    "expansion_news": 7,
    "competitor_mention": 6,

    # Medium-intent signals
    "general_hiring": 4,
    "industry_event": 3,
    "content_engagement": 3,

    # Relationship signals
    "mutual_connection": 5,
    "previous_contact": 6,
    "referred_lead": 8,

    # Negative signals
    "recent_layoffs": -3,
    "budget_freeze_mentioned": -5,
    "competitor_selected": -7,
}


@dataclass
class ScoredProspect:
    company: str
    contact: str
    call_time: str
    raw_score: float
    normalized_score: int
    priority_rank: int
    score_breakdown: dict
    reasoning: str
    is_followup: bool


def score_deal_size(prospect: dict) -> tuple[float, str]:
    """Score based on estimated deal size."""
    size_indicators = prospect.get("size_indicators", {})

    employee_count = size_indicators.get("employees", 0)
    revenue_estimate = size_indicators.get("revenue", 0)

    # Simple scoring based on company size
    if employee_count > 1000 or revenue_estimate > 100_000_000:
        return 10.0, "Enterprise-scale opportunity"
    elif employee_count > 200 or revenue_estimate > 20_000_000:
        return 7.0, "Mid-market opportunity"
    elif employee_count > 50:
        return 5.0, "SMB opportunity"
    else:
        return 3.0, "Small business"


def score_timing(prospect: dict) -> tuple[float, str]:
    """Score based on timing signals."""
    timing_signals = prospect.get("timing_signals", [])

    score = 5.0  # Base score
    reasons = []

    for signal in timing_signals:
        if signal == "budget_cycle_q4":
            score += 3
            reasons.append("Q4 budget planning")
        elif signal == "contract_expiring":
            score += 4
            reasons.append("Contract expiring soon")
        elif signal == "active_evaluation":
            score += 5
            reasons.append("Actively evaluating")
        elif signal == "just_funded":
            score += 3
            reasons.append("Recently funded")

    return min(score, 10.0), "; ".join(reasons) if reasons else "Standard timing"


def score_warmth(prospect: dict) -> tuple[float, str]:
    """Score based on relationship warmth."""
    relationship = prospect.get("relationship", {})

    if relationship.get("is_followup"):
        last_outcome = relationship.get("last_outcome", "neutral")
        if last_outcome == "positive":
            return 9.0, "Warm follow-up (positive last contact)"
        elif last_outcome == "neutral":
            return 7.0, "Follow-up (neutral last contact)"
        else:
            return 5.0, "Follow-up (needs re-engagement)"

    if relationship.get("referred"):
        return 8.0, "Referred lead"

    if relationship.get("mutual_connections", 0) > 0:
        return 6.0, f"{relationship['mutual_connections']} mutual connections"

    if relationship.get("inbound"):
        return 7.0, "Inbound interest"

    return 4.0, "Cold outreach"


def score_signals(prospect: dict) -> tuple[float, str]:
    """Score based on buying signals detected."""
    signals = prospect.get("signals", [])

    total_score = 0
    signal_reasons = []

    for signal in signals:
        signal_score = SIGNAL_SCORES.get(signal, 0)
        total_score += signal_score
        if signal_score > 0:
            signal_reasons.append(signal.replace("_", " "))

    # Normalize to 0-10 scale
    normalized = min(max(total_score / 2, 0), 10)

    reason = f"Signals: {', '.join(signal_reasons)}" if signal_reasons else "No strong signals"
    return normalized, reason


def calculate_priority_score(
    prospect: dict,
    weights: dict = None
) -> ScoredProspect:
    """Calculate overall priority score for a prospect."""
    weights = weights or DEFAULT_WEIGHTS

    # Calculate component scores
    deal_score, deal_reason = score_deal_size(prospect)
    timing_score, timing_reason = score_timing(prospect)
    warmth_score, warmth_reason = score_warmth(prospect)
    signal_score, signal_reason = score_signals(prospect)

    # Weighted total
    raw_score = (
        deal_score * weights["deal_size"] +
        timing_score * weights["timing"] +
        warmth_score * weights["warmth"] +
        signal_score * weights["signals"]
    )

    # Compile reasoning
    reasons = []
    if timing_score >= 8:
        reasons.append(timing_reason)
    if signal_score >= 7:
        reasons.append(signal_reason)
    if warmth_score >= 7:
        reasons.append(warmth_reason)
    if deal_score >= 8:
        reasons.append(deal_reason)

    return ScoredProspect(
        company=prospect.get("company", "Unknown"),
        contact=prospect.get("contact", "Unknown"),
        call_time=prospect.get("call_time", "Unknown"),
        raw_score=round(raw_score, 2),
        normalized_score=int(raw_score * 10),
        priority_rank=0,  # Will be set after sorting
        score_breakdown={
            "deal_size": {"score": deal_score, "reason": deal_reason},
            "timing": {"score": timing_score, "reason": timing_reason},
            "warmth": {"score": warmth_score, "reason": warmth_reason},
            "signals": {"score": signal_score, "reason": signal_reason}
        },
        reasoning="; ".join(reasons) if reasons else "Standard priority",
        is_followup=prospect.get("relationship", {}).get("is_followup", False)
    )


def main(
    prospects: list[dict],
    weights: dict = None
) -> dict[str, Any]:
    """
    Calculate and rank prospect priorities.

    Args:
        prospects: List of prospect objects with signals
        weights: Optional custom weights for scoring components

    Returns:
        dict with ranked prospects and scoring details
    """
    weights = weights or DEFAULT_WEIGHTS

    # Score all prospects
    scored = [calculate_priority_score(p, weights) for p in prospects]

    # Sort by raw score descending
    scored.sort(key=lambda x: x.raw_score, reverse=True)

    # Assign ranks
    for i, prospect in enumerate(scored, 1):
        prospect.priority_rank = i

    # Convert to dicts for JSON serialization
    ranked = []
    for s in scored:
        ranked.append({
            "company": s.company,
            "contact": s.contact,
            "call_time": s.call_time,
            "priority_rank": s.priority_rank,
            "score": s.normalized_score,
            "reasoning": s.reasoning,
            "is_followup": s.is_followup,
            "breakdown": s.score_breakdown
        })

    return {
        "ranked": ranked,
        "weights_used": weights,
        "total_prospects": len(prospects)
    }


if __name__ == "__main__":
    import sys

    # Example usage
    example_prospects = [
        {
            "company": "DataFlow Systems",
            "contact": "Sarah Chen",
            "call_time": "2pm",
            "size_indicators": {"employees": 200, "revenue": 25_000_000},
            "timing_signals": ["just_funded", "active_evaluation"],
            "signals": ["recent_funding", "job_postings_relevant"],
            "relationship": {"is_followup": False, "mutual_connections": 2}
        },
        {
            "company": "Acme Manufacturing",
            "contact": "Tom Bradley",
            "call_time": "10am",
            "size_indicators": {"employees": 500},
            "timing_signals": ["contract_expiring"],
            "signals": [],
            "relationship": {"is_followup": True, "last_outcome": "neutral"}
        },
        {
            "company": "FirstRate Financial",
            "contact": "Linda Thompson",
            "call_time": "4pm",
            "size_indicators": {"employees": 300},
            "timing_signals": [],
            "signals": [],
            "relationship": {"is_followup": False}
        }
    ]

    result = main(prospects=example_prospects)
    print(json.dumps(result, indent=2))
FILE:research-checklist.md
# Prospect Research Checklist

## Company Research

### Basic Information
- [ ] Company name (verify spelling)
- [ ] Industry/vertical
- [ ] Headquarters location
- [ ] Employee count (LinkedIn, website)
- [ ] Revenue estimate (if available)
- [ ] Founded date
- [ ] Funding stage/history

### Recent News (Last 90 Days)
- [ ] Funding announcements
- [ ] Acquisitions or mergers
- [ ] Leadership changes
- [ ] Product launches
- [ ] Major customer wins
- [ ] Press mentions
- [ ] Earnings/financial news

### Digital Footprint
- [ ] Website review
- [ ] Blog/content topics
- [ ] Social media presence
- [ ] Job postings (careers page + LinkedIn)
- [ ] Tech stack (BuiltWith, job postings)

### Competitive Landscape
- [ ] Known competitors
- [ ] Market position
- [ ] Differentiators claimed
- [ ] Recent competitive moves

### Pain Point Indicators
- [ ] Glassdoor reviews (themes)
- [ ] G2/Capterra reviews (if B2B)
- [ ] Social media complaints
- [ ] Job posting patterns

## Contact Research

### Professional Profile
- [ ] Current title
- [ ] Time in role
- [ ] Time at company
- [ ] Previous companies
- [ ] Previous roles
- [ ] Education

### Decision Authority
- [ ] Reports to whom
- [ ] Team size (if manager)
- [ ] Budget authority (inferred)
- [ ] Buying involvement history

### Engagement Hooks
- [ ] Recent LinkedIn posts
- [ ] Published articles
- [ ] Podcast appearances
- [ ] Conference talks
- [ ] Mutual connections
- [ ] Shared interests/groups

### Communication Style
- [ ] Post tone (formal/casual)
- [ ] Topics they engage with
- [ ] Response patterns

## CRM Check (If Available)

- [ ] Any prior touchpoints
- [ ] Previous opportunities
- [ ] Related contacts at company
- [ ] Notes from colleagues
- [ ] Email engagement history

## Time-Based Research Depth

| Time Available | Research Depth |
|----------------|----------------|
| 5 minutes | Company basics + contact title only |
| 15 minutes | + Recent news + LinkedIn profile |
| 30 minutes | + Pain point signals + engagement hooks |
| 60 minutes | Full checklist + competitive analysis |
FILE:signal-indicators.md
# Signal Indicators Reference

## High-Intent Signals

### Job Postings
- **3+ relevant roles posted** = Active initiative, budget allocated
- **Senior hire in your domain** = Strategic priority
- **Urgency language ("ASAP", "immediate")** = Pain is acute
- **Specific tool mentioned** = Competitor or category awareness

### Financial Events
- **Series B+ funding** = Growth capital, buying power
- **IPO preparation** = Operational maturity needed
- **Acquisition announced** = Integration challenges coming
- **Revenue milestone PR** = Budget available

### Leadership Changes
- **New CXO in your domain** = 90-day priority setting
- **New CRO/CMO** = Tech stack evaluation likely
- **Founder transition to CEO** = Professionalizing operations

## Medium-Intent Signals

### Expansion Signals
- **New office opening** = Infrastructure needs
- **International expansion** = Localization, compliance
- **New product launch** = Scaling challenges
- **Major customer win** = Delivery pressure

### Technology Signals
- **RFP published** = Active buying process
- **Vendor review mentioned** = Comparison shopping
- **Tech stack change** = Integration opportunity
- **Legacy system complaints** = Modernization need

### Content Signals
- **Blog post on your topic** = Educating themselves
- **Webinar attendance** = Interest confirmed
- **Whitepaper download** = Problem awareness
- **Conference speaking** = Thought leadership, visibility

## Low-Intent Signals (Nurture)

### General Activity
- **Industry event attendance** = Market participant
- **Generic hiring** = Company growing
- **Positive press** = Healthy company
- **Social media activity** = Engaged leadership

## Signal Scoring

| Signal Type | Score | Action |
|-------------|-------|--------|
| Job posting (relevant) | +3 | Prioritize outreach |
| Recent funding | +3 | Reference in conversation |
| Leadership change | +2 | Time-sensitive opportunity |
| Expansion news | +2 | Growth angle |
| Negative reviews | +2 | Pain point angle |
| Content engagement | +1 | Nurture track |
| No signals | 0 | Discovery focus |
