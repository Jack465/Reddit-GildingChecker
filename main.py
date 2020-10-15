# This was a test project I did for something posted in r/requestabot, I never finished it but it might work. use at own risk idc.

import praw

# Variables
targetSubreddit = "askreddit"
flairOne = "d97f5f6a-ddf4-11ea-bb0b-0e0b84a570ed"
flairTwo = "ddba2a42-ddf4-11ea-99cb-0e685b3b3d2"

reddit = praw.Reddit(client_id='###',
                client_secret='###',
                user_agent='script testing',
                username='###',
                password='###')

posts = reddit.subreddit("askreddit").top("week", limit=10)

for post in posts:
    try:
        try: # theres probably a short hand way to do this, but this was the quick solution I thought of.
            platnium = post.gildings['gid_3']
        except KeyError:
            platnium = "0"
        if post.gildings['gid_2'] is not None or platnium is not 0:
            #reddit.subreddit(targetSubreddit).flair.set(post.author, "", flairOne)
           # print("Changed flair for user {}".format(post.author))

            print("{} by {} has {} gold {} platnium".format(post.id, post.author, post.gildings['gid_2'], platnium))
    except KeyError:
        pass
