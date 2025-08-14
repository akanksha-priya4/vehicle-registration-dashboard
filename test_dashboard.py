"""
Test script for Vehicle Registration Dashboard
Run this to verify all components are working correctly
"""

import sys
import os

def test_imports():
    """Test if all required packages can be imported"""
    try:
        import streamlit
        import pandas
        import plotly
        import numpy
        print("✅ All required packages imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_local_modules():
    """Test if local modules can be imported"""
    try:
        from data_scraper import VehicleDataScraper
        from data_processor import VehicleDataProcessor
        from utils import calculate_growth, format_number, get_color_for_growth
        from config import DASHBOARD_CONFIG, DATA_CONFIG
        print("✅ All local modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Local module import error: {e}")
        return False

def test_data_generation():
    """Test data generation functionality"""
    try:
        from data_scraper import VehicleDataScraper
        scraper = VehicleDataScraper()
        data = scraper.generate_sample_data()
        
        if data is not None and len(data) > 0:
            print(f"✅ Data generation successful: {len(data)} records created")
            print(f"   - Columns: {list(data.columns)}")
            print(f"   - Date range: {data['date'].min()} to {data['date'].max()}")
            print(f"   - Vehicle types: {data['vehicle_type'].unique()}")
            return True
        else:
            print("❌ Data generation failed: No data created")
            return False
    except Exception as e:
        print(f"❌ Data generation error: {e}")
        return False

def test_data_processing():
    """Test data processing functionality"""
    try:
        from data_scraper import VehicleDataScraper
        from data_processor import VehicleDataProcessor
        
        # Generate test data
        scraper = VehicleDataScraper()
        data = scraper.get_data()
        
        # Process data
        processor = VehicleDataProcessor(data)
        processed_data = processor.process_data()
        
        if processed_data and 'daily_totals' in processed_data:
            print("✅ Data processing successful")
            print(f"   - Daily totals: {len(processed_data['daily_totals'])} records")
            print(f"   - Vehicle type totals: {len(processed_data['vehicle_type_totals'])} records")
            return True
        else:
            print("❌ Data processing failed: Invalid processed data structure")
            return False
    except Exception as e:
        print(f"❌ Data processing error: {e}")
        return False

def test_utility_functions():
    """Test utility functions"""
    try:
        from utils import (
            calculate_growth, format_number, get_color_for_growth,
            get_available_years, get_available_quarters, get_vehicle_categories
        )
        
        # Test growth calculation
        growth = calculate_growth(110, 100)
        assert growth == 10.0, f"Expected 10.0, got {growth}"
        
        # Test number formatting
        formatted = format_number(1500000)
        assert "1.5M" in formatted, f"Expected 1.5M, got {formatted}"
        
        # Test color assignment
        color = get_color_for_growth(5.5)
        assert color == '#28a745', f"Expected green color, got {color}"
        
        # Test available options
        years = get_available_years()
        quarters = get_available_quarters()
        categories = get_vehicle_categories()
        
        assert len(years) > 0, "No years available"
        assert len(quarters) == 4, "Expected 4 quarters"
        assert len(categories) == 4, "Expected 4 categories"
        
        print("✅ All utility functions working correctly")
        return True
    except Exception as e:
        print(f"❌ Utility function error: {e}")
        return False

def test_growth_calculations():
    """Test growth calculation algorithms"""
    try:
        from data_processor import VehicleDataProcessor
        from data_scraper import VehicleDataScraper
        
        # Generate test data
        scraper = VehicleDataScraper()
        data = scraper.get_data()
        
        # Test processor
        processor = VehicleDataProcessor(data)
        processor.process_data()
        growth_metrics = processor.calculate_growth_metrics()
        
        if growth_metrics and 'overall' in growth_metrics:
            print("✅ Growth calculations successful")
            print(f"   - Overall YoY: {growth_metrics['overall']['yoy']:.2f}%")
            print(f"   - Overall QoQ: {growth_metrics['overall']['qoq']:.2f}%")
            return True
        else:
            print("❌ Growth calculations failed: Invalid metrics structure")
            return False
    except Exception as e:
        print(f"❌ Growth calculation error: {e}")
        return False

def test_dashboard_components():
    """Test dashboard component integration"""
    try:
        from app import load_data
        
        # Test data loading function
        processor = load_data()
        
        if processor and hasattr(processor, 'processed_data'):
            print("✅ Dashboard components integrated successfully")
            return True
        else:
            print("❌ Dashboard component integration failed")
            return False
    except Exception as e:
        print(f"❌ Dashboard component error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚗 Vehicle Registration Dashboard - Component Tests")
    print("=" * 60)
    
    tests = [
        ("Package Imports", test_imports),
        ("Local Modules", test_local_modules),
        ("Data Generation", test_data_generation),
        ("Data Processing", test_data_processing),
        ("Utility Functions", test_utility_functions),
        ("Growth Calculations", test_growth_calculations),
        ("Dashboard Components", test_dashboard_components)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running: {test_name}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The dashboard should work correctly.")
        print("\nTo run the dashboard:")
        print("1. Install requirements: pip install -r requirements.txt")
        print("2. Run dashboard: streamlit run app.py")
        print("3. Or use launcher: python launch_dashboard.py")
        return True
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)