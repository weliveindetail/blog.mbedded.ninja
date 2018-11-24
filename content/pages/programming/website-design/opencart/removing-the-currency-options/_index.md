---
author: gbmhunter
date: 2013-04-15 09:38:21+00:00
draft: false
title: Removing The Currency Options
type: page
url: /programming/website-design/opencart/removing-the-currency-options
---

One way to easily remove the currency options is to use CSS to hide the currency elements. To do this, open up your open cart's theme css file (usually found at "catalog/view/theme/<theme-name>/stylesheet/stylesheet.css"), and add the following code:

    
    /* Hides the currency options */
    #currency { display: none; }


[singlepic id=649 w=800 h=800 float=center template=caption]