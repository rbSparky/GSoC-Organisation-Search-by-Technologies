import re

f = open("gsoc.txt", "r")
s = f.read() 
x = re.findall(">(.*?)<", s)
print(x)

name = []
nameb = 0
techb = 0
tech = []
topicb = 0
topics = []

j = 0
for i in x:
    if i == 'close':
        name.append(x[j-1])
        nameb = 1
        topicb = 0
    if(i == 'Technologies'):
        techb = 1
    if(i == 'Topics'):
        techb = 0
        topicb = 1
    if techb:
        tech.append(i)
    if topicb:
        topics.append(i)
    j += 1

print(name)
for i in tech:
    if i:
        if i == 'Technologies':
            print('\n' + i)
        else:
            print(i.strip(), end = ' ')
print()
for i in topics:
    if i and (i not in name):
        if i == 'Topics':
            print('\n' + i)
        else: 
            print(i.strip(), end = ' ')
print()

topics.append(1)

f = open('out.txt', 'w')
curtech, curtopic = 0, 0
html = ''
for i in range(len(name)):
    html += '<li><p><b>' + name[i] + '</b><br><b>Tags: </b>'
    for j in range(curtech+1, len(tech)):
        if(tech[j] == 'Technologies'):
            curtech = j
            break
        elif tech[j]:
            html += tech[j].strip() + ','
    html += '<br><b>Technologies: </b>'
    for j in range(curtopic+1, len(topics)-1):
        if(topics[j+1] == 'Topics'):
            curtopic = j+1
            break
        elif topics[j]:
            html += topics[j].strip() + ','
    html += '</p></li>\n'
print(html)
f.write(html)
f.close()


