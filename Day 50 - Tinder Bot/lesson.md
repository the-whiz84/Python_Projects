# Day 50 - Tinder Bot: Popups, OAuth Windows, and Intercepted Clicks

Day 50 is a good example of how browser automation becomes harder when the website is built around popups, permission prompts, and third-party login flows. The script does not just click a single button on one page. It has to move through Tinder's login modal, switch into a Facebook authentication window, come back to the original tab, dismiss more browser-level prompts, and then keep swiping while occasional match popups block the interface.

This kind of project benefits from some theory because the hard part is not Python syntax. The hard part is browser state. Selenium has to know which window it is controlling, which elements are currently visible, and whether another layer of UI has moved in front of the button we want to click.

## 1. This Project Introduces Browser Context Switching

The main new concept is that Selenium can control only one browser context at a time. A context might be the original Tinder tab or a newly opened Facebook login window. When Tinder opens a third-party authentication popup, Selenium does not automatically follow it. The script has to switch there explicitly.

The code captures both window handles like this:

```python
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
```

This is an important browser-automation concept. `window_handles` gives Selenium's internal identifiers for every open tab or popup. `switch_to.window(...)` tells the driver which DOM it should talk to next. Without that call, Selenium would still be looking at the Tinder page while the Facebook login fields are open somewhere else.

## 2. OAuth Login Flows Change the Shape of the Automation

The script chooses the Facebook login path and then fills the email and password fields inside that separate popup:

```python
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)
```

This is a good place to pause on the theory. OAuth-style login flows often delegate authentication to another provider because the main site does not want to handle passwords directly. For automation, that means the login process is no longer a single page on the same site. The bot must cross an application boundary and then return.

That is why Day 50 is more than another Selenium exercise. It teaches you to treat the browser as a set of moving contexts instead of one static page.

## 3. Returning to the Original Window Is Part of the Flow

After the Facebook step, the script switches back:

```python
driver.switch_to.window(base_window)
sleep(5)
```

That line is easy to overlook, but it is essential. Once the authentication step finishes, the next buttons we need belong to Tinder again, not Facebook. In browser automation, entering a popup is only half the job. You also need to restore the original context before continuing.

The extra `sleep(5)` reflects another real browser-automation issue. After login, Tinder still needs time to render the main interface and any permission dialogs. Python is ready immediately; the web app is not.

## 4. Permission Modals and Cookie Banners Are Part of the UI State

After returning to Tinder, the script clicks through several modal prompts:

```python
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
```

This is worth spelling out because it matches a common pattern in modern websites. The page you want is often blocked by one or more overlays:

- login modals
- cookie banners
- location prompts
- notification prompts

From a human perspective, these are minor interruptions. From an automation perspective, they completely change what is clickable. A script that ignores them usually fails before it ever reaches the main task.

## 5. The Swiping Loop Is Simple, but the Interface Is Not

Once the setup is done, the core loop is short:

```python
for n in range(100):
    sleep(1)

    try:
        like_button = driver.find_element(
            By.XPATH,
            value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
        )
        like_button.click()
```

This is another good reminder that advanced automation often rests on ordinary Python. The loop itself is basic. The real complexity comes from the interface around it. The script can click the button only if the app is in the expected state and no other element is sitting on top of it.

The `sleep(1)` also deserves a short note. Delays in automation are not only about giving pages time to load. They also reduce the chance of issuing clicks faster than the UI can update.

## 6. `ElementClickInterceptedException` Teaches You About Overlays

The most interesting error in this project is `ElementClickInterceptedException`:

```python
except ElementClickInterceptedException:
    try:
        match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
        match_popup.click()
    except NoSuchElementException:
        sleep(2)
```

This exception happens when Selenium tries to click one element, but another visible element is covering it. In Tinder, that often means a match modal has appeared in front of the swipe buttons.

This is helpful generic theory for Python automation because it teaches a broader lesson: when UI automation fails, the problem is not always "wrong selector." Sometimes the selector is correct, but the page state has changed and a different layer is intercepting the action.

In other words, browser automation has geometry as well as logic. The element must exist, but it must also be reachable.

## 7. Exception Handling Turns a Brittle Script into a Resilient One

Without the nested `try/except`, one match popup would stop the entire run. With the exception handling in place, the bot can recover and continue.

That makes this lesson useful beyond Selenium. It demonstrates a solid Python principle: when working against an external system, expect interruptions and decide how to recover from them. A resilient automation script does not assume the page will stay perfect forever.

It is also a good example of separating the normal path from the recovery path:

- normal path: find like button and click it
- recovery path: close the blocking popup or wait briefly, then continue

## 8. Why XPath Appears So Often Here

You will notice that much of this script uses XPath instead of IDs or friendly CSS selectors. That usually means the page does not expose many stable attributes for the elements we need, or the author chose the quickest working locator during inspection.

This is worth mentioning because it affects maintainability. XPath is sometimes necessary, but it is often fragile. If Tinder changes the nesting structure of the page, the automation may break even if the visible interface still looks similar. That is one reason browser bots aimed at consumer apps tend to require frequent maintenance.

## How to Run the Project

Set the required environment variables:

```bash
export FB_EMAIL="your_email"
export FB_PASSWORD="your_password"
```

Install Selenium if needed:

```bash
pip install selenium
```

Run the bot:

```bash
python main.py
```

The project depends on a working Chrome and ChromeDriver setup. Since sites like Tinder change frequently, some selectors may also need maintenance before the script runs successfully.

## Summary

Day 50 teaches one of the most important browser-automation ideas in the course: Selenium must control the correct browser context at the correct time. The bot switches into a third-party login popup, returns to the main app, clears modal obstacles, and keeps swiping while handling intercepted clicks. The lesson is not just about Tinder itself. It is about managing state, overlays, and recovery paths in any UI automation workflow.
