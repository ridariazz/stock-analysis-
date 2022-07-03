# Stock Analysis Using VBA 

## Overview of Project

### Goal/Purpose 
The purpose of this analysis was to be able to analyze an entire dataset of stocks from 2017 and 2018. The goal of this assignment was to be able to refactor a VBA code to see if we can allow the script to run faster and be able to loop through all the data one time to collect the total volume and return for the years of 2017 and 2018. Our main purpose is to determine whether refactoring an existing code has increased efficiency of the overall analysis. 

### Background 

Before refactoring the code, lets look at the data and allow it to make sense so we know what we are working with. 
The data presented to us has has two sheets with the stock performances for the years of 2017 and 2018. 
The stock information in the data includes the date stock was issued, opening/closing and adjusted closing prices, the volume of the stock and lastly the highest/lowest prices. 
Our goal is to create another sheet, "All Stocks Analysis," where we will compute the 12 different stocks (tickers) of intrest presented in the data and their relative total volume and return for the years of 2017 and 2018 by creating a macro. 

## Results 

### Analysis
Using the data we have from 2017 and 2018, I created a new module (Module 2) to paste the code given for refactoring purposes. We must create a new macro on this new moldule, so our previous code in Module 1 doesn't get affected and we are able to continue forward without errors. We have thousands of stocks to compute performance for and the overall total volume of revenue of the stock market over the last few years from our dataset; therefore, we need to also look at how refactoring our code can allow us to produce a quicker execution time.  

The refactored code is down below (Figure 1). 

**Figure 1**

Figure 2 displays the part of the code we refactored which is creating a *for loop* to initialize the ticker volumes to zero and also input a for loop that will loop over all the rows in the spreadsheet. 

**Figure 2**

<img width="597" alt="Screen Shot 2022-07-02 at 6 44 29 PM" src="https://user-images.githubusercontent.com/106577074/177021760-a5c89eb6-79fe-409e-bbdb-6fed14ade3ba.png">

Next, we want to analyze the total volume and return for stocks for any year. Here, we need to create a script within' our for loop which will increase the current stock *ticker volume (tickerVolumes variable)* and adds the ticker volume for the current step. 

**Figure 3**

<img width="775" alt="Screen Shot 2022-07-02 at 8 49 51 PM" src="https://user-images.githubusercontent.com/106577074/177023801-cd9585e6-dc23-402e-ab1f-cccb85821d62.png">

Then, we write an if-then statement to check if the current row is the first row with the selected *tickerIndex*. If it is, then we assign the current closing price to the *tickerEndingPrices* variable. Following along, we write another script which increases the tickerIndex if the next row's ticker doesn't match the previous row's ticker. This entire process allows us to correctly assign and determine the variables to calculate our stock volume and returns for the respective years.

**Figure 4**

<img width="685" alt="Screen Shot 2022-07-02 at 8 55 47 PM" src="https://user-images.githubusercontent.com/106577074/177023952-55b4612c-ca23-41bf-9c8c-f2b3b5b86491.png">

Lastly, we wrote a for loop which will loop through all of our arrays for the 12 tickers and calculate the total volume and return for the years of 2017 or 2018. 

**Figure 5**

<img width="693" alt="Screen Shot 2022-07-02 at 8 59 52 PM" src="https://user-images.githubusercontent.com/106577074/177024046-6b0cb2bc-9b7c-4741-95ef-43079d97f290.png">

Here is how our entire subroutine for "All Stocks Analysis Refactored" looks like:

<img width="740" alt="Screen Shot 2022-07-02 at 6 23 01 PM" src="https://user-images.githubusercontent.com/106577074/177024100-21754fad-bdb0-498b-8e49-c227b9240d63.png">

<img width="865" alt="Screen Shot 2022-07-02 at 6 23 11 PM" src="https://user-images.githubusercontent.com/106577074/177024101-4ac40366-ea43-4433-86f4-e503b70e6091.png">

