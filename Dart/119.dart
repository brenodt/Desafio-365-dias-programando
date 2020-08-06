

import 'dart:math';  // Usaremos a função sqrt() desse pacote

void main() {
  // Saída: [3, 5, 7, 11, 13, 17, 19]
  print(numerosPrimos(2, 23).toString());
}

// Retorna uma lista de números inteiros
List<int> numerosPrimos(int inicio, int fim) {
  List<int> saida = List<int>();  // inicializa variável de saída

  // Avalia se o intervalo é válido
  if (inicio <= fim && inicio > 1 && fim > 1) {

    for (var numero = inicio; numero < fim; numero++) {
      var ultimoValor = sqrt(numero) + 1;  // calcula o último valor
      var primo = true;  // inicia considerando que o número é primo

      for (var divisor = 2; divisor < ultimoValor; divisor++) {
        if (numero.remainder(divisor) == 0) {  // caso seja divisível
          primo = false;  // o número não é primo
          break;  // finaliza o loop
        }
      }
      // Caso chegue aqui com primo == true, o número é primo
      if (primo) {
        saida.add(numero);  // Adicionamos o número no final da saída
      }
    }
  } 
  return saida;
}