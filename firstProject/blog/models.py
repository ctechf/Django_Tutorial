from django.db import models
# Create your models here.

#author_Model
class Author(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username  = models.CharField(max_length=50)
    def __str__(self):
        return self.username + " - " + self.fname + " " + self.lname #return data
    
"""
CREATE TABLE `blog_author` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `fname` varchar(50) NOT NULL, `lname` varchar(50) NOT NULL, `username` varchar(50) NOT NULL);
"""
#post_Model
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_posted = models.DateField()
    date_updated = models.DateField()
    def __str__(self):
        return str(self.id) + " - " + self.title + " " + str(self.date_updated) #return data
"""
CREATE TABLE `blog_post` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(50) NOT NULL, `content` varchar(500) NOT NULL, `date_posted` date NOT NULL, `date_updated` date NOT NULL, `author_id` integer NOT NULL);
ALTER TABLE `blog_post` ADD CONSTRAINT `blog_post_author_id_dd7a8485_fk_blog_author_id` FOREIGN KEY (`author_id`) REFERENCES `blog_author` (`id`);
"""