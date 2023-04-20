calculator: y.tab.c lex.yy.c
	gcc y.tab.c lex.yy.c -w

lex.yy.c: calculator.l
	flex calculator.l

y.tab.c: calculator.y
	bison -dy calculator.y