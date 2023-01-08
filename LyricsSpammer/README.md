# Function 

Sends the text inside the file line by line wherever you want.

# History

I was totally bored and decided to create something to annoy my friends on Whatsapp and Telegram.

# Use mode

1 - In the `lyrics.txt` file put the text you want to send, remember that it will be sent line by line, if not skipped all the text will be sent at once.

2 - Run `main.py` and go to the app where you want the text to be sent, remember to click on the text box where it should be typed, run! You only have 10 seconds to do this.

# Notes

On line 10 there is the following code:

```python
pyautogui.hotkey('ctrl', 'enter')
```
I used this code to send the message in telegram, where my settings make the keys that send the message to be Ctrl + Enter.

According to your app, you can change the keys or simply replace the line with:

```python
pyautogui.press('enter')
```
