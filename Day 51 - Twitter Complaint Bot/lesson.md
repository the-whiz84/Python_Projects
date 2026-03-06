# Day 51 - Twitter Complaint Bot: Using OOP for Multi-Site Automation

Day 51 combines two separate web tasks into one Python workflow. The bot first measures the current internet speed on Speedtest, stores the download and upload values, then opens X and posts a complaint message if the measured speeds are below the expected contract values.

This is the first automation lesson where object-oriented structure really helps. The script is no longer a single chain of browser actions on one site. It needs to carry state from one website into another. That is exactly the kind of problem where a class can make the code easier to reason about.

## 1. Why a Class Helps in This Project

The main file is intentionally short:

```python
from twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 200
PROMISED_UP = 100
ISP = ""

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()

tweet = f"Hey {ISP}, why is my internet speed {twitter_bot.down}  Mbps Down / {twitter_bot.up} Mbps Up?!\nWhen I pay for guaranteed speeds of {PROMISED_DOWN}/{PROMISED_UP}"
twitter_bot.tweet_at_provider(tweet)
```

That short script works because the class handles the messy details. It owns the browser session, stores the current speed values, and exposes two methods with clear jobs:

- `get_internet_speed()` gathers the measurements
- `tweet_at_provider(...)` posts the message

This is a good example of why classes can be useful in Python. The point is not to make the code sound more advanced. The point is to keep related state and behavior together.

## 2. The Constructor Stores Shared State

The class starts by creating a Chrome driver and storing credentials:

```python
class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0
        self.username = os.environ.get("TWITTER_USERNAME")
        self.password = os.environ.get("TWITTER_PASSWD")
```

This is where OOP becomes practical rather than theoretical. Both methods need access to the same browser session, and the tweeting method also depends on data collected earlier by the speed test. Keeping those values on `self` means the object can carry information from one stage of the workflow to the next.

Without this structure, the script would likely rely on global variables or awkward argument passing. For a tiny script that might be tolerable, but for a multi-step automation flow it quickly gets messy.

## 3. Measuring Speed Is an Automation Step with Its Own Timing Rules

The `get_internet_speed()` method handles everything related to Speedtest:

```python
def get_internet_speed(self):
    self.driver.get("https://www.speedtest.net")
    time.sleep(3)
    self.driver.find_element(By.ID, value="onetrust-reject-all-handler").click()
    time.sleep(1)
    self.driver.find_element(
        By.XPATH,
        value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
    ).click()
    time.sleep(40)

    self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
    self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
```

There are two useful lessons here.

First, this method is self-contained. It opens the site, dismisses the cookie layer, starts the test, waits for the asynchronous measurement to complete, and stores the result. That makes the method easy to describe and easy to call.

Second, it shows how automation often depends on waiting for an external process. The speed test is not instant. Python can fire the click immediately, but the network measurement takes time. That is why the method pauses for much longer than the earlier Selenium exercises.

## 4. Storing the Results on `self` Makes the Next Step Simple

After the speed test finishes, the values are available as object attributes:

```python
self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
```

That design matters because the complaint message is built later in `main.py`. Instead of returning a complicated structure and threading it through more functions, the object simply keeps the measured state. This is one of the most approachable examples of encapsulation in the repository: the object remembers what happened so the rest of the program can use it.

## 5. Logging Into X Reuses the Same Browser Session

The second method opens X and performs the login flow:

```python
def tweet_at_provider(self, tweet):
    self.driver.get("https://x.com/i/flow/login")
    time.sleep(5)

    username = self.driver.find_element(By.NAME, value='text')
    username.send_keys(self.username, Keys.ENTER)
    time.sleep(2)

    password = self.driver.find_element(By.NAME, value="password")
    password.send_keys(self.password, Keys.ENTER)
```

This is a good example of why the class owns the driver. The object does not need to create a second browser or pass a driver around between helper functions. It continues using the same Selenium session and simply navigates to a new site.

That makes the automation feel like one continuous process, even though it crosses application boundaries.

## 6. Human-in-the-Loop Still Matters for Security Checks

The method pauses again before posting:

```python
# Extra time added to enter MFA code manually
time.sleep(30)
```

This is a simple but realistic design choice. Social platforms often introduce extra verification for automated or unfamiliar login sessions. Rather than trying to bypass every security prompt, the script leaves a window where the human can enter the MFA code manually.

That is worth keeping in the lesson because it teaches an honest version of automation. Not every step should be automated. Sometimes the right design is to automate the repeatable work and leave the security checkpoint to a human.

## 7. Posting the Complaint Is the Final Stage of the Pipeline

After the login and cookie prompt handling, the method finds the message box and posts the text:

```python
refuse_cookies = self.driver.find_element(
    By.XPATH,
    value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div/span/span'
)
refuse_cookies.click()

message_input = self.driver.find_element(
    By.XPATH,
    value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div'
)
message_input.send_keys(tweet)
```

This part ties the whole project together. The complaint text is not hardcoded at the point of posting. It depends on data gathered earlier from a different website. That makes the full project a pipeline:

- collect measurement data
- store it in the object
- generate a message from that state
- publish the message on another platform

That is a useful automation pattern well beyond this single project.

## 8. This Lesson Shows a Practical Use of OOP

If object-oriented programming has ever felt abstract, this project gives a concrete use case. The class is not here because "everything should be a class." It is here because the workflow has shared state:

- one browser session
- saved credentials
- download and upload measurements
- multiple methods operating on the same data

That is exactly the kind of scenario where an object can keep the code organized.

## How to Run the Project

Set the required environment variables:

```bash
export TWITTER_USERNAME="your_username"
export TWITTER_PASSWD="your_password"
```

Install Selenium if needed:

```bash
pip install selenium
```

Run the project:

```bash
python main.py
```

You may need to be present to handle MFA or changing login prompts on X.

## Summary

Day 51 turns OOP into something practical. The class keeps the browser session, credentials, and measured internet speeds in one place, which makes it possible to connect a Speedtest run to a later social-media post. The project also reinforces a broader automation lesson: once a script spans multiple websites and multiple stages, structure matters just as much as Selenium selectors.
