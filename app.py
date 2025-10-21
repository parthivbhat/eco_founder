import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Product, EcoMetric, ProductAlternative
from eco_calculator import calculate_eco_score, get_eco_grade
from recommender import get_recommendations

app = Flask(__name__)

# Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db.init_app(app)

@app.route('/')
def index():
    """Homepage - show all products"""
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    """Individual product details page"""
    product = Product.query.get_or_404(product_id)
    eco_metric = EcoMetric.query.filter_by(product_id=product_id).first()
    grade, grade_text = get_eco_grade(product.eco_score)
    
    return render_template('product.html', 
                         product=product, 
                         eco_metric=eco_metric,
                         grade=grade,
                         grade_text=grade_text)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    """Recommendation page"""
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product = Product.query.filter(Product.name.contains(product_name)).first()
        
        if product:
            recommendations = get_recommendations(product.id)
            return render_template('recommendations.html', 
                                 original_product=product,
                                 recommendations=recommendations)
        else:
            return render_template('recommendations.html', 
                                 error="Product not found")
    
    return render_template('recommendations.html')

@app.route('/api/calculate-score', methods=['POST'])
def calculate_score():
    """API endpoint to calculate eco-score"""
    data = request.get_json()
    
    score = calculate_eco_score(
        data.get('carbon_footprint', 0),
        data.get('water_usage', 0),
        data.get('biodegradability', 0),
        data.get('recyclability', 0),
        data.get('packaging', 0)
    )
    
    grade, grade_text = get_eco_grade(score)
    
    return jsonify({
        'score': score,
        'grade': grade,
        'grade_text': grade_text
    })

@app.route('/search')
def search():
    """Search products by name or category"""
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    
    products = Product.query
    
    if query:
        products = products.filter(Product.name.contains(query))
    
    if category:
        products = products.filter_by(category=category)
    
    products = products.all()
    
    return render_template('index.html', products=products)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
