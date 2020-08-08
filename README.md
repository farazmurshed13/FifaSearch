fifasearch lets a user find useful stats for any player in FIFA 20 within seconds

Languages/Tools: Python, Flask, Twilio, Heroku
Player Stats: Player name, team name, age, overall rating, potential rating, contract expiry date        
Source: sofifa.com

**Application:**
1. User sends an sms message to a Twilio verified phone number
    - format1: "_player-name_" i.e. "cristiano"
    - format2: "_player-name_, _team-name_" i.e. "cristiano, juventus"
    - substrings are used for search, so a shortened form such as "cris" would still let "cristiano" be a result
2. Within 5 seconds, user should receive an sms response 
    - format1: "_player-name_, _age_, _rating_/_potential_, _team-name_ (exp: _contract-end-yr_) "
    - format2: "_#_ result(s) found"
    - Searches with 1 result receive format1; other receive format2
    - Twilio message segments are charged separately, and outputs longer than 160 chars are split into multiple
      segments. To prevent this, format2 exists.
      
**Notes:**
- User must have a Twilio phone number, connected to a webhook url that hosts Flask application (i.e. Heroku)
- interact.py handles incoming sms and supplies response, using Flask and TwiML
- scrape_fifa.py scrapes data from web source and stores in JSON file 
- requirements.txt lists necessary installations
- Procfile is used for Heroku Git integration