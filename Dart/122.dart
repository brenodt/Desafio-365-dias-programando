

import 'dart:math';

void main() {
  int tamanhoDaLista = 10;
  int potencia = 3;

  List<int> numeros = List.from(Iterable.generate(tamanhoDaLista));

  print(cubo(numeros, potencia));
  // Saída:
  // [[0, 0], [1, 1], [2, 8], [3, 27], [4, 64], [5, 125], 
  //  [6, 216], [7, 343], [8, 512], [9, 729]]
}

List<List> cubo(List<int> n, int potencia) {
  List<List> saida = [];

  for (var item in n) {
    saida.add([item, pow(item, potencia)]);
  }
  return saida;
}