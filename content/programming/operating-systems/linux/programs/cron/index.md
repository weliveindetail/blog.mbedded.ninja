---
authors: [ "Geoffrey Hunter" ]
categories: [ "Programming", "Operating Systems", "Linux", "Programs" ]
date: 2014-02-03
draft: false
title: cron
type: page
---

## Overview

Most web-servers give you the ability to setup and run cron tasks for maintaining your website. These are normally setup from cPanel or equivalent, and is called a [webcron](http://en.wikipedia.org/wiki/Webcron).

## The Basics

To list the current crontabs type:

```sh   
sudo crontab -l
```

## Special Characters

There are a number of characters which have a special meaning when writing a crontab.

<table >
	<thead>
		<tr>
			<th>Character</th>
			<th>Description</th>
			<th>Compatibility</th>
		</tr>
	</thead>
  <tbody>
    <tr>
      <td><code>*</code></td>
      <td>The asterisk character matches any occurrence of the relevant time field. For example, <code>*</code> in the second field (hour field) will cause it to match every hour.</td>
      <td>Works with most versions of cron.</td>
    </tr>
    <tr>
      <td><code>-</code></td>
      <td>A hyphen is used to define a range for a time field. For example, <code>10-45</code> in the minute field matches every minute in the hour between 10 and 45 (inclusive).</td>
      <td>Works with most versions of cron.</td>
    </tr>
    <tr>
      <td><code>/</code></td>
      <td>The forward-slash character describes increments of ranges (so is used with the <code>-</code> character.</td>
      <td>Works with most versions of cron.</td>
    </tr>
    <tr>
      <td><code>,</code></td>
      <td>The comma is used to indicate items of a list. For example, <code>2001, 2013, 2050</code> matches the years 2001, 2013 and 2050.</td>
      <td>Works with most versions of cron.</td>
    </tr>
  </tbody>
</table>

## Predefined Timing Words

These are pretty self-explanatory.

<table>
	<thead>
		<tr>
			<th>Word</th>
			<th>Description</th>
			<th>Equivalent To</th>
		</tr>
	</thead>
  <tbody>
    <tr>
      <td>@hourly</td>
      <td>Runs once an hour (at the beginning of the hour).</td>
      <td>0 * * * *</td>
    </tr>
    <tr>
      <td>@daily</td>
      <td>Runs once an day (at midnight).</td>
      <td>0 0 * * *</td>
    </tr>
    <tr>
      <td>@weekly</td>
      <td>Runs once an week (at midnight every Sunday).</td>
      <td>0 0 * * 0</td>
    </tr>
    <tr>
      <td>@monthly</td>
      <td>Runs once an month (at midnight on the first day of the month).</td>
      <td>0 0 1 * *</td>
    </tr>
    <tr>
      <td>@yearly (or @annually)</td>
      <td>Runs once an year (at midnight on the first day of the year).</td>
      <td>0 0 1 1 *</td>
    </tr>
    <tr>
      <td>@reboot</td>
      <td>Runs on reboot. Note that this can either be implemented as running only on reboot (e.g. on Debian systems), or everytime the cron daemon starts (i.e. startup, but could trigger at other times also).</td>
      <td>n/a</td>
    </tr>
  </tbody>
</table>

## Logging

By default, cron saves the output to the user's mailbox. You can save it to a separate logfile instead with the following syntax:

```sh   
* * * * * shell-command-here >> /var/log/cron-log-file.log 2>&1
```

This redirects both stdout and stderr to the file `cron-log-file.log`.
