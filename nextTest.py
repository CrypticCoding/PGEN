from tinydb import TinyDB, Query
db = TinyDB('output.json')
newQuery = Query()

table = db.table('accounts')
#db.search(User.name == 'John')


i=0

file = open ('file.txt', 'r')

f = file.readlines()
