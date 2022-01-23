[![Netlify Status](https://api.netlify.com/api/v1/badges/201fc4ed-fb79-4fe9-99dc-e6ac0f7ca556/deploy-status)](https://boring-hodgkin-b0d1fa.netlify.app/)



# GSoC-Organisation-Search-by-Technologies

<img width="775" alt="search" src="https://user-images.githubusercontent.com/59335537/150690113-7a56ae7f-77c3-4ed0-92be-0eab4b6c83ed.png">


[Site Link](https://boring-hodgkin-b0d1fa.netlify.app/) 

Search Google Summer of Code organisations by technologies / programming languages used.

## To-Do 
- Add searchbar for technologies as well 
- Clean up data

## How it was made
I wrote a python script to automate the process of extracting data of all organisations from the GSoC 2021 website, I couldn't do it just by regulat html scraping as the blocks were expandable, so the python script opened the block, inspected the element, then copied that ```<div>``` and pasted it into a file for all the organisations. 

Once all the data was collected I made the search feature over the data.
