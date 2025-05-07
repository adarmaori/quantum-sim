#!/usr/bin/env python3
import unittest
import sys
import os

def run_tests():
    # Add the current directory to the Python path so we can import our modules
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    # Discover and run all tests
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return appropriate exit code for CI
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests()) 