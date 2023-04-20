%{
#include <stdio.h>
#include <string.h>
#include "y.tab.h"

%}

%option noyywrap

%%

[0-9]+          {yylval.value = atof(yytext); return VALUE;}
[0-9]+"."[0-9]+ {yylval.value = atof(yytext); return VALUE;}
"+"             {return PLUS;}
"-"             {return MINUS;}
"/"             {return DIVIDE;}
"*"             {return TIMES;}
"%"             {return MODULO;}
"^"             {return POWER;}
"("             {return LEFT;}
")"             {return RIGHT;}
[ \t]           {}
"\n"            {return DONE;}
.               {printf("Invalid Expression Entered: "); return 0;}

%%