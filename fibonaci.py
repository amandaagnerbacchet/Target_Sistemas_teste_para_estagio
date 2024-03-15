
def verifica_fibonacci(numero):
    fib1 = 0
    fib2 = 1
    
    if numero == fib1 or numero == fib2:
        return True
    
    while fib2 <= numero:
        prox_fib = fib1 + fib2
        if numero == prox_fib:
            return True
        fib1 = fib2
        fib2 = prox_fib
    
    return False

def main():
    numero = int(input())
    
    if verifica_fibonacci(numero):
        print("Pertence à sequência de Fibonacci.")
    else:
        print("Não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
