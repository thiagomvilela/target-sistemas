def fibonacci(num):
    """Função que retorna uma lista com a sequência de Fibonacci até o número informado."""
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return fib

def pertence_fibonacci(num):
    """Função que verifica se o número informado pertence à sequência de Fibonacci."""
    fib = fibonacci(num)
    if num in fib:
        print(f"{num} pertence à sequência de Fibonacci: {fib}")
    else:
        print(f"{num} não pertence à sequência de Fibonacci: {fib}")

# Exemplo de uso:
pertence_fibonacci(13)