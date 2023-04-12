from github import Github, GithubException
import datetime
import time

# Step 1: Install PyGithub library using pip
# pip install PyGithub

# Step 2: Authenticate with GitHub API
access_token = "your_access_token_here"
g = Github(access_token)

# Step 3: Connect to GitHub API and get list of users you are following
user = g.get_user()
following = user.get_following()

# Step 4: Unfollow each user and handle rate limits
for user in following:
    try:
        g.get_user().remove_from_following(user)
    except GithubException as e:
        if e.status == 403:
            reset_time = g.get_rate_limit().core.reset
            time_to_wait = reset_time - datetime.datetime.now(datetime.timezone.utc)
            time.sleep(time_to_wait.total_seconds())
