---
author: gbmhunter
date: 2011-09-05 07:21:39+00:00
draft: false
title: My Workshop
type: page
url: /electronics/general/my-workshop
---

# Storage




## Component Trays




Organisation! Component trays are the shiz. When you want a component, they are right there and waiting. It is like walking into a shop, but without the cost (or course you have to fill them up, but you forget about the purchasing after a while). I use component trays for through hole resistors, through-hole capacitors, diodes, transistors, MOSFET's, and common IC's (555's, max232's, etc). I have smaller containers for the surface mount equivalents.


<table style="width: 500px;" border="0" class="aligncenter" >
<tbody >
<tr >

<td >[singlepic id=67 w=300 h=300 float=center]
</td>

<td >[singlepic id=69 w=300 h=300 float=center]
</td>
</tr>
</tbody>
</table>



## Storage Boxes





No, I didn't eat all that ice cream myself. But they are all 2L ice-cream containers, eaten by my family over the last 8 years. They make really good stackable containers for holding compnents and anything else that is too big or not used enough for the component trays.





[singlepic id=93 w=400 h=400 float=center]





For storing SMD components such as resistors, capacitors, and ferrite beads, I use these modular storage containers from DealExtreme. They are great because a) cheap, b) small, c) modular, d) have flip-top lids which spring open. I use a labeller to create small labels for each one, describing the component.





[singlepic id=971 w=600 h=600 float=center]





# Tools





## Power Supply





A variable voltage-limited or current-limited power supply is a must for any serious electronic work. The current-limiting especially, as it prevent circuits from blowing up when prototyping.





I brought a cheap 0-30V, 0-5A power supply from AliExpress. It is the YH-305D, as shown below. It set me back about NZ$130, including shipping.





[singlepic id=1056 w=400 h=400 float=center]





