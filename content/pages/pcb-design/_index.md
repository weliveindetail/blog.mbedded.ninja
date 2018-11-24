---
author: gbmhunter
date: 2011-12-12 05:07:14+00:00
draft: false
title: PCB Design
type: page
url: /pcb-design
---

# Child Pages




[sb_child_list template=2 orderby=title order=asc nest_level=1]




# PCB Design Tools




Here's a list of some useful design tools which come in useful when making PCB's.


<table style="width: 900px;" border="0" >
<tbody >
<tr >
Name
Comment
Picture
Link
</tr>
<tr >

<td >Saturn PCB Toolkit
</td>

<td >Very simple but extensive PCB design aid. And it's free! Includes a via current calculator, trace width calculator, bandwidth calculator, differential pair calculator, mechanical data, conductor impedance calculator, unit conversions, planar inductor calculator, thermal resistance calculator and more!
</td>

<td >[singlepic id=314 w=160 h=120 float=center]
</td>

<td >[http://saturnpcb.com/pcb_toolkit.htm](http://saturnpcb.com/pcb_toolkit.htm)
</td>
</tr>
<tr >

<td >Standard Resistor Calculator
</td>

<td >Invaluable when working out the closest manufactured resistor to the value you need in your design. There are tons of web-based calculators out there, and most let you choose a resistor series (e.g. E12, E24 e.t.c), or a precision (e.g. 5%, 1%). The higher the precisioin (1% is higher than 5%), the more expensive the resistor.
</td>

<td >[singlepic id=565 w=160 h=120 float=center]
</td>

<td >[http://www.daycounter.com/Calculators/Standard-Resistor-Value-Calculator.phtml](http://www.daycounter.com/Calculators/Standard-Resistor-Value-Calculator.phtml)
</td>
</tr>
<tr >

<td >Cladlab Calculators
</td>

<td >And of course, there is this site's own calculators, can help you choose component values when it comes to things like resistive voltage dividers, and low-pass RC filters.
</td>

<td >
</td>

<td >[http://blog.mbedded.ninja/electronics/general/online-calculators](http://www.daycounter.com/Calculators/Standard-Resistor-Value-Calculator.phtml)
</td>
</tr>
</tbody>
</table>


# Soldermask




All values are typical: Minimum Solder Mask Sliver = 0.1016mm (4mill) Solder Mask Thickness = 11um over copper, 20um over fibreglass (the difference is to that the resulting soldermask surface is flat) Common Solder Mask Colours: green (the most common), black, yellow, blue, clear, red and white Typical Dielectric Constant: 3-3.3 Note that the darker the solder mask colour (e.g. black), the harder it is to see the copper traces underneath, which in some cases makes it more difficult to debug a faulty PCB. The soldermask colour must be compatible with the silkscreen colour.




# Silkscreen




The silkscreen is a printed layer which is used to convey information to the user(s) of the board. It usually contains outlines of components, component polarity indicators, component designators, test-point information, and the PCB designer/version. The silkscreen layer(s) helps greatly when manually placing components and soldering the board. The silkscreen is printed on-top of the soldermask, on one or both sides of the board. On really cheap PCB runs, the silkscreen is left-off altogether (because it is not a necessary layer for the board to function).  For good readability, it should contrast well with the colour of the soldermask. Common silkscreen colours are:


<table style="width: 600px;" class="centeralign" >

<tr >
Silkscreen Colour
Relative Cost (out of 5)
Compatible Soldermask Colours
</tr>

<tbody >
<tr >

<td >White
</td>

<td >1
</td>

<td >Green, Red, Black
</td>
</tr>
<tr >

<td >Black
</td>

<td >2
</td>

<td >Green, White, Yellow
</td>
</tr>
<tr >

<td >Red
</td>

<td >4
</td>

<td >White, Yellow
</td>
</tr>
</tbody>
</table>


The silkscreen has to printed on either soldermask or bare PCB, it cannot be printed onto bare or tinned copper. For this reason, you cannot have soldermask ontop of component pads. [singlepic id=760 w=320 h=240 float=right] For components that protrude of the edge of the PCB (for example, connectors, or right-angled switches/leds, see the picture to the left), it is useful to indicate this on the silkscreen layer with diagonal lines as shown in the image below.




[singlepic id=761 w=400 h=400 float=center]




# Solder Paste




Solder paste is applied in the PCB manufacturing process just before the board is populated and soldered. It is the way that solder is applied in mass-quantities by a machine, and consists of a powdered metal solder suspended in a thick paste of flux. It is usually passed through a metal stencil which is placed ontop of the PCB, which has laser-cut holes in where the paste is to be applied. Since solder paste is only used when the board are to be populated by machine, it is normally not a concern when designing prototypes that will be soldered by hand, and is part of the "design for manufacture" process. For large areas that are going to be covered to solder paste (such as thermal pads on QFN packages), it is recommended that you "window" the stencil, as shown in the image below.




[singlepic id=1077 w=600 h=600 float=center template=caption]




# Designators




Designators normally only face in two directions only (i.e. down-facing and right-facing).




[singlepic id=1355 w=800 h=600 float="center" template="caption"]




If you cannot fit the designators next to their relevant components (e.g. a dense PCB), you can place a group of designators beside their components with the same orientation/placement, and the user can still understand which designator belongs to which component. You can see this being done on PC components such as motherboards and GPU's.




[singlepic id=1354 w=800 h=600 float="center" template="caption"]




# Estimating PCB Design Time




A good way of estimating the time to design a PCB board is by working out the utilization ratio. This is the total land area of all components divided by the total surface area of the board. A utilization ratio of 0.25 is easy enough to route, and the board starts getting harder as the ratio hits 0.50 and above. There is a good article, '[Estimating PCB Design Time And Complexity](http://www.pcbdesign007.com/pages/zone.cgi?a=74943&artpg=1)', that explains this in more detail, and even has a program to work it out for you.




# Clearances




There are many different types of clearances on a PCB board, and it can be really confusing sometimes to find out you can an can't do in terms of component and track placement.




## Copper To Board-Edge Clearance




Typical copper to board-edge clearance : 0.3048mm (12mill) This is the closest you can put copper to the board edge. This usually accomodates for slight board-misaglignment and tool in-accuracies when routing the the board into shape so that the router will not cut into the copper and leave 'exposed copper' ( a big no-no, usually). However, there are cases in which this rule is ignored, for example when you a making an RD shield or box from pieces of PCB, and need the copper to go right to the edge so that they can be soldered together into a box shape. This clearance is usually larger than the 'track and gap' clearance.




## Copper (Track And Gap) Clearance




The copper to copper and copper width clearance are usually have the same value. This is commonly called the 'Track and Gap' clearance. **Typical Values:**





	  * 0.5mm - Homemade PCB's
	  * 0.2mm - Professionally printed PCB's
	  * 0.1mm - High-end PCB's



# 




# Multi-Layer Routing




Route on the top or bottom layers if possible, especially when prototyping, this makes debugging and rework easier to do (you can't cut a track on one of the inside layers!).




# EMC Considerations/Noise Supression




This is a big topic, and has it's own page [here](http://blog.mbedded.ninja/electronics/circuit-design/noise-supression).




# PCB Antennas




## RF Antennas




In some situations, antennas for wireless communications can be formed directly on the PCB, with no need for an external component. They are normally used with carrier frequencies in the UHF range (300MHz-3GHz), due to these have frequencies having the appropriate wavelength for PCB construction. They are very cheap, and easy to tune, at the expense of sacrificing some communication range relative to a external antenna. PCB antennas are commonly made for:





	  * [RFID](http://blog.mbedded.ninja/electronics/circuit-design/rfid)
	  * 2.4GHz communication (e.g. ZigBee, Wi-Fi, ANT+)



## Stress Relief Antennas




Antennas can also be used for stress relief during soldering for stress-sensitive parts, such as accelerometers and gyros. Un-used pins on the stress-sensitive component package are routed a minimum distance from the pad, just like the used pins, so that when soldering using reflow or infrared techniques, all the solder on the pads melts and solidifies at the same time, reducing the stress on the component.




[singlepic id=1260 w=800 h=800 float=center template=caption]




## Undesired Antennas




Any PCB antenna that isn't for radio transmission or stress relief is probably a **bad** thing. These are cause by tracks end in the middle of nowwhere, and are often created un-intentionally when routing the PCB.




# Heatsinking




See the [Heatsinking page](http://blog.mbedded.ninja/electronics/circuit-design/heatsinks).




# Mounting




Don't forget to consider how the PCB is going to be mounted. One of the most common things accidentally left of a PCB. Normally all it requires is four holes (un-plated) in the corners for screwing in bolts/supports or just enough free PCB space to stick on rubber feet. M3 bolts and nuts are commonly used. Remember to consider the implications of using metal bolts next to/on-top of electrical signals. There are nylon bolts and washers when insulation is needed. Lock-tight can be good to prevent bolts/screws from undoing. The following picture shows the four mounting holes on a PCB. Notice one is underneath a component (the Xbee module).




[singlepic id=955 w=800 h=800 float=center template=caption]




[singlepic id=954 w=200 h=200 float=right]




Standoffs are good for providing clearance between the PCB and the mounting surface. You can buy plastic or metallic standoffs for most electronic suppliers, and they come in round or hex shapes. Electrical enclosures usually come with standoffs built into the structure.




[singlepic id=313 w=160 h=120 float=center template=caption]




Below is an example of a SMD standoff from [Pem Engineering](http://www.pemnet.com/).




[singlepic id=1078 w=500 h=500 float=center template=caption]




# Desiccant




Desiccant (a moisture absorbing compound), can be a good thing to use if your PCB is at risk of condensation. [singlepic id=973 w=400 h=400 float=center template=caption] See the [Desiccant page](http://blog.mbedded.ninja/electronics/components/desiccant) for more info.




# Making It Look Good




It could be said that PCB design is an art form. Personally, I take great pleasure in making a PCB that got the looks as well as the functionality. And it's helpful that most steps toward making a PCB look good actually tie in well with good design practises anyway.




This is an example of a PCB which I really like. It is called "[The Mojo](http://embeddedmicro.com/products/the-mojo)", and it is a Arduino-like FPGA development board. I love the black and green colour combination of the soldermask and silkscreen respectively.




[singlepic id=1101 w=800 h=600 float=center template=caption]




# Late Cycle Rework




"Late cycle rework" is the term given to PCB reworking done at the late stages, just before being sent of to the PCB manufacturer. Late cycle work is normally a bad thing, it is estimated that work done in this stage cost 10x as much as it does in the earlier stage.




# Panelization




Panelization is when you combine multiple PCB designs onto one PCB board, with the normal intention of saving costs associated with producing individual PCB's. Most PCB manufacturers support panelization and will route/v-score each design out for you, so you can separate them easily.




[Altium](http://blog.mbedded.ninja/electronics/general/altium) supports panelization. There is also software called [GerbMerge](https://github.com/unwireddevices/gerbmerge), an open-source tool which merges Gerber files together.




# Sending It To A PCB Manufacturer




For a review on different PCB manufacturers and their capabilities, see the [PCB Manufacturers section of the Electrical Suppliers page](http://blog.mbedded.ninja/electronics/general/electrical-suppliers#pcb-manufacturers).




# PCB Rework




Below is an example of a screwed PCB after too much rework was done on a 0.5mm pitch QFN package.




[singlepic id=678 w=600 h=600 float=center template=caption]




# PCB Design Checklist




Click [here](http://blog.mbedded.ninja/electronics/circuit-design/pcb-design/pcb-design-checklist).