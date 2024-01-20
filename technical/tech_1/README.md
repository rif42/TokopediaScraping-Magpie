## Assumptions
This program runs under the assumptions:  
- data is scraped on the search page  
- scraped data is only the result of the search, not the ads and recommendations (because they use different classes and ID's in their divs)  
- the desired price data is an average between the price spread. for example if seller sells xiaomi phones, there are xiaomi 13 for $200 and xiaomi 14 $300, the card will state $200-$300, and the scraper will average the price spread to $250  

## Lessons Learned
Always start small and simple, test and iterate while add more features slowly. Scraping (and programming in general) has a lot of uncertainty. write-test iteration is better because you always see what works and advance from there. When problems arise, you spot them early and no need to rework the entire codebase.  

For some reason the search by class doesnt work reliably in tokopedia. Usually some websites use completely random css classes and ID, making it impossible to search by class. But Tokopedia uses seemingly random names, but they stay that way. As a result, i have to use XPATH to search. The firefox dev tool helps a lot because i can click an element, copy their xpath and compare them with other elements without trial and error on every single divs.  

Error handling is extremely important. In automation, you want the program to be as independent as possible, requiring no human intervention when its running. An error completely stops the program, unless its handled properly.  

Lambda functions help alot in iterating dataframe columns without lengthy for loops. Chatgpt suggested this approach and i expanded upon it.  

## Challenges
Error handling is the hardest challenge. I have to account for every possibility of error and handle them, or risk the program crash or stops due to error.  

Finding and confirming the element was a decent challenge. In the end i used xpath so i can target custom attributes and it works well.  

In scraping, reliability and fixed pattern is always desired, but reality often differ from what we desire. Patterns can move and shift, and it will throw off our program. Its almost always better to use exact timings such as wait-until as opposed to fixed timings such as for loops. In this program i used fixed timings for loop to scroll down to the page navigation. I admit this wasn't ideal, but im curious if its reliable enough as it is. In the end, its reliable enough to be used throughout my testing sessions. Will change it to wait-until.  

The preprocessing is a bit challenging, but given my python background, i understood the basic workflow and was able to utilize chatgpt to optimize the code.  

## Usage of ChatGPT
I see chatpgt as a faster and more convenient google search. Give it enough information and context, and it will help you. But if you ask too much, it will hallucinate and lead you astray. Also, you can't ask ChatGPT a question if you dont know what you're asking.  
Generally, i try to figure out the workflow first, then build it slowly, asking chatgpt when im stuck or forgot. Then after its done, i usually ask chatgpt to optimize the code and clean it up a bit. At this point, chatgpt has enough information to actually do its work, and i can get new lessons on how to optimize my code so i can implement it myself in the future.