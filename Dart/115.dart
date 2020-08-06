

void main() {
  // Para 0 <= i < 101, imprimir o valor de FizzBuzz(i)
  for (var i = 0; i < 101; i++) {
    var fb = FizzBuzz(i);
    print(fb);
  }

}

String FizzBuzz(int numero) {
  var saida = '';  // Inicializando a variável de saída

  // Caso o número seja divisível por 3, adicionar 'Fizz' na saída
  if (numero % 3 == 0) {
    saida += 'Fizz';
  }
  // Caso o número seja divisível por 5, adicionar 'Buzz' na saída
  if (numero % 5 == 0) {
    saida += 'Buzz';
  }
  // Dessa forma, nos casos em que o número é divisível pelos dois,
  // não ocorrerá saídas incorretas

  /* 
    Utilizando o operador ternário para determinar o que deve ser
    retornado:

    o tamanho da variável `saida` é maior que zero?
        > Se sim, retorne `saida`
        > Se não, retorne o número convertido para texto
    
    · Operador Ternário:
    condição ? verdadeiro : falso
  */
  return saida.length > 0 ? saida : numero.toString();
}