from abc import ABC, abstractmethod

class SocialMediaPlatform(ABC): 
    @abstractmethod
    def create_post(self):
        pass
    @abstractmethod
    def share_post(self):
        pass

    @abstractmethod
    def comment_post(self):
        pass
    @abstractmethod
    def interact_with_others(self):
        pass

class Facebook(SocialMediaPlatform):
    def create_post(self, user, post):
        user.add_post(post)
        print(f"{user.name} created new post - {post.post_content}")


    def share_post(self, user,  post):
        user.add_post(post)
        print("You shared the post - {post.post_content}")

    def comment_post(self, post):
        print("You commented the post - {post.post_content}")

    def interact_with_others(self, user1, user2):
        print("You are interacted with {user2.name}")

class Post(ABC):
    def __init__(self, user, post_content, post_date):
        self.user = user
        self.post_content = post_content
        self.post_date = post_date

    @abstractmethod
    def post_type(self):
        pass

class TextPost(Post):
    def post_type(self):
        print("Text post")

class PhotoPost(Post):
    def post_type(self):
        print("Photo post")
    

class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.posts = []

    def add_post(self, post):
        self.posts.append(post.post_content)

class Comment:
    def __init__(self, user, comment_content, comment_date):
        self.user = user
        self.comment_content = comment_content
        self.comment_date = comment_date

user1 = User("User1", "Phone")
user2 = User("user2", "Mail")

post1 = TextPost(user1, "text", 27)
post2 = PhotoPost(user2, "photo", 20)

facebook = Facebook()
facebook.create_post(user1, post2)
facebook.create_post(user1, post1)
facebook.share_post(user1, post2 )

print(user1.posts)
