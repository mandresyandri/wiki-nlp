import re

# clean text data
def regex_clean(data: list, cleaned_data = list()):
    for text in data:
        text = re.sub(r'\n', '', text)
        text = re.sub(r'\[(\d+)\]', '', text)
        text = re.sub(r'\xa0', ' ', text)
        text = re.sub(r'/[^/]+/', '', text)
        cleaned_data.append(text)

    return ''.join(cleaned_data)
