class IContent:
    pass

class Content(IContent):
    def __str__(self):
        return str(vars(self))
