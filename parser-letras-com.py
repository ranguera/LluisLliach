from html.parser import HTMLParser
import urllib.request
import re



# class MyHTMLParser(HTMLParser):
# 	prev_tag = ""
# 	opened = False
# 	song = ""
#
# 	def handle_starttag(self, tag, attrs):
# 		#print("Encountered a start tag:", tag)
# 		self.prev_tag = tag
# 		for attr in attrs:
# 			if(attr[0] == 'id'):
# 				if(attr[1] == 'HOTWordsTxt'):
# 					self.opened = True
#
# 	def handle_endtag(self, tag):
# 		#print("Encountered an end tag :", tag)
# 		self.prev_tag = ''
# 		if(tag == 'div'):
# 			self.opened = False
#
# 	def handle_data(self, data):
# 		#print("Encountered some data  :", data)
# 		if(self.opened and self.prev_tag != 'span'):
# 			print(data.strip())
# 			self.song += data.strip().lower() + '\n'
#
#
text_file = open('musica2.txt', "a", encoding='utf-8')
#
def cleanbr(raw_html):
	cleanr = re.compile('<br>')
	cleantext = re.sub(cleanr, '\n', raw_html)
	return cleantext

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext.replace('(adsbygoogle = window.adsbygoogle||[]).pauseAdRequests=1;(adsbygoogle = window.adsbygoogle||[]).push({});', '')

def parse_url(url):
	contents = urllib.request.urlopen(url).read().decode('utf-8')
	tmp = contents.split('<main')[1].split('<i>musica.com</i>')[0]
	lletra_bruta = tmp.split('alt=\"\" width=\"13\" height=\"12\">')[1]
	lletra = cleanhtml(cleanbr(lletra_bruta))
	print(lletra)
	print('_'*80)
	text_file.write(lletra+"\n\n\n\n")

def parse_all():
	links = open('data/links/musica-com2.txt', 'r', encoding='utf-8').read().split('<li>')
	i=1
	for link in links:
		tmp = link.split('<p>')[0].split('\"')[1]
		print(str(i) + ': ' + tmp)
		i+=1
		parse_url(tmp)

#song = parse_url('http://www.coveralia.com/letras/a-ti-mujer-camela.php')
parse_all()
# text_file.close()