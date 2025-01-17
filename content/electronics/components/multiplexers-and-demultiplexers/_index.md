---
authors: [ "Geoffrey Hunter" ]
categories: [ "Electronics", "Components" ]
date: 2021-01-28
description: ""
draft: false
lastmod: 2021-01-30
tags: [ "electronics", "components", "multiplexers", "demultiplexers" ]
title: "Multiplexers And Demultiplexers"
type: "page"
---

{{% warning-is-notes %}}

## Overview

_Multiplexers_ (a.k.a. a MUX or _data selector_) are integrated circuits which can be used to select one of many input signals and connect it to a single output signal. A _demultiplexer_ does the reverse, it connects a single input signal to one of many output signals.

## Analogue Multiplexers And Demultiplexers

Analogue multiplexers pass an analogue signals from one of many inputs to a single output. Whilst a digital multiplexer buffers and amplifies the output, an analogue multiplexer does not, you can simply view it as a simple switched connection between input and output (albeit with a larger resistance than a mechanical switch). For this reason, **analogue multiplexers are bidirectional** (signals can pass from input to output, as well as pass from output to input), whilst **digital multiplexers are single direction only** (from input to output).

{{% img src="cd4051b-functional-diagram-ti.png" width="400px" caption="The functional diagram of the CD4051B 8:1 analogue multiplexer by Texas Instruments. Image retrieved from https://www.ti.com/lit/ds/symlink/cd4052b.pdf on 2021-01-30." %}}

It's important to note that most analogue multiplexers have a much higher resistance than a traditional mechanical switch or even transistor, with most specifying an _on-state resistance (max)_ between `\(30\)` and `\(150\Omega\)`.

### Deviations From An Ideal Switch

* The on-state resistance of a analogue multiplexer is much higher than a mechanical switch.
* The voltage on the input and output cannot exceed `\(V_{DD}\)` and `\(V_{EE}\)` by more than a diodes forward voltage drop (`\(\approx 0.6V\)`, any higher than this and conduction from your signal to the rails occurs, distorting your signal).

### Datasheet Parameters
 
#### On-State Resistance

The resistance between the input and output when the input is switched to the output. Typically specified as a maximum, with nominal values being between `\(30\)` and `\(150\Omega\)`.

### Switching Procedure

* Break-before-make

### Manufacturer Part Numbers

* **4051**: Common part number segment used by a number of manufacturers for a analogue 8:1 multiplexer.
* **74HC4051**: Family of "4051 style" analogue multiplexers by Nexperia.
* **CD4051**: Family of "4051 style" analogue multiplexers by Texas Instruments.
* **CD74HC**: Popular range of analogue multiplexers by Texas Instruments.

### Suppliers

* [DigiKey link to the Analog Switches, Multiplexers, Demultiplexers section](https://www.digikey.com/en/products/filter/integrated-circuits-ics/747)