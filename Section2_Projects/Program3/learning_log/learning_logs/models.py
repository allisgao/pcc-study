from django.db import models

# Create your models here.

class Topic(models.Model):
    """ user learining topic"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return model's string expression"""
        return self.text


class Entry(models.Model):
    """ details of a topic"""
    #topic = models.ForeignKey(Topic)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'


    # def __str__(self):
    #     """ return models' string expression"""
    #
    #     return self.text[:50] + "..."


    def __str__(self):
        """ return models's string express"""
        show_text = ''
        if len(self.text) > 50:
            show_text = self.text[:50] + " ..."
        else:
            show_text = self.text

        return show_text











