from json import loads
from os import listdir


class FileJson:

    def __init__(self, filelocal: str='./static/files/ds.json'):

        try:
            self.file_loc = filelocal

            location_list = self.file_loc.split('/')[:-1]
            location_string = "/".join([i for i in location_list])
            fname = self.file_loc.split('/')[-1]

            if fname in listdir(location_string):
                self.fileExists = True
            else:
                raise FileNotFoundError("file not Found")

        except:
            # print(error)
            self.fileExists = False

    def getfile(self):
        """
        gets the raw content as a sting
        :return:
        """

        file_str = ""

        with open(self.file_loc, mode='r') as f:
            file_str = f.read()

        f.close()

        return file_str

    def getjson(self):
        """
        gets the file from content, and loads the json content
        :return:
        """

        filestr = self.getfile()  # get the raw file content
        return loads(filestr)


class DataElemements(FileJson):

    def get_page(self, page_key: str):
        """
        get_page gets the page based on the name
        :param page_key:
        :return:
        """

        content_dict = self.getjson()  # gets the content of the file

        try:
            if 'page_{}'.format(page_key) in content_dict.keys():
                return content_dict['page_{}'.format(page_key)]['content']
            else:
                raise BaseException('page dose not exist')
        except BaseException as err:
            print(err)

    def get_nav(self):

        content_dict = self.getjson()
        return_list = []

        for e in list(content_dict.keys()):
            if 'page_' in e:
                return_list.append({
                        "text": e.split('page_')[1],
                        "icon": content_dict[e]['icon']
                    })
        if 'blog' in content_dict.keys():
            return_list.append({
                'text': 'blog',
                'icon': 'fa-newspaper-o'
            })

        return return_list

    def get_siteTitle(self):
        """
        gets the site title dynamicaly
        :return: str
        """

        content_dict = self.getjson()

        if 'site_title' in content_dict.keys():
            return content_dict['site_title']
        else:
            return 'unamed'
