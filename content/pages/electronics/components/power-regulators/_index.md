---
author: gbmhunter
date: 2012-08-20 07:20:46+00:00
draft: false
title: Power Regulators
type: page
url: /electronics/components/power-regulators
---

[latexpage]

# Overview

Power regulators aim to convert an input DC voltage into a DC output voltage. There are many different ways of doing this, an each design has its benefits and advantages. The important parameters of DC/DC converters are efficiency, output ripple, complexity, and maximum output current.

# Child Pages

[sb_child_list template=2 orderby=title order=asc nest_level=1]

# Terminology

<table ><tbody ><tr >TermDescription</tr><tr >
<td >Boost converter
</td>
<td >A DC/DC converter topology which converts an input voltage into a **higher** output voltage.
</td></tr><tr >
<td >Buck converter
</td>
<td >A DC/DC converter topology which converts an input voltage into a **lower** output voltage.
</td></tr><tr >
<td >Controller
</td>
<td >A power conversion device that requires a external switch (typically a MOSFET).
</td></tr><tr >
<td >Converter
</td>
<td >A power conversion device that has an integrated switch (typically a MOSFET).
</td></tr><tr >
<td >Cuk converter
</td>
<td >A DC/DC converter topology which converts an input voltage into either a **higher** or **lower** output voltage. A Cuk converters output voltage is opposite in polarity to it's input voltage (which is a disadvantage in most cases).
</td></tr><tr >
<td >Down Conversion
</td>
<td >Converting an input voltage into a lower output voltage.
</td></tr><tr >
<td >Ripple
</td>
<td >Used when talking about voltages and currents, it is the **absolute or percentage change in voltage or current** (max - min) over an operating cycle. You typically don't want more than 20% ripple current through an inductor (w.r.t. it's average current).
</td></tr><tr >
<td >SEPIC
</td>
<td >SEPIC (single-ended primary inductance converter) is a DC/DC converter topology similar to a buck-boost, which converts an input voltage into either a **higher** or **lower** output voltage.
</td></tr><tr >
<td >Synchronous rectification
</td>
<td >When the diode in a simple DC/DC converter is replaced with a switched MOSFET to improve efficiencies. Synchronous rectification allows DC/DC converter to climb above 90% efficiency in ideal situations.
</td></tr><tr >
<td >Topology
</td>
<td >The type of design/technology of the converter (e.g. a buck converter is one type of topology, while a boost converter is another).
</td></tr></tbody></table>

# Topology Summary

<table border="0" ><tbody ><tr >TopologyAdvantagesDisadvantagesCommentsImage</tr><tr >
<td >Linear Voltage Regulator (LDO)
</td>
<td >  * Simple  * Cheap  * Very low output ripple  * Low EMI
</td>
<td >  * Inefficient  * Can only decrease the voltage
</td>
<td >Uses transistors to create a dynamically changing resistance to drop the voltage to the required level (hence linear). Dissipates the energy as heat, and therefore is very inefficient, and limited in power. Linear regulators have very low radiated EMI because they do not have a switching element. For the very same reason they also have very low output ripple, and high PSRR (power supply rejection ratio).
</td>
<td >[singlepic id=295 w=160 h=120 float=]
</td></tr><tr >
<td >Buck Converter
</td>
<td >  * Very high efficiency (>90%)
</td>
<td >  * Can only decrease the voltage  * Medium complexity  * High EMI
</td>
<td >Uses an inductor, capacitor and switching element to reduce the input voltage. The alternative method to a buck converter for reducing the input voltage is a linear voltage regulator. Very high efficiencys in some cases due to the absense resistive power losses.
</td>
<td >[singlepic id=330 w=160 h=120 float=]
</td></tr><tr >
<td >Boost Converter
</td>
<td >  * High efficiency (>80%)
</td>
<td >  * Can only increase the voltage  * Medium complexity  * High EMI
</td>
<td >Uses an inductor, capacitor and switching element to increase the input voltage.
</td>
<td > 
</td></tr><tr >
<td >Buck-Boost
</td>
<td >  * Most flexible in terms of voltage, can either decrease or increase input voltage.
</td>
<td >  * Slightly lower efficiency than a dedicated boost or buck converter  * Input voltage range extremes are usually less than a dedicated buck or boost converter.  * High EMI  * Larger part count than a dedicated buck or boost converter.
</td>
<td >This is basically a combination buck and boost converter in one, and so can either increase or decrease the input voltage.
</td>
<td > 
</td></tr><tr >
<td >Charge Pump
</td>
<td >  * Very high efficiency (99%)  * Simple, requires minimal external componentry
</td>
<td >  * Low output current  * High output resistance  * Fixed output voltages
</td>
<td >Uses capacitors, diodes, and a oscillating switch to move charge from one capacitor to another, and in the process, increasing the voltage on the second cap. Normally the voltage is doubled, and multiple elements can be connected together to create larger voltage increases.
</td>
<td > 
</td></tr><tr >
<td > Joule Thief
</td>
<td >  * Simple  * Moderately efficient  * Good at extracting all the energy from a power source.
</td>
<td >  * Low power
</td>
<td > Used in low power and cheap applications, e.g. powering an LED from a 1.5V battery.
</td>
<td >[singlepic id=296 w=160 h=120 float=]
</td></tr></tbody></table>

