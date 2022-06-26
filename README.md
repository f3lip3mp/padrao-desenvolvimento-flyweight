# Flyweight - Structural (Estrutural)

## Intenção

*Flyweight é um padrão de projeto estrutural que tem a intenção de usar compartilhamento para suportar eficientemente grandes quantidades de objetos de forma granular.*

---

## Sobre o Flyweight

O Flyweight visa dividir um objeto em dois estados: o estado intrínseco e o estado extrínseco.

O estado **intrínseco** de um objeto é a parte que nunca muda ou muda poucas vezes dentro do sistema. Por exemplo, imagine um objeto de endereço de um cliente com os seguintes dados: rua, número, bairro, cidade, cep, complemento, etc... O estado intrínseco deste objeto seriam as coisas que podem se repetir de cliente para cliente. Pense comigo, se vários clientes são do mesmo bairro, sabemos que outros dados também não mudam, como cidade e cep. Esses são parte do estado intrínseco do objeto de endereço.

Por outro lado temos o estado **extrínseco**. Esse estado mantém dados que estão constantemente variando. No caso do endereço, o número, o complemento e os dados do cliente mudam para cada localização. Esses valores podem ser movidos para fora do objeto a fim de liberar a memória que podem consumir.

A solução que o Flyweight entrega é bastante intuitiva: 

- separe o estado do objeto em **intrínseco** e **extrínseco**
- mantenha o estado **intrínseco** dentro do objeto de forma imutável, já que ele será compartilhado com outros objetos
- quando necessário, receba o restante dos dados (o estado **extrínseco**) no método que precisar desses dados
- para evitar a duplicação de objetos flyweight, usa-se uma fábrica que verifica se um flyweight precisa ser criado ou se foi criado anteriormente.

Apesar de intuitivo, isso gera bastante complexidade no sistema, por isso é necessário analisar com cuidado essa situação. Ao separar o estado de um objeto, precisaremos de uma forma de unir esses dados novamente no momento do uso. 

---

## Aplicabilidade

Só use o Flyweight quanto TODAS as condições a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de objetos;
- os custos de armazenamento são altos por causa da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar extrínsecos;
- muitos objetos podem ser substituídos por poucos objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

## Consequências

O que é bom ou ruim no Flyweight:

**Bom:**
- economiza memória RAM

**Ruim:**
- Pode gerar outros problemas de desempenho não relacionados com a RAM
- Seu código vai se tornar muito complexo