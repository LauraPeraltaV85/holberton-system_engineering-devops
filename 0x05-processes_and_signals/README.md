0x05. Processes and signals

0. What is my PID 
Write a Bash script that displays its own PID.

1. List your processes
Write a Bash script that displays a list of currently running processes.

Requirements:	    
	- Must show all processes, for all users, including those which might not have a TTY
	- Display in a user-oriented format
	- Show process hierarchy

2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

	- You cannot use pgrep

3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

	- You cannot use ps

4. To infinity and beyond
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

	- In between each iteration of the loop, add a sleep 2

5. Kill me now
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

	- You must use kill

6. Kill me now made easy
Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

	- You cannot use kill or killall

7. Highlander mandatory
Write a Bash script that displays:

      - To infinity and beyond indefinitely
      - With a sleep 2 in between each iteration
      - I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

8. Beheaded process mandatory
Write a Bash script that kills the process 7-highlander.