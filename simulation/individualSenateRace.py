import random
import statistics 

baseNationalEnvironment = 0.755 

historicalAdjustment = 0

enthusiasmMax = 2.5 

enthusiasmMin = -4.5

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

def election(baseEnvironment, x):
  nationalEnvironment = simNatlEnv(baseEnvironment)
  demSeats = 0;
  swingAdj = random.uniform(-6.27, 5.0)
  race = x + nationalEnvironment + swingAdj 
  return race 

def simulate(env):
  demWins = 0
  gopWins = 0
  
  results = []
  
  i = 100000 

  pvi = float(input("PVI: "))
  for x in range(i):
    result = election(env, pvi)
    results.append(result)
    if result >= 0:
      demWins += 1
    else:
      gopWins += 1
  average = sum(results)/(i)
  results.sort()
  bottom = results[0]
  top = results[i-1]
  firstDecile = results[int(0.1*i)]
  ninthDecile = results[int(i-(0.1*i)-1)]


  print("S̲e̲n̲a̲t̲e̲")
  print("Democrat wins " + str(int((demWins/(i/100)) + 0.5)) + " in 100 times")
  print("Republican wins " + str(int((gopWins/(i/100)) + 0.5)) + " in 100 times")
  print(average)
  print("Best case for Dems: " + str(top))
  print("Best case for GOP: " + str(bottom))
  print("Reasonable range of results: " + str(firstDecile) + " | " + str(ninthDecile))

simulate(baseNationalEnvironment)

