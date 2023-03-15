"""
5. Data Structures, 13. Stacks

Stack is a data structure. A stack of books.
Last in - First Out: LIFO

Back button in an internet browser
"""
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("Disable")
