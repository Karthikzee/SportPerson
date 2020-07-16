# Sports Person

[![N|Solid](https://i.imgur.com/sQVAM2n.png)](https://github.com/Karthikzee/SportPerson)

Sport Person is my Final Project Submission for the Course CS50 offered by Harvard University on edX.

Sport Person is Free-to-use web application to view sports scores like Cricket, Foot Ball and Basket Ball.

This web app was built using Python more specifically Django web framework for the backend and Html, CSS And Javascript was used for the frontend.

The data used in the app is recieved using a open source sports score API called as [Sports.py](https://pypi.org/project/sports.py/)

Data from scores api is recieved as Dictionary of teams and scores which is then iterated over and stored in sqlite data base.

The data in data base is used to display the scores.

Users must login before viewing the score, this is to keep track of number of users using the web application.

The registration form and login was created using the default registration pages provided by the Django web Framework.

# How to Run the Project
1. Clone download the Repository [Sports Person](https://github.com/Karthikzee/SportPerson.git) .

2. Go to cd into SportPerson/SportPerson

3. Run
``` python
pip install -r requirements.txt
```
OR
``` python
pip3 install -r requirements.txt
```

4. After installation of required dependencies you can launch a local server using
``` python
python manage.py runserver
```
and go to the mentioned local host address

I am Karthik G, Bengaluru, India and this was Sports Person.

Thank You Prof.David J Malan, Mr.Doug Lloyd, Brian Yu, CS50, Harvard and edX. :)

