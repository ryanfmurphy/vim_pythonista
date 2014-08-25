import editor,re

def i(): # go into insert mode (so far this means nothing)
	global vmode
	vmode='insert'
def a(): # "Append", go into insert mode a space later
	fw(1)
	i()

def instxt(pos,txt): # insert text
	editor.replace_text(pos,pos,txt)

# shortcuts
getsel = editor.get_selection
getlsel = editor.get_line_selection

def o(): # open line below
	end=getlsel()[1]
	instxt(end,'\n')
	mv(end)
	i()
	
def O(): # open line above
	bgn=getlsel()[0]
	instxt(bgn,'\n')
	mv(bgn)
	i()

def csr(): # where is the cursor? return a byte/char number
	return getsel()[0]

def mvcsr(x): # move cursor
	editor.set_selection(x,x)
def fw(n): # move pythonista cursor forward n
	mvcsr(csr()+n)
def bk(n): fw(-n)

def fwtxt(): # txt after csr
	return editor.get_text()[csr()+1:]
def bktxt(): # txt b4 csr
	return editor.get_text()[:csr()]
def rbktxt(): # txt b4 cursor reversed for backwards-searching
	return ''.join(reversed(bktxt()))

def fnd(regex,txt): # shortcut for finding first regex position in txt
	return re.search(regex,txt).start()

def ch(): # current char at cursor
	return editor.get_text()[csr()]
def ws(ch): return ch in ' \t\n' # is whitespace
def isw(ch): # is word char
	return bool(re.match(r'\w',ch))

def Eamt(txt=None): # how far to move for E command
	if not txt: txt=fwtxt()
	return fnd(r'[ \t\n]',txt)+1
	#todo it should skip over ]', in the abv ln
def eamt(txt=None): # how far for e
	if not txt: txt=fwtxt()
	return fnd(r'\W',txt)+1
def wamt(txt=None): # once you go to end of word, how much further for next word?
	if not txt: txt=fwtxt()
	return fnd(r'\S',txt)+1
def W(): # move forward 1 WORD
	fw(Eamt())
	if ws(ch()): fw(wamt())
def w(): # move forward 1 word
	#if isw(ch()):
	fw(eamt())
	#else: fw(1)
	if ws(ch()): fw(wamt())
def B(): # move backwords 1 WORD #todo b/B not working properly
	bk(Eamt(rbktxt()))
	if ws(ch()): bk(wamt(rbktxt()))
def b(): # move backwards 1 word
	bk(eamt(rbktxt()))
	if ws(ch()): bk(wamt(rbktxt()))
def E(): fw(Eamt()) # end of WORD
def e(): fw(eamt()) # end of word


