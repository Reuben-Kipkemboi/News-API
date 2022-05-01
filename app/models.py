class News:
    
    '''
    Defining news objects
    '''
    def __init__(self, title, urlToImage, description,author, publishedAt, url):
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.author  = author
        self.publishedAt = publishedAt
        self.url = url
        
        
class Sources:
    
    '''
    Defining sources objects
    '''
    def __init__(self,id, name,description,category , language, country,url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.language = language
        self.country = country
        self.url = url