Execution order
1.Render.py
2.Server.py
3.Controller.py


1. Follow the prompt on Server.py
(Enter Render port and IP, shown on Render after excuting Render.py, into Server prompt)
2. Follow the prompt on Controller.py
(Enter Render port and IP, shown on Render after excuting Render.py, into Controller prompt)
3. Enter Commands
(Shown on Controller command line)
4. Exits when needed 
(connection closes after shudown)

p.s. 
1.Due to project design, connection to all 3 module must be established before command enter.
	Code MAYNOT work if not followed.
2.All human enter error is not handled.
	Code MAY need to restart (close out and re excute) when a command is not properly input
3.'rsrs' function only works AFTER you paused the stream.
	to replay, use sttn [filename]
4.Code envirment is in Python 3.7.4 
	Code won't work under python 2
5.Server.py must be in a Folder with the txt file to be stream,
(Render.py/Controller.py can also be in it)
	Code may have issue whenever theres too many files to list
	Code will try to list everything.
6.function to sss and rsrs is printed on the render since user will be looking at the render. 
7. After Paused, rsrs or sss must be used to finish streaming before sttn can be used 
