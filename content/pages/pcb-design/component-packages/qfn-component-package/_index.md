---
author: gbmhunter
date: 2014-12-04 09:55:02+00:00
draft: false
title: QFN Component Package
type: page
url: /pcb-design/component-packages/qfn-component-package
---

# Overview


<table >
<tbody >
<tr >

<td >Name
</td>

<td >Quad-flat No-leads Package
</td>
</tr>
<tr >

<td >Synonyms
</td>

<td >



	  * **2077-02** | Freescale QFN-16 Pins-5x3 Body-3x3mm)
	  * **CP-32-2** | Analog Devices QFN-32 Pins-8x8 Pitch-0.50mm Body-5x5mm)
	  * **DO-214AC**
	  * **LFCSP** | Analog Devices
	  * **MLF** | Micro-leadframe
	  * **QFN-UT** | Ultra-thin QFN packages by Samtech
	  * **RQZ** | QFN-48, 7x7mm, 050mm pitch by Texas Instruments
	  * **RSB** | QFN-40 by Texas Instruments
	  * **SOT....** | NXP's name for it's QFN range of packages, not this does not include packages such as the SOT-23, which are NOT QFN packages)


</td>
</tr>
<tr >

<td >Variants
</td>

<td >n/a
</td>
</tr>
<tr >

<td >Similar To
</td>