I also have a high-power DC-DC buck converter that I use when I need high current. It is a 12A, 4.5-30V in, 0.8-28V out (adjustable) buck converter that is rated to 100W without a fan and up to 200W with active cooling. It was about NZ$13 (US$9) on [AliExpress](http://www.aliexpress.com/). Here is a [link to the product](http://www.ebay.com/itm/ws/eBayISAPI.dll?ViewItem&item=321013571373&ssPageName=ADME:X:AAQ:US:1123).





[singlepic id=1058 w=400 h=400 float=center]





## Oscilloscope





Hitachi V-1050F 100MHz Oscilloscope - This thing is an ancient beast. I picked it up for NZ$300 on [TradeMe](http://www.trademe.co.nz/) in about 2004. It is a analogue (CRT) oscilloscope that looks like it was first built in the 1980's. It has four channels (with two of them being fully customisable), and the ability to go down to 20ns resolution. The annoying thing about it is that is that being analogue, the trace quickly disappears from the screen with slow signals (since it works by repeatedly moving an electron beam across the screen), making it hard to do some measurements or get a full idea of the signal shape.



<table style="width: 500px;" border="0" class="aligncenter" >
<tbody >
<tr >

<td >[singlepic id=87 w=300 h=300 float=center]
</td>

<td >[singlepic id=89 w=300 h=300 float=center]
</td>
</tr>
</tbody>
</table>



As of 2012 I got a new oscilloscope, a Rigol ADS 1102CAL. It has a 100MHz bandwidth. Brought it for NZ$400 from [AliExpress](http://www.aliexpress.com/).





[singlepic id=695 w=500 h=500 float=center]





Newer oscilloscopes like this one usually have USB ports for saving captures of waveforms to. You can usually select from a range of file formats such as an image (.png, .jpeg), comma-separated values (.csv), or a proprietary binary format such as .wfm. I have found .csv files to be to most useful, since it gives you all of the raw data. I'm pretty sure the .wfm files also store all of the data, but for some reason I have had trouble trying to extract the timing information from them.





I have used the .csv files to display graphs via Google visualizations on various pages on this site. My GitHub repo [eng-graphs-js](https://github.com/gbmhunter/eng-graphs-js) has all the graph data as well as the rendering code.





## Logic Analyser





Logic analysers are great tools for looking a digital circuits! Most oscilloscopes are great for looking at analogue waveforms, but have serious limitations when looking at digital waveforms (except fancy versions, which have digital analysers built in, or offer a hardware extension).





Logic analysers usually have 8 or more inputs. They record the 1's and 0's on the inputs, and often have advanced features like comm protocol decode support. This means they can decode the information sent across common communication protocols, making debugging easier as you no longer have to look at each individual bit and work out what was sent. They commonly support protocols such as [UART](http://blog.mbedded.ninja/electronics/circuit-design/uart), [SPI](http://blog.mbedded.ninja/electronics/circuit-design/communication-protocols/spi-protocol), and [I2C](http://blog.mbedded.ninja/electronics/circuit-design/i2c-communication), and less commonly LIN and CAN.





The particular [Saleae](http://www.saleae.com/) "[Logic](http://www.saleae.com/logic)" logic analyser below uses a [PSoC microcontroller](http://blog.mbedded.ninja/programming/microcontrollers/psoc).





[singlepic id=1059 w=400 h=400 float=center]





## UART-To-RS-232 Converter





One of these is essential for debugging embedded designs. My favourite is the TTL-232RG-VIP-WE "USB to TTL Serial Cable - 1.8m Wire End Version" made by FTDI chip. All of the electronics is enclosed in the USB cable, which has loose colour coded wires at the other end. It is the external-voltage version, which means that instead of the cable supplying Vcc for the UART, it's provided by the external circuitry. This means the cable can work of a number of voltages, and no level converter is needed!





## USB-To-RS-485 Converter





Plenty of industrial, hard-wearing and/or long-distance electrical equipment uses the RS-485 interface for communicating. The DT-5019 is a great USB-to-RS-485 converter for talking to devices uses this protocol with a computer.





[singlepic id=1092 w=500 h=250 float=center template=caption]





I got this from [DealExtreme](http://dx.com/), part number [54289](http://dx.com/p/dtech-usb-2-0-to-rs422-rs485-adapter-cable-1-2m-cable-54289), for US$19.70 in Jan 2013 (inc. shipping to NZ). It is made by Dtech.





This particular converter comes with standard DB9 connector and also a breakout board with terminal blocks, perfect for most prototyping situations. It supports both the RS-422 (full-duplex) and RS-485 (half-duplex) protocols, over a maximum of 1200m! The drivers are already present on Windows 7/Windows 8 machines, and a driver CD is supplied. It had 600W surge protection and 15kV ESD protection. LED's on the device show the current status (which is great for debugging).





Supported transmission speeds are:



<table style="width: 500px;" border="0" >
<tbody >
<tr >

<td >**Distance**
</td>

<td >**Transmission Speed**
</td>
</tr>
<tr >

<td >300m
</td>

<td >921600bps
</td>
</tr>
<tr >

<td >600m
</td>

<td >38400bps
</td>
</tr>
<tr >

<td >1200m
</td>

<td >9600bps
</td>
</tr>
</tbody>
</table>



[singlepic id=1088 w=600 h=800 float=center template=caption]





The manual for this Dtech converter  can be downloaded below.





[wpfilebase tag=file id=13 /]





# Components





## Capacitors





Large capcitors are a geeks version of a flash car or a huge plasma screen. Except better.





These pics below are of my largest capacitors, 20 1800uF, 500V monstrosities. I got these for a total of NZ$40 from TradeMe of someone who didn't know they actual worth (possibly NZ$1000's!, I don't even think they knew they were capacitors). I have yet to use them for anything but shorting out pieces of wire (and with only two in parallel). A coil gun HAS to be made from these soon.



<table align="center" style="width: 500px;" border="0" class="aligncenter" >
<tbody >
<tr >

<td >[singlepic id=61 w=250 h=300 float=center]
</td>

<td >[singlepic id=63 w=250 h=300 float=center]
</td>

<td >[singlepic id=65 w=250 h=300 float=center]
</td>
</tr>
</tbody>
</table>



My 'monster' cap bank. Me and a mate made this in 2005 for a coil gun. Each capacitor is from a disposable camera. They are 7 rows with 20 capacitors in each, and they are all connected in parallel The voltage is 330V and the capacitance of each ranges from 80-120µF. The total approximate capacitance is 14,000µF. But the poor camera cap charging circuits just couldn't handle the jandle. So it never got used. Unfortunatly as of Jan 2011 it is broken (I think a car ran into it, long story). I might get around to fixing this sometime...



<table align="center" style="width: 500px;" border="0" class="aligncenter" >
<tbody >
<tr >

<td >[singlepic id=75 w=250 h=300 float=center]
</td>

<td >[singlepic id=83 w=250 h=300 float=center]
</td>
</tr>
<tr >

<td >[singlepic id=85 w=250 h=300 float=center]
</td>

<td >[singlepic id=81 w=250 h=300 float=center]
</td>
</tr>
</tbody>
</table>


## 





## PCB's





PCB's are useful when developing a circuit past the quick prototype stage. I have both blank copper PCB sheets as well as protoboard (copper tracks running parallel with each other), and variations on proto-board esigned to make it easier to hook up IC's and other chips.





[singlepic id=91 w=400 h=400 float=center]





## Laser





[singlepic id=668 w=200 h=200 float=left]





3kV HeNe Laser - I picked this laser up from Trademe in 2005 for NZ$40. The tube is about 400mm long and 80mm in diameter. The power supply is a seperate PCB which runs of 12V. So far I have never managed to get the laser running continously, only turning on intermittantly every few seconds. It seems there is a problem with the power supply and it cannot supply the required current to keep the laser on. It also emits quite a annoying squeal when running (I'm guesssing it's the switching frequency). I am unsure of it's output power...





[singlepic id=667 w=300 h=300 float=center]





# Software





## Altium





Altium is a CAD package for designing circuit boards. It is a very expensive (like most high-end CAD packages) piece of software, that I do not own personally. Luckily, the company I work for has commercial licences, which I use when designing PCB's. If you want to know more about it, go to the [Altium page](http://blog.mbedded.ninja/electronics/general/altium).





## Console Calculator





Website: [http://www.zoesoft.com/console-calculator/](http://www.zoesoft.com/console-calculator/)





I can happily say that console calculator is the best software-based calculator in the world. It is an open-source, cross-platform calculator with powerful features in a tidy and easy to use interface. It kind of looks like a command prompt window (or console window for you 'nix' fans), that accepts maths commands. Console Calculator supports many built in functions, the ability to create your own, quick conversion between units, the ability to add your own units, customisable rounding/display modes, ridiculous 269 digit floating point precision (many other calculators are only 64-bit), decimal, hexadecimal and binary number system support, and more!