"""This script uses the Bisection Method to find the root of a continuous function (f(x)) within a given interval. """

def main(f, a, b, Ex, Ef):
    if f(a) * f(b) >= 0: # Verify Bolzano's conditions
        print("Error. f(a) * f(b) should be < 0.")
        return
    
    n = 0
    while True:
        m = (a + b)/2
        n += 1
        print(f"{n}, {a:.4f}, {b:.4f}, {m:.4f}, {f(a):.4f}, {f(b):.4f}, {f(m):.4f}")
        if (b-a)/2 < Ex or abs(f(m)) < Ef: # Stopping criteria
            print(f"The estimated root is {m}")
            break
        else:
            if f(m) * f(a) > 0:
                a = m
            elif f(m) * f(b) > 0:
                b = m

f = lambda x: (x ** 3) - 1 # A sample function to test the algorithm: f(x) = x^3 - 1

a = float(input("Enter lower bound (a): "))
b = float(input("Enter upper bound (b): "))
Ex = float(input("Enter error tolerance for x (Ex): "))
Ef = float(input("Enter error tolerance for f(x) (Ef): "))
main(f, a, b, Ex, Ef)