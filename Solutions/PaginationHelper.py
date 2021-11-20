import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index + 1 > self.page_count():
            return -1
        elif page_index + 1 <= len(self.collection) // self.items_per_page:
            return self.items_per_page
        else:
            return len(self.collection) % self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index + 1 > len(self.collection) or item_index < 0:
            return -1
        elif item_index + 1 >= self.items_per_page:
            return math.ceil((item_index + 1) / self.items_per_page) - 1
        else:
            return 0
