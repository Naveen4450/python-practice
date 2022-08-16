class book():
    def __init__(self,title,author,publisher,price,royality):
        self.author=author
        self.publisher=publisher
        self.price=price
        self.royality=royality
        self.title=title
    def get_author(self):
        return self.author
    def get_publisher(self):
        return self.publisher
    def get_price(self):
        return self.price
    def get_royality(self):
        return self.royality
    def get_title(self):
        return self.title
    def set_author(self,author):
        self.author=author
        return
    def set_publisher(self,publisher):
        self.publisher=publisher
        return
    def set_price(self,price):
        self.price=price
        return
    def set_royality(self,royality):
        self.royality=royality
        return
    def set_title(self,title):
        self.title=title
        return
    def royality(self,copies):
        if(copies<=500):
            return 0.1*self.price*copies
        if(copies>500 and copies<=1000):
            return 0.1*self.price*500+1.25*self.price*(copies-500)
        if(copies>1000):
            return 0.1*self.price*500+1.25*self.price*(copies-500)+1.5*self.price*(copies-1500)
class ebook(book):
    def __init__(self,title,author,publisher,price,royality,format):
        super().__init__(title,author,publisher,price,royality)
        self.format=format
    def set_format(self,format):
        self.format=format
        return
    def get_format(self):
        return self.format
    def royality(self,copies):
        return 0.88+super().royality(copies)
            

