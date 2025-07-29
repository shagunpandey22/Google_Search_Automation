# 🤖 Google Search Automation Using Selenium & undetected_chromedriver

## 📌 Project Overview

This project demonstrates how to automate Google Search using Python's Selenium library combined with `undetected_chromedriver` to simulate human-like browser interactions.  
It tackles one of the most common and tricky tasks in browser automation — performing a live search on **Google**, which has strong anti-bot mechanisms.

---

## 🎯 Objective of the Script

### The automation was designed to:
1. Launch a real Chrome browser using `undetected_chromedriver`.
2. Apply a **custom User-Agent** to make the browser appear human.
3. Navigate to **Google.com**.
4. **Accept cookie consent** (if prompted).
5. Detect and **sign out of any logged-in Google account**.
6. Prompt the user to enter a search term.
7. Enter the term in the search bar and **submit the search**.
8. **Detect bot protection/CAPTCHA** and capture a screenshot if blocked.
9. Validate search success by checking:
   - Page title
   - URL contents
   - Search results container presence
   - Appearance of search term in result titles
10. Capture a final screenshot (`search_results.png`) for verification.

---

## ✅ Achievements

| Task                                | Status      | Notes |
|-------------------------------------|-------------|-------|
| Launch browser                      | ✅ Success   | Opened using `undetected_chromedriver` |
| Set custom User-Agent               | ✅ Success   | Helps mimic real browser identity |
| Open Google and handle cookies      | ✅ Success   | Clicked "Accept All" when prompted |
| Detect and sign out of account      | ✅ Success   | Clicked sign-out if user was logged in |
| Accept user input and perform search| ✅ Success   | Sent query to search bar and submitted |
| Detect CAPTCHA or block page        | ⚠️ Partial   | CAPTCHA shown occasionally |
| Validate search result accuracy     | ✅ Success   | Checked page title, URL, and result headers |
| Save screenshots                    | ✅ Success   | Saved `search_results.png` or `captcha_page.png` |

---

## ⚠️ Challenges Faced

### 1. Google’s Advanced Bot Detection
- Google uses behavioral detection and fingerprinting techniques.
- CAPTCHA pages (like "Are you a robot?") often interrupt automation attempts.

### 2. IP and Header Flagging
- Repeated requests from the same IP or missing headers led to soft blocks.
- Required realistic browser fingerprints to avoid suspicion.

### 3. Handling Dynamic Page Elements
- Cookie popups, login prompts, and UI elements are often delayed or loaded dynamically.
- Needed explicit wait conditions (`WebDriverWait`) to ensure reliable execution.

---

## 💡 Key Learnings

### What is a **User-Agent**?

A **User-Agent** is a string sent to websites by browsers. It tells the site what kind of device, OS, and browser you're using.

#### Example:
Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/90.0.4430.212 Safari/537.36


✅ A realistic User-Agent helped:
- Prevent early detection as a bot
- Mimic legitimate browser traffic
- Improve chances of receiving normal page content (not CAPTCHA)

---

## 🖼 Output Files

| Filename              | Description                              |
|-----------------------|------------------------------------------|
| `search_results.png`  | Screenshot of successful search results  |
| `captcha_page.png`    | Screenshot captured if CAPTCHA appeared  |

These images provide evidence of whether the script succeeded or was blocked.

---

## 🧰 Requirements

- Python 3.7 or above
- Google Chrome installed
- ChromeDriver (managed by `undetected_chromedriver`)

### Install Dependencies:
```bash
pip install selenium undetected-chromedriver

🧠 Final Thoughts
Building this automation was a valuable hands-on exercise in navigating modern bot detection systems.
It taught the importance of browser fingerprinting, timing control, and how small signals (like headers or missing interactions) can expose automation.

Despite the difficulty, the script achieved most of its goals and helped deepen understanding of browser behavior simulation.
