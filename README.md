# week-3-day-4-homework: NOTES

line by line notes to my solution

30. imported re to be able to use regular expressions (regex)
    
32. opened the associated text file to access the data
33. saved info to a variable for easier access
    
35. I set up my regex to identity the user's name (first and last must each start with an uppercase), age (typical human
    are at the low end 1 digit and can go up to 3, so I set those as my range), and country (had to ensure that it would
    for country names comprising two words e.g., United States, South Africa, etc.) as well as single words(e.g., Canada).
    However, since not all must be two words, I appened the * to the second range to declare that it was ok if there were 0
    occurences, but to continue if it was found.

37. Defined our function so that it takes in the argument of the data (user_records) and our regex pattern (user_info).
38. created a variable set initially to 0 to tally the count of valid records
39. created a variable set initially to 0 to tally the count of invalid records

41. Cosmetic output data (for the sake of it)
42. Cosmetic output data (for the sake of it)
43. Cosmetic output data (for the sake of it)
44. Cosmetic output data (for the sake of it)
45. Set up for loop through each line in the data (user_records) and begin extracting the information
46. Assign information matching my criteria (user_info) to the variable of match
47. Set up conditional to weed out valid records and invalid records while also updating the tally
48. In my regex user_info I had framed the information into groups, group(1) = name, group(2)= age, and group(3) = country. 
    Here, I assign the values of group(2) the variable age.
49. Like with age, I assign the value of group(3) as country, which comprises the second element to be printed.
50. print a formatted string, using the previously assigned variables of age and country, to display the records should they be valid.
51. Increment the tally by one for each valid record found.
52. Set up else statement in the case that a record does not return valid.
53. If the record is invalid, print the ("Invalid Records") statement
54. Increment the tally of the invalid records for each record that does not meet the valid requirement
55. Print the count of the valid records
56. Print the count of the invalid records

58. Indent back outside of the function and call it.