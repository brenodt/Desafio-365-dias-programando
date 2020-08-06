import 'dart:math';

void main() {
  /*
      Ambos retornam o mesmo resultado!
  */
  var r = 35.0;
  print(area(r));  // 3848.4510006474966


  var d = 70.0;
  print(area(d, true));  // 3848.4510006474966

}

double area(double r, [bool diametro=false]) {

  r = diametro ? r / 2 : r;

  return pi * pow(r, 2);

}

