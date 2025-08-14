"""
Test script for Vehicle Registration Dashboard
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
        return True
    except ImportError as e:
        print(f"Import error: {e}")
        return False

def test_local_modules():
    """Test if local modules can be imported"""
    try:
        from data_scraper import VehicleDataScraper
        from data_processor import VehicleDataProcessor
        from utils import calculate_growth, format_number
        return True
    except ImportError as e:
        print(f"Local module import error: {e}")
        return False

def test_data_generation():
    """Test data generation functionality"""
    try:
        from data_scraper import VehicleDataScraper
        scraper = VehicleDataScraper()
        data = scraper.generate_sample_data()
        return data is not None and len(data) > 0
    except Exception as e:
        print(f"Data generation error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚗 Vehicle Registration Dashboard - Component Tests")
    print("=" * 60)
    
    tests = [
        ("Package Imports", test_imports),
        ("Local Modules", test_local_modules),
        ("Data Generation", test_data_generation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running: {test_name}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The dashboard should work correctly.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)