# Day 51 - Twitter Complaint Bot: Encapsulating State with OOP

Today, we orchestrate an advanced cross-system workflow: building a bot that interacts with two entirely disconnected web ecosystems simultaneously. We are building a "Complaint Bot" that benchmarks your internet speed against your ISP contract on Speedtest.net, and, if inadequate, automatically authenticates into Twitter (X) to publicly ping the provider with the metrics.

As the scope of our scripts expands across multiple domains, functional programming (`def do_this():`) begins to break down. Storing the download speed, the browser session, and the credentials in global variables creates unmanageable spaghetti code.

Today, we graduate to **Object-Oriented Programming (OOP)** for automation.

## Architecting the Bot Class

Instead of a sprawling linear script, we instantiate the environment into a single, cohesive class. This encapsulates the specific state of the transaction.

```python
class InternetSpeedTwitterBot:

    # The Constructor initializes the instance's state
    def __init__(self, promised_down, promised_up) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)

        # State variables encapsulated within the object instance
        self.up = 0
        self.down = 0
        self.promised_down = promised_down
        self.promised_up = promised_up
```

By locking the `driver` array and the metric variables deeply inside `self`, you guarantee that your scraping methods and your posting methods are always referencing the exact same authenticated context.

### Single Responsibility Principle

A core tenet of software engineering is the **Single Responsibility Principle**. A function should do exactly one thing.

Our class exposes public methods representing distinct, atomic workflows:

1. `def get_internet_speed(self):` -> Exclusively responsible for navigating Speedtest, managing the long polling delays required for the test (often 40+ seconds), and mutating `self.up` and `self.down`.
2. `def tweet_at_provider(self, message):` -> Exclusively responsible for the Twitter OAuth pipeline and submitting the final payload.

```python
def get_internet_speed(self):
    self.driver.get("https://www.speedtest.net")
    time.sleep(3) # Wait for UI to mount

    # Locate and trigger the test
    self.driver.find_element(By.XPATH, value='...').click()

    # The test is asynchronous. We block the execution thread for 40 seconds to allow completion.
    time.sleep(40)

    # We mutate the internal state of the class instance
    self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
```

## Bypassing Security & MFA Wait States

Authenticating into Twitter requires maneuvering through a heavily monitored flow. Social networks frequently flag headless Chrome instances. We utilize `time.sleep()` to map out human-like latency between key strokes.

```python
# Pass user credentials into the React input forms
username = self.driver.find_element(By.NAME, value='text')
username.send_keys(self.username, Keys.ENTER)

# Yield the thread to allow Twitter's backend to process the email and serve the password DOM
time.sleep(2)

password = self.driver.find_element(By.NAME, value="password")
password.send_keys(self.password, Keys.ENTER)
```

**MFA Interrupts:**
If Twitter detects a new execution environment (which they frequently do with Selenium binaries), they will throw a Two-Factor Authentication (MFA) challenge page.

Rather than engineering a massive pipeline to intercept your email/SMS, we execute a simple Human-in-the-Loop block in the script. The script sleeps for 30 seconds explicitly to yield control back to you. You type the code on your keyboard, and the autonomous execution silently resumes in the background.

## The Clean Orchestrator

Because the heavy lifting is completely abstracted into the Class file, `main.py` becomes beautifully declarative:

```python
twitter_bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
twitter_bot.get_internet_speed()

# Only execute the secondary pipeline if the primary condition fails
if float(twitter_bot.down) < PROMISED_DOWN:
    tweet = f"Hey ISP, why is my internet speed exactly {twitter_bot.down} Mbps Down?"
    twitter_bot.tweet_at_provider(tweet)
```

## Running the Speed Complaint Bot

1. Set your Twitter (X) credentials securely in your environment:
   ```bash
   export TWITTER_USERNAME='your_username'
   export TWITTER_PASSWD='your_password'
   ```
2. Open `main.py` and set `PROMISED_DOWN` and `PROMISED_UP` constants to match your ISP contract.
3. Run the script:
   ```bash
   python "main.py"
   ```
4. Be physically present to authorize an MFA code if Twitter triggers a secondary security challenge!

## Summary

By migrating our procedural scripts into Object-Oriented architectures, you unlocked the ability to build massive, cross-domain pipelines without collapsing under the weight of global variable spaghetti. You mapped asynchronous web events to atomic Class methods, cleanly separating concerns.

Tomorrow, we dive back into the DOM to handle modals that actively resist standard scrolling paradigms using direct JavaScript injection!
