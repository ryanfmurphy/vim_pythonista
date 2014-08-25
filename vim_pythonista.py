import editor,re

def i():
	global vmode
	vmode='insert'
def a():
	fw(1)
	i()

def instxt(pos,txt):
	editor.replace_text(pos,pos,txt)

getsel = editor.get_selection
getlsel = editor.get_line_selection

def o():
	end=getlsel()[1]
	instxt(end,'\n')
	mv(end)
	i()
	
def O():
	bgn=getlsel()[0]
	instxt(bgn,'\n')
	mv(bgn)
	i()

def csr():
	return getsel()[0]

def mvcsr(x): # move cursor
	editor.set_selection(x,x)
def fw(n):
	mvcsr(csr()+n)
def bk(n): fw(-n)

def fwtxt(): # txt after csr
	return editor.get_text()[csr()+1:]
def bktxt(): # txt b4 csr
	return editor.get_text()[:csr()]
def rbktxt():
	return ''.join(reversed(bktxt()))

def fnd(regex,txt):
	return re.search(regex,txt).start()

def ch():
	return editor.get_text()[csr()]
def ws(ch): return ch in ' \t\n'
def isw(ch):
	return bool(re.match(r'\w',ch))

def Eamt(txt=None):
	if not txt: txt=fwtxt()
	return fnd(r'[ \t\n]',txt)+1
	#todo it should skip over ]', in the abv ln
def eamt(txt=None):
	if not txt: txt=fwtxt()
	return fnd(r'\W',txt)+1
def wamt(txt=None):
	if not txt: txt=fwtxt()
	return fnd(r'\S',txt)+1
def W():
	fw(Eamt())
	if ws(ch()): fw(wamt())
def w():
	#if isw(ch()):
	fw(eamt())
	#else: fw(1)
	if ws(ch()): fw(wamt())
def B(): #todo bB not working properly
	bk(Eamt(rbktxt()))
	if ws(ch()): bk(wamt(rbktxt()))
def b():
	bk(eamt(rbktxt()))
	if ws(ch()): bk(wamt(rbktxt()))
def E(): fw(Eamt())
def e(): fw(eamt())


