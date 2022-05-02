import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    """
    The subclass 
    """
    def setUp(self):
        self.new_Source = Sources("cnn","CNN News", "new description", "Business", "en", "Qatar", "https...")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Source, Sources))
if __name__ == "__main__":
    
    unittest.main()