from operator import itemgetter
import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        submission_dict = {
                'title': response_dict['title'], 
                'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
                'comments': response_dict['descendants'],
                }
    except KeyError:
        print("A key is missing in this id.")
    else:
        submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
        reverse=True)

x_values = []
y_values = []
for submission_dict in submission_dicts:
    link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    x_values.append(link)
    comments = submission_dict['comments']
    y_values.append(comments)

data = {
        'type': 'bar',
        'x': x_values,
        'y': y_values,
        'marker': {
            'color': (60, 100, 150),
            'line': {'width': 1.5, 'color': (25, 25, 25)},
            },
        'opacity': 0.6,
        }
my_layout = {
        'title': 'Most active article submissions on hacker-news',
        'titlefont': {'size': 18},
        'xaxis': {
            'title': 'Article submission names',
            'titlefont': {'size': 14},
            'tickfont': {'size': 10},
            },
        'yaxis': {
            'title': 'Amount of comments',
            'titlefont': {'size': 14},
            'tickfont': {'size': 10},
            },
        }
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')
