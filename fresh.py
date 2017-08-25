import praw

def authenticate():
  sensitive_file = open("sensitive.txt", "r")
  c_id = sensitive_file.readline().rstrip()
  c_secret = sensitive_file.readline().rstrip()
  reddit = praw.Reddit(client_id=c_id, 
                       client_secret=c_secret,
                       user_agent='USERAGENT')
  return reddit                     

def search(reddit):
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
  search(authenticate())

if __name__ == "__main__":
  main()
