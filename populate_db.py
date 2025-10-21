from app import app, db
from models import Product, EcoMetric, ProductAlternative
from eco_calculator import calculate_eco_score

def populate_database():
    """Populate database with sample products"""
    
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Clear existing data
        db.session.query(ProductAlternative).delete()
        db.session.query(EcoMetric).delete()
        db.session.query(Product).delete()
        db.session.commit()
        
        # ========== PERSONAL CARE ==========
        
        # Conventional products
        plastic_toothbrush = Product(
            name="Plastic Toothbrush",
            description="Standard plastic toothbrush",
            category="Personal Care",
            material="Plastic",
            is_eco_friendly=False,
            price=50,
            brand="Colgate",
            eco_score=25
        )
        
        disposable_razor = Product(
            name="Disposable Razor",
            description="Single-use plastic razor",
            category="Personal Care",
            material="Plastic",
            is_eco_friendly=False,
            price=99,
            brand="Gillette",
            eco_score=20
        )
        
        synthetic_soap = Product(
            name="Chemical Soap Bar",
            description="Soap with artificial fragrances",
            category="Personal Care",
            material="Synthetic",
            is_eco_friendly=False,
            price=40,
            brand="Lux",
            eco_score=30
        )
        
        plastic_comb = Product(
            name="Plastic Comb",
            description="Regular plastic hair comb",
            category="Personal Care",
            material="Plastic",
            is_eco_friendly=False,
            price=25,
            brand="BrandX",
            eco_score=28
        )
        
        # Eco-friendly alternatives
        bamboo_toothbrush = Product(
            name="Bamboo Toothbrush",
            description="Biodegradable bamboo toothbrush with natural bristles",
            category="Personal Care",
            material="Bamboo",
            is_eco_friendly=True,
            price=180,
            brand="The Bamboo Brush",
            eco_score=85
        )
        
        safety_razor = Product(
            name="Safety Razor",
            description="Reusable metal safety razor with replaceable blades",
            category="Personal Care",
            material="Metal",
            is_eco_friendly=True,
            price=899,
            brand="Pearl Shaving",
            eco_score=88
        )
        
        organic_soap = Product(
            name="Organic Neem Soap",
            description="Handmade soap with natural neem and turmeric",
            category="Personal Care",
            material="Natural",
            is_eco_friendly=True,
            price=120,
            brand="Khadi Natural",
            eco_score=90
        )
        
        wooden_comb = Product(
            name="Neem Wood Comb",
            description="Handcrafted wooden comb from neem tree",
            category="Personal Care",
            material="Neem Wood",
            is_eco_friendly=True,
            price=250,
            brand="Vega",
            eco_score=87
        )
        
        neem_toothpaste = Product(
            name="Neem Toothpaste",
            description="Herbal toothpaste with neem extract, no chemicals",
            category="Personal Care",
            material="Natural",
            is_eco_friendly=True,
            price=85,
            brand="Patanjali",
            eco_score=82
        )
        
        # ========== KITCHEN & HOME ==========
        
        # Conventional
        plastic_bottle = Product(
            name="Plastic Water Bottle",
            description="Single-use plastic water bottle",
            category="Kitchen",
            material="Plastic",
            is_eco_friendly=False,
            price=20,
            brand="Bisleri",
            eco_score=15
        )
        
        plastic_bag = Product(
            name="Plastic Shopping Bag",
            description="Non-biodegradable plastic carry bag",
            category="Kitchen",
            material="Plastic",
            is_eco_friendly=False,
            price=5,
            brand="Generic",
            eco_score=10
        )
        
        plastic_straw = Product(
            name="Plastic Straws (Pack of 50)",
            description="Single-use plastic drinking straws",
            category="Kitchen",
            material="Plastic",
            is_eco_friendly=False,
            price=30,
            brand="Party Supplies",
            eco_score=12
        )
        
        # Eco-friendly
        reusable_bottle = Product(
            name="Stainless Steel Water Bottle",
            description="Reusable insulated stainless steel bottle (1L)",
            category="Kitchen",
            material="Stainless Steel",
            is_eco_friendly=True,
            price=599,
            brand="Milton",
            eco_score=90
        )
        
        jute_bag = Product(
            name="Jute Shopping Bag",
            description="Reusable jute carry bag with handles",
            category="Kitchen",
            material="Jute",
            is_eco_friendly=True,
            price=150,
            brand="Ecobags",
            eco_score=92
        )
        
        steel_straw = Product(
            name="Steel Straws (Pack of 6)",
            description="Reusable stainless steel straws with cleaning brush",
            category="Kitchen",
            material="Stainless Steel",
            is_eco_friendly=True,
            price=299,
            brand="Eco365",
            eco_score=89
        )
        
        cloth_napkin = Product(
            name="Organic Cotton Napkins (Pack of 6)",
            description="Washable and reusable cotton table napkins",
            category="Kitchen",
            material="Organic Cotton",
            is_eco_friendly=True,
            price=350,
            brand="Fabindia",
            eco_score=86
        )
        
        compost_bin = Product(
            name="Kitchen Compost Bin",
            description="Biodegradable waste composting bin for kitchen",
            category="Kitchen",
            material="Recycled Plastic",
            is_eco_friendly=True,
            price=799,
            brand="Khamba",
            eco_score=84
        )
        
        # ========== FASHION ==========
        
        # Conventional
        synthetic_tshirt = Product(
            name="Polyester T-Shirt",
            description="Regular synthetic fabric t-shirt",
            category="Fashion",
            material="Polyester",
            is_eco_friendly=False,
            price=299,
            brand="Max",
            eco_score=35
        )
        
        rubber_slippers = Product(
            name="Rubber Slippers",
            description="Standard rubber flip-flops",
            category="Fashion",
            material="Rubber",
            is_eco_friendly=False,
            price=199,
            brand="Relaxo",
            eco_score=32
        )
        
        # Eco-friendly
        organic_tshirt = Product(
            name="Organic Cotton T-Shirt",
            description="100% organic cotton t-shirt, naturally dyed",
            category="Fashion",
            material="Organic Cotton",
            is_eco_friendly=True,
            price=799,
            brand="No Nasties",
            eco_score=88
        )
        
        jute_slippers = Product(
            name="Jute Slippers",
            description="Handmade jute and cotton slippers",
            category="Fashion",
            material="Jute",
            is_eco_friendly=True,
            price=450,
            brand="Desi Kolhapuri",
            eco_score=85
        )
        
        khadi_fabric = Product(
            name="Khadi Fabric (1 meter)",
            description="Hand-spun and hand-woven khadi cotton fabric",
            category="Fashion",
            material="Khadi Cotton",
            is_eco_friendly=True,
            price=350,
            brand="Khadi India",
            eco_score=91
        )
        
        # ========== OFFICE ==========
        
        # Conventional
        regular_notebook = Product(
            name="Regular Paper Notebook",
            description="Standard notebook made from virgin paper",
            category="Office",
            material="Paper",
            is_eco_friendly=False,
            price=80,
            brand="Classmate",
            eco_score=40
        )
        
        plastic_pen = Product(
            name="Plastic Ballpoint Pen",
            description="Disposable plastic pen",
            category="Office",
            material="Plastic",
            is_eco_friendly=False,
            price=10,
            brand="Reynolds",
            eco_score=25
        )
        
        # Eco-friendly
        recycled_notebook = Product(
            name="Recycled Paper Notebook",
            description="Notebook made from 100% recycled paper",
            category="Office",
            material="Recycled Paper",
            is_eco_friendly=True,
            price=150,
            brand="Paperwrks",
            eco_score=83
        )
        
        bamboo_pen = Product(
            name="Bamboo Pen",
            description="Eco-friendly pen made from bamboo with refillable ink",
            category="Office",
            material="Bamboo",
            is_eco_friendly=True,
            price=120,
            brand="Ecoware",
            eco_score=86
        )
        
        plantable_pencil = Product(
            name="Plantable Pencils (Pack of 5)",
            description="Pencils with seeds that can be planted after use",
            category="Office",
            material="Wood & Seeds",
            is_eco_friendly=True,
            price=199,
            brand="Seed Pencils",
            eco_score=94
        )
        
        # ========== CLEANING ==========
        
        # Conventional
        chemical_detergent = Product(
            name="Chemical Detergent (1kg)",
            description="Synthetic washing powder with harsh chemicals",
            category="Cleaning",
            material="Synthetic",
            is_eco_friendly=False,
            price=180,
            brand="Surf Excel",
            eco_score=28
        )
        
        plastic_dish_soap = Product(
            name="Liquid Dish Soap (500ml)",
            description="Chemical dish soap in plastic bottle",
            category="Cleaning",
            material="Synthetic",
            is_eco_friendly=False,
            price=120,
            brand="Vim",
            eco_score=30
        )
        
        # Eco-friendly
        natural_detergent = Product(
            name="Natural Washing Detergent (1kg)",
            description="Biodegradable detergent made from soap nuts and herbs",
            category="Cleaning",
            material="Natural",
            is_eco_friendly=True,
            price=299,
            brand="Satopradhan",
            eco_score=87
        )
        
        eco_dish_bar = Product(
            name="Eco Dishwashing Bar",
            description="Chemical-free dishwashing bar, plastic-free packaging",
            category="Cleaning",
            material="Natural",
            is_eco_friendly=True,
            price=95,
            brand="Nimi's",
            eco_score=89
        )
        
        vinegar_cleaner = Product(
            name="White Vinegar Cleaner (500ml)",
            description="Natural all-purpose cleaner made from vinegar",
            category="Cleaning",
            material="Natural",
            is_eco_friendly=True,
            price=150,
            brand="HealthOxide",
            eco_score=90
        )
        
        # Add all products to session
        products = [
            plastic_toothbrush, disposable_razor, synthetic_soap, plastic_comb,
            bamboo_toothbrush, safety_razor, organic_soap, wooden_comb, neem_toothpaste,
            plastic_bottle, plastic_bag, plastic_straw,
            reusable_bottle, jute_bag, steel_straw, cloth_napkin, compost_bin,
            synthetic_tshirt, rubber_slippers,
            organic_tshirt, jute_slippers, khadi_fabric,
            regular_notebook, plastic_pen,
            recycled_notebook, bamboo_pen, plantable_pencil,
            chemical_detergent, plastic_dish_soap,
            natural_detergent, eco_dish_bar, vinegar_cleaner
        ]
        
        for product in products:
            db.session.add(product)
        
        db.session.commit()
        
        # Add eco metrics for all products
        metrics = [
            # Personal Care - Conventional
            EcoMetric(product_id=1, carbon_footprint=8, water_usage=500, 
                     biodegradability_score=20, recyclability_score=30, packaging_impact=25),
            EcoMetric(product_id=2, carbon_footprint=7, water_usage=400,
                     biodegradability_score=15, recyclability_score=25, packaging_impact=20),
            EcoMetric(product_id=3, carbon_footprint=6, water_usage=300,
                     biodegradability_score=35, recyclability_score=40, packaging_impact=30),
            EcoMetric(product_id=4, carbon_footprint=5, water_usage=200,
                     biodegradability_score=25, recyclability_score=35, packaging_impact=28),
            
            # Personal Care - Eco
            EcoMetric(product_id=5, carbon_footprint=2, water_usage=100,
                     biodegradability_score=95, recyclability_score=80, packaging_impact=90),
            EcoMetric(product_id=6, carbon_footprint=2, water_usage=120,
                     biodegradability_score=90, recyclability_score=90, packaging_impact=88),
            EcoMetric(product_id=7, carbon_footprint=1, water_usage=80,
                     biodegradability_score=98, recyclability_score=85, packaging_impact=92),
            EcoMetric(product_id=8, carbon_footprint=1.5, water_usage=90,
                     biodegradability_score=92, recyclability_score=82, packaging_impact=89),
            EcoMetric(product_id=9, carbon_footprint=2, water_usage=110,
                     biodegradability_score=88, recyclability_score=78, packaging_impact=84),
            
            # Kitchen - Conventional
            EcoMetric(product_id=10, carbon_footprint=10, water_usage=800,
                     biodegradability_score=10, recyclability_score=40, packaging_impact=15),
            EcoMetric(product_id=11, carbon_footprint=12, water_usage=600,
                     biodegradability_score=5, recyclability_score=20, packaging_impact=10),
            EcoMetric(product_id=12, carbon_footprint=9, water_usage=450,
                     biodegradability_score=8, recyclability_score=25, packaging_impact=12),
            
            # Kitchen - Eco
            EcoMetric(product_id=13, carbon_footprint=3, water_usage=150,
                     biodegradability_score=85, recyclability_score=95, packaging_impact=85),
            EcoMetric(product_id=14, carbon_footprint=1, water_usage=50,
                     biodegradability_score=100, recyclability_score=90, packaging_impact=95),
            EcoMetric(product_id=15, carbon_footprint=2, water_usage=100,
                     biodegradability_score=88, recyclability_score=92, packaging_impact=90),
            EcoMetric(product_id=16, carbon_footprint=1.5, water_usage=120,
                     biodegradability_score=90, recyclability_score=85, packaging_impact=88),
            EcoMetric(product_id=17, carbon_footprint=2.5, water_usage=140,
                     biodegradability_score=85, recyclability_score=80, packaging_impact=86),
            
            # Fashion - Conventional
            EcoMetric(product_id=18, carbon_footprint=15, water_usage=2000,
                     biodegradability_score=30, recyclability_score=45, packaging_impact=35),
            EcoMetric(product_id=19, carbon_footprint=8, water_usage=600,
                     biodegradability_score=28, recyclability_score=38, packaging_impact=32),
            
            # Fashion - Eco
            EcoMetric(product_id=20, carbon_footprint=3, water_usage=400,
                     biodegradability_score=95, recyclability_score=88, packaging_impact=90),
            EcoMetric(product_id=21, carbon_footprint=2, water_usage=200,
                     biodegradability_score=92, recyclability_score=85, packaging_impact=87),
            EcoMetric(product_id=22, carbon_footprint=1.5, water_usage=180,
                     biodegradability_score=98, recyclability_score=90, packaging_impact=93),
            
            # Office - Conventional
            EcoMetric(product_id=23, carbon_footprint=5, water_usage=350,
                     biodegradability_score=45, recyclability_score=50, packaging_impact=40),
            EcoMetric(product_id=24, carbon_footprint=4, water_usage=200,
                     biodegradability_score=22, recyclability_score=30, packaging_impact=25),
            
            # Office - Eco
            EcoMetric(product_id=25, carbon_footprint=2, water_usage=150,
                     biodegradability_score=90, recyclability_score=85, packaging_impact=85),
            EcoMetric(product_id=26, carbon_footprint=1.5, water_usage=100,
                     biodegradability_score=92, recyclability_score=88, packaging_impact=88),
            EcoMetric(product_id=27, carbon_footprint=1, water_usage=80,
                     biodegradability_score=100, recyclability_score=95, packaging_impact=96),
            
            # Cleaning - Conventional
            EcoMetric(product_id=28, carbon_footprint=11, water_usage=900,
                     biodegradability_score=25, recyclability_score=35, packaging_impact=28),
            EcoMetric(product_id=29, carbon_footprint=9, water_usage=700,
                     biodegradability_score=28, recyclability_score=38, packaging_impact=30),
            
            # Cleaning - Eco
            EcoMetric(product_id=30, carbon_footprint=2, water_usage=200,
                     biodegradability_score=95, recyclability_score=88, packaging_impact=90),
            EcoMetric(product_id=31, carbon_footprint=1.5, water_usage=150,
                     biodegradability_score=96, recyclability_score=90, packaging_impact=91),
            EcoMetric(product_id=32, carbon_footprint=1, water_usage=100,
                     biodegradability_score=98, recyclability_score=92, packaging_impact=92),
        ]
        
        for metric in metrics:
            db.session.add(metric)
        
        # Add product alternatives (linking conventional to eco)
        alternatives = [
            # Personal Care
            ProductAlternative(conventional_product_id=1, eco_product_id=5, similarity_score=0.85),
            ProductAlternative(conventional_product_id=2, eco_product_id=6, similarity_score=0.88),
            ProductAlternative(conventional_product_id=3, eco_product_id=7, similarity_score=0.92),
            ProductAlternative(conventional_product_id=4, eco_product_id=8, similarity_score=0.87),
            
            # Kitchen
            ProductAlternative(conventional_product_id=10, eco_product_id=13, similarity_score=0.90),
            ProductAlternative(conventional_product_id=11, eco_product_id=14, similarity_score=0.95),
            ProductAlternative(conventional_product_id=12, eco_product_id=15, similarity_score=0.89),
            
            # Fashion
            ProductAlternative(conventional_product_id=18, eco_product_id=20, similarity_score=0.88),
            ProductAlternative(conventional_product_id=19, eco_product_id=21, similarity_score=0.85),
            
            # Office
            ProductAlternative(conventional_product_id=23, eco_product_id=25, similarity_score=0.83),
            ProductAlternative(conventional_product_id=24, eco_product_id=26, similarity_score=0.86),
            
            # Cleaning
            ProductAlternative(conventional_product_id=28, eco_product_id=30, similarity_score=0.87),
            ProductAlternative(conventional_product_id=29, eco_product_id=31, similarity_score=0.89),
        ]
        
        for alt in alternatives:
            db.session.add(alt)
        
        db.session.commit()
        
        print("✅ Database populated successfully!")
        print(f"Added {len(products)} products across 5 categories")
        print(f"Added {len(metrics)} eco-metrics")
        print(f"Added {len(alternatives)} product alternatives")
        print("\n📦 Categories:")
        print("   - Personal Care: 9 products")
        print("   - Kitchen: 8 products")
        print("   - Fashion: 5 products")
        print("   - Office: 5 products")
        print("   - Cleaning: 5 products")

if __name__ == '__main__':
    populate_database()
