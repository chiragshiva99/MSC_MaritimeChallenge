# DDW 2D Bonus Submission 
SC05 Group 6 
- Chirag Shivakumar (1004996)
- Ethan Pang (1005197)
- Lin Xi (1005145)
- Nicole Shuan (1005429)
- Tran Nguyen Bao Long (1005227)

## 0. Run on Voc
- **Step 1:** Clone

```shell
$ git clone https://github.com/chiragshiva99/DDW_2d_bonus.git 
```
- **Step 2:** Create virtual environment and install `requirements.txt`
```shell
$ cd DDW_2d_bonus

$ python -m venv virtenv

$ source virtenv/bin/activate

$ python -m pip install -U --force-reinstall -r requirements.txt
```
- **Step 3:** Set `voc` option in `DDW_2d_bonus/app/__init__.py`
```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)
```
- **Step 4:** make and executable `.sh` and run flask
(Make sure you are in `DDW_2d_bonus` and have `runflaskvoc.sh` in the same dir)
```shell
> chmod a+x ./runflaskvoc.sh

> ./runflaskvoc.sh
```
- **Step 5:** Open this link  [`https://myserver.vocareum.com/`](https://myserver.vocareum.com/) to access our webpage

To stop the web app type `CTRL+C`. 

## 1. Webpage Overview
### Home.html - Overview of Design Thinking Project 3
![](https://i.imgur.com/Ox42ypt.jpg)
![](https://i.imgur.com/xZBVlwl.jpg)
### About.html - Content from our HASS Presentation (Has Covid 19 divided society?)
![](https://i.imgur.com/nJkaKae.jpg)
![](https://i.imgur.com/Rq0nec9.jpg)

### Task-1.html- Data for Model 1
:::info
When we develop our model, we applied various filter, so the only input data our model supports is:
- **Population Density** from `100` to `500` 
- **Human Development Index** from `0.85` to `0.99`
- **Monthly Cases** from `100` to `30,000`
:::
![](https://i.imgur.com/vVV2HPr.jpg)
![](https://i.imgur.com/6jW62vN.jpg)

### Task-2.html- Data for Model 2
![](https://i.imgur.com/XxZXFUj.jpg)
![](https://i.imgur.com/7SXlZpq.jpg)
![](https://i.imgur.com/J990j99.png)

:::info
Our model only support percentage value so the allowed input is:
- **Mental Illness Percentage** from `1` to `100`
- Number of Fast food restaurants per 100 000 people from `1` to `100`
- Hypertension Percentage from `1` to `100`
:::
