from html.parser import HTMLParser
import urllib.request
import re


def parse_all(music, theurl):
	req = urllib.request.Request(url=theurl, headers={
		'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})

	content = urllib.request.urlopen(req).read().decode('utf-8')

	tmp = content.split('llista__basica_2">')[1].split('</ul></div>')[0]
	tmp2 = tmp.split('<li><a href="')

	links = dict()
	json_header = '{"prompt":"", "completion":"'
	file = open(music + ".txt", "a", encoding="utf-8")

	for item in tmp2:
		link = item.split('"')[0]
		index = link.rfind('/')
		titol = link[index+1:]
		links[titol] = link

	links.pop('')

	for link in links:
		print(link)
		if link != 'io-cumpateshu':
			lletra = parse_url(links[link])
			if lletra != '-1':
				line = json_header + ' ' + lletra + 'END"}\n'
				file.write(line)

	file.close()

def parse_url(theurl):
	#print(theurl)
	req = urllib.request.Request(url=theurl, headers={
		'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})

	lletra = ''

	content = urllib.request.urlopen(req).read().decode('utf-8')

	if 'no disposa de lletra' in content or 'Cançó sense lletra' in content:
		lletra = '-1'
	else:
		tmp = content.split('class="enc-lletra__lletra user-text seleccionable">')[1].split('</div>')
		lletra = tmp[0].replace('<br />', '').replace('"', '\'')

	return lletra


# parse_all("palau", "https://www.viasona.cat/grup/ferran-palau/totes-les-lletres")
# parse_all("llach", "https://www.viasona.cat/grup/lluis-llach/totes-les-lletres")
# parse_all("manel", "https://www.viasona.cat/grup/manel/totes-les-lletres")
# parse_all("quimi", "https://www.viasona.cat/grup/quimi-portet/totes-les-lletres")
# parse_all("riba", "https://www.viasona.cat/grup/pau-riba/totes-les-lletres")
# parse_all("sisa", "https://www.viasona.cat/grup/sisa/totes-les-lletres")
# parse_all("celio", "https://www.viasona.cat/grup/quico-el-celio-el-noi-i-el-mut-de-les-ferreries/totes-les-lletres")
# parse_all("inadaptats", "https://www.viasona.cat/grup/inadaptats/totes-les-lletres")
# parse_all("fanegas", "https://www.viasona.cat/grup/black-fanegas/totes-les-lletres")
# parse_all("quico", "https://www.viasona.cat/grup/quico-pi-de-la-serra/totes-les-lletres")
parse_all("buhos", "https://www.viasona.cat/grup/buhos/totes-les-lletres")