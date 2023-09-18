import re
ignore_messages = ['Media Omitted']

def parse_whatsapp_conversation(conversation):
    messages = []
    buffer = []
    for line in conversation:
        # Check if the line starts with a date pattern
        match = re.match(r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} - ', line)
        if match:
            if buffer:
                # Save the message from the buffer
                messages.append(parse_message(''.join(buffer)))
                buffer = []
        buffer.append(line)
    if buffer:
        messages.append(parse_message(''.join(buffer)))

    return messages

def parse_whatsapp_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return parse_whatsapp_conversation(lines)

def parse_message(message):
    date_pattern = r'(?P<date>\d{1,2}/\d{1,2}/\d{2,4}), (?P<time>\d{1,2}:\d{2})'
    author_pattern = r'- (?P<author>.*?):'
    content_pattern = r'- .*?: (?P<content>.*)'

    date_match = re.search(date_pattern, message)
    author_match = re.search(author_pattern, message)
    content_match = re.search(content_pattern, message)

    content = content_match.group('content').strip() if content_match else None

    # Remove the unwanted phrases from content
    for phrase in ignore_messages:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        content = pattern.sub("", content)

    parsed_message = {
        'timestamp': f"{date_match.group('date')} {date_match.group('time')}" if date_match else None,
        'author': author_match.group('author') if author_match else None,
        'content': content
    }

    return parsed_message
