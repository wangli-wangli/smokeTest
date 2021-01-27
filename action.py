from baseUse import baseUse
class action():
    def __init__(self, HOSTNAME, Authorization):
        self.HOSTNAME = HOSTNAME
        self.Authorization = Authorization
        self.baseUse=baseUse(self.HOSTNAME, self.Authorization)
    def login(self):
        path = '/passport-service/getSigByUser'
        ContentType = "application/json;charset=UTF-8"
        method="get"
        params = None
        result=self.baseUse.useApi(path, ContentType, params,method)
        code=result
        print(code)
