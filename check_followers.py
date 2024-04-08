from bs4 import BeautifulSoup

def parse_accounts(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'lxml')
    accounts = {a.text: a['href'] for a in soup.find_all('a', href=True)}
    return accounts

# Parse the followers and following HTML files
followers = parse_accounts('followers_1.html')
following = parse_accounts('following.html')

# Find accounts you're following who aren't following you back
not_following_back = {username: url for username, url in following.items() if username not in followers}

# Print the usernames and URLs of the non-followers
print("Users you're following who aren't following you back:")
for username, url in not_following_back.items():
    print(f"{username}: {url}")

# You might also want to print the total number of such users
print(f"\n{len(followers)} followers.")
print(f"{len(following)} following.")
print(f"\nTotal: {len(not_following_back)} people don't follow you back.")



# Adjusted HTML content generation without 'date'
html_content = """
<html>
<head>
    <title>Users Not Following Back</title>
    <script>
        document.addEventListener('DOMContentLoaded', (event) => {
            document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
                const isChecked = localStorage.getItem(checkbox.id) === 'true';
                checkbox.checked = isChecked;

                checkbox.addEventListener('change', () => {
                    localStorage.setItem(checkbox.id, checkbox.checked);
                });
            });
        });
    </script>
</head>
<body>
    <h1>Users Not Following Back</h1>
    <ul>
"""

for index, (username, url) in enumerate(not_following_back.items()):
    checkbox_id = f"checkbox_{index}"
    html_content += f"<li><input type='checkbox' id='{checkbox_id}'> <a href='{url}' target='_blank'>{username}</a></li>\n"

html_content += """
    </ul>
</body>
</html>
"""

with open('not_following_back.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Exported to not_following_back.html")


