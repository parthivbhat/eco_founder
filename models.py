from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(100))
    is_eco_friendly = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float)
    brand = db.Column(db.String(100))
    eco_score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f'<Product {self.name}>'

class EcoMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    carbon_footprint = db.Column(db.Float, default=0)
    water_usage = db.Column(db.Float, default=0)
    biodegradability_score = db.Column(db.Integer, default=0)
    recyclability_score = db.Column(db.Integer, default=0)
    packaging_impact = db.Column(db.Integer, default=0)
    
    product = db.relationship('Product', backref=db.backref('eco_metrics', lazy=True))
    
    def __repr__(self):
        return f'<EcoMetric for Product {self.product_id}>'

class ProductAlternative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conventional_product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    eco_product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    similarity_score = db.Column(db.Float, default=0.0)
    
    conventional = db.relationship('Product', foreign_keys=[conventional_product_id])
    eco_alternative = db.relationship('Product', foreign_keys=[eco_product_id])
    
    def __repr__(self):
        return f'<Alternative {self.conventional_product_id} -> {self.eco_product_id}>'
