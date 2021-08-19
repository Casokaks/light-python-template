"""
Test module
==================================

Author: Casokaks (https://github.com/Casokaks/)
Created on: Aug 15th 2021

"""

from unittest import TestCase
from .test_config import TEST_CONFIG
# import package to test

class TestSomething(TestCase):
    """Test Class."""
    
    def get_test_config(self, t=TEST_CONFIG):
        """Empty test."""
        return t
    