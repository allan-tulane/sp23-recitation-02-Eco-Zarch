"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):

  if n == 1:
    return 1
  else: 
    return a * simple_work_calc(n/b, a, b) + n

def test_simple_work():
  
  assert simple_work_calc(16, 2, 2) == 80
  assert simple_work_calc(4, 3, 2) == 19
  assert simple_work_calc(8, 4, 2) == 120
  
  # Additional test cases
  assert simple_work_calc(2, 2, 2) == 4
  assert simple_work_calc(27, 4, 3) == 175
  assert simple_work_calc(32, 3, 2) == 665

def work_calc(n, a, b, f):
  
  if n <= 1:
    return f(n)
  else:
    return a * work_calc(n/b, a, b, f) + f(n)

def span_calc(n, a, b, f):
  
  if n <= 1:
    return f(n)
  else:
    return a * span_calc(n/b, a, b, f) + 1

def test_work():
  
  assert work_calc(10, 2, 2,lambda n: 1) == 31
  assert work_calc(20, 1, 2, lambda n: math.log(n)) == 7.577185932924767
  assert work_calc(30, 3, 2, lambda n: n) == 623.4375
  
  # Additional Test Cases
  assert work_calc(4, 4, 4,lambda n: 1) == 5
  assert work_calc(8, 4, 2, lambda n: math.log(n)) == 18.71497387511852
  assert work_calc(32, 3, 2, lambda n: n) == 665

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  
  result = []
  for n in sizes:
    # compute S(n) using current a, b, f
    result.append((
      n,
      span_fn1,
      span_fn2
    ))
    return result


def print_results(results):
  print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))


def test_compare_work():
  
  work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: 1)
  work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n)
  
  res = compare_work(work_fn1, work_fn2)
  print_results(res)
  
def test_compare_span():
  assert span_calc(10, 2, 2, lambda n: 1) == 31
  assert span_calc(30, 3, 4, lambda n: n) == 25.65625
  
  span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)
  span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n)
  
  res = compare_work(span_fn1, span_fn2)
  print_results(res)
  