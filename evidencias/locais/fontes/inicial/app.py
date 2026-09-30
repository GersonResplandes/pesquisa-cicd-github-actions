from decimal import Decimal, ROUND_HALF_UP

def total(preco, quantidade):
    if not isinstance(quantidade, int) or isinstance(quantidade, bool) or quantidade < 1:
        raise ValueError("quantidade deve ser inteiro positivo")
    valor = Decimal(str(preco))
    if not valor.is_finite() or valor < 0:
        raise ValueError("preco deve ser finito e nao negativo")
    return (valor * quantidade).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
