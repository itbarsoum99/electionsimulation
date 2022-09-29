import random
import statistics 

baseNationalEnvironment = 0.8 

historicalAdj = 0.2

enthusiasmMax = 1.5 

enthusiasmMin = -3.0

# pvi = [-15,-10.6,5.35,-18.6,15.6,9.15,9.6,-6,2.1,16.6,-20.6,9.6,-13.6,-9.25,-12.6,-18.6,-14.6,16.6,-10.7,2.45,6.75,12.6,-1.65,-22.6,-2.9,-22.6,-20,8.6,3.45,-10.6,-18.6,-15.6,16,12.1,-3.65]


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

  historicalAdj = random.uniform(-0.2, 0.2)
  
  enthusiasmAdj = random.uniform(enthusiasmMin, enthusiasmMax)

  natlEnv = baseNationalEnvironment + errorAdj + historicalAdj + enthusiasmAdj

  return natlEnv

def election(baseEnvironment, x):
  nationalEnvironment = simNatlEnv(baseEnvironment)
  demSeats = 0;
  swingAdj = random.uniform(-6.1, 5.0)
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

  pvi = float(input("PVI: "))
  for x in range(i):
    result = election(env, pvi)
    numSeats.append(result)
    if result >= 1:
      demWins += 1
    else:
      gopWins += 1

  print("S̲e̲n̲a̲t̲e̲")
  print("Democrat wins " + str(int((demWins/(i/100)) + 0.5)) + " in 100 times")
  print("Republican wins " + str(int((gopWins/(i/100)) + 0.5)) + " in 100 times")

simulate(baseNationalEnvironment)

