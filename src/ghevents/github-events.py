#!/usr/bin/env python
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    text = requests.get(url).text
    events = json.loads(text)
    return events

def print_events(events, n=5):
    """Print the first n GitHub events as type and repository name."""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    """Retrieve and print GitHub events for the configured user."""
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()