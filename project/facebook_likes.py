import urllib2
import json
from pprint import pprint

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,link&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "flipkart" # username or id
token = "EAACEdEose0cBAMizvPd0ngoq5k3u2ZAuSZCPoDPTkwRKup524Y4QS5UujlvLvBov5P6cczuNluRdrzmjQBlhO6ZBvUkZB67KfFV96qk904sQ0i8ktH8FzXGcYOEFnaP1VCqXVa7gaZCpAZBflMRxKcZAjTSkuO0FDq4Dtn0KoMsXwZDZD"  # Access Token
page_data = get_page_data(page_id,token)
pprint (page_data)

iid=str(page_data['id'])
print iid
print "Page Name:"+ page_data['name']
print "Likes:"+ str(page_data['likes'])
print "Link:"+ page_data['link']


