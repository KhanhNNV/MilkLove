import requests
from datetime import datetime
import random
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')


def readHeader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        curl_command = file.read()

    headers = {}
    header_pattern = r"-H '([^:]+): ([^']+)'"
    matches = re.findall(header_pattern, curl_command)

    for match in matches:
        header_name, header_value = match
        headers[header_name.strip()] = header_value.strip()

    return headers

def postTweet(content, execute_at,count,header):
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

    response = requests.post(url, json=data, headers=header)
    if response.status_code == 200:
        print(count)
    else:
        print("Error:", response.status_code, response.text)

def convertTimeToTimestamp(time_str):
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    return time.timestamp()

def scheduleTweets(content_list, time,header):
    timestamp = convertTimeToTimestamp(time)
    for i, content in enumerate(content_list):
        randomTime=random.choice([120, 180, 240, 300])
        if (i==0):
            execute_at=timestamp
        else:
            execute_at = timestamp + randomTime
            timestamp=execute_at
        postTweet(content, execute_at,i,header)

def createContentList(fileKey,fileContent):
    content_list = []

    #read key and hastag
    with open(fileKey, "r",encoding="utf-8") as file:
        key = file.read()

    #read content
    with open(fileContent, "r",encoding="utf-8") as file2:
        count = 0
        for line in file2:
            content = ""
            count += 1
            content += f"{count}. " + line.strip() + "\n" + "\n" + key + "\n"
            content_list.append(content)
    
    return content_list
def readTime(file_path):
    with open(file_path, 'r') as file:
        time = file.readline().strip()
    return time
if __name__ == "__main__":
    content_list = createContentList("kw_ht.inp","test.inp")
    header = readHeader("header.inp")
    time = readTime("time.inp")
    scheduleTweets(content_list, time,header)
    
