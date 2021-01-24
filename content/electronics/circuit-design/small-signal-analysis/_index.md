---
author: "gbmhunter"
categories: [ "Electronics", "Circuit Design" ]
date: 2021-01-24
description: "Explanation, analysis method and more info on small-signal analysis of circuit designs."
draft: false
lastmod: 2021-01-24
tags: [ "electronics", "circuit design", "small-signal analysis", "small-signal", "analysis", "dynamic resistance", "resistance", "quiescent" ]
title: "Small-Signal Analysis"
type: "page"
---

{{% warning-is-notes %}}

## Overview



## Small-Signal Analysis Method

1. **Find the quiescent point (DC operating point) of the circuit**. Remove all signal sources, leaving the DC supplies, and find the DC voltages and currents at each node in the circuit.

1. **Linearize the non-linear circuit components at the DC operating point**. The most basic example of this is a diode, whose current is approximately proportional to the square of the voltage across it. But as long as the signal is small (hence the name, small-signal analysis!) compared to the DC operating point of the diode, you can approximate this to a linear relationship, i.e. `\( \Delta V = \Delta I R\)`. This resistance is called the _dynamic resistance_.

1. **Find the small-signal solution**: Now the DC sources are removed. Voltage sources are replaced with `\(0\Omega\)` resistors (short circuit), current sources are replaced with `\(\infty \Omega\)` resistors (open circuit). The signal sources are re-introduced and then finally node voltages and currents are solved using easy linear equations.

Taking it a step further: The complete solution is just the sum of the DC operating point + the small-signal solution.

## Resistor Divider

{{% img src="resistor-divider-before-replacing-vin.png" width="500px" caption="Resistor divider, before replacing Vin." %}}

We assume Vin is a perfect voltage source, therefore we can replace it with a short.

{{% img src="resistor-divider-vin-replaced-with-short.png" width="500px" caption="Resistor divider, Vin replaced with short." %}}