from html.parser import HTMLParser
import urllib.request
import html

def parse_all(music, theurl):
	file = open("poemes.txt", "a", encoding="utf-8")
	json_header = '{"prompt":"", "completion":"'

	for i in range(3246,4825):
		lletra = html.unescape(parse_url("https://www.versos.cat/poema/" + str(i) + "/"))
		lletra = lletra.split('</h1>')[1].replace('\t', '').replace('\r', '')
		print(lletra)
		line = json_header + ' ' + lletra + ' END"}\n'
		file.write(line)

	file.close()

def parse_url(theurl):
	#print(theurl)
	req = urllib.request.Request(url=theurl, headers={
		'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})

	lletra = ''

	content = str(urllib.request.urlopen(req).read(), 'utf-8')

	if 'poema no trobat' in content:
		lletra = '-1'
	else:
		tmp = content.split('<h1 class="titol-poema" itemprop="name">')[1].split('</div>')
		lletra = tmp[0].replace('<br />', '\n').replace('"', '\'').replace('<em>','').replace('</em>','').replace('<p>','').replace('</p>','')

	return lletra



# https://www.versos.cat/poema/4825/
parse_all("a", "a")