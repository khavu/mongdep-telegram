"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests
import database


def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['source'])
    database.insert_db(table_name='thichngammong', values=post['source'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/

access_token = 'EAACEdEose0cBABtL9VWVoxZB8YzByjZBZC3lHnJ3EjWAUDHtkwI0B3QzhKZAHiSWyhGxfT7S7DaqZBAiQDNqAJgCEQklmzjSeaSWI2ezYQmm631Hsc6pEboXkJS6CJ7ZCrFeePDbPYhFctNbxXYcDKrQoxA6oQ290xSYJV0K2eVZCHjECjwm1uwpix53ImZB5esZD'
user = 'thichngammong'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'photos/uploaded')

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break

