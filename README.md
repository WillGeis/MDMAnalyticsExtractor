# MDMAnalyticsExtractor

This is a basic program that extracts .msg information that can have analytics done, such as:

 - Lead time for solving an issue
 - Number of issues solved/month
 - User to solve the issue (not implemented)

This is used as Master Database Management issues are largely managed via email, which is not able to publish statistics on user tickets.

# Modifying your code to extract out of the correct folder

Programs are modified via this line in the code (messageextractor.py & messageextractorfolderfinder.py):
![image](https://github.com/user-attachments/assets/de80ab7c-3b97-4a40-afec-64503028d256)

**Note:** messageextractorfolderfinder.py is only made because of the way that I structure archives on my personal machine C:\ . . . messagefolder\datedfolder\submsgs.msg\

# Running the programs

When you have verified that you have python is on your machine by inputting this into a terminal:

```
    >python --version
```

You can run the extractors first:

```
    >py messageextractor.py
    >py messageextractorfolderfinder.py
```

Then the analytics programs

```
    >py analytics.py
    >py analyticsmodern.py
```

Realistically, if you have structured your folders differently, you can get away with just using messageextractor.py and analytics.py
