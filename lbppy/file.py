import lbppy
import urllib

class File():
    def __init__(self, file_path, transcription_type, confighash):
        self.file_path = file_path
        self.confighash = confighash
        if (self.confighash != None):
            self.stylesheets = self.confighash["stylesheets"]

        self.transcription = transcription_type
        #if (self.confighash != nil):
        #	self.xslt_dir = "#{@confighash[:xslt_base]}#{@xslt_version}/#{@transcription_type}/"

    def file(self):
        response = urllib.request.urlopen(self.file_path)
        # this conditional is needed for private repos requring basic auth
        #if (response.base_uri.to_s != self.file_path):
            #response = urllib.request.urlopen(self.file_path, {:http_basic_authentication => [self.confighash["git_username"], self.confighash["git_password"] ]})

        return response
