import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    """
    The subclass 
    """
    def setUp(self):
        self.new_news = News("https://cdn.cnn.com/cnnnext/dam/assets/220428170659-02-willy-joseph-cancel-super-tease.jpg","headlines", "new description", "Reuby and Reuby", "2022-04-30T15:01:23Z")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))
if __name__ == "__main__":
    
    unittest.main()
        
        