def search_books(self, search_string):
    s = search_string.lower()
    return [b for b in self.books 
            if s in b.author.lower() or s in b.title.lower()]
