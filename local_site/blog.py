from tinydb import TinyDB
from tinydb import Query
from datetime import date


class BlogWorker:

    def __init__(self, file: str = "./static/files/blog.db"):
        self.file = file

    def _makeTimeStamp(self):
        """
        makes a time stamp for the day
        :return:
        """

        raw = date.today()

        return f"{raw.day}/{raw.month}/{raw.year}"

    def post(self, title: str, post: str):
        """
        adds a new row to posts
        :param title:
        :param post:
        :return:
        """
        db = TinyDB(self.file)
        table_db = db.table('post')
        table_db.insert({
            'title': title,
            'content': post,
            'date': self._makeTimeStamp()
        })

        db.close()
        return True

    def get(self):
        """
        getts all posts
        :return:
        """

        db = TinyDB(self.file)
        table_db = db.table('post')

        data = []
        for e in table_db.all():
            data.append({
                'post_title': e['title'],
                'post': e['content'],
                'date': e['date'],
                'id': e.eid
            })

        db.close()

        return data

    def get_single(self, eid: int):

        db = TinyDB(self.file)
        table_db = db.table('post')

        return table_db.get(eid=int(eid))