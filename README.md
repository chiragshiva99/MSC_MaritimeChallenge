# DDW 2D Bonus Submission 

Contributors 
- Ankita Parashar
- Chirag Shivakumar 
- Devanshi Joshi
- Prachi Jayesh Suthar 

## Run Server
- **Step 1:** Clone

```shell
$ git clone https://github.com/chiragshiva99/MSC_MaritimeChallenge.git
```
- **Step 2:** Create virtual environment and install `requirements.txt`
```shell
$ cd marineproject

$ python -m venv virtenv

for Mac
$ source virtenv/bin/activate

for Windows
> virtenv/bin/activate

$ python -m pip install -U --force-reinstall -r requirements.txt
```
- **Step 3:** Run Server 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
-**Step 4:** Open this link  [`http://127.0.0.1:8000/`] to access our webpage

To stop the web app type `CTRL+C`. 


