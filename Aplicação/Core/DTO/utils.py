def copiar_atributos_de_instancia(origem, destino):
    """
    Copia todos os atributos de instância (dados) de um objeto para outro.

    Parâmetros:
    - origem: objeto de onde os dados serão copiados.
    - destino: objeto que receberá os dados copiados.

    Observações:
    - Apenas atributos armazenados em `__dict__` são copiados.
    - Métodos e atributos de classe não são afetados.
    - Atributos com o mesmo nome no destino serão sobrescritos.
    """
    for chave, valor in origem.__dict__.items():
        setattr(destino, chave, valor)