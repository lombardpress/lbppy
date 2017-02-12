import lbppy

resource = lbppy.Resource.find("http://scta.info/resource/lectio1/critical")

print(resource.title())
