# LGBTQ-Pertinent-Legislation-and-Politicians

Project to get data on LGBTQ related legislation as well as state level politicans in potentially every state.
Scrapes laws from ACLU: https://www.aclu.org/legislation-affecting-lgbtq-rights-across-country and politician data from ballotpedia: https://ballotpedia.org
Originally started summer 2021, made for Arkansas, currently updating for Texas in 2022.

As of now, it seems ACLU web scraper does not and can not work consistently because status of bills are not always placed in <p> statements, so they can not be sorted via findAll or similar methods, and my previous technique of sorting them does not work because they do not start or end consistently (previously they all ended with dates).  
