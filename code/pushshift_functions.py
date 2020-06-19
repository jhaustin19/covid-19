import pandas as pd
import requests
import time

def get_subreddit_posts(params):
    """
    Returns posts from a given subreddit as specified in params.
    """
    url = 'https://api.pushshift.io/reddit/search/submission'
    return requests.get(url, params).json()['data']


def get_all_subreddit_posts(subreddit):
    """
    Returns a list whose elements are each bundles of posts from the given
    subreddit. Every post from the subreddit should be in the bundles.
    """
    print(f'Now grabbing posts from /r/{subreddit}')
    
    # Create list to hold all the posts we acquire
    posts = []

    # Make initial pull of reddit posts. Note that setting 'after' to 0 will
    # Cause the request to pull the oldest posts on a subreddit first.
    data = get_subreddit_posts({
            'subreddit': subreddit,
            'size': 500,
            'after': 0,
    })

    # As long as the pull of posts was successful, the following should run.
    # get_subreddit_posts will return None if pull was not successful
    while data:
        posts.append(data)

        # By design, the newest post will always be from the last list in posts.
        data = get_subreddit_posts({
            'subreddit': subreddit,
            'size': 500,
            'after': max([post['created_utc'] for post in posts[-1]])
,
        })
        time.sleep(5)

    return posts


def create_posts_df(subreddit):
    """
    Returns a DataFrame representing every post from the given subreddit.
    """
    post_list = get_all_subreddit_posts(subreddit)
    df_list = [pd.DataFrame(posts) for posts in post_list]
    return pd.concat(df_list, ignore_index=True)


def create_combined_df(subreddits):
    """
    Returns a DataFrame representing every post from each of the given
    subreddits.
    
    subreddits: should be a list of strings, each string should represent a 
    valid subreddit you want to pull posts from
    """
    # Create list of dataframes to be aggregated
    dfs = []

    for subreddit in subreddits:
        # Create dataframe of posts from the given subreddit, add to dfs list
        df = create_posts_df(subreddit)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
