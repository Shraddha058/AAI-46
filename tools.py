from typing import List, Dict
import datetime


def decompose_goal(goal: str) -> List[str]:
    """Break high-level marketing goal into actionable steps."""
    normalized_goal = goal.strip().lower()

    predefined_steps = {
        "competitor ads": [
            "Identify top competitors",
            "Collect competitor ad creatives",
            "Analyze messaging and CTAs",
            "Identify gaps and opportunities",
            "Propose ad strategy",
        ],
        "launch a new fitness app": [
            "Define target audience and positioning",
            "Create pre-launch content and landing page",
            "Set up acquisition channels (Meta, Google, influencers)",
            "Run beta campaign and collect testimonials",
            "Launch with paid and organic push",
            "Measure CAC, retention, and optimize creatives",
        ],
    }

    if normalized_goal in predefined_steps:
        return predefined_steps[normalized_goal]

    # Generic fallback so the planner always has a complete path forward.
    return [
        f"Define audience and value proposition for: {goal}",
        "Audit market and competitors",
        "Select channels and campaign strategy",
        "Build messaging, creatives, and offers",
        "Launch campaign with timeline and owners",
        "Track KPIs and optimize weekly",
    ]


def validate_resources(steps: List[str]) -> Dict:
    """Mock validation of tools and resources."""
    return {
        "data_sources": True,
        "ad_library_access": True,
        "budget_available": True,
        "team_available": True,
    }


def generate_schedule(steps: List[str]) -> List[Dict]:
    """Create optimized execution timeline."""
    today = datetime.date.today()
    schedule = []

    for i, step in enumerate(steps):
        schedule.append(
            {
                "task": step,
                "start_date": str(today + datetime.timedelta(days=i)),
                "end_date": str(today + datetime.timedelta(days=i + 1)),
            }
        )

    return schedule
