%{
#include "rdparser.h"
%}
%%
#		  		{ return CARDINAL; }
[0-9]{4}"-"[0-9]{2}"-"[0-9]{2}	{ return DATA; }
(?i:batismode)	  		{ return BATISMO; }
(?i:nascimentode) 		{ return NASCIMENTO; }
(?i:mae)	 		{ return MAE; }
(?i:pai)	 		{ return PAI; }
\"[^"]+\"	 		{ return PALAVRAS; }
(.|\n)				{ ; } 
%%

int yywrap(void) {
	return 1;
}
