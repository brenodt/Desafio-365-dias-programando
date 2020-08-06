import 'dart:math';

void main() {
  var v = 5;

  print(somaDeQuadradosUM(v));
  print(somaDeQuadradosDOIS(v));
  /*
      Ambos chegam no mesmo resultado: 55
  */
}

int somaDeQuadradosUM(int n) {
  if (n > 0) {
    var numerosAteN = Iterable.generate(n + 1);
    return numerosAteN.reduce((soma, numero) => soma + pow(numero, 2));
  }
  else {
    return 0;
  }
}

int somaDeQuadradosDOIS(int n) {
  int soma = 0;
  if (n > 0) {
    for (int i = 1; i <= n; i++) {
      soma += pow(i, 2);
    }
  }
  return soma;
}
