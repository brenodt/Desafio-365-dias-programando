const List<String> ALFABETO = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g',
  'h', 'i', 'j', 'k', 'l', 'm', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u',
  'v', 'w', 'x', 'y', 'z'
];

void main() {
  var p = 'Hello World!';
  var espelho = espelhaPalavra(p);
  print(espelho);  // svool dliow!
  p = 'ABC';
  espelho = espelhaPalavra(p);
  print(espelho);  // zyx
}

String espelhaPalavra(String palavra) {
  String palavraEspelhada = '';
  for (var indice = 0; indice < palavra.length; indice++) {
    var letra = palavra[indice].toLowerCase();
    if (ALFABETO.contains(letra)) {

      int indiceInverso = abs(ALFABETO.indexOf(letra) - 25);
      
      palavraEspelhada += ALFABETO[indiceInverso];
      
    }
    else {
      palavraEspelhada += letra;
    }
  }
      
  return palavraEspelhada;
}
      
int abs(int i) {
  return i < 0?-i:i;
}

