def amount_of_pages(summary):
    pages = 0
    while summary > 0:
        pages += 1
        summary -= len(str(pages))
    return pages


sum = 11
print(amount_of_pages(sum))
