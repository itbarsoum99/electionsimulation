# 2022 Midterm Simulation Model

## Background and disclaimer
This project consists of a very basic election simulation model written in python.

I'm an amateur data analyst, amateur political scientist, and amateur computer scientist and I have absolutely no expertise whatsoever, so don't bet all your money on my model.

## Current predictions (updated 09/24)

**House of Representatives**

Republicans win 64 in 100.

Median outcome: 221R—214D

**Senate**

Democrats win 79 in 100.

Median outcome: 51D—49R

## Methodology

### Elections
Simulates each of 435 seats in the House and each of 35 Class III seats in the Senate.

<pre>districtPVI + (baseNEnv ± hAdj ± eAdj ± errorAdj) ± incumbencyAdv + swingAdj = election result</pre>


The district PVI (<code>districtPVI</code>) is sourced from [the Cook Political Report](https://www.cookpolitical.com/cook-pvi/2022-partisan-voting-index/district-map-and-list).

*In the Senate, individual race polls are also taken into account.*

The base national environment (<code>baseNEnv</code>) is from [FiveThirtyEight's generic ballot polling average](https://projects.fivethirtyeight.com/polls/generic-ballot/).

The historical adjustment (<code>hAdj</code>) is based on [inaccuracies from 2018 polling](https://projects.fivethirtyeight.com/polls/generic-ballot/2018/) compared to the final results.

The enthusiasm adjustment (<code>eAdj</code>) is equivalent to a randomly selected number in a range between half of the margin in each party's best [voter enthusiasm poll](https://morningconsult.com/2022-midterm-elections-tracker/) during the previous month.

The error adjustment (<code>errorAdj</code>) assumes that the base national environment could vary by up to 50% in either direction.

The incumbency advantage (<code>incumbencyAdv</code>) is [based on 2018 data from hundreds of races](https://fivethirtyeight.com/features/how-much-was-incumbency-worth-in-2018/).

The swing adjustment (<code>swingAdj</code>) assumes that any given election could swing up to 5 points in either direction. (*In Senate races, where race polls are taken into account, it assumes a [1.1-point bias in favor of Democrats.](https://fivethirtyeight.com/features/will-the-polls-overestimate-democrats-again/)*)


### Simulation
Results are simulated 500,000 times and the averages are used.

## Changelog
**Saturday, September 24, 2022:** Model launched with initial simulations

**Sunday, September 25, 2022:** Incorporated <code>swingAdj</code> in House races

___

2022 Midterm Elections Model © 2022 by Isaac Barsoum is licensed under CC BY-NC-SA 4.0
