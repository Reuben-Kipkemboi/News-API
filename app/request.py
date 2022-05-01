from unicodedata import category
from app import app
import urllib.request,json
from .models import sources

Sources = sources.Sources
#making our api key available to be used 
news_api_key = app.config['NEWS_API_KEY']

base_news_url = app.config['NEWS_API_BASE_URL']

# NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?apiKey={}'
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
        name = single_news.get('name')
        description = single_news.get('description')
        category = single_news.get('category')
        language = single_news.get('language')
        country = single_news.get('country')
        url = single_news.get('url')
        
        if url:
            news_object = Sources(name,description,category, language, country,url) 
            news_response.append(news_object)  
 
    return news_response    
        




