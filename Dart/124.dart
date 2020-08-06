


void main() {

  print(fatorial(6));  // Saída: 720
}

int fatorial(int n) {
  // Eliminando valores que não 
  // devem ser calculados
  if (n < 0) {
    return -1;
  }


  if (n==0 || n==1) {
    return 1;
  }
  return n * fatorial(n - 1);
}