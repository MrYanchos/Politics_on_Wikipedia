'''
Extracts a validation set in using "bias" comments in XML data.
'''


in_text = False # True if currently reading the <text> portion of a revision
upcoming = False # True if one has passed a comment containing "bias," - pay attention to next <text>
current_text = '' # Keeps track of most recent text

output_file = 'pairs.txt'
file = open(output_file, 'w')

def first_text_extractor(line, first):
    '''
    Extracts text from XML when <text... or </text> is expected, otherwise unneeded
    First=True if you expect it the line to begin with <text..., First=False if you expect </text>
    '''
    output_text = ''
    if first:
        line_without_info = line.split(">")[1:]
    else:
        line_without_info = line.split("</text>")[:-1]
    for i in line_without_info:
        output_text += i
    return output_text

def differences(prev, curr):
    '''
    Returns the set difference between two strings (split by sentences). Returns two differences.
    First is sentences unique to first parameter, second is sentences unique to second parameter.
    '''
    output_biased = ''
    output_unbiased = ''
    prev = set(prev.split("."))
    curr = set(curr.split("."))
    for i in prev.difference(curr):
        output_biased += i
        output_biased += '.'
    for i in curr.difference(prev):
        output_unbiased += i
        output_biased += '.'
    return output_biased, output_unbiased

with open('simplewiki-20201101-pages-meta-history.xml', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if '</text>' in line: 
            in_text = False
            current_text += first_text_extractor(line, False)
            
            if upcoming:
                upcoming=False
                biased,unbiased = differences(previous_text, current_text)
                to_write = biased + "^^^^^" + unbiased
                file.write(to_write)
            continue
        if '<text' in line:
            in_text = True
            current_text = first_text_extractor(line, True)
            continue
        if in_text:
            current_text += line
            continue
        
        if '<comment>' in line: # note: comments appear before the text
            if 'bias' in line.lower(): #so current text is actually the previous text
                previous_text = current_text
                upcoming = True

file.close()