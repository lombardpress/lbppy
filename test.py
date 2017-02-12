import lbppy

resource = lbppy.Resource.find("http://scta.info/resource/l1-cpspfs/critical/transcription")

text = resource.file_part(**{"path": "doc", "partid": "l1-cpspfs"})
print(text.transcription_type)
