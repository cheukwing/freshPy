import praw

def search():
  reddit = praw.Reddit(client_id='', 
                       client_secret="",
                       user_agent='USERAGENT')

  artists_file = open("artists.txt", "r")
  for artist in artists_file:
    hasFresh = False
    names = artist.split(' / ')
    
    for name in names:
      for submission in reddit.subreddit('hiphopheads').search(
                          name, time_filter="week"):
        title = submission.title
        if "[FRESH" in title:
          if not hasFresh:
            print names[0].upper().rstrip() + ":"

          print "  * " + title
          hasFresh = True

def main():
  search()

if __name__ == "__main__":
  main()
