

void main() {
  // o underline antes de uma variável ou método em Dart indica
  // que esse elemento é privado, e não pode ser acessado fora do módulo
  String _palavra = 'arara';
  // Chama a função e armazena o resultado em uma variável
  var _palindromo = palindromo(_palavra);
  // Uso o operador ternário para imprimir no terminal se a palavra é
  // ou não um palíndromo. Neste caso, a saída é 'É um palíndromo.'
  _palindromo ? print('É um palíndromo.') : print('Não é um palíndromo');
}

bool palindromo(String palavra) {
  var inverso = '';  // Inicializa a variável
  
  /* Opção de loop #1:

   for (var i = 0; i < palavra.length; i++) {
     inverso = palavra[i] + inverso;
   }
  
  */

  // Opção de loop # 2:
  for (var i = palavra.length - 1; i >= 0; i--) {
    inverso += palavra[i];
  }

  // Retorna o resultado da comparação
  return palavra == inverso;
}
