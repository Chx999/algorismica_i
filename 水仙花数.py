def Narcissistic_number():
    result = []
    for num in range(100,1000):
          digit1 = num // 100
          digit2 = (num // 10) % 10
          digit3 = num % 10
          if num == digit1**3 + digit2**3 + digit3**3:
                result.append(num)
    return result

print(Narcissistic_number())