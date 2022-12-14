import random
import statistics 

baseNationalEnvironment = 1.25

historicalAdjustment = 0.8 

enthusiasmMax = 2.0 

enthusiasmMin = -4.5

pvi = [-22.6,-20.6,-20.9,-20,-18.6,-18.6,-18.6,-15.6,-15,-14.6,-13.6,-12.6,-10.6,-10.6,-10.75,-10.2,-6.4,-5.05,-2.9,-2.3,1.85,1.75,3.1,4.85,7,8.55,11.5,13.45,8.6,14.85,17.4,15.6,16,16.6,16.6]

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
  marginOfError = 0.5 * baseEnv
  errorAdj = random.uniform(-marginOfError, marginOfError) 

  historicalAdj = random.uniform(-historicalAdjustment, historicalAdjustment)
  
  enthusiasmAdj = random.uniform(enthusiasmMin, enthusiasmMax)

  natlEnv = baseNationalEnvironment + errorAdj + historicalAdj + enthusiasmAdj

  return natlEnv

def election(baseEnvironment):
  nationalEnvironment = simNatlEnv(baseEnvironment)
  demSeats = 36;
  for x in pvi:
    swingAdj = random.uniform(-6.27, 5.0)
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
    if result >= 50:
      demWins += 1
    else:
      gopWins += 1
  average = int(sum(numSeats)/(i))
  numSeats.sort()
  median = numSeats[int(i/2)]
  min = numSeats[0]
  max = numSeats[i-1]
  mode = statistics.mode(numSeats)
  bottom = numSeats[int(0.1 * i)]
  top = numSeats[int(i-(0.1*i)-1)]
  q1 = numSeats[int(0.25 * i)]
  q3 = numSeats[int(i-(0.25*i)-1)]


  print("S̲e̲n̲a̲t̲e̲")
  print("Democrats win " + str(int((demWins/(i/100)) + 0.5)) + " in 100 times")
  print("Republicans win " + str(int((gopWins/(i/100)) + 0.5)) + " in 100 times")
  print("Average seats: " + str(average) + "D—" + str(100-average) + "R")
  print("Median seats: " + str(median) + "D—" + str(100-median) + "R")
  print("Mode seats: " + str(mode) + "D—" + str(100-mode) + "R")
  print("Minimum seats: " + str(min) + "D—" + str(100-min) + "R")
  print("Maximum seats: " + str(max) + "D—" + str(100-max) + "R")
  print("Top bound: " + str(top) + "D—" + str(100-top) + "R")
  print("Bottom bound: " + str(bottom) + "D—" + str(100-bottom) + "R")
  print("First quartile: " +str(q1) +"D")
  print("Third quartile: " +str(q3) +"D")


simulate(baseNationalEnvironment)

