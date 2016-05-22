1) Escreva uma função encontra_maior_palavra() que recebe uma string contendo uma frase ou texto e retorne a maior palavra e seu tamanho.

2) Um pangrama é uma frase que contém todas as palavras do alfabeto pelo menos uma vez, por exemplo: "Juiz faz com que whisky de malte baixe logo preço de venda". Você deve escreve uma função que receba uma frase e verifica se ela é ou não um pangramas. 

3) Em criptografia uma Cifra de César é uma técnica simples de encriptação em que cada palavra de um texto é trocado por uma letra algumas posições distante seguindo o alfabeto. Por exemplo, com uma troca de 3, A seria trocado por D, B se tornaria E e assim adiante. ROT-13 ("rotacione por 13 casas") é um exemplo comum de cifra de César onde a troca é de 13. Em Python a chave do ROT-13 pode ser representada pelo seguinte dicionário:

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

Sua tarefa é implementar funções que encriptem e decriptem mensagens ROT-13. Quando terminar você poderá ler a seguinte frase secreta:

'Ubwr ru srfgn yn ab zrh NC, cbqr ncnerpre... inv ebyne ohaqn n yryr.'

4) Escreva uma função que mapeie uma lista de palavras em uma lista de inteiros o contendo o tamanho das palavras correspondentes. Bônus: escreva duas versões da função, uma usando o loop for e outra usando list comprehension.

5) O alfabeto fonético da OTAN define palavras-chave para letras do alfabeto por meio de um princípio acrofônico (Alfa para A, Bravo para B etc.) para que combinações de letras e números sejam fáceis de entender em transmissões de voz por rádio ou telefone independente de seu idioma. A seguir consta um dicionário Python com uma versão do alfabeto fonético:

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}

Escreva uma função que receba uma função que traduza uma string em palavras do alfabeto fonético da OTAN.


6) Crie uma função `troll(frase)` que, dado uma frase, altere a ordem dos caracteres de algumas palavras aleatórias (use a biblioteca `random`). Por exemplo a frase "Hoje é festa lá no meu AP" poderia ficar "Hoje é tsafe lá no eum PA".


7) Escreva uma função que, dado um texto, adicione pontos nos finais de linhas caso necessário. Por exemplo o seguinte texto:

Estou sem criatividade para criar textos
Portanto vou encher linguiça
Puts... deveria ter usado o gerador de lero-lero

Ficaria:

Estou sem criatividade para criar textos.
Vou encher um pouco de linguiça.
Puts... deveria ter usado o gerador de lero-lero.

8) Um hapáx legómenon (abreviado para hapáx) é uma palevra que aparece somente uma vez em um contexto, seja no trabalho de um autor ou em um único texto. Crie uma função que dado o nome de um arquivo de texto retorna todos seus "hapáxes". Não esqueça de fazer com que seu programa ignore caixa alta.
