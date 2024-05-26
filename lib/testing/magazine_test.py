class Magazine:
    """Magazine class"""

    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Magazine name must be a string")
        if not 2 <= len(new_name) <= 16:
            raise ValueError("Magazine name must be between 2 and 16 characters long")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Magazine category must be a string")
        if len(new_category) == 0:
            raise ValueError("Magazine category must have a length greater than 0")
        self._category = new_category
