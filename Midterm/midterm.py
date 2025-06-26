
def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    
    # write code here and update return statement with your dictionary
    frequency_dict = {}

    for tweet in tweets:                                                                # For Loop to go through each tweet in list
        if "RT @" in tweet:                                                             # Indicates a retweet
            RT_index = tweet.index("RT @")                                              # Start of ReTweet String
            colon_index = tweet.index(":")                                              # End of username
            username = tweet[(RT_index+4):colon_index]                                  # Stores username from string slice
            frequency_dict[username] = int(frequency_dict.get(username, 0)) + 1         # Adds username to dict and increments

    return frequency_dict




def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""


    ans = "" # delete this line and enter your own code

    for x in range(left, right):

        for y in range(top, bottom):

            for location in deposits:

                if location[0:2] == (x,y):
                    ans += "X"
                    break

            else:
                ans += "-"

        ans += "\n"

    return ans



def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""

    tonnage = 0

    for x in range(left, right):

        for y in range(top, bottom):

            for location in deposits:

                if location[0:2] == (x,y):
                    tonnage += location[2]
                    break

    return round(tonnage, 4)





def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    
    count = 0
    counted_list = []

    for item in dates_list:
        if dates_list.count(item)>1 and item not in counted_list:
            counted_list.append(item)
            count += dates_list.count(item)

    return count


