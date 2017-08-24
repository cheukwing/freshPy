import praw

def search():
  reddit = praw.Reddit(client_id='', 
                       client_secret="",
                       user_agent='USERAGENT')

  artists_file = open("artists.txt", "r")
  for artist in artists_file:
    hasFresh = False
    names = artist.split(' / ')
    print names[0].upper().rstrip() + ":"
    
    for name in names:
      for submission in reddit.subreddit('hiphopheads').search(
                          name, time_filter="week"):
        title = submission.title
        if "[FRESH" in title:
          print "  * " + title
          hasFresh = True

    if not hasFresh:
      print "Nothing!"

def main():
  search()

if __name__ == "__main__":
  main()
