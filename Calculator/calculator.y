%{
#include <stdio.h>
#include <string.h>
int yywrap( );
void yyerror(const char* str);
double result = 0;
%}

%union {
  double value;
}

%token <value> VALUE
%token PLUS
%token MINUS
%token DIVIDE
%token TIMES
%token MODULO
%token LEFT  //parentheses
%token RIGHT  //parentheses
%token POWER
%token DONE
%token UMINUS
%token UPLUS

%left PLUS MINUS 
%left DIVIDE TIMES MODULO
%right POWER
%left LEFT RIGHT
%left UMINUS UPLUS

%type <value> statement expression

%%

statement: expression DONE {result = $1; return 0;}

expression: VALUE                         {$$ = $1;}
          | expression PLUS expression    {$$ = $1 + $3;}
          | expression MINUS expression   {$$ = $1 - $3;}
          | expression TIMES expression   {$$ = $1 * $3;}
          | expression DIVIDE expression  {$$ = $1 / $3;}
          | expression MODULO expression  {$$ = fmod($1, $3);}
          | expression POWER expression   {$$ = pow($1, $3);}
          | LEFT expression RIGHT         {$$ = $2;}
          | MINUS expression %prec UMINUS {$$ = -$2;}
          | PLUS expression %prec UPLUS   {$$ = +$2;}
          ;

%%

int yywrap( ) {
  return 1;
}

void yyerror(const char* str) {
  fprintf(stderr, "Compiler error: '%s'.\n", str);
  exit(1);
}

int main( ) {
  while(1) {
    printf("Enter Mathematical Expression: ");
    yyparse( );
    printf("Result = %lf\n", result);
  }
  return 0;
}
