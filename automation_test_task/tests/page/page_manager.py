class PagesManager(object):

    def __init__(self, driver):

        self.driver = driver

    def create_page(self, class_):
        return class_(
            self.driver
        )
