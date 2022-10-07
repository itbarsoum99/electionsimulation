import random
import statistics

baseNationalEnvironment = 1.08 

historicalAdjustment = 0.8

enthusiasmMax = 2.0 

enthusiasmMin = -2.0

pvi = [-18.7,-19.7,-21.7,-35.7,-19.7,-20.7,16.7,-5.3,-4.7,-3.3,26.7,4.7,-13.7,-3,17.7,-12.7,-18.7,-24.7,-11.7,-17.7,-22.7,-14.7,20.7,39.7,42.7,4,24.7,28,28.7,25.7,23.7,20.7,25.7,-18.7,11.7,2.3,-10.7,15.7,8.7,10.7,1.3,18.7,28.7,-4,25.7,17.7,22.7,14.7,34.7,15.7,23.7,37,16.7,14.7,19.7,-4.7,-5.7,22,34.7,26.7,-0.7,17.7,5.7,-11.7,5.7,-11.7,16.7,14.7,20.7,9.7,19.7,28.7,7.7,31.7,19.7,-9.7,-15.7,-11.7,11.7,4,0,14.7,5.7,9.7,15.7,5.7,9.7,-21.7,16.7,-10.7,-19.7,-6,10.7,-4,-9.7,-12.7,-15.7,-15.7,-8,27.7,-9.7,9.7,7.7,27.7,11.7,-10.7,-2.7,-4.7,-11.7,-6,-13.7,-16.7,-5,-13.7,10.7,-11.7,-15,-13.7,-10.7,30.7,-24.7,5.7,-20.7,29.7,34.7,-11,12.7,-18.7,-24.7,16.7,14,-24.7,-16.7,20,13.7,7.7,-24,3,6.7,-19.3,-10.3,2,21.7,20,24.7,20.7,5.7,38.7,8.7,21.7,5.7,-16.7,-20.7,-20.7,-13.7,-21.7,21.7,-21.7,-16,-5.7,-6.7,-0.3,-18.7,-20.7,-13.7,1.7,-16.7,-26.7,-23.7,9,-21.7,-34.7,-11.7,-25.7,27.7,-23.7,-16.7,-19.7,-21.7,11.7,-3.3,-13.7,9.7,12.7,40,17.7,4.7,32.7,31.7,11.7,15.7,13.7,14.7,25.7,13.7,37.7,17.7,8.7,-15.7,-3,9.7,25.7,23,-18.7,1,-7.7,-17.7,13.7,0.7,1.7,-20.7,-9.7,3.7,10.7,19.7,32.7,-14.7,-21.7,-10.7,-20.7,13.7,-17.7,-22,29.7,-9.7,-18.7,-23,13.7,-23.7,-24,-30.7,-6,-18.7,-11.7,-2.7,-31.7,5.7,-10.7,3.7,5.7,2.7,4.7,12.7,32.7,8.7,14.7,-7.7,7.7,-16.7,6.7,10.7,1.7,22,10.7,7.7,-1.7,6.7,-3,37.7,-8.7,34,40.7,30.7,37.7,22.7,5.7,3.7,0,-5.7,9.7,-11.7,1,-12,-13.7,7,11.7,2,5,32.7,17.7,33.7,28.7,27.7,2,-24.7,-8,15.7,-2,6,14.7,12.3,16,-15.7,6.7,-10.7,-22.7,-8.7,-22.7,-0.7,-6.7,30.7,-20.7,-1,-11.7,-8.7,-27.7,22.7,-22.7,-17.7,-18.7,-7,-16.7,-0.3,-16.7,-29,-26.7,-21.7,-14.7,20.7,-17.7,24.7,4,2,4,-2.7,-7.7,-15.7,8,-27.7,-20.7,-23.7,-15.7,0,22.7,41.7,9.7,16.7,7.7,0.7,-1.3,-23.7,14.7,4,-9.7,-10.7,-23.7,-14.7,-14.7,16.7,-11,-18.7,-32.7,-20.7,-21.7,-24.7,-9,-19.7,-12.7,-23.7,24.7,-26,-15.7,-25.7,-14.7,-28.7,-19.7,-1,19.7,-16.7,25.7,-28.7,-17.7,17.7,-15.7,-13.7,-7.7,-12.7,-21.7,-15.7,-15.7,5.7,20.7,-11,27,-16.7,16.7,26.7,9,21,-20.7,24,-12,-18.7,-16.7,-17.7,15.7,-16,28.7,-14.7,-13.7,-15.7,-18.7,16,-8.7,8.7,20.7,0.7,19.7,18.7,-9.7,-16.7,3.7,28.7,-25.7,15.7,9.7,11.7,-5,-13.7,-10.7,8.7,38.7,3.7,23.7,-25.7,-22,-5.7,21.7,-4,27.7,-16.7,-12.7,-14.7,-12.7,-25]

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
  print("Democrats win " + str(int((demWins/(i/100)) + 0.5)) + " in 100 times")
  print("Republicans win " + str(int((gopWins/(i/100)) + 0.5)) + " in 100 times")
  print("Average seats: " + str(average) + "D—" + str(435-average) + "R")
  print("Median seats: " + str(median) + "D—" + str(435-median) + "R")
  print("Mode seats: " + str(mode) + "D—" + str(435-mode) + "R") 
  print("Minimum seats: " + str(min) + "D—" + str(435-min) + "R") 
  print("Maximum seats: " + str(max) + "D—" + str(435-max) + "R") 
  print("Top bound: " + str(top) + "D—" + str(435-top) + "R") 
  print("Bottom bound: " + str(bottom) + "D—" + str(435-bottom) + "R") 
  print(numSeats)


simulate(baseNationalEnvironment)
