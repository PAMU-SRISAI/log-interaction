# log-interaction
Interaction with the log files and finding the count of ERROR and INFO and keeping in csv files. Then converting them to html to view the table in webpage.

# If your working with bash

`Step-1:` Covert csv2html.py and log2csv.py files to executable files using `sudo chmod +x csv2html.py` and `chmod +x log2csv.py`

`Step-2:` Now run log2csv.py file to get "error_message.csv" and "user_statistics.csv" files.

`Step-3:` Now run following commands to get html files
        `./csv_to_html.py error_message.csv error_msg.html`
        `./csv_to_html.py user_statistics.csv user_stats.html`

"error_msg.html" and "user_stats.html" are the required html files.
