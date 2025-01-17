---
authors: [ "Geoffrey Hunter" ]
categories: [ "Electronics", "Electronic Components" ]
date: 2013-10-02
description: "EEPROM, flash, SD cards and more info about memory."
draft: false
lastmod: 2020-06-25 
tags: [ "memory", "EEPROM", "flash", "I2C", "M25P128" ]
title: "Memory"
type: "page"
---

## EEPROM

Even though flash is technically a form of EEPROM, the word EEPROM is usually reserved to smaller-memory, read/write/erase 1 byte at-a-time ICs (flash is usually erased in pages and has way more memory).

The cheapest EEPROM on the market is usually available with an I2C, 1-wire (e.g. UNI/O), or SPI-like (e.g. Microwire) interface, in packages such as the SOT-23-6, SOIC-8 and DIP-8.

{{< img src="example-eeprom-pinout-in-sot-23-6-package.png" width="361px" caption="Example pinout of a EEPROM IC in a SOT-23-6 component package." >}}

### Unique IDs

Some EEPROM chips also come with unique ID's burnt into memory. The [DS28E05 by Maxim Integrated](http://datasheets.maximintegrated.com/en/ds/DS28E05.pdf) is one such example. It provides a unique 64-bit ID number which can be read back from read-only memory. It also serves as it's 1-wire address.

{{< img src="ds28e05-eeprom-ic-connected-to-micro-using-1-wire.pdf.png" width="390px" caption="The DS28E05 EEPROM I2C, connected to a microcontroller via the 1-wire interface."  >}}

## Flash

Flash sometimes uses flip-flop style pin naming conventions. The M25P128 is one such example.

{{< img src="m25p128-flash-ic-that-uses-flip-flop-style-naming-for-spi-pins.png" width="427px" caption="The M25P128 flash IC which uses flip-flop style pin naming conventions." >}}

## SD Cards

NAND flash is used as the main memory device inside of SD cards. There is also a memory controller IC (typically a microcontroller) which acts as an intermediary between the flash and the connected device reading/writing to/from the memory.

### The TRIM command

The TRIM command is an ATA command which can be sent to an SSD controller by the OS. It is sent from the OS when a file is deleted from the filesystem, and the OS tells the SSD controller which NAND pages have been deleted. If the controller supports TRIM commands, then it will flag the pages for deletion so that the SSD controller can erase/free the pages. This increases the pool of available memory the wear-levelling algorithm can work with, allowing it to work more effectively and increasing the life time of the storage device.

```text
# m     h       dom     mon     dow     command
0       1       *       *       *       ionice -c 3 fstrim -v /
```

### Wear-levelling

> Wear leveling is an intrinsic part of the erase pooling functionality of cards in the SanDisk microSD Card Product Family using NAND memory.[^sandisk-sd-oem-product-manual]

There are two types of wear-levelling, _static_ and _global_.

A local cached copy of [SanDisk Whitepaper: SanDisk Flash Memory Cards Wear Leveling, October 2003](/electronics/components/memory/sandisk-white-paper-flash-memory-cards-wear-leveling.pdf).

### Multi-level Cells (MLCs)

In the context of NAND memory, a cell is an individual storage element (essentially a MOSFET). The first NAND cells were used to store one 1-bit of information and are called _single-level cells_. A _multi-level cell_ (MLC) is a cell which can hold more than one bit of information. Most cheaper, high-density SD cards on the market in the 2010's/2020's utilize multi-level cell NAND flash to offer memory spaces of 64GB, 128GB and beyond. However, multi-level cells come at a cost --- they are less reliable than their single-layer cell (SLC) counterparts.

1. **SLC** (_Single Level Cell_) is the highest grade of NAND flash. Each cell only has one voltage level it is charged to, allowing only 1-bit to be stored per cell. It is very hard to purchase via standard retail outlets. [Example](https://nz.rs-online.com/web/p/micro-sd-cards/1448058/). As of 2020, 8GB class 10 SLC cards retail for approx. US$120, approx. 5-10x more expensive than their MLC counterparts[^digikey-sd-memory-cards-section].
2. **MLC** (_Multi Level Cell_) has 4 voltage levels per cell, allowing 2 bits of information to be stored. Read speeds are typically lower than _SLC_ because the controller may need to read the cell at two different voltages to help resolve errors[^wikipedia-multi-level-cell]. MLC cards are also marketed for industrial use. The Intel 8087 was one of the first mass-produced ICs to use MLC technology.

SLC memory is recommended for SD cards that are going to be used for intensive and/or critical applications in where the SD card will be written to frequently. This includes RaspberryPis that will be used frequently for more than just personal/hobbyist use. RaspberryPis typically use an SD card as it's main source of non-volatile RAM, and writing to the hard disk writes to the RaspberryPi.

Cheaper MLC memory is recommended for typical, standard SD card applications such as storing photos, music and transferring files between devices.

[^sandisk-sd-oem-product-manual]: [https://datasheet.ciiva.com/26837/getdatasheetpartid-335894-26837658.pdf](https://datasheet.ciiva.com/26837/getdatasheetpartid-335894-26837658.pdf)
[^wikipedia-multi-level-cell]: [https://en.wikipedia.org/wiki/Multi-level_cell](https://en.wikipedia.org/wiki/Multi-level_cell)
[^digikey-sd-memory-cards-section]: <https://www.digikey.com/products/en/memory-cards-modules/memory-cards/501>