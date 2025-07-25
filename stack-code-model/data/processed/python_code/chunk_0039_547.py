# Define ':' for sequencing: as a low-precedence operator that ignores operands
# and just returns the RHS.
def binary : 1 (x y) y;

# Recursive fib, we could do this before.
def fib(x)
  if (x < 3) then
    1
  else
    fib(x-1)+fib(x-2);

# Iterative fib.
def iter(x)
  var a = 1, b = 1, c in
  (for i = 3, i < x in
     c = a + b : a = b : b = c) : b;