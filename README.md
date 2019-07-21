# WordPlease
A blog platform with an API REST enterely made with Django

## For initiate the project:

```shell
pip install -r requirements.txt
```
and
```shell
python manage.py createsuperuser
```

## When running the project, we can use the URLS:


### Web
```shell
http://127.0.0.1:8000/
```


### API

```shell
http://127.0.0.1:8000/api/posts
```
GET: This url will return all posts if we are logged as superuser, if not we will have to add a blog parameter, as in this case <http://127.0.0.1:8000/api/posts/?blog=pedro>
Adding this parameter we will visualize all the posts of this blog that have been publicated, unless we identify ourselves as the owner or the blog (or a superuser), in this case the API will return all the posts, included those that are not publicated yet.
POST: Creting a new post. For this action we have to be authenticated.

```shell
http://127.0.0.1:8000/api/posts/<post-id>
```
GET: We will get the detail of the post (if it's publicated yet, we are the author or a superuser)
PUT: Will update the post (if we are the author or superuser)
DELETE: Will delete the post (if we are the author or superuser)

```shell
http://127.0.0.1:8000/api/blogs
```
GET: This url will return the list of blogs with the names and URLs of these, GET will be the only method accepted


```shell
http://127.0.0.1:8000/api/users
```
GET: This url will return a list of users in the case of being a superuser.
POST: It allows the creation of new users without the need of being authenticated.

```shell
http://127.0.0.1:8000/api/users/<user-id>
```
GET: We will get the detail of the user (if we are the user or a superuser)
PUT: Will update the user (if we are the user or a superuser)
DELETE: Will delete the user (if we are the user or a superuser)
