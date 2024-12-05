import requests
from datetime import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')


def postTweet(content, execute_at,count):
    url = "CreateScheduledTweet"

    data = {
        "variables": {
            "post_tweet_request": {
                "auto_populate_reply_metadata": False,
                "status": content,
                "exclude_reply_user_ids": [],
                "media_ids": [],
                "thread_tweets": []
            },
            "execute_at": execute_at  
        },
        "queryId": "LCVzRQGxOaGnOnYH01NQXg"
    }

    header = {
        ''
    }

    response = requests.post(url, json=data, headers=header)
    if response.status_code == 200:
        print(count)
    else:
        print("Error:", response.status_code, response.text)

def convertTimeToTimestamp(time_str):
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    return time.timestamp()

def scheduleTweets(content_list, time):
    timestamp = convertTimeToTimestamp(time)
    for i, content in enumerate(content_list):
        execute_at = timestamp + 120 * i 
        postTweet(content, execute_at,i)

def createContentList():
    content_list = []

    #read key and hastag
    with open("kw_ht.inp", "r",encoding="utf-8") as file:
        key = file.read()

    #read content
    with open("doc.inp", "r",encoding="utf-8") as file2:
        count = 0
        for line in file2:
            content = ""
            count += 1
            content += f"{count}. " + line.strip() + "\n" + "\n" + key + "\n"
            content_list.append(content)
    
    return content_list

if __name__ == "__main__":
    content_list = createContentList()
    time = "2024-12-07 16:30"  
    scheduleTweets(content_list, time)
