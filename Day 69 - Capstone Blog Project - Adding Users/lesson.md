
# 1. Creating Relational Databases

Given that the 1st user is the admin and the blog owner. It would make sense if we could link the blog posts they write to their user in the database. 
In the future, maybe we will want to invite other users to write posts in the blog and grant them the admin privileges.

So we need to create a relationship between the <User> table and the <BlogPost> table to link them together. 
So we can see which <BlogPosts> a <User> has written. Or see which <User> is the author of a particular <BlogPost>.

# If we were just writing Python code, you could imagine creating a User object which has a property called posts that contains a List of BlogPost objects.

e.g.

class User:
    def __init__(self, name, email, password):
         self.name = name
         self.email = email
         self.password = password
         self.posts = []
 
class BlogPost:
    def __init__(self, title, subtitle, body):
         self.title = title
         self.subtitle = subtitle
         self.body = body
 
new_user = User(
    name="Angela",
    email="angela@email.com",
    password=123456,
    posts=[
        BlogPost(
            title="Life of Cactus",
            subtitle="So Interesting",
            body="blah blah"
        )
    ]        
}

This would make it easy to find all the BlogPosts a particular user has written. But what about the other way around? 
How can you find the author of a particular BlogPost object? 
This is why we're using a database instead of just simple Python data structures.

# In relational databases such as SQLite, MySQL or PostgreSQL we're able to define a relationship between tables using a <ForeignKey> and a <relationship()> method.

e.g. If we wanted to create a <One to Many> relationship between the <User> Table and the <BlogPost> table, where One <User> can create many <BlogPost> objects, we can use the SQLAlchemy docs to achieve this.

https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html


# 2. A new database schema

CHALLENGE 1: Modify the class <User>(UserMixin, db.Model)  and class <BlogPost>(db.Model) code to create a bidirectional <One-to-Many> relationship between the two tables. 
The <User> should be the parent and the <BlogPost> will be child. 
You should be able to easily locate the <BlogPosts> a <User> has written and also the <User> of any <BlogPost> object.

Note, you will be changing the schema here by adding an <foreign key>, the <author_id>. 
This will be a breaking change. The blog website will not work after you have made this change.

# 3. Re-create the database with a new admin user and posts

Our old database is no longer compatible with the new database structure - there are no entries for author_id in the old posts.
Our new code in the main.py modifies our database model by adding a new column into our database that was not present in the original <blog.db>  

There is no need to preserve the sample data and testing data so we will delete the database and create a new one from scratch. 
However, this raises an important point: database schemas need to be defined early during the development process. 
Once an application has launched and accumulated lots of data, you will need to preserve this data by migrating to the new database. 
Lucky for us, we can leave out the migration step.