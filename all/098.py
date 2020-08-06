

from difflib import get_close_matches
  

if __name__ == "__main__": 
    referência = 'boictoe'
    palavras = ['boicote', 'boi', 'cote', 'céu', 'noite', 'foice', 'breu']
    ocorrências = 5
    similaridade = 0.5
    
    saída = get_close_matches(referência, palavras, n=ocorrências, cutoff=similaridade)
    print(saída)  # ['boicote', 'noite', 'foice', 'boi', 'cote']

    similaridade = 0.65
    saída = get_close_matches(referência, palavras, ocorrências, similaridade)
    print(saída)  # ['boicote', 'noite', 'foice']

    similaridade = 0.8
    saída = get_close_matches(referência, palavras, ocorrências, similaridade)
    print(saída)  # ['boicote']
