
class Html_lists:

    def __init__(self, js: list=[], css: list=[], page: list=[]):
        """

        :param js:
        :param css:
        :param page:
        :return:
        """
        self.javaScript = js
        self.css = css
        self.page = page

    def get_js(self, jslist: list=[]):

        rList = []

        for e in self.javaScript:

            if type(e) == str:
                rList.append(e)

        for e in jslist:

            if type(e) == str:
                rList.append(e)

        return rList

    def get_css(self, csslist: list=[]):

        rlist = []

        for e in self.css:
            if type(e) == str:
                rlist.append(e)

        for e in csslist:
            if type(e) == str:
                rlist.append(e)

        return rlist

    def get_pages(self):
        """
        gets the pages list back
        :return:
        """

        rlist = []

        for e in self.page:
            if (
                type(e) == dict and
                'icon' in e.keys() and
                'text' in e.keys()
            ):
                rlist.append(e)

        return rlist
