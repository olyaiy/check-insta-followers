# Instagram Unfollower Tracker

A simple and legal tool to check who doesn't follow you back on Instagram, designed to ensure your account remains in good standing by complying with Instagram's terms of use.

## Getting Started

This tool helps you identify Instagram followers who don't reciprocate your follow. Unlike other platforms that might risk your account by violating Instagram's terms of service with automated requests, this project operates entirely offline, using data directly downloaded from your Instagram account.

### Prerequisites

To use this tool, you'll need:

- Python 3
- `beautifulsoup4` and `lxml` libraries installed in Python
- Your Instagram followers and following information in HTML format

### Installation

1. Ensure you have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the required Python libraries by running:
  ```pip install beautifulsoup4 lxml```

3. Download your Instagram Information File by visiting https://www.instagram.com/download/request/ and following the instructions provided by Instagram.

### Usage

1. Once you have your Instagram data:
- Locate the followers_1.html and following.html files within the downloaded zip file.
- Place these files in the same directory as the check_followers.py script.

2. Run the script using:
```python check_followers.py```
or
```python3 check_followers.py```
 depending on the version of python installed

4. The script will output a list of users you're following who aren't following you back, a link to their page, a checkbox next to each user which remembers its state, along with the total counts for followers, following, and non-reciprocal follows.

### Why Did I make this?

Instagram employs sophisticated algorithms to detect automation and non-human behavior. Using unauthorized tools to track unfollowers can lead to account restrictions or even permanent bans. This project allows you to safely manage your followers list without risking your account, by analyzing

This tool was created with the intent to comply with Instagram's terms of use and ensure the longevity of your account. It uses the Instagram Information File, which Instagram is obliged to provide under Article 15 of the General Data Protection Regulation (GDPR). By performing all actions offline and avoiding mass unfollow actions, it aims to prevent any negative consequences such as temporary blocks or permanent bans on your Instagram account.

