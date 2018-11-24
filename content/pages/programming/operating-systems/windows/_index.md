---
author: gbmhunter
date: 2013-07-19 04:38:03+00:00
draft: false
title: Windows
type: page
url: /programming/operating-systems/windows
---

# Overview


These pages are all about the Windows operating system and the command-line interface. For information about how to write batch scripts and it's programming syntax, see the [Batch Files page](http://blog.mbedded.ninja/programming/languages/batch-files).


# Child Pages


<table style="width: 600px;" border="0" >
<tbody >
<tr >

<td >[Windows Driver Development](http://blog.mbedded.ninja/programming/operating-systems/windows/windows-driver-development)
</td>

<td >Info about writing drivers for Windows.
</td>
</tr>
<tr >

<td >[Customizing Folders With Desktop.ini](http://blog.mbedded.ninja/programming/operating-systems/windows/desktop-ini)
</td>

<td >How to create a desktop.ini file, how to change the icon for a folder, and add a tool-tip/description for a folder.
</td>
</tr>
</tbody>
</table>


# Auto-complete


Did you know that MS-DOS has an auto-complete function, just like Linux, except **it's turned OFF by default?** To turn it on, type the following into the command line:

    
    cmd /f


And to turn it off again (why would you ever want to do such a thing!):

    
    cmd /f:off


Now, to use it! It works slightly different to Linux. Instead of one button (_tab_), there are two. Press **_Ctrl-D_** to auto-complete directories, or **_Ctrl-F_** to auto-complete files.

If there are multiple choices, pressing the button repeatedly will cycle through the options.


# Comments


There are two ways to display comments:

    
    rem This is a comment
    
    : This is also a comment, and using a much simper keyword than rem




# File Manipulation




## Displaying Files


To display a list of files and folders in the current directory, use the command:

    
    dir


This will display the full-length filenames/foldernames. To display the names in short format (6 letters, a matilda (~) and then a numeral, usually 1, followed by the extension), use the following:

    
    dir /X




## xcopy


xcopy is a native Windows command which copies files and folders. It has more features than the copy command.

Syntax: xcopy source [destination] [/a] [/b] [/c] [/d [:date]] [/e] [/f] [/g] [/h] [/i] [/j] [/k] [/l] [/m] [/n] [/o] [/p] [/q] [/r] [/s] [/t] [/u] [/v] [/w] [/x] [/y] [/-y] [/z] [/exclude:file1[+file2][+file3]...] [/?]

xcopy does not have any support for resuming an interrupted command. So if you are in the middle of copying a large number of files, and it gets interrupted (the connection drops, a fileame is too long, e.t.c), you will have to start again.

In Windows 95 and 98, two versions of xcopy are natively available, xcopy and xcopy32. When using xcopy, xcopy32 is automatically called if inside a Windows environment. For this reason, **you never have to call xcopy32 directly**.

There are more advanced command-line Windows copy programs, such as robocopy, which supports resuming. If you are looking for a GUI, try RichCopy. Although I have had RichCopy v4.0 crash on me when coming across multiple files which have file names too long for Windows to support.

[singlepic id=1148 w=600 h=450 float=center template=caption]


## robocopy


If xcopy wasn't enough, there is also robocopy. robocopy first shipped with the XP Resource Kit, and was provided standard with Windows 7 and 8.

The standard syntax is:

    
    robocopy source_folder destination_folder [files_to_copy] [options]


where files_to_copy defaults to *.* (all files) if nothing is provided.

The most popular options are (in rough order of popularity):
<table style="width: 600px;" border="0" >
<tbody >
<tr >

<td >**Options**
</td>

<td >**Description**
</td>
</tr>
<tr >

<td >\s
</td>

<td >Copy all sub-folders also (similar to recursive mode in Linux systems)
</td>
</tr>
<tr >

<td >\MOV
</td>

<td >Move files rather than copy them (i.e. delete after copy). This does not delete directories, use \MOVE for that.
</td>
</tr>
<tr >

<td >\MOVE
</td>

<td >Moves files and folders rather than copy them (i.e. delete after copy). If you only want to move files, and not delete directories, see \MOV.
</td>
</tr>
<tr >

<td >\r:n
</td>

<td >Retry failed copies n times. Default is 1 million! This can be a bit ridiculous, especially with a 30s wait period between retries. For backing up large amounts of data, I recommend setting this to a lower value (e.g. \r:1), and then investigating how many fails occurred after the transfer is complete.
</td>
</tr>
</tbody>
</table>



## Deleting Files And Directories


Confusingly, windows has a range of different delete commands, and the one you need use depends on what version of windows you are running, and whether you are deleting files, empty folders, or folders containing files.

    
    # Delete a file (1st way)
    del filename.ext
    
    # Delete a file (2nd way)
    # Note that "del" and "erase" are the same command
    erase filename.ext
    
    # Remove a directory which is empty
    rmdir directory-name
    
    # Remove a directory which is not empty
    rmdir directory-name /S


