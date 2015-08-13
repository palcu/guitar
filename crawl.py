import markdown2

html_content = ""
with open("README.md") as songs_in_markdown:
    html_content = markdown2.markdown(songs_in_markdown.read())

with open("offline/index.html", "w") as songs_in_html:
    songs_in_html.write(html_content)
