# encoding: utf-8

import sys
import csv
import jieba
import jieba.posseg as pseg

def main():
	reload(sys)
	sys.setdefaultencoding( "utf-8" )
	
	# with open('wipo--20161021.csv','r') as f,open('name.csv','w') as g:
	# 	reader=csv.reader(f)
	# 	writer=csv.writer(g)
	# 	for  line in reader:
	# 		writer.writerow([''.join(line[-1])])

	# names=set()
	# with open('name.txt','r') as f,open('name(unique).txt','w') as g:
	# 	for line in f:
	# 		names.add(line.strip())
	# 	print(len(names))
	# 	for each in names:
	# 		g.write(each+'\n')

	wordList = []
	file = open(r'name(unique).txt' , 'r').read()
	words = list(pseg.cut(file))	
	for w in words:
		wordList.append(w.word)
	wordDict = {}
	wordSet = set(wordList)
	for word in wordSet:
		wordDict[word] = wordList.count(word)
	wordDict = sorted(wordDict.iteritems(), key=lambda d:d[1], reverse = True)
	# print wordDict
	file = open('wordcount.txt','w')
	for word in wordDict:
		#print(json.dumps(word[0], ensure_ascii=False, encoding='UTF-8')) ,word[1]
		file.write(word[0])
		file.write(" ")
		file.write(str(word[1]))
		file.write("\n")
	file.close()

if __name__ == '__main__':
	main()