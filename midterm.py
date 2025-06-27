
def count_retweets_by_username(tweets):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    
    frequency_dict = {}

    for tweet in tweets:  # For Loop to go through each tweet in list
        if "RT @" in tweet:  # Indicates a retweet
            rt_index = tweet.index("RT @")  # Start of ReTweet String
            colon_index = tweet.index(":")  # End of username
            username = tweet[(rt_index+4) : colon_index]  # Stores username from string slice
            frequency_dict[username] = frequency_dict.get(username, 0) + 1  # Adds username to dict and increment

    return frequency_dict  # Returns frequency dictionary


def display(deposits, top, bottom, left, right):
    """Display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""

    ans = ""  # Keeping ans format for output

    for x in range(left, right):  # First, go through columns

        for y in range(top, bottom):  # Then, go through rows

            for location in deposits:  # Then, go through each item in deposits

                if location[0:2] == (x,y):  # Search for matching x,y coords
                    ans += "X"  # When you get a match, mark with an 'X'
                    break  # There can only be one match per coord, so break

            else:
                ans += "-"  # If the loop makes it through with no match, mark with '-'

        ans += "\n"  # Adds a new line for the next row

    return ans  # Returns answer as a string grid


def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""

    tonnage = 0  # Establish starting variable

    for x in range(left, right):  # First, go through columns

        for y in range(top, bottom):  # Then, go through rows

            for location in deposits:  # Then, go through each item in deposits

                if location[0:2] == (x,y):  # Search for a match
                    tonnage += location[2]  # increment tonnage when match found
                    break  # break loop, when match is found

    return round(tonnage, 4)  #  return result rounded to 4 decimals


def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    
    count = 0  # Establish starting count
    counting_dict = {}  # Establish dict of counted B-days

    for item in dates_list:  # Go through each date in list

        if item not in counting_dict:
            counting_dict[item] = 1  # If date not in counting dict, add it with count 1

        else:
            counting_dict[item] += 1  # If date already counted, increment by 1


    for x in counting_dict.values():  # Loop through counted values

        # I found the Unique Pairs formula shown below from stack overflow: 
        # https://stackoverflow.com/questions/18859430/how-do-i-get-the-total-number-of-unique-pairs-of-a-set-in-the-database 
        
        count += x * (x-1) // 2  # Unique pairs formula - calculates # of unique pairs, returns integer

    return count  # Return total count

    # Explanation for O(n): I went from nested for loops to in-line for loops, this takes big theta from O(n^2) to O(2n)
    #  Because in big theta we drop the constant coefficients, this simply equates to O(n).