import random
import statistics

baseNationalEnvironment = -1.31 

historicalAdjustment = 1.2 

enthusiasmMax = 0 

enthusiasmMin = -4.5 

pvi = [-35.7,-34.7,-32.7,-31.7,-30.7,-29,-28.7,-28.7,-27.7,-27.7,-26.7,-26.7,-26,-25.7,-25.7,-25.7,-25.7,-25,-24.7,-24.7,-24.7,-24.7,-24.7,-24.7,-24.7,-24,-24,-23.7,-23.7,-23.7,-23.7,-23.7,-23.7,-23.7,-23,-22.7,-22.7,-22.7,-22.7,-22,-22,-21.7,-21.7,-21.7,-21.7,-21.7,-21.7,-21.7,-21.7,-21.7,-21.7,-20.7,-20.7,-20.7,-20.7,-20.7,-20.7,-20.7,-20.7,-20.7,-20.7,-20.7,-19.7,-19.7,-19.7,-19.7,-19.7,-19.7,-18.7,-18.7,-18.7,-18.7,-18.7,-18.7,-18.7,-18.7,-18.7,-18.7,-18.7,-18.7,-17.7,-17.7,-17.7,-17.7,-17.7,-17.7,-17.7,-17.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16.7,-16,-16,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15.7,-15,-14.7,-14.7,-14.7,-14.7,-14.7,-14.7,-14.7,-14.7,-13.7,-13.7,-13.7,-13.7,-13.7,-13.7,-13.7,-13.7,-13.7,-13.7,-13.7,-12.7,-12.7,-12.7,-12.7,-12.7,-12.7,-12,-12,-11.7,-11.7,-11.7,-11.7,-11.7,-11.7,-11.7,-11.7,-11.7,-11.7,-11,-11,-11,-10.7,-10.7,-10.7,-10.7,-10.7,-10.7,-10.7,-10.7,-10.7,-9.7,-9.7,-9.7,-9.7,-9.7,-9.7,-9.7,-9,-8.7,-8.7,-8.7,-8.7,-8,-8,-7.7,-7.7,-7.7,-7.7,-7,-6.7,-6.7,-6,-6,-6,-5.7,-5.7,-5.7,-5.7,-5.3,-5,-5,-4.7,-4.7,-4.7,-4,-4,-4,-3.3,-3.3,-3,-3,-3,-2.7,-2.7,-2.7,-2,-1.7,-1.3,-1,-1,-0.7,-0.7,-0.3,-0.3,0,0,0,0.7,0.7,0.7,1,1,1.3,1.7,1.7,1.7,2,2,2,2,2.3,2.7,3,3.7,3.7,3.7,3.7,3.7,4,4,4,4,4,4.7,4.7,4.7,5,5.7,5.7,5.7,5.7,5.7,5.7,5.7,5.7,5.7,5.7,5.7,6,6.7,6.7,6.7,6.7,7,7.7,7.7,7.7,7.7,7.7,7.7,8,8.7,8.7,8.7,8.7,8.7,8.7,9,9,9.7,9.7,9.7,9.7,9.7,9.7,9.7,9.7,9.7,10.7,10.7,10.7,10.7,10.7,10.7,11.7,11.7,11.7,11.7,11.7,11.7,11.7,12.7,12.7,12.7,13.7,13.7,13.7,13.7,13.7,13.7,14,14.7,14.7,14.7,14.7,14.7,14.7,14.7,14.7,15.7,15.7,15.7,15.7,15.7,15.7,15.7,16,16,16.7,16.7,16.7,16.7,16.7,16.7,16.7,16.7,17.7,17.7,17.7,17.7,17.7,17.7,17.7,18.7,18.7,19.7,19.7,19.7,19.7,19.7,19.7,20,20,20.7,20.7,20.7,20.7,20.7,20.7,20.7,21,21.7,21.7,21.7,21.7,22,22,22.7,22.7,22.7,22.7,23,23.7,23.7,23.7,24,24.7,24.7,24.7,24.7,25.7,25.7,25.7,25.7,25.7,25.7,26.7,26.7,26.7,27,27.7,27.7,27.7,27.7,27.7,28,28.7,28.7,28.7,28.7,28.7,28.7,29.7,29.7,30.7,30.7,30.7,31.7,31.7,32.7,32.7,32.7,32.7,33.7,34,34.7,34.7,34.7,37,37.7,37.7,37.7,38.7,38.7,39.7,40,40.7,41.7,42.7]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def simNatlEnv(baseEnv):
  error = 0.5 * baseEnv
  errorAdj = random.uniform(-error, error)

  historicalAdj = random.uniform(-historicalAdjustment, historicalAdjustment)
  
  enthusiasmAdj = random.uniform(enthusiasmMin, enthusiasmMax)

  natlEnv = baseNationalEnvironment + errorAdj + historicalAdj + enthusiasmAdj

  return natlEnv

def election(baseEnvironment):
  nationalEnvironment = simNatlEnv(baseEnvironment)
  demSeats = 0;
  for x in pvi:
    swingAdj = random.uniform(-5.0, 5.0)
    race = x + nationalEnvironment + swingAdj 
    if race == 0:
      race = random.choice([-1, 1])
      print("coin flipped.")
    if race > 0:
      demSeats += 1
  return demSeats

def simulate(env):
  demWins = 0
  gopWins = 0
  
  numSeats = []
  
  i = 100000

  for x in range(i):
    result = election(env)
    numSeats.append(result)
    if result >= 218:
      demWins += 1
    else:
      gopWins += 1
  average = int(sum(numSeats)/(i))
  numSeats.sort()
  median = numSeats[int(i/2)]
  mode = statistics.mode(numSeats)
  min = numSeats[0]
  max = numSeats[i-1]
  bottom = numSeats[int(0.1*i)]
  top = numSeats[int(i-(0.1*i)-1)]

  print("H̲o̲u̲s̲e̲")
  print("Democrats win " + str((demWins/(i/100))) + " in 100 times")
  print("Republicans win " + str((gopWins/(i/100))) + " in 100 times")
  print("Average seats: " + str(average) + "D—" + str(435-average) + "R")
  print("Median seats: " + str(median) + "D—" + str(435-median) + "R")
  print("Mode seats: " + str(mode) + "D—" + str(435-mode) + "R") 
  print("Minimum seats: " + str(min) + "D—" + str(435-min) + "R") 
  print("Maximum seats: " + str(max) + "D—" + str(435-max) + "R") 
  print("Top bound: " + str(top) + "D—" + str(435-top) + "R") 
  print("Bottom bound: " + str(bottom) + "D—" + str(435-bottom) + "R") 

simulate(baseNationalEnvironment)
