# test_syncthegraph.py
"""
Tests for SyncTheGraph module.
"""

import unittest
from syncthegraph import SyncTheGraph

class TestSyncTheGraph(unittest.TestCase):
    """Test cases for SyncTheGraph class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SyncTheGraph()
        self.assertIsInstance(instance, SyncTheGraph)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SyncTheGraph()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
