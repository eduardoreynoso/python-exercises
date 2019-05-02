import requests
import re


if __name__ == '__main__':
    response = requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
    source = response.text
    source = source.replace('Donald Trump', 'Puppies')

    source = re.sub('<img.*?src=".*?"', '<img src="https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12193133/German-Shepherd-Puppy-Fetch.jpg"', source)

    with open('my_page.html', 'w+') as f:
        f.buffer.write(source.encode('utf-8'))
