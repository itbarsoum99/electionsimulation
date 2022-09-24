# 2022 Midterm Simulation Model

## Background
* This project consists of a very basic election simulation model written in python.
* I'm an amateur data analyst, political scientist, and computer scientist and I have absolutely no expertise whatsoever, so don't bet all your money on my model.

## Methodology

### Elections
Simulates each of 435 seats in the House and each of 35 Class III seats in the Senate.

<blockquote>districtPVI + (baseNEnv ± historicalAdj ± enthusiasmAdj ± errorAdj) ± incumbencyAdvantage = election result</blockquote>

<small>In the Senate, individual race polls are also taken into account.</small>

The district PVI (<code>districtPVI</code>) is sourced from [the Cook Political Report](https://www.cookpolitical.com/cook-pvi/2022-partisan-voting-index/district-map-and-list).

The base national environment (<code>baseNEnv</code>) is from [FiveThirtyEight's generic ballot polling average](https://projects.fivethirtyeight.com/polls/generic-ballot/).

The historical adjustment (<code>historicalAdj</code>) is based on inaccuracies from 2018 polling compared to the final results.

The enthusiasm adjustment (<code>enthusiasmAdj</code>) is equivalent to a randomly selected number in a range between half of the margin in each party's best [voter enthusiasm poll](https://morningconsult.com/2022-midterm-elections-tracker/) during the previous month.

The error adjustment (<code>errorAdj</code>) assumes that the national environment could vary by up to 50% in either direction.

The incumbency advantage (<code>incumbencyAdvantage</code>) is [based on 2018 data from hundreds of races](https://fivethirtyeight.com/features/how-much-was-incumbency-worth-in-2018/).

### Simulation
* Python is used to introduce randomness
* Results are simulated 40,000 times and the averages are used


