__author__ = 'aviram'

class Crowdmap():
    def __init__(self, l_post):
        self.posts_list = l_post

    def get_all_posts_for(self, name):
        list_of_posts = list()
        for l in self.posts_list:
            if name in l:
                list_of_posts.append(l)
        return list_of_posts

    def is_location_for_name(self, name):
        return True