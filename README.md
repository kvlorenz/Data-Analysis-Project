# Data-Analysis-Project
Hi Everyone! This is a fun little ad hoc project that allows you to analyze a
record of purchases in terms of the size of each purchase and its cost for using a
certain type of check. The project is based on a spreadsheet made by the UCSD IPPS
services which includes around 15000 purchases in the actual file. I have uploaded
a sample of what the csv looks like without giving away the actual data to protect
the privacy of those purchases. The structure of the csv file looks like this:

PO_NUMBER,CHECK_NUMBER,CHECK_DATE,PAID_AMOUNT,CANCEL_IND,PAYEE_ID,ORGIN_CODE,ORGANIZATION,PAYMENT TYPE

The payment type is denoted with a single character. A "4" is for a paper check, an
"A" is for direct deposit, an "S" is for same day check, and an "X" is for virtual
card. The paper and same day checks cost $7.43 per purchase while the virtual and 
direct deposit checks are $4.50 per purchase. What this program does is classify
each purchase based on the size of the purchase and graph what each the frequency of
what check is used for different sizes. With the actual data, I created two graphs
(as seen in the file "graph.jpg") that shows the results of the varying purchases.

If you would like to know more about this project or would like to request any
modifications that I can do, e-mail me at kvlorenz@ucsd.edu.
