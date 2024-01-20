## Problem 1 : Changes from website owner
PT.Goto as the owner of Tokopedia can change the website and app however and whenever i want. This is outside of our control. They can add a popup, add another row of ads, or change the search layout to the website. All of these might affect the performance of our scraping script.  

### Solution
Do a daily run checks to see if the script is working or not. Or download the page everyday and compare the difference of class names. Update the script when you see potential breakage.  

## Problem 2 : Error Handling and Force Majeure
Scraping scripts are usually designed to run for a lot of time uninterrupted. Bad error handling can cause errors to stop the operation completely, wasting a lot of resources and time because we have to start over. Force majeure like electrical outage, internet outage, or human errors could also sabotage the scraping process.  

### Solution  
Make an incremental data collection to storage. For example, for this tokopedia scraping program, i will extract all the data from one page, then immediately export one page worth of data to csv file, then continue scraping the next page. Let's say we're scraping 300 pages, and at page 12 an internet outage happens. This way, we still have the scraped data from page 1-12, and we know exactly where to start again. Once all 300 pages are scraped, a function will aggregate them into one csv, and do further preprocessing if needed.

## Problem 3 : Finding reliable pattern to extract data  
Sometimes the data we need are so unique, we can't find and exctract it using regular means. This is where the skill and experience of the programmer comes in to "MacGyver" their way into the solution.

### Solution
Let the data be null and impute it later using regression function or a specially trained machine learning model. Depends on how much the null data, this approach seems to be the best solution.