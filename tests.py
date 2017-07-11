import unittest

from app import Html_lists
from app.sitedata import FileJson, DataElemements
from app.blog import BlogWorker

class TestAppHtml(unittest.TestCase):

    def test_init(self):
        """
        testing the init function which tests the
        assignments of values i the creation of the object.
        :return:
        """

        jsList = ['testjs']
        cssList = ['testcss']
        pageList = ['testPage']

        htmlinit = Html_lists(jsList, cssList, pageList)

        self.assertEqual(
            htmlinit.javaScript,
            jsList
        )

        self.assertEqual(
            htmlinit.css,
            cssList
        )

        self.assertEqual(
            htmlinit.page,
            pageList
        )

    def test_get_js(self):
        """
        testing the get js method
        :return:
        """

        jsList = ['testjs']
        cssList = ['testcss']
        pageList = ['testPage+']

        htmlel = Html_lists(jsList, cssList, pageList)

        self.assertEqual(  # test the returning elements with out arguments
            type(htmlel.get_js()),
            list
        )

        self.assertEqual(  # test the returning elements wit aguments
            type(htmlel.get_js(['test'])),
            list
        )

        self.assertEqual(  # test content
            htmlel.get_js(),
            jsList
        )

        self.assertEqual(
            htmlel.get_js(['test the thing']),
            ['testjs', 'test the thing']
        )

    def test_get_css(self):
        """
        testing the get js method
        :return:
        """

        jsList = ['testjs']
        cssList = ['testcss']
        pageList = ['testPage+']

        htmlel = Html_lists(jsList, cssList, pageList)

        self.assertEqual(  # test the returning elements with out arguments
            type(htmlel.get_css()),
            list
        )

        self.assertEqual(  # test the returning elements wit aguments
            type(htmlel.get_css(['test'])),
            list
        )

        self.assertEqual(  # test content
            htmlel.get_css(),
            cssList
        )

        self.assertEqual(
            htmlel.get_css(['test']),
            ['testcss', 'test']
        )

    def test_get_page(self):
        """
        tests the get page methods
        :return:
        """

        htmlel = Html_lists(page=[{'text': 'testtext', 'icon': 'icon'}])
        testingobj = htmlel.get_pages()

        self.assertEqual(
            testingobj,
            [{'text': 'testtext', 'icon': 'icon'}]
        )

        pass

class TestSiteDataFileJson(unittest.TestCase):

    def test_init(self):

        file_ds = './static/files/test-ds.json'
        json_file = FileJson(file_ds)

        self.assertEqual(
            json_file.file_loc,
            file_ds
        )

    def test_getFile(self):

        file_ds = './static/files/test-ds.json'
        json_file = FileJson(file_ds)

        self.assertEqual(
            type(json_file.getfile()),
            str
        )

    def test_getjson(self):

        file_ds = './static/files/test-ds.json'
        json_file = FileJson(file_ds)

        self.assertEqual(
            type(json_file.getjson()),
            dict
        )

class TestDataElemements(unittest.TestCase):

    def test_get_page(self):

        dEle = DataElemements('./static/files/test-ds.json')
        content = dEle.get_page('main')
        self.assertEqual(
            dEle.get_page('main'),
            content
        )

    def test_get_nav(self):

        dEle = DataElemements('./static/files/test-ds.json')
        content = dEle.get_nav()

        self.assertEqual(
            content,
            dEle.get_nav()
        )

    def test_get_siteTitle(self):
        dEle = DataElemements('./static/files/test-ds.json')
        content = dEle.get_siteTitle()

        self.assertEqual(
            type(content),
            str
        )

class Test_blogWorker(unittest.TestCase):

    def test_init(self):
        fileLocalation = './static/files/test.db'
        blogworker = BlogWorker(fileLocalation)

        self.assertEqual(
            blogworker.file,
            fileLocalation
        )

    def test_post(self):
        fileLocalation = './static/files/test.db'
        blog = BlogWorker(fileLocalation)

        self.assertEqual(
            blog.post('title', 'message'),
            True
        )

    def test_get(self):
        fileLocalation = './static/files/test.db'
        blog = BlogWorker(fileLocalation)

        a = blog.get()

        self.assertEqual(
            type(a),
            list
        )

        for e in a:
            self.assertEqual(
                type(e),
                dict
            )

            self.assertEqual(
                list(e.keys()),
                ['post_title', 'post', 'date']
            )

if __name__ == '__main__':
    unittest.main()