<td >



	  * [SON (DFN)](http://blog.mbedded.ninja/pcb-design/component-packages/son-component-package)
	  * UQFN
	  * VQFN


</td>
</tr>
<tr >

<td >Mounting
</td>

<td >SMD
</td>
</tr>
<tr >

<td >Pin Count
</td>

<td >12-108
</td>
</tr>
<tr >

<td >Pitch
</td>

<td >



	  * 0.40mm
	  * 0.50mm
	  * 0.65mm


</td>
</tr>
<tr >

<td >Solderability
</td>

<td >Surprisingly easy to solder by hand, as long as the pads extend around to the sides of the IC, and you drill a hole to solder the centre pad from the reverse. QFN packages can also be soldered easily with a infrared rework station or the 'frying pan' technique.
</td>
</tr>
<tr >

<td >Thermal Resistance
</td>

<td >n/a
</td>
</tr>
<tr >

<td >Dimensions
</td>

<td >0.40mm pitch QFN packages:




	  * QFN-UT-20: 3x3x0.6mm (LA: 9mm2)
	  * QFN-56: 7x7x1mm (LA: 49mm2)
	  * QFN-64: 8x8x1mm (LA: 64mm2)
	  * QFN-72: 9x9x1mm (LA: 81mm2)
	  * QFN-88: 10x10x1mm (LA: 100mm2)
	  * QFN-108: 12x12x1mm (LA: 144mm2)



0.50mm pitch QFN packages:





	  * QFN-16: 3x3x1mm (LA: 9mm2)
	  * QFN-20: 3x3x1mm (LA: 9mm2)
	  * QFN-24: 4x4x1mm (LA: 16mm2)
	  * QFN-32: 5x5x1mm (LA: 25mm2)
	  * QFN-36: 6x6x1mm (LA: 36mm2)
	  * QFN-48: 7x7x1mm (LA: 49mm2)
	  * QFN-56: 8x8x1mm (LA: 64mm2)
	  * QFN-64: 9x9x1mm (LA: 81mm2)
	  * QFN-68: 10x10x1mm (LA: 100mm2)



0.65mm pitch QFN packages:





	  * QFN-16: 4x4x1mm (LA: 16mm2)
	  * QFN-20: 4x4x1mm (LA: 16mm2)
	  * QFN-32: 7x7x1mm (LA: 49mm2)


</td>
</tr>
<tr >

<td >Height
</td>

<td >1mm (max, applies to all QFN packages, includes stand-off). Some a smaller (e.g. the UT/ultra-thin QFN packages).
</td>
</tr>
<tr >

<td >3D Models
</td>

<td >0.50mm Pitch: 




	  * [QFN-20 3x3mm](http://www.3dcontentcentral.com/secure/download-model.aspx?catalogid=171&id=173415)
	  * [QFN-36 6x6mm](http://www.3dcontentcentral.com/secure/download-model.aspx?catalogid=171&id=201710)
	  * [QFN-56 8x8mm](http://www.3dcontentcentral.com/secure/download-model.aspx?catalogid=171&id=214813)



0.65mm Pitch:





	  * [QFN-32 7x7mm](http://www.3dcontentcentral.com/secure/download-model.aspx?catalogid=171&id=167937)
	  * [QFN-44 8x8mm](http://www.3dcontentcentral.com/secure/download-model.aspx?catalogid=171&id=413189)


</td>
</tr>
<tr >

<td >Common Uses
</td>

<td >



	  * Microcontrollers
	  * High-pin count, low footprint area IC's


</td>
</tr>
</tbody>
</table>


The QFN component package is commonly used today for higher pin-count IC's such as microcontrollers. It is a **near chip-scale package**, with all the pins being around the perimeter and an optional thermal pad(s) in the center. It is one of the highest pin-density SMD packages without resorting to BGA. Note that there are different pitch footprints within the QFN family! And QFN packages do not have to be square (square is the most common), some rectangular versions exist with a different number of leads on the two sides (they always have the same number of pins on the opposite side).




QFN packages offer benefits over other packages for high-speed circuits, as well as high heat dissipation capabilities. QFN packages are lacking gull-wing leads (like that present on the QFP package), which create noise in high-speed applications.




Texas Instruments recommends rounded pads on the QFN package to prevent solder bridging. Also, stencil windows are recommended for the solder paste on the thermal pad so that a limited amount of solder is added. Too much solder can cause the QFN package to "float" around during the soldering process.




A QFN-like package with pins on only two of the fours sides is a SON package (DFN).




Confusingly, NXP names it's range of QFN  packages with SOT... (e.g, SOT-662-1), a name which is commonly reserved for transitory packages such as the popular SOT-23.




# Solder Mask




TI recommends a non-solder mask defined (NSMD) pad over a solder mask defined (SMD) pad. This is to produce consistent and reliable solder joints. As a rule-of-thumb, you want solder mask openings that are 0.1-0.14mm larger than the pad size. By default, Altium uses NSMD pads.




Some QFN packages have an exposed metal feature on the underside to indicate pin 1. If this is the case, make sure this area is covered with solder mask to prevent shorting to neighbouring traces. This is an unusual feature, and personally I have not used any QFN packages with this present.




# Solder Paste




It is recommended to reduce the amount of solder paste applied to the centre pad to prevent the QFN package from floating during reflow. A rule-of-thumb is to have between 50-80% coverage on the center pad (this obviously does not apply to QFN packages with no pad).


<table >
<tbody >
<tr >

<td >
{{< figure src="not recommended" width="359" caption="](/images/2014/12/qfn-68-component-package-with-no-solder-paste-aperture-reduction-on-center-pad.png) A QFN-68 package with no solder paste aperture reduction on the center pad (not recommended)." caption-position="bottom" >}}

</td>

<td >
{{< figure src="recommended" width="340" caption="](/images/2014/12/qfn-68-component-package-with-solder-paste-aperture-reduction-on-center-pad.png) A QFN-68 package with solder paste aperture reduction on the center pad (recommended)." caption-position="bottom" >}}

</td>
</tr>
</tbody>
</table>


It may be necessary to mask or plug vias in the center pad to prevent solder paste being carried through the via and away from the pad during reflow. Small holed vias (such as vias with a hole diameter of 0.3mm or less) do not normally cause a big problem.




# Singulation Methods




There are two singulation methods for QFN packages:





	  * Punch singulation: This is used on individually-molded QFN packages.
	  * Saw singulation: This is used on _molded array_ QFN packages.



The main difference between these two singulation methods is the cross-sectional profile. Punch singulation gives a tapered cross-section (larger cross-section at the bottom than the top), while sawn singulation gives a completely square cross-section.



{{< figure src="/images/2014/12/qfn-component-package-sawn-vs-punch-vs-col-singulation.png" width="573" caption="Cross-sectional comparison of sawn and punch singulated QFN packages. Image from http://cache.freescale.com/files/analog/doc/app_note/AN1902.pdf." caption-position="bottom" >}}



Punch singulated QFN packages are JEDEC compliant.




# Voiding




Volatiles that get trapped underneath the pad during reflow can cause voids to form underneath the component (areas in where the pad is not soldered to the PCB). Another potential cause of voiding is when too much solderpaste is applied to the centre pad, which causes the package to float on the PCB during reflow.




# Stresses




Because the QFN package sits directly on the PCB and has no standoff, they are less resilient to mechanical stresses that say, QFP packages. The amount of PCB board flex must be taken into consideration. Excessive stress can damage a QFN package.




# Lead Styles


<table >
<tbody >
<tr >

<td >
{{< figure src="this is a good thing" width="205" caption="](/images/2014/07/qfn-package-e-style-leads-fully-exposed-on-side-of-package.png) A QFN package with "e" style leads which are fully exposed on the side of the package (this is a good thing)." caption-position="bottom" >}}

</td>

<td >
{{< figure src="this is a not a good thing" width="207" caption="](/images/2014/07/qfn-package-s-style-leads-not-exposed-on-side-of-package.png) A QFN package with "S" style leads which are only partially exposed on the side of the package (this is a not a good thing)." caption-position="bottom" >}}

</td>

<td >
{{< figure src="/images/2014/07/qfn-package-wf-style-dimpled-leads.png" width="206" caption="A QFN package with "WF" style leads. They have dimples which allow for improved soldering." caption-position="bottom" >}}

</td>
</tr>
</tbody>
</table>


# Unique Corner Pins




QFN packages exist in where the **corner pins have to be of a different shape** to all the others for **clearance reasons**. The only example of this I have ever seen is the package for the [IvenSense MPU-9250 IMU](https://www.invensense.com/products/motion-tracking/9-axis/mpu-9250/). It is a QFN package with 24 pins in a 3x3x1.0mm size with 6 0.40mm pitch pins on each edge. Because of the high pin density, the outer pins on each edge almost touch each other, and so a different pin shape is used. This also means you use a different pad shape for the package footprint.


<table >
<tbody >
<tr >

<td >
{{< figure src="/images/2014/12/qfn-24-component-package-with-unique-corner-pads-mpu-9250-dimensions.png" width="306" caption="The corner pins on the QFN package used by the IvenSense MPU-9250 have a unique shape." caption-position="bottom" >}}

</td>

<td >
{{< figure src="notice how they are smaller" width="260" caption="](/images/2014/12/qfn-24-component-package-with-unique-corner-pads-mpu-9250-land-pattern.png) The footprint for the IvenSense MPU-9250 IMU which uses a QFN package with unique corner pin shapes (notice how they are smaller)." caption-position="bottom" >}}

</td>
</tr>
</tbody>
</table>


# Standardization Of Pinout For Logic Functions




JEDEC has a standard on the pinout of QFN packages for logic functions.




[JESD75-5 - JEDEC Standard - QFN Pinouts For Logic Functions](/images/2014/12/JESD75-5-JEDEC-Standard-QFN-Pinouts-For-Logic-Functions.pdf)




# 