class Course():
    def __init__(self,id,name,short_description,date,language,purpose,chapter,requirement,description,target,price,promotion,info,categories):
        self._id = id
        self._name = name
        self._short_description = short_description
        self._date = date
        self._language = language
        self._purpose = purpose
        self._chapter = chapter
        self._requirement = requirement
        self._description = description
        self._target = target
        self._price = price
        self._promotion = promotion
        self._info = info
        self._categories = categories
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def short_description(self):
        return self._short_description
    @property
    def date(self):
        return self._date
    @property
    def language(self):
        return self._language
    @property
    def purpose(self):
        return self._purpose
    @property
    def chapter(self):
        return self._chapter
    @property
    def requirement(self):
        return self._requirement
    @property
    def description(self):
        return self._description
    @property
    def target(self):
        return self._target
    @property
    def price(self):
        return self._price
    @property
    def promotion(self):
        return self._promotion
    @property
    def info(self):
        return self._info
    @property
    def categories(self):
        return self._categories

