class Article:
    all = []

    def __init__(self, author, magazine, article_name):
        self.author = author
        self.magazine = magazine
        self.article_name = article_name
        Article.all.append(self)

    @property
    def article_name(self):
        return self._article_name
    
    @article_name.setter
    def article_name(self, new_article_name):
        if hasattr(self, "article_name"):
            AttributeError("Article name cannot be changed")
        else:
            if isinstance(new_article_name, str):
                if 5 <= len(new_article_name) <= 50:
                    self._article_name = new_article_name
                else:
                    ValueError("Article name must be between 5 and 50 characters")
            else:
                TypeError("Article name must be a string")
            
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            TypeError("Author must be an instance of Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("Magazine must be an instance of Magazine")
            
    def __repr__(self):
       return f'<Article: author={self.author.name}, magazine={self.magazine.name}, article_name="{self.article_name}">'
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name can't be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                TypeError("Name must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, article_name):
        return Article(self, magazine, article_name)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None
        
    def __repr__(self):
        return f'<Author: name={self.name}>'

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")   
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")   

    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        article_titles = [article.article_name for article in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None

    def contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author)   
        if (list_of_authors):
            return list_of_authors
        else:
            return None

    def __repr__(self):
        return f'<Magazine: name={self.name}, category={self.category}>'
