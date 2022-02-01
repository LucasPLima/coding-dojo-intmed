# Calculadora

Este projeto tem como objetivo permitir a criação de calculadoras com fórmulas específicas. Esse projeto foi inspirado em uma feature de calculadora médica recentemente entregue no projeto Atlas. 


## Funcionamento

### Fluxo de utilização
* Uma calculadora é cadastrada e a ela é atribuída uma **fórmula**.
* A calculadora cadastrada também deve ter **variáveis** atribuídas a ela, que representam os valores que poderão ser recebidos para realizar o cálculo da fórmula cadastrada.
	* Cada variável tem um nome e um identificador atribuído a ela.
* Após a conclusão do cadastro, uma requisição pode ser feita passando um array de valores para que algum cálculo seja feito e um valor resultante será retornado.

## Endpoints

|Endpoint | Descrição |
|--|--|
| /calculadoras | Lista calculadoras cadastradas |
| /calculadoras/:id | Carrega uma calculadora específica |
| /calculadoras/:id/calcular | Endpoint utilizado para realizar o cálculo associado a calculadora |
| /calculadoras/:id/variaveis | Lista variaveis de uma calculadora específica |
| /calculadoras/:id/variaveis/:id_variavel | Carrega variável específica de uma calculadora |

### Informações de estruturas

#### Calculadoras
* Nome
* Descrição
* Expressão

#### Variáveis
* Nome
* Identificador
* Unidade
* Foreign Key de Calculadora Associada

### Payloads
* Para cadastrar uma calculadora, podemos utilizar a seguinte estrutura:
 `{
   "nome":"Calculadora Teste",
   "descricao": "Teste!",
   "expressao": "x + 3"
 }`
 * Para cadastrar uma variável, podemos utilizar a seguinte estrutura:
 `{
   "nome": "Peso",
    "identificador": "peso",
    "unidade": "kg",
 }`
 * Para fazer um cálculo, passamos os seguintes dados:

    `{ valores: [2, 3, 4] }`
## Validações e  casos de uso

### Calculadora
* Deve ser possível cadastrar, atualizar, deletar e visualizar as calculadoras.
* O nome da calculadora não pode ser duplicado.
* Uma calculadora só deverá realizar algum cálculo se uma **fórmula** tiver sido atribuída a ela.
* A calculadora deverá receber um array de valores que respeitem a ordem das variáveis cadastradas.

### Variáveis
* Deve ser possível cadastrar, atualizar, deletar e visualizar as variáveis.
* Variáveis podem ter identificadores semelhantes entre calculadoras, porém não podem ter nomes duplicados dentro da mesma calculadora.
* Variáveis precisam ter um identificador cadastrado.
* Em alguns casos, a ordem das variáveis importa.
* As unidades das variáveis podem ser nulas.

### Gerais
* O projeto deve seguir os conceitos do REST, portanto os *status codes* para cada operação devem ser respeitados.


> Written with [StackEdit](https://stackedit.io/).