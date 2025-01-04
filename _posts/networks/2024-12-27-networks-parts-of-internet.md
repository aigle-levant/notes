---
title: "Parts of the Internet"
subtitle: "Protocols, IP, Domain - what are they?"
categories: [concepts, networks]
tags: [internet]
---

## Client-server infrastructure

Computers connected to the internet serve as clients and servers to each other.

Clients are the devices that access the internet. Servers are the computers storing webpages, sites, apps, etc.

### Domain Name System [DNS]

When you type the address of a website and press enter, the browser looks up a registry called Domain Name System [DNS] to find the IP address of the website [here, it's called a domain] to retrieve it, which is similar to how one would find their name in the voting list.

It does this to send request to the right server.

#### IP address

Internet Protocol [IP] address is an unique identifier for a computer in a network. It is made up of 4 sets of numbers separated by dots.

> `142.250.190.78` is the IP address of the domain `google.com`

There are 2 versions of IP address - IPv4 and IPv6. IPv4 is currently more popular.

#### Domain

It is another name for a website.

It organises, delivers content and allows you to access services in the internet.

A domain's name is a label for an IP address.

### HTTP request

Upon finding the IP address, the browser sends a HTTP request to the server. This is done using protocols like TCP / IP and is performed across your internet connection.

#### Protocols

These are sets of rules that deal with how data is transmitted [sending and receiving] across the internet.

##### Transmission Control Protocol [TCP]

It ensures that data delivered is error-free, reliable and organised. Its alternative, UDP, is used for streaming and gaming.

##### Internet Protocol [IP]

It handles addressing and routing data packets across the internet. This is where IP addresses are defined.

##### Hyper Text Transfer Protocol [HTTP] / HTTP Secure [HTTPS]

These are used for accessing webpages. HTTPS uses encryption, making this process even more secure.

##### DNS

It converts domain names into IP addresses.

### Post-approval

If approved, server responds with `200 OK` and sends data packets to the browser. These packets contain parts of the website.

Now the browser assembles them into a webpage and displays it to you.
