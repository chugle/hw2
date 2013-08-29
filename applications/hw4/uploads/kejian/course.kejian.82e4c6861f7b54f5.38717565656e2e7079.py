def conflict(state, nextX):
  nextY = len(state)
        for i in  range(nextY):
          if abs(state[i]-nextX) in (0, nextY-i):
            return True
        return False




def queens(num=8, state=()):
  for pos in range(num):
    if not conflict(state, pos):
      # print "sss",state
                        if len(state) == num-1:
                          # print "aaaa",(pos,),"\n"
                                yield (pos,)
                        else:
                          for result in queens(num, state + (pos,)):
                            #  print "bbbb",result
                                        yield  result+(pos,)


queens()

