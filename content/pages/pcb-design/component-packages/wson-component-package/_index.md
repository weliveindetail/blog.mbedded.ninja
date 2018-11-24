---
author: gbmhunter
date: 2015-01-21 20:58:38+00:00
draft: false
title: WSON Component Package
type: page
url: /pcb-design/component-packages/wson-component-package
---

# Overview

<table style="width: 800px;" ><tbody ><tr >
<td >Name
</td>
<td >WSON (Small-outline No-lead Package)
</td></tr><tr >
<td >Synonyms
</td>
<td > 
</td></tr><tr >
<td >Variants
</td>
<td >Varying number of pins.
</td></tr><tr >
<td >Similar To
</td>
<td >  * SOIC
</td></tr><tr >
<td >Mounting
</td>
<td >SMD
</td></tr><tr >
<td >Pin Count
</td>
<td >8 (all also have exposed thermal pad)
</td></tr><tr >
<td >Pitch
</td>
<td >1.27mm (just like SOIC), except for Texas Instrument's WSON
</td></tr><tr >
<td >Solderability
</td>
<td >Hard to solder with a soldering iron due to underside thermal pad.
</td></tr><tr >
<td >Thermal Resistance
</td>
<td > 
</td></tr><tr >
<td >Dimensions
</td>
<td >

**WSON-8**  * Package: 6.0x5.0x0.80mm (w*l*h, Winbond package code ZP)  * Recommended Land Pattern: 6.10x5.10mm (31.11mm2)
</td></tr><tr >
<td >3D Models
</td>
<td > 
</td></tr><tr >
<td >Common Uses
</td>
<td >  * Flash memory ICs  * Secondary-side bias regulators for DC-DC converters
</td></tr></tbody></table>

# Comments

The WSON package has a exposed thermal pad on the underside. However, it is not normally electrically connected to anything, and is optionally soldered to the PCB. It is recommended to be soldered when the PCB has a large amount of flex, else left unconnected.

Warning: Texas Instruments has a WSON package which does not have a pitch of 1.27mm! 

Below is an "odd shaped" SON package used by Numonyx flash chips that goes under the name VDFPN8. Notice the half-round appearance of the pins.

{{< figure src="SON-8" width="554" caption="](/images/2014/12/component-package-vdfpn8-mlp8-outline-dimensions.png) Outline and dimensions for the VDFPN8 (SON-8) component package of a Numonyx flash IC.Image from http://www.micron.com/~/media/Documents/Products/Data%20Sheet/NOR%20Flash/Serial%20NOR/M25P/M25P128.pdf." caption-position="bottom" >}}

#  