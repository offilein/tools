import webbrowser


#print(webbrowser._browsers)
browser = webbrowser.get('firefox')

urls = ['https://www.youtube.com/', 'https://twitter.com/', 'https://www.reddit.com/', 'https://www.twitch.tv/', 'https://github.com/']

first = True
for url in urls:
    if first:
        browser.open_new(url)
        first = False
    else:
        browser.open_new_tab(url)

