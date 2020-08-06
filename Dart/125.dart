

void main() {
  List<int> minhaLista = [1, 0, 2, 3, 2, 4, 0, 1, 7, 8, 4, 3, 2, 0, 1];
  
  // Saída >> [1, 0, 2, 3, 2, 4, 0, 1, 7, 8, 3, 2, 0, 1]
  print(removeEnesimo(minhaLista, 4, 2));
  
}

List<int> removeEnesimo(List<int> lista, int elemento, int ocorrencia) {
  if (lista.where((n) => n == elemento).length >= ocorrencia) {
    var conta = 0;
    for (var i = 0; i < lista.length; i++) {
      if (lista[i] == elemento) {
        conta++;
      }

      if(conta == ocorrencia) {
        lista.removeAt(i);
        break;
      }
    }
  }
  return lista;
}
