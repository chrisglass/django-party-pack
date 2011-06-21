from django.db import models

class Poll(models.Model):
    """An individual poll to be tested"""
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
           return self.question    

class Choice(models.Model):
    """Choices on a poll"""
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    def __unicode__(self):
            return self.choice    