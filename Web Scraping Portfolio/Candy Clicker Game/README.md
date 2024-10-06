# PyAutoGUI & Selenium: Automation of Clicker Game
This Clicker Game Automation Project uses PyAutoGUI and Selenium modules of Python to execute the clicking action in the game. Through automation, we can increase the efficiency of gameplay and reach the missions more quickly, providing for a better game experience.
Link to Game: https://www.crazygames.com/game/candy-clicker-2

## Modules Used: PyAutoGUI & Selenium
- **PyAutoGUI:** A tool for controlling the computer's keyboard and mouse, as well as interacting with graphical interfaces.
- **Selenium (WebDriver & By):** Selenium is a web automation testing library that developers can use WebDriver to automate browser actions, such as filling out forms, clicking buttons or links, and retrieving and validating webpage content. The By module allows locating and selecting elements on the webpage.

## ActionChains vs. PyAutoGUI
- **ActionChains** is a feature provided by Selenium to simulate complex user actions in WebDriver. It can mimic mouse movements, clicks, drag-and-drop actions, right-clicking, and keyboard inputs. However, since Candy Clicker 2 was developed using Canvas, the elements in the game cannot be located using standard CSS selectors, which means Selenium and ActionChains cannot be used for automation.
- On the other hand, **PyAutoGUI** is a tool that controls the computer’s mouse and keyboard, suited for graphical interface operations and does not rely on browser or webpage elements.

Therefore, for this project, PyAutoGUI is used to implement auto-clicking because it can accurately interact with graphical elements on the screen, unrestricted by the limitations of element selection within a web browser.



