from BeautifulSoup import *
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''
soup = BeautifulSoup(input)
ids=soup('id')
print ids
names=soup('name')
print names
for name in names:
    print name.contents[0]
attributes=soup('user')
print attributes
for y in attributes:
    print y.get('x',None)
for tag in ids:
    print tag.contents[0]
    for x in names:
        print x.contents[0]
        for y in attributes:
            print y.get('x',None)

# use tag.contents[0] to retrieve value of name or id
# use tag.get('x',None) to get value of attribute but first define tag using soup
