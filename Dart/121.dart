

void main() {

  List<int> lista = [123, 0, 5, 17, 78, 90, 26, 14, 7, 8];
  int n = 18;

  // List.where() espera uma função que retorna um valor
  // booleano como argumento:
  //  
  // bool (int test) {
  //   return n <= test; 
  // }
  lista = lista.where((test){return n <= test;}).toList();
  
  print(lista);
  // SAÍDA: [123, 78, 90, 26]
}