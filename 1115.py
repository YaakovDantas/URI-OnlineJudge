for i in range (10000):
  x, y = map(int,raw_input().split())
  if x == 0 or y == 0:
    break
  elif x > 0 and y > 0:
    print "primeiro"
  elif x < 0 and y > 0:
    print "segundo"
  elif x < 0 and y < 0:
    print "terceiro"
  else:
    print "quarto"
    
