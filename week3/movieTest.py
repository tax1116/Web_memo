from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


all_movie = list(db.movies.find())
target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
#print (target_movie['star'])

for movie_compare in all_movie:
    if movie_compare['star'] == target_movie['star']:
        db.movies.update_one({'title': movie_compare['title']}, {"$set": {'star': 0}})
        print(movie_compare['title'])
## 코딩 할 준비 ##