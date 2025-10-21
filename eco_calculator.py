def calculate_eco_score(carbon_footprint, water_usage, biodegradability, recyclability, packaging):
    """
    Calculate eco-score (0-100) based on environmental metrics
    """
    # Normalize values (lower is better for carbon/water, higher for bio/recyc/packaging)
    carbon_score = max(0, 100 - (carbon_footprint * 10))
    water_score = max(0, 100 - (water_usage / 10))
    
    # Weighted calculation
    total_score = (
        carbon_score * 0.30 +
        water_score * 0.25 +
        biodegradability * 0.20 +
        recyclability * 0.15 +
        packaging * 0.10
    )
    
    return min(100, max(0, round(total_score)))

def get_eco_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 80:
        return 'A', 'Excellent'
    elif score >= 60:
        return 'B', 'Good'
    elif score >= 40:
        return 'C', 'Fair'
    elif score >= 20:
        return 'D', 'Poor'
    else:
        return 'E', 'Very Poor'