<img width="696" alt="Screen Shot 2022-07-02 at 6 23 24 PM" src="https://user-images.githubusercontent.com/106577074/177024102-8e4c755b-359c-4104-bd6a-effdf18402ec.png">

<img width="734" alt="Screen Shot 2022-07-02 at 6 23 35 PM" src="https://user-images.githubusercontent.com/106577074/177024104-0b6bad65-9de1-47b3-a79b-f7e783a95baa.png">

## Summary 

### Refactoring Codes

Refactoring allows our code to be a lot cleaner and help us make sense of what we are trying to code for. Starting a code from scratch can be very difficult and almost feel a bit disorganized. Therefore, refactoring paves a path for us to get to our destination, but tweak things along the way to overall make the code work the most efficient for us. 

**Advantages** 

The advantages of refactoring include ways we can create faster programming by looking at the bugs that currently exist or how we can fix the flaws; i.e. slow execution times or computing of the data. For instance, in this assignment, we wanted to compute the total volume and return for the years 2017 and 2018, so besides copying/pasting the code twice (to compute both 2017 and 2018 stock data), we just tweaked the original code to improve efficiency. In the end of refactoring, we got a quicker execution time and a message box that can compute data of stocks for the years 2017 and 2018 all in one. 

**Disadvantages** 

There are also disadvtanges to refactoring. For instance, adding new loops or scripts can allow the code to have more errors and new bugs which I most certainly came across. The smallest little typo or error in the code itself can cause the entire computer to be confused and not know how to move forward as it can easily be confused by what we are trying to execute. Also, if we need larger codes to refactor, that can potentially cause risk for our codes if the original code itself did not have the proper test cases. 

This article by [Stack Overflow](https://stackoverflow.com/questions/43983284/what-are-the-advantages-and-disadvantages-of-refactoring-code-smell-in-software) really put the pros and cons of refactoring into perspective for me and allowed me to see how refactoring can be a great thing, but also a very dangerous and tricky aspect of coding to work with. 

## Refactoring the original VBA Script 

The most obvious advantage of refactoring the original Stocks Analysis script was the decrease in macro run time. The original script took about 0.2 seconds to run the code for the year 2017 and 2018, but with the refactored code, both years took ~0.08! The cons, well, the most minor things I looked over upon (like formatting) and not putting the correct variables in the for loops kept giving me errors. 

**Figure 6: 2017 Macro Run Times**

*Original code* 

<img width="269" alt="Screen Shot 2022-07-02 at 6 03 01 PM" src="https://user-images.githubusercontent.com/106577074/177031964-584971c9-e2c1-4bd6-85e6-260be7371cfe.png">

*w/ Refactored Code*

<img width="261" alt="Screen Shot 2022-07-02 at 1 03 20 PM" src="https://user-images.githubusercontent.com/106577074/177024547-38048e69-5533-4e56-973a-22808f36c159.png">

**Figure 7: 2018 Macro Run Time**

*Original Code*

<img width="274" alt="Screen Shot 2022-07-02 at 6 03 18 PM" src="https://user-images.githubusercontent.com/106577074/177031967-640d92e3-d88d-462b-90ba-081449c78bc4.png">

*w/ Refactored Code*

<img width="261" alt="Screen Shot 2022-07-02 at 1 03 34 PM" src="https://user-images.githubusercontent.com/106577074/177024539-658e084f-0c8a-4e2f-862d-50a831734c20.png">

## Conclusion 

After completing our analysis with the help of our refactored code, we are able to determine the patterns of stock performances for the years 2017 and 2018. Stocks in 2017 were generating more total daily volume and return versus 2018 where majority of those same stocks were bringing in less total daily volume and went down in their overall return percentage. However, the smart stocks to invest in would be ENPH and RUN as those two stocks were the only ones that didn't have a decrease to their overall value. RUN, in fact, generated a higher return percentage of 78.5% and total daily volume in 2018 versus 2017! 
