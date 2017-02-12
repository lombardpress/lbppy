import lbppy
class ResourceIdentifier():
    def __init__(self, url):
        self.url = url
        #self.short_id = url.split("resource/").last

    def to_s(self):
        self.url

    def resource(self):
        lbppy.Resource #need class level method here called "find"
