import os
import django
import json
from django.contrib.auth.models import User
from blog.models import Post

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_social.settings')
django.setup()

# Load the data from the JSON file
with open('post.json', 'r') as file:
    data = json.load(file)

# Iterate over the data and create new Post objects
for post_data in data:
    user = User.objects.get(id=post_data['user_id'])
    Post.objects.create(
        title=post_data['title'],
        content=post_data['content'],
        author=user
    )