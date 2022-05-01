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