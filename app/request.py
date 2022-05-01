# from app import app
import urllib.request,json
from .models import News
from .models import Sources

# Sources = sources.Sources
# News = news.News
#making our api key available to be used 
# news_api_key = app.config['NEWS_API_KEY']
news_api_key = None
# base_news_url = app.config['NEWS_API_BASE_URL']
base_news_url = None

# articles_url = app.config['SOURCE_ARTICLES_URL']
articles_url = None

def configure_request(app):
    global news_api_key,base_news_url, articles_url
    news_api_key = app.config['NEWS_API_KEY']
    base_news_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['SOURCE_ARTICLES_URL']

def get_news(sources):
    """
    getting news from different sources
    """
    get_news_url = base_news_url.format(sources,news_api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_results = json.loads(get_news_data)
        
        news_response = None
        if get_news_results['sources']:
            news_results_list = get_news_results['sources']
            news_response = process_results(news_results_list)
    return news_response
#processing the results
def process_results(news_sources_list):
    #news sources object
    
    news_response = []
    for single_news in news_sources_list:
        
        id =single_news.get('id')
        name = single_news.get('name')
        description = single_news.get('description')
        category = single_news.get('category')
        language = single_news.get('language')
        country = single_news.get('country')
        url = single_news.get('url')
        if url:
            news_object = Sources(id,name,description,category, language, country, url) 
            news_response.append(news_object)  
 
    return news_response  

def get_article(id):
    get_article_details_url = articles_url.format(id, news_api_key)
   
    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)
        
        article_object = None
        if article_details_response['articles']:
            article_details_results_list = article_details_response['articles']
            article_object = process_news_articles(article_details_results_list)
             
    return article_object 

def process_news_articles(articles_list):
    '''
    method for processing the response we get after requesting for articles .....
    '''
    articles_results = []
    for single_article in articles_list:
            title = single_article.get('title')
            urlToImage = single_article['urlToImage']
            description = single_article.get('description')
            author = single_article.get('author')
            publishedAt = single_article.get('publishedAt')
            url = single_article.get("url")
            
            if urlToImage:
                article_object = News(title, urlToImage, description,author,publishedAt,url)
                articles_results.append(article_object)
            
    return articles_results

     
            
        




