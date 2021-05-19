# project profMarcin_POM
<p>
Automatic tests of some functionalities of <strong><em>&nbsp;ProfMarcin&nbsp;</em></strong> android application.<br>
Page Object Model and simple Data-driven testing are applied.
</p>
<p>
Most convenient usage:&nbsp;&nbsp;<em><strong>python3 suite_raport.py</strong></em><br>
Html reports are placed in <em>test_results</em> in the default directory
</p>

### Dependencies
java 1.8\
Android Studio 4.1.2\
node.js 14.16.0\
npm 6.14.11\
appium 1.20.2\
appium-doctor 1.16.0\
Pycharm 2021.1\
python 3.8.5\
pip 21.0.1\
Appium Python Client 1.1.1\
selenium 3.141.0\
ddt 1.4.2

<h2>List of test cases</h2>
Totals: 11 test cases<br>
Order: as they appear in the source code<br>
<hr>
01<br>
<strong>def test_guessed_word_presents_on_buttons(self):</strong><br>
<hr>
02<br>
<strong>test_behaviour_after_proper_button_clicked(self):</strong><br>
"""
After clicking the button with guessed word, additional buttons should appear
and incorrect buttons should be disabled.
"""
<hr>
03<br>
<strong>def test_switching_to_settings(self):</strong><br>
"""
Can switch to Settings?<br>
Passed if there are checkable elements in the activity we switch to.
"""
<hr>
04<br>
<strong>def test_clicking_on_At_button(self):</strong><br>
"""
What happens after we click on @ button.<br>
Passed if:<br>
1. the number of newly created buttons equals the number of old buttons AND<br>
2. the new word buttons list equals the old one (order NOT important) AND<br>
3. all the new buttons are enabled AND<br>
4. guessed word remains unchanged.<br>
"""
<hr>
05<br>
<strong>def test_moving_to_next_exercise(self):</strong><br>
"""
What happens after we click on the button with green arrow.<br>
Passed if:<br>
1.new word buttons appear AND<br>
2.buttons under the picture disappeared AND<br>
3.the number of the new word buttons equals the number of the old ones AND<br>
4.all newly created buttons are enabled.<br>
Note: picture may not be present; it is correct, do not test this.<br>
"""
<hr>
06<br>
<strong>def test_behaviour_after_improper_button_clicked(self):</strong><br>
""" How the app behaves after we clicked an improper word button(s)?<br>
Passed if:<br>
1. additional buttons (buttons with @ and with green arrow) do NOT appear<br>
2. no word button is disabled<br>
"""
<hr>
07<br>
<strong>def test_increase_level_above_upmost_limit(self):</strong><br>
""" Is it possible to increase difficulty level above permitted value? """
<hr>
08<br>
<strong>def test_decrease_level_below_lowest_limit(self):</strong><br>
""" Is it possible to lower difficulty level below permitted value?"""
<hr>
09<br>
@data(1, 2, 6)<br>
<strong>def test_number_of_buttons_equals_difficulty_level(self, diff_level):</strong><br>
"""<br>
Sets the number of buttons to a diff_level<br>
Then checks if there appear the same number of buttons on MainActivity<br>
"""<br>
<span style="color:green; font-weight:bold">Note: Test case 09 should be performed more than once, with different difficulty levels.<br>Use ddt.</span>
<hr>
10<br>
<strong>def test_switching_to_info_activity(self):</strong><br>
""" Can switch to Info?<br>
Passed if:<br>
1. there is "android:id/action_bar_title" element in the activity we switch to AND<br>
2. it contains "Informacje o aplikacji" text<br>
"""
<hr>
11<br>
<strong>def test_switching_to_main_activity(self):</strong><br>
""" Can we switch to Main Activity while on Info page? """
<p>&nbsp;</p>






