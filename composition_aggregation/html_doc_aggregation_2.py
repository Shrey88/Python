"""
   Aggregation: (has a relationship)

    aggregration is similar  and consider as weak form of composition
    now each composition the object that another object is composed of does not exist outside of the container
"""


class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title):
        super().__init__('head', '')

        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)

"""
    so here we are completely removing the composition and going to add aggregation
"""


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


"""
    so compared to composition, aggregation also behaves like has a relationship.
    instead of creating the objects of head, body and doctype in the __init__ method of the HtmlDoc
    we have created them separately and passed to the constructor of HtmlDoc object, so the class is rewritten 
    making the difference between the composition and aggregation more obvious.
    
    so my_page has still got doctype, head, body; it's just that what owns the object has changed now 
    so even if we delete the my_page object we can still use the independent objects of doctype head and body.
    
"""
if __name__ == '__main__':
    # my_page = HtmlDoc('Document Title')
    # my_page.add_tag('h1', 'Main Heading')
    # my_page.add_tag('h2', 'sub-heading')
    # my_page.add_tag('P', 'This is a paragraph that will appear on the page')
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)

    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances "
                     " of objects to build up another object.")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it;s composed of "
                     " - if it;s destroyed, those objects continue to exist")

    new_doctype = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_doctype, new_header, new_body)

    with open('test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)
