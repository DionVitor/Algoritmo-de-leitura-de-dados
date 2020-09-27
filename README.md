# Análise de dados

## O objetivo do programa é saber qual a a sequência de 5 letras alfabéticas exclui o mínimo de palavras possíveis de um banco de dados. Em que, se a letra estiver na sequência, ela excluirá todas as palavras do banco de dados que contenham essa letra, e assim acontece com as próximas 4 letras.

Exemplificando, se a sequência de letras for: 'a', 'b', 'c', 'd', 'e'. A palavra Amor será excluida, pois ela possui uma letra proibida, o 'a'. Já se a palavra for Óculos, ela não será excluída, pois não tem nenhuma letra da sequência de letras.

Em síntese, existem milhões de arrays iguais (que excluem o mesmo número de palavras do banco de dados), por isso, algumas arrays devem ser desconsideradas.

Como por exemplo as arrays: ['a', 'b', 'c', 'd', 'e'] e ['a', 'b', 'c', 'e', 'd'], em que cada array tem o mesmo resultado para 120 outras arrays (5!).

E também existem as arrays de letras iguais, a qual não devem ser consideradas, pois não retornam um resultado de análise de 5 letras de fato.

Como por exemplo a array: ['a', 'a', 'a', 'a', 'a'] ou ['a', 'a', 'c', 'd', 'e'], em que a primeira só retorna o número de palavras sem o 'a', e a segunda que retorna apenas o número de palavras sem 'a', 'c', 'd' e 'e'.
