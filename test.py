import lbppy

resource = lbppy.Resource.find("http://scta.info/resource/lectio1/critical/transcription")

# call for file part with specified kwargs
#text = resource.file(**{"path": "doc", "partid": "l1-cpspfs"})
title = resource.file().editor()
print(title)