# DC/DC Converters And Controllers

[singlepic id=294 w=200 h=200 float=right template=caption] DC/DC converters and controllers are IC's which contain all of the logic and most of the passive componentry that makes up a switching power converter. When the industry talks about a DC/DC converter, they are talking about a chip which has an integrated switch (usually a [MOSFET](http://blog.mbedded.ninja/electronics/components/mosfets)). When they talk about a DC/DC controller, they are talking about a chip which requires an external switch. Most DC/DC converters and controllers require at least an external input capacitor, switching inductor, and output capacitor. Some however, like Linear Technology uModule range, have the inductor/capacitors built in also. These tend to be rather expensive! Two important patents in the history of DC/DC converters are patent [US3040271](http://www.google.com/patents/US3040271) and [US4097773](http://www.google.com/patents/US4097773). DC/DC converters are also used to charge batteries from solar panels. In this case, they are operated in an unusual fashion, because you want to regulate the input voltage to what provides maximum power extraction from the solar panel, rather than regulating the output voltage. Sometimes AC/DC power supplies are called LPS, which is an acronym for "**limited power supply**". This term is related to the IEC60950-1 standard. [singlepic id=1344 w=400 h=400 float=center template=caption]

## Efficiencies

The efficiency of DC/DC converters can be as high as 96-98%!  You will see a figure like this quoted in most DC/DC converter IC datasheets. However, this efficiency only applies when the **converter is operating at one specific point** (the right input voltage, output voltage, load current, and temperature). Your own personal design will most likely be using the converter at a variety of different operating points, which may or may not include the one for maximum efficiency. When in actual use over a range of operating conditions, an average of about 80% efficiency is common from a good DC/DC converter. **Only use this rating for comparing the quality of one DC/DC converter against another.**

## Burst Mode

DC/DC converters can extend their efficient operating current range by enabling the converter to operate in what is called a "burst" mode at low currents. When a converter is in this mode, it provides a burst of pulses to power the output until the output voltage climbs over a set threshold, turns off, and doesn't turn back on again until the load voltage drops below a certain threshold. This turns out to be more efficient than continuous mode at low currents, but also **increases the total noise** radiated from the DC/DC converter. Most converters that employ this technique have a way of forcing the converter to stay in fixed frequency mode to reduce noise, which is useful for when powering devices such as GPS IC's.

## AC/DC Converters

Although strictly not a DC/DC converter, you can purchase ready-to-go PCB-mounted AC/DC converter modules that are designed to plug straight into the AC mains (90-270VAC(rms)), and output a DC voltage typically between 3.3 and 24V. Power ratings are typically 1-10W. The one shown below is made by MeanWell. [singlepic id=949 w=500 h=500 float=center template=caption] The types which are designed to be plugged straight into the wall are called wall-warts. They usually have two-core wire going to a DC jack connector. The wire with the white stripes on it is usually positive.

## Current Sharing

You can balance current-sharing between two similar power supplies by adding in-line resistance to each of power supply outputs, before connecting them together. Normally power resistors are required (>= 5W), and resistances between 1mΩ and 1Ω are used. Basically, you want to choose the largest resistance that at maximum current won't overheat, and won't drop to much voltage so that the load does not operate correctly. I have used this technique successfully for the [Luxcity UV Tonic project](http://blog.mbedded.ninja/electronics/projects/luxcity-uv-tonic-control-system) to current-share between two computer power supplies that were driving the 64 solenoids.

#  

# Buck-Boost Converter

A buck-boost power converter is a power supply which can produce an output voltage which can be both higher or lower than the input voltage. A buck-boost converter is similar to a SEPIC converter. Buck-boosts are not used unless an output voltage which could be both lower and higher than the input voltage is specifically required, as usually a sole buck or boost converter is cheaper, has a lower part count, and is more efficient. Maxim claims that a boost with linear regulator instead of a buck circuit can out perform a buck/boost in certain applications.

#  

# Joule Thiefs

The team at RustyBolt has experimented with plenty of different Joule thief designs, and documented the results well on [their website](http://rustybolt.info/wordpress/).