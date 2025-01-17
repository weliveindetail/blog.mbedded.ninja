---
authors: [ "Geoffrey Hunter" ]
categories: [ "Updates", "Site Admin" ]
date: 2013-03-28
draft: false
tags: [ "code", "descendants", "highlighter", "menu", "plugins", "programming", "syntax", "Wordpress" ]
title: Changes Over The Last 3 Months
type: post
---

The [C](/programming/languages/c), [C++](/programming/languages/c-plus-plus), and [C#](/programming/languages/c-sharp) programming pages have been updated with lots more info.

I changed the syntax highlighter plugin from [Syntax Highlighter Evolved](http://www.viper007bond.com/wordpress-plugins/syntaxhighlighter/) to the more feature rich [Crayon Syntax Highlighter](https://github.com/aramk/crayon-syntax-highlighter). Code should be displayed better with this plugin, as I was experiencing tab conversion problems (when pasting from other programs) with the other plugin. I haven't got the colours quite right yet (the old plugin theme looks nicer!)...but I'm working on that.

{{< img src="old-and-new-code-display-plugin-comparison.jpg" caption="A comparison between the old and new syntax highlighter plugin used on CladLabs."  width="600px" >}}

I managed to tweak the [Add Descendants To Menu Items plugin](http://www.viper007bond.com/wordpress-plugins/add-descendants-as-submenu-items/) to only include children in the menu, and not grand-children descendants or further. Visit the [Wordpress Plugins That This Site Uses page](/programming/website-design/content-management-systems/wordpress/wordpress-plugins-that-this-site-uses/) to see how to modify it. It now means I can add as many grandchildren to the menu pages without them cluttering up the menu. This has allowed me to split large single-page topics into smaller many-page sections, and improves the readability of this site.
