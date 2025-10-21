from models import Product, ProductAlternative, EcoMetric

def calculate_similarity(product1, product2):
    """Calculate similarity between two products"""
    similarity = 0.0
    
    # Category match (40%)
    if product1.category == product2.category:
        similarity += 0.4
    
    # Price similarity (30%)
    if product1.price and product2.price:
        price_diff = abs(product1.price - product2.price)
        max_price = max(product1.price, product2.price)
        price_sim = 1 - (price_diff / max_price) if max_price > 0 else 0
        similarity += price_sim * 0.3
    
    # Material compatibility (30%)
    if product1.material and product2.material:
        if product1.material.lower() in product2.material.lower() or \
           product2.material.lower() in product1.material.lower():
            similarity += 0.3
    
    return round(similarity, 2)

def get_recommendations(product_id, limit=5):
    """Get eco-friendly alternatives for a product"""
    from models import db
    
    # Check if alternatives already exist
    alternatives = ProductAlternative.query.filter_by(
        conventional_product_id=product_id
    ).limit(limit).all()
    
    if alternatives:
        recommendations = []
        for alt in alternatives:
            eco_product = Product.query.get(alt.eco_product_id)
            recommendations.append({
                'product': eco_product,
                'similarity': alt.similarity_score,
                'eco_score': eco_product.eco_score
            })
        return recommendations
    
    # If no pre-computed alternatives, find similar eco products
    original_product = Product.query.get(product_id)
    if not original_product:
        return []
    
    eco_products = Product.query.filter_by(
        is_eco_friendly=True,
        category=original_product.category
    ).limit(limit).all()
    
    recommendations = []
    for eco_prod in eco_products:
        similarity = calculate_similarity(original_product, eco_prod)
        recommendations.append({
            'product': eco_prod,
            'similarity': similarity,
            'eco_score': eco_prod.eco_score
        })
    
    # Sort by eco_score and similarity
    recommendations.sort(key=lambda x: (x['eco_score'], x['similarity']), reverse=True)
    
    return recommendations[:limit]
