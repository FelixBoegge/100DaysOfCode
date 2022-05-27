from linked_list_for_leetcode import Node
from linked_list_for_leetcode import Linked_list


class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = Node(url, None, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps:
            steps -= 1
            self.cur = self.cur.prev
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps:
            steps -= 1
            self.cur = self.cur.next
        return self.cur.val


class Node:

    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

bh = BrowserHistory("leetcode.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
print(bh.back(1))
print(bh.back(1))
print(bh.forward(1))
bh.visit("linkedin.com")
print(bh.forward(2))
print(bh.back(2))
print(bh.back(7))
