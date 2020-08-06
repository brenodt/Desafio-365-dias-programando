// A função main() sempre deve estar presente e
// executa o código do restante do sistema, como 
// é em outras linguagens, como C ou Java 
void main(List<String> arguments) {
  print('Hello world!');  // Toda declaração deve terminar em ';'
  contaParesImpares(lista);
  /*
      Saída no terminal:
      >>Hello world!
      >>Número de Pares: 5
      >>Número de Ímpares: 3
  */
}

// Aqui é declarada uma variável fora do escopo
// principal. Imagine que vem de fora do código
List<int> lista = [1, 10, 3, 27, 6, 70, 48, 20];

// Declaramos a função executada
void contaParesImpares(List<int> lista) {
  var pares = 0;  // variáveis internas podem ter o tipo omitido
  var impares = 0;

  for (var i = 0; i < lista.length; i++) {
    if (lista[i] % 2 == 0) {
      pares++;
    } else {
      impares++;
    }
  }

  print('Número de Pares: ${pares} \nNúmero de Ímpares: ${impares}');
}

